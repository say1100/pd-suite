# pd-suite · Product Design Agent Skills / 产品设计全流程 Agent Skills

**Compatible with Claude Code · Codex CLI · Cursor · Gemini CLI — any agent that supports the open Agent Skills standard (`SKILL.md`).**

> Turn your AI coding assistant into a product design partner: walk a vague idea through a structured decision chain — **requirements → solution comparison → feasibility review → demo → verification** — with verifiable, gate-checked assets at every step, until the idea is *validated and buildable*.
>
> 让 AI 编码助手成为你的产品设计搭档:把一个模糊想法,沿**"理需求 → 比方案 → 评可行性 → 做 Demo → 定验证"**的决策链结构化走完,每一步产出可校验的资产,直到"验证过能做"。触发词按中文口吻优化,兼容英文交互。

## 为什么需要

AI 助手做产品设计普遍有四个毛病:**想到哪做到哪**(没有固定流程)、**结论无依据**(评审像算命)、**产出口径随意**("效果不错"式表述)、**demo 与验证脱节**(做完了才发现没埋点没数据)。本套件把这四件事全部工程化:流程写进 SKILL.md、证据纪律写进规则、模糊词被脚本拦截、demo 与评测用"埋点清单"强制耦合。

## 两个技能

### 1. pd-suite(全流程套件,7 个场景)

| # | 场景 | 你说 | 产出 | 质量把门 |
|---|---|---|---|---|
| 1 | 需求梳理 | "整理这些反馈/访谈纪要" | schema 化需求清单(谁·场景·痛点·P0/P1/P2) | `check_schema.py` |
| 2 | 方案对比 | "两个方案帮我对比" | trade-off 矩阵(强制含"最便宜验证方案") | P0 覆盖门禁 |
| 3 | 可行性评审 | "这方案靠谱吗" | GO/PIVOT/NO-GO 报告(转发独立评审技能) | 见技能 2 |
| 4 | Demo 设计 | "做个 demo" | 两段式:链路图+四态矩阵草稿 →确认→ 代码+埋点清单 | `check_demo_gate.py` |
| 5 | 验证评估 | "怎么验证?定指标" | 验证链路+指标卡+kill criteria | `check_metrics.py` |
| 6 | 变更记录 | "改定位了,影响什么" | 变更影响单(🔴🟡🟢)+ ADR | 只追加不改写 |
| 7 | 交付文档 | "写 PRD/出汇报"(需显式) | PRD/汇报/评审材料 | 零新数据,数字全带来源 |

### 2. plan-feasibility-review(独立评审技能)

证据可回溯的可行性评审方法论:隐含假设提取排序 → 六跳因果链审计 → 可证伪性检查 → Pre-mortem → Demo 可验证性判定(埋雷式)→ GO/PIVOT/NO-GO + Kill criteria + 按性价比排序的下一步。附**黄金测试集**(5 个埋雷用例+答案 key)与触发测试集,开箱可自测。

## 设计亮点

- **埋点耦合**:Demo 交付必须附数据采集点位清单,验证评估凭此开工——设计与验证硬闭环,不会出现"demo 做完没数据可评";
- **两段式交付**:先交链路图+四态矩阵草稿,用户确认后才生成代码,防止打磨白费;
- **脚本把门**:三个校验器(需求 schema / demo 门禁 / 指标卡)以退出码判交付资格,"效果不错""显著提升"等模糊表述直接拦截;
- **反讨好评审**:发现致命缺陷必须直说;好计划不允许虚构红旗(测试集内置"好计划"用例专测此事);
- **三份炼化设计规范**(design/engineering/testing-guidance):融合 Impeccable、taste-skill、ui-ux-pro-max、Playwright 官方 agent-cli 等社区技能的精华,含"去 AI 味黑名单"与规则冲突裁决表;
- **数据飞轮**:失灵原话进收集箱 → 修触发边界 → 回归测试;案例库随使用生长,可升格进黄金集。

## 快速开始

```bash
# 1. 复制 skills/ 下两个文件夹到你的技能目录
#    Windows: C:\Users\<你>\.agents\skills\
#    macOS/Linux: ~/.agents/skills/

# 2. 新开会话,试试:
#    "帮我看看这个计划靠不靠谱:做一个面向大学生的二手教材交易小程序……"

# 3. (可选)跑内置自测:见 plan-feasibility-review/tests/README.md
```

详见 [INSTALL.md](pd-suite/INSTALL.md)。

## 目录结构

```
skills/
├── pd-suite/
│   ├── SKILL.md                 # 路由层:意图表 + 全局约定 + 执行前核对清单
│   ├── inbox.md                 # 口吻/失灵收集箱(数据飞轮入口)
│   ├── INSTALL.md               # 安装指南
│   ├── skills/                  # 7 个场景子技能(均含 SKILL.md + prompts/ + references/ + scripts/)
│   └── tests/                   # 触发测试集(11 条用例 + 失灵修复记录)
└── plan-feasibility-review/
    ├── SKILL.md + references/   # 评审方法论(逻辑审计/demo 可验证性)
    ├── tests/                   # 黄金集(埋雷用例+答案key)+ 触发集 + 总览
    └── cases/                   # 案例留档模板
```

## 测试状态

- 触发测试:11 条(6 召回 + 4 边界 + 1 重叠探测)全部通过,含 1 次"写 PRD 误触发"的修复回归记录;
- 门禁实测:模糊词指标卡拦截、缺埋点清单拒收、"跳过确认直接写代码"被规则顶回;
- 黄金集:5 用例(3 埋雷 + 1 好计划测误报 + 1 缺料测诚实度),封版线:命中率 ≥80%、好计划误报 = 0。

## License

MIT(自建部分)。如分发配套的官方技能,请遵循其各自 LICENSE。
