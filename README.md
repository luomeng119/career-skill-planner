# Career Skill Planner

> 告诉 AI 你的职业，它帮你把工作拆成一套可用的 Skill 库。

![License](https://img.shields.io/badge/license-MIT-blue)
![Version](https://img.shields.io/badge/version-v1.0.0-green)
![Claude Code](https://img.shields.io/badge/Claude_Code-compatible-purple)

---

## 这是什么

一个 [Claude Code](https://docs.anthropic.com/en/docs/claude-code) Skill，也是一个 **Skill 工厂**。

用法很简单：说出你的职业，它输出一份清单，告诉你这个职业可以做哪些 Skill、每个 Skill 怎么做、提示词直接复制发给 Agent 就能生成。

不需要懂提示词工程，不需要从零想工作流。把职业说清楚，剩下的它来。

---

## 为什么做这个

做了 100 多个 Skill 之后，发现一个问题：凭感觉做，很容易做一堆重叠的，同时漏掉一些真正高频的场景。

后来想通了——**按职业拆是最不容易遗漏的方式**。每个职业都有自己的工作流、固定的输出物、反复踩的坑。把这些梳理清楚，Skill 该做什么、做多少，自然就清楚了。

产品经理是我自己的职业，所以先做了这个。拆出来 13 个 Skill，覆盖从需求到复盘的完整链路。然后想：任何职业都可以这样做，就把这个拆解过程本身也做成了 Skill。

---

## 基于的项目

本项目基于 [zephyrwang6/career.skill](https://github.com/zephyrwang6/career.skill) 扩展而来。原项目是元 Skill 方法论的开创者，提供了完整的职业拆解框架和防呆机制。本项目的扩展包括：

- **25+ 经过验证的 Skill 模板**（产品经理 13 个、UI 设计师 6 个、内容运营 6 个、前端工程师 8 个）
- **端到端测试和 CI/CD 保障**
- **用户反馈闭环机制**
- **Web 搜索增强分析**
- **完整的输出示例和贡献指南**

感谢 [zephyrwang6](https://github.com/zephyrwang6) 开创了这个方法论。

---

## 快速开始

### 安装

**第一步**：克隆本仓库

```bash
git clone https://github.com/luomeng119/career-skill-planner.git
```

**第二步**：把核心 Skill 放进你的 Claude Code skills 目录

```bash
cp career-skill-planner/SKILL.md ~/.claude/skills/career-skill-planner/SKILL.md
```

**第三步**：（可选）安装模板库

```bash
cp -r career-skill-planner/templates ~/.claude/skills/career-skill-planner/templates
```

### 使用

**方式一：职业 Skill 规划**

在 Claude Code 里说：

```
帮我规划前端工程师的 Skill
```

或者：

```
我是内容运营，帮我拆 Skill
```

**方式二：直接使用模板**

浏览 `templates/` 目录，找到你职业的 Skill 模板，直接安装使用：

```bash
cp templates/product-manager/prd-writer.md ~/.claude/skills/prd-writer/SKILL.md
```

**方式三：自定义职业**

如果模板库没有你的职业，用规划器生成：

```
我是临床医生，帮我拆 Skill
```

---

## 已验证的职业

| 职业 | Skill 数 | 状态 |
|------|:--------:|------|
| 产品经理 | 13 | ✅ 已验证 |
| UI 设计师 | 6 | ✅ 已验证 |
| 内容运营 | 6 | ✅ 已验证 |
| 前端工程师 | 8 | ✅ 已验证 |

每个 Skill 模板都包含：触发词、工作流、质量检查清单、防呆机制。

---

## 输出示例

每个职业的完整输出示例见 `examples/` 目录：

- [产品经理示例](examples/product-manager-example.md)
- [UI 设计师示例](examples/ui-designer-example.md)
- [内容运营示例](examples/content-ops-example.md)
- [前端工程师示例](examples/frontend-engineer-example.md)

---

## 模板状态标签

| 标签 | 含义 |
|------|------|
| ✅ 已验证 | 在实际工作中使用并通过端到端测试 |
| 🟡 实验性 | 框架完整，但未经大规模实战验证 |
| ⏳ 待验证 | 初步创建，需要社区反馈完善 |

---

## 目录结构

```
career-skill-planner/
├── README.md                    # 本文件
├── SKILL.md                     # 核心：职业 Skill 规划器
├── CHANGELOG.md                 # 版本变更日志
├── CONTRIBUTING.md              # 贡献指南
├── templates/                   # 按职业分类的 Skill 模板库
│   ├── product-manager/         # 产品经理 13 个
│   ├── ui-designer/             # UI 设计师 6 个
│   ├── content-ops/             # 内容运营 6 个
│   └── frontend-engineer/       # 前端工程师 8 个
├── examples/                    # 各职业完整输出示例
│   ├── product-manager-example.md
│   ├── ui-designer-example.md
│   ├── content-ops-example.md
│   └── frontend-engineer-example.md
├── test/
│   └── smoke-test.sh            # 端到端冒烟测试
└── .github/
    └── workflows/
        └── ci.yml               # GitHub Actions CI
```

---

## 防呆说明

输入不完整没关系，Skill 会自动处理：

- **职业名称清晰**（"财务分析师"、"UI 设计师"）→ 直接输出清单
- **职业名称过于宽泛**（"运营"、"总监"、"分析师"）→ 给你一道选择题，选完立刻输出
- **完全不知道怎么描述**（"我工作比较杂"）→ 给你一个三行填空，填完输出

---

## 与 Claude Code 的兼容性

| Claude Code 版本 | 兼容状态 |
|-----------------|---------|
| 2.0+ | ✅ 完全兼容 |
| 1.x | ⚠️ 部分兼容（部分高级功能不可用） |

推荐使用最新版本的 Claude Code 以获得最佳体验。

---

## 贡献

欢迎 PR！详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

把你的职业拆解结果贡献进来，帮助更多人用 AI 提效。

---

## 许可证

MIT — 自由使用、修改和分发。

---

## 一点想法

这个东西的本质是：**把"怎么用 AI 提效"这个问题，变成一个有标准答案的填空题**。

不是所有人都有时间去研究提示词、设计工作流。但每个人都知道自己的职业是什么、每天在做什么。

从职业出发，是让 AI 工具真正落地的最短路径。

---

made with [Claude Code](https://docs.anthropic.com/en/docs/claude-code) · 基于 [zephyrwang6/career.skill](https://github.com/zephyrwang6/career.skill) 扩展
