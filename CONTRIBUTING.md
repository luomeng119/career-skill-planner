# Contributing to Career Skill Planner

感谢你考虑为这个项目贡献！以下是参与贡献的指南。

---

## 目录

- [贡献方式](#贡献方式)
- [Skill 模板质量标准](#skill-模板质量标准)
- [端到端测试要求](#端到端测试要求)
- [格式规范](#格式规范)
- [PR 流程](#pr-流程)
- [行为准则](#行为准则)

---

## 贡献方式

### 1. 新增职业 Skill 拆解

如果你想把你的职业拆解成 Skill 并贡献进来：

1. Fork 本仓库
2. 在 `templates/` 下创建你的职业目录（如 `templates/teacher/`）
3. 为你的职业创建 5-8 个 Skill 模板文件
4. 在 `examples/` 下创建完整的输出示例
5. 提交 PR

### 2. 改进现有 Skill 模板

如果你发现某个 Skill 模板可以改进：

1. Fork 本仓库
2. 修改对应的模板文件
3. 提交 PR，说明改进理由

### 3. 改进核心规划器

如果你对 SKILL.md 的分析框架、防呆机制等有改进建议：

1. Fork 本仓库
2. 修改 SKILL.md
3. 提交 PR，说明改进理由

---

## Skill 模板质量标准

每个 Skill 模板文件（`.md`）必须包含以下 YAML frontmatter：

```yaml
---
name: xx-feature-name
description: |
  一句话描述这个 Skill 做什么。
  触发场景：用户说"XX"、"YY"、"ZZ"时触发。
status: verified  # verified | experimental | pending
compatibility: "2.0+"  # Claude Code 兼容版本
---
```

### 模板正文结构

每个 Skill 模板正文必须包含：

1. **角色定义** — 这个 Skill 中的 Agent 扮演什么角色
2. **触发词** — 用户在什么场景下应该使用这个 Skill
3. **输入格式** — 用户需要提供什么
4. **工作流** — 步骤 → 步骤 → 输出
5. **输出格式** — 产出的形态
6. **质量检查清单** — 输出前的自检项
7. **防呆机制** — 用户信息不完整时的处理策略
8. **示例** — 至少一个完整的输入→输出示例

### 质量门槛

- [ ] 提示词可以直接复制使用，不需要用户修改
- [ ] 工作流至少 3 步，每步有明确的输入和输出
- [ ] 质量检查清单至少 3 项
- [ ] 防呆机制至少覆盖 1 个场景
- [ ] 包含至少 1 个完整示例

---

## 端到端测试要求

贡献的 Skill 模板必须通过以下测试：

### 1. 格式验证

```bash
./test/smoke-test.sh templates/your-profession/your-skill.md
```

检查项：
- YAML frontmatter 格式正确
- 包含必需的字段（name, description, status, compatibility）
- 文件大小在合理范围内（1KB - 50KB）

### 2. 内容验证

- 提示词可以在 Claude Code 中成功生成一个可用的 Skill 文件
- 生成的 Skill 文件可以被 Claude Code 正确加载
- 用一个典型输入触发 Skill，验证输出质量

### 3. CI 检查

PR 提交后，GitHub Actions 会自动运行：
- 格式检查
- 必需字段检查
- 模板数量统计

---

## 格式规范

### 文件命名

```
{职业缩写}-{功能名}.md
```

例如：
- `pm-prd-writer.md`（产品经理 - PRD 编写）
- `ds-design-system.md`（UI 设计师 - 设计系统）
- `fe-code-review.md`（前端工程师 - 代码审查）

### 命名约定

| 职业 | 缩写 |
|------|------|
| 产品经理 | pm |
| UI 设计师 | ds |
| UX 设计师 | ux |
| 内容运营 | co |
| 前端工程师 | fe |
| 后端工程师 | be |
| 数据分析师 | da |
| 项目经理 | pj |
| 设计师 | de |

### Markdown 规范

- 使用 4 个空格缩进（非 Tab）
- 代码块指定语言类型
- 列表使用 `-` 而非 `*`
- 标题层级不超过 3 层

---

## PR 流程

1. Fork 本仓库并创建特性分支
2. 按照上述规范编写内容
3. 运行 `./test/smoke-test.sh` 确保通过
4. 提交 PR，填写 PR 模板
5. 等待 Maintainer 审查（通常 3-5 个工作日）
6. 根据反馈修改后合并

### PR 模板

```markdown
## 贡献类型
- [ ] 新增职业 Skill 拆解
- [ ] 改进现有 Skill 模板
- [ ] 改进核心规划器
- [ ] 修复 Bug
- [ ] 改进文档

## 变更内容
<!-- 简要描述你做了什么变更 -->

## 测试情况
<!-- 是否通过了 smoke-test.sh？ -->

## 相关 Issue
<!-- 如果关联了某个 Issue，请标注 -->
```

---

## 行为准则

- 尊重所有贡献者，不论经验水平
- 接受建设性批评
- 关注对社区最有利的事情
- 对其他社区成员表示同理心和礼貌

---

## 问题反馈

如果你发现了 Bug 或有功能建议：

1. 搜索 [Issues](https://github.com/luomeng119/career-skill-planner/issues) 确认是否已被报告
2. 如果没有，创建一个新 Issue
3. 使用 Issue 模板，提供清晰的复现步骤或建议

---

感谢你的贡献！🎉
