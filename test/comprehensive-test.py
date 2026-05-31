#!/usr/bin/env python3
"""
Career Skill Planner — 大规模模板测试脚本
测试策略：
1. 格式验证：所有模板的 YAML frontmatter、章节结构
2. 内容验证：检查必需字段、示例存在性
3. 防呆机制验证：检查每个模板是否有防呆描述
4. 提示词质量验证：检查提示词是否可直接使用
5. 交叉验证：确保模板之间无重叠
"""

import os
import re
import json
import sys
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"

# ANSI colors
GREEN = "\033[0;32m"
RED = "\033[0;31m"
YELLOW = "\033[0;33m"
BLUE = "\033[0;34m"
NC = "\033[0m"

def log_pass(msg): print(f"{GREEN}[PASS]{NC} {msg}")
def log_fail(msg): print(f"{RED}[FAIL]{NC} {msg}")
def log_warn(msg): print(f"{YELLOW}[WARN]{NC} {msg}")
def log_info(msg): print(f"{BLUE}[INFO]{NC} {msg}")

class TestResult:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.warnings = 0
        self.results = []

    def add(self, test_name, status, detail=""):
        self.results.append({"test": test_name, "status": status, "detail": detail})
        if status == "pass": self.passed += 1
        elif status == "fail": self.failed += 1
        else: self.warnings += 1

    def summary(self):
        total = self.passed + self.failed + self.warnings
        return f"\n{'='*60}\n总计: {total} | 通过: {self.passed} | 失败: {self.failed} | 警告: {self.warnings}\n{'='*60}"

# ===== Test 1: 格式验证 =====
def test_format(result):
    log_info("=== 测试 1: 格式验证 ===")
    for md_file in sorted(TEMPLATES_DIR.rglob("*.md")):
        rel = md_file.relative_to(BASE_DIR)
        content = md_file.read_text(encoding="utf-8")

        # Check frontmatter
        if not content.startswith("---"):
            result.add(f"{rel}: frontmatter", "fail", "缺少 --- 起始标记")
        else:
            result.add(f"{rel}: frontmatter", "pass")

        # Check required fields
        fields = ["name:", "description:", "status:", "compatibility:"]
        for field in fields:
            if re.search(rf"^{field}", content, re.MULTILINE):
                result.add(f"{rel}: {field}", "pass")
            else:
                result.add(f"{rel}: {field}", "fail", f"缺少 {field}")

        # Check status value
        status_match = re.search(r"^status:\s*(.+)", content, re.MULTILINE)
        if status_match:
            status_val = status_match.group(1).strip().strip('"').strip("'")
            if status_val in ("verified", "experimental", "pending"):
                result.add(f"{rel}: status={status_val}", "pass")
            else:
                result.add(f"{rel}: status", "warn", f"非标准 status: {status_val}")
        else:
            result.add(f"{rel}: status", "fail", "无 status 字段")

        # Check file size
        size = len(content)
        if size < 500:
            result.add(f"{rel}: size", "warn", f"过小 ({size}B)")
        elif size > 60000:
            result.add(f"{rel}: size", "warn", f"过大 ({size}B)")
        else:
            result.add(f"{rel}: size", "pass", f"{size}B")

# ===== Test 2: 章节结构验证 =====
def test_structure(result):
    log_info("=== 测试 2: 章节结构验证 ===")
    required_sections = [
        "## 角色", "## 触发词", "## 用户提供什么",
        "## 工作流", "## 输出格式", "## 质量检查清单", "## 防呆机制"
    ]
    for md_file in sorted(TEMPLATES_DIR.rglob("*.md")):
        rel = md_file.relative_to(BASE_DIR)
        content = md_file.read_text(encoding="utf-8")

        for section in required_sections:
            if re.search(rf"^{section}", content, re.MULTILINE):
                result.add(f"{rel}: {section}", "pass")
            else:
                result.add(f"{rel}: {section}", "fail", "章节缺失")

        # Check for example section
        if "示例" in content or "Example" in content:
            result.add(f"{rel}: 示例", "pass")
        else:
            result.add(f"{rel}: 示例", "warn", "缺少示例")

# ===== Test 3: 防呆机制验证 =====
def test_defensive_design(result):
    log_info("=== 测试 3: 防呆机制验证 ===")
    keywords = ["防呆", "兜底", "缺失", "假设", "[假设]", "标注"]
    for md_file in sorted(TEMPLATES_DIR.rglob("*.md")):
        rel = md_file.relative_to(BASE_DIR)
        content = md_file.read_text(encoding="utf-8")

        found = [kw for kw in keywords if kw in content]
        if len(found) >= 2:
            result.add(f"{rel}: 防呆机制", "pass", f"包含: {', '.join(found[:3])}")
        else:
            result.add(f"{rel}: 防呆机制", "warn", f"防呆关键词不足: {found}")

# ===== Test 4: 提示词质量验证 =====
def test_prompt_quality(result):
    log_info("=== 测试 4: 提示词质量验证 ===")
    for md_file in sorted(TEMPLATES_DIR.rglob("*.md")):
        rel = md_file.relative_to(BASE_DIR)
        content = md_file.read_text(encoding="utf-8")

        # Check for 「」quote marks (Chinese prompt quotes)
        has_quotes = "「" in content and "」" in content
        if has_quotes:
            result.add(f"{rel}: 提示词格式", "pass", "使用「」引号")
        else:
            result.add(f"{rel}: 提示词格式", "warn", "未使用「」引号标记提示词")

        # Check prompt length (should be substantial)
        prompt_sections = re.findall(r"「(.{50,})」", content)
        if prompt_sections:
            avg_len = sum(len(p) for p in prompt_sections) / len(prompt_sections)
            if avg_len > 100:
                result.add(f"{rel}: 提示词长度", "pass", f"平均 {avg_len:.0f} 字符")
            else:
                result.add(f"{rel}: 提示词长度", "warn", f"提示词偏短，平均 {avg_len:.0f} 字符")
        else:
            result.add(f"{rel}: 提示词长度", "warn", "未找到有效提示词")

# ===== Test 5: 模板去重验证 =====
def test_no_overlap(result):
    log_info("=== 测试 5: 模板去重验证 ===")
    all_names = {}
    for md_file in sorted(TEMPLATES_DIR.rglob("*.md")):
        name = md_file.stem
        category = md_file.parent.name
        if name in all_names:
            result.add(f"去重: {name}", "fail", f"重复: {all_names[name]} 和 {category}")
        else:
            all_names[name] = category
            result.add(f"去重: {name}", "pass")

    # Check for similar names (potential overlap)
    names = list(all_names.keys())
    for i, n1 in enumerate(names):
        for n2 in names[i+1:]:
            # Check if names share significant prefix
            prefix_len = 0
            for a, b in zip(n1, n2):
                if a == b: prefix_len += 1
                else: break
            if prefix_len >= 6:
                result.add(f"潜在重叠: {n1} vs {n2}", "warn",
                          f"共享前缀 {prefix_len} 字符")

# ===== Test 6: 中文内容验证 =====
def test_chinese_content(result):
    log_info("=== 测试 6: 中文内容验证 ===")
    for md_file in sorted(TEMPLATES_DIR.rglob("*.md")):
        rel = md_file.relative_to(BASE_DIR)
        content = md_file.read_text(encoding="utf-8")

        chinese_chars = re.findall(r'[一-鿿]', content)
        if len(chinese_chars) > 50:
            result.add(f"{rel}: 中文", "pass", f"{len(chinese_chars)} 字")
        else:
            result.add(f"{rel}: 中文", "warn", f"中文内容偏少: {len(chinese_chars)} 字")

# ===== Test 7: 模板统计 =====
def test_statistics(result):
    log_info("=== 测试 7: 模板统计 ===")
    categories = {}
    for md_file in sorted(TEMPLATES_DIR.rglob("*.md")):
        cat = md_file.parent.name
        categories[cat] = categories.get(cat, 0) + 1

    for cat, count in sorted(categories.items()):
        result.add(f"分类统计: {cat}", "pass", f"{count} 个模板")

    total = sum(categories.values())
    result.add("总计", "pass", f"{total} 个模板")

    # Check recommended count (5-8 per profession)
    for cat, count in categories.items():
        if count < 5:
            result.add(f"{cat}: 数量检查", "warn", f"仅 {count} 个，建议 5-8 个")
        elif count > 8:
            result.add(f"{cat}: 数量检查", "warn", f"{count} 个，建议不超过 8 个")
        else:
            result.add(f"{cat}: 数量检查", "pass", f"{count} 个，在推荐范围内")

# ===== Main =====
def main():
    result = TestResult()
    log_info("Career Skill Planner — 大规模模板验证")
    log_info(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log_info(f"模板目录: {TEMPLATES_DIR}")
    log_info("")

    test_format(result)
    test_structure(result)
    test_defensive_design(result)
    test_prompt_quality(result)
    test_no_overlap(result)
    test_chinese_content(result)
    test_statistics(result)

    print(result.summary())

    # Save detailed report
    report_path = BASE_DIR / "test" / "report.json"
    report_path.parent.mkdir(exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "summary": {
                "total": result.passed + result.failed + result.warnings,
                "passed": result.passed,
                "failed": result.failed,
                "warnings": result.warnings
            },
            "details": result.results
        }, f, ensure_ascii=False, indent=2)
    log_info(f"详细报告已保存: {report_path}")

    if result.failed > 0:
        sys.exit(1)
    else:
        log_pass("所有关键检查通过！")
        sys.exit(0)

if __name__ == "__main__":
    main()
