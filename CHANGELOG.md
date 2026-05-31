# Changelog

所有版本变更记录在此文件。格式基于 [Keep a Changelog](https://keepachangelog.com/)，版本号遵循 [Semantic Versioning](https://semver.org/)。

## [1.0.0] - 2026-05-31

### Added
- 核心职业 Skill 规划器（基于 zephyrwang6/career.skill 扩展）
- 25+ 经过验证的 Skill 模板：
  - 产品经理 13 个（pm-prd-writer, pm-review-board, pm-user-research, pm-data-analysis, pm-roadmap-planner, pm-requirement-prioritizer, pm-stakeholder-communication, pm-iteration-review, pm-ab-test-design, pm-feature-spec, pm-competitive-analysis, pm-project-retro, pm-team-alignment）
  - UI 设计师 6 个（ds-design-system, ds-wireframe, ds-visual-review, ds-component-library, ds-interaction-design, ds-design-handoff）
  - 内容运营 6 个（co-content-planning, co-copywriting, co-data-report, co-channel-ops, co-seo-optimizer, co-content-calendar）
  - 前端工程师 8 个（fe-code-review, fe-component-design, fe-performance-optimize, fe-accessibility-audit, fe-api-integration, fe-responsive-design, fe-state-management, fe-testing-strategy）
- 端到端冒烟测试脚本（test/smoke-test.sh）
- GitHub Actions CI 流水线（.github/workflows/ci.yml）
- 用户反馈闭环机制（Issue Template + 标签系统）
- 各职业完整输出示例（examples/ 目录）
- 贡献指南（CONTRIBUTING.md）
- 模板状态标签系统（✅已验证 / 🟡实验性 / ⏳待验证）
- SKILL.md v1.0 版本号和模型兼容性说明
- Web 搜索增强分析框架（v1.0 新增）

### Changed
- 原版 SKILL.md 增加版本号字段和兼容性说明
- 分析框架从 5 个维度扩展到 6 个（新增"行业工具链"维度）
- 输出格式增加"推荐工具/技术栈"字段

### Credits
- 方法论基于 [zephyrwang6/career.skill](https://github.com/zephyrwang6/career.skill)
- 感谢原项目开创了"按职业拆解 Skill"的方法论
