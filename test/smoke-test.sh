#!/usr/bin/env bash
# Career Skill Planner — Smoke Test Script
# 验证所有 Skill 模板文件的格式和内容完整性
# 用法: ./smoke-test.sh [path/to/skill.md]

set -euo pipefail

PASS=0
FAIL=0
WARN=0

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

info()  { echo -e "${GREEN}[PASS]${NC} $1"; }
warn()  { echo -e "${YELLOW}[WARN]${NC} $1"; }
fail()  { echo -e "${RED}[FAIL]${NC} $1"; FAIL=$((FAIL + 1)); }

check_file() {
  local file="$1"
  echo "── $file ──"

  # 1. 文件存在且非空
  if [[ ! -f "$file" ]]; then
    fail "文件不存在"
    return 1
  fi
  if [[ ! -s "$file" ]]; then
    fail "文件为空"
    return 1
  fi
  info "文件存在且非空"

  # 2. YAML frontmatter 检查
  local first_line
  first_line=$(head -1 "$file")
  if [[ "$first_line" != "---" ]]; then
    fail "缺少 YAML frontmatter 起始标记 (---)"
    return 1
  fi
  info "YAML frontmatter 起始标记存在"

  # 3. 必需字段检查
  local content
  content=$(cat "$file")

  local required_fields=("name:" "description:" "status:" "compatibility:")
  for field in "${required_fields[@]}"; do
    if echo "$content" | grep -q "^${field}"; then
      info "必需字段存在: $field"
    else
      fail "缺少必需字段: $field"
    fi
  done

  # 4. status 值检查
  local status_val
  status_val=$(echo "$content" | grep "^status:" | head -1 | sed 's/status:\s*//' | tr -d '"' | tr -d "'" | xargs)
  case "$status_val" in
    verified|experimental|pending)
      info "status 值有效: $status_val"
      ;;
    *)
      warn "status 值无效或缺失: '$status_val' (应为 verified/experimental/pending)"
      ;;
  esac

  # 5. 文件大小检查 (1KB - 50KB)
  local size
  size=$(wc -c < "$file")
  if [[ $size -lt 1024 ]]; then
    warn "文件过小 (${size}B < 1KB)，可能内容不完整"
  elif [[ $size -gt 51200 ]]; then
    warn "文件过大 (${size}B > 50KB)，建议拆分"
  else
    info "文件大小合理 (${size}B)"
  fi

  # 6. 正文关键结构检查
  local sections=("## 角色" "## 触发词" "## 用户提供什么" "## 工作流" "## 输出格式" "## 质量检查清单" "## 防呆机制")
  for section in "${sections[@]}"; do
    if echo "$content" | grep -q "^${section}"; then
      info "章节存在: $section"
    else
      fail "缺少章节: $section"
    fi
  done

  # 7. 示例检查
  if echo "$content" | grep -qi "示例"; then
    info "包含示例"
  else
    warn "缺少示例"
  fi

  # 8. 中文内容检查（至少有一些中文）
  if echo "$content" | grep -qE '[一-龥]'; then
    info "包含中文内容"
  else
    warn "缺少中文内容"
  fi

  echo ""
}

# 主逻辑
if [[ $# -eq 0 ]]; then
  # 无参数：扫描所有模板文件
  echo "🔍 扫描所有 Skill 模板..."
  echo ""

  TEMPLATE_DIR="${1:-templates}"
  if [[ ! -d "$TEMPLATE_DIR" ]]; then
    fail "模板目录不存在: $TEMPLATE_DIR"
    exit 1
  fi

  TOTAL=0
  while IFS= read -r -d '' file; do
    TOTAL=$((TOTAL + 1))
    if ! check_file "$file"; then
      :
    fi
  done < <(find "$TEMPLATE_DIR" -name "*.md" -print0 | sort -z)

  echo "═══════════════════════════════════════"
  echo "总计: $TOTAL 个文件 | 通过: $PASS | 失败: $FAIL | 警告: $WARN"
  echo "═══════════════════════════════════════"

  if [[ $FAIL -gt 0 ]]; then
    echo -e "${RED}❌ 部分检查未通过${NC}"
    exit 1
  else
    echo -e "${GREEN}✅ 所有检查通过${NC}"
    exit 0
  fi
else
  # 指定文件
  check_file "$1"
  exit $FAIL
fi
