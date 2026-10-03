---
name: pd-demo
description: "Demo 设计:交互链路+四态矩阵(草稿)→ 用户确认 → 可运行前端 + 埋点清单。pd-suite 包内模块,不独立触发。"
user-invocable: false
---

# Demo 设计

**入口必答一题**(用户没说就先问):这个 demo 给谁看?投资人(看故事线)/ 客户(看核心任务闭环)/ 内部(验证技术可行)——打磨深度上限由此决定,见 `references/audience-depth.md`。

**铁律:两段式交付。** 阶段一(草稿)不经用户确认,禁止进入阶段二(代码)。

## 阶段一|草稿(先做,可验证)

| 步骤 | 做什么 | 依据 |
|------|--------|------|
| D1 页面清单 | 从 P0 核心任务推导页面清单,每页一句话职责 | prompts/steps.md §D1 |
| D2 链路图 | 页面间跳转 mermaid 图;每个 P0 任务必须存在完整可达路径 | §D2 |
| D3 四态矩阵 | 每页 × (正常/空态/错误态/加载态) 逐格定义 | §D3 |
| D4 交付确认 | 链路图+四态矩阵交用户确认,记录修改 | — |

## 阶段二|实现(确认后)

| 步骤 | 做什么 | 依据 |
|------|--------|------|
| D5 打磨基线 | 先定 design tokens(色/字/距),可参考已装 theme-factory 的主题;**tokens 三层纪律与硬编码扫描见 `references/engineering-guidance.md`** | §D5 |
| D6 生成代码 | 可运行前端(HTML/React);复杂多组件用已装 web-artifacts-builder 脚手架;**视觉规范遵循 `references/design-guidance.md`(融合版:Impeccable+taste+ui-ux-pro-max+官方 frontend-design 提炼去重)——按场景路由:冷启动§一/新建§二/改进§三,硬规则§四强制,去 AI 味黑名单§五命中即改** | §D6 |
| D7 自检 | 本地跑通 + 截图核对;有 Playwright 环境时用 webapp-testing 走一遍 P0 任务路径。**执行决策树/with_server 用法/playwright-cli 升级路径/响应式三档核验,见 `references/testing-guidance.md`** | §D7 |
| D8 埋点清单 | 产出 `track-events.md`(页面×交互×字段×事件名),作为交付物一部分 | §D8 |

## 交付门禁

跑 `python skills/pd-demo/scripts/check_demo_gate.py <交付目录>`,exit 0 才算交付完成:
- `link-matrix.md`(链路图)存在且含 mermaid 块;
- 四态矩阵行数 ≥ 页面数;
- `track-events.md` 存在且 ≥1 条事件。
缺埋点清单 = 未交付,`pd-eval` 也有权拒收。

## 边界

单页纯视觉微调(无链路/埋点诉求)→ 让给 frontend-design,不进本流程。
