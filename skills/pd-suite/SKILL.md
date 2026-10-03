---
name: pd-suite
description: "产品设计全流程技能包(软件/AI 产品):需求梳理→方案对比→可行性评审→Demo 设计→验证评估的闭环。当用户要做产品相关工作——理需求/整理访谈纪要、出方案/技术选型、评估靠不靠谱、做 demo/页面/交互流程、定指标/验证评估——时使用,即使用户没有点名技能。触发词:理需求、需求梳理、方案对比、技术路线、可行性、demo、原型、交互流程、埋点、评估体系。不处理:纯单页视觉美化(归 frontend-design)、撰写 PRD/方案书/计划书等纯文档创作任务(未点名时直接处理;**显式点名"写 PRD/出汇报"则走 pd-deliverables**)、模型训练调参、专利交底书。"
version: "0.2.0"
user-invocable: true
argument-hint: "[理需求 | 方案对比 | 可行性 | demo设计 | 验证评估] [材料/目录]"
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch
---

# pd-suite 产品设计技能包

按用户意图 **Read** 对应子技能的 SKILL.md 再执行。**子技能均为包内模块,不独立触发。**

| 意图 | 子技能 | 做什么 | 交接物 |
|------|--------|--------|--------|
| 理需求 | `skills/pd-requirements/` | 碎片想法/访谈纪要 → schema 化需求清单 | `outputs/requirements.md` |
| 方案对比 | `skills/pd-concept/` | 需求 → ≥2 候选方案 + trade-off 矩阵 | `outputs/tradeoff-matrix.md` |
| 可行性 | `skills/pd-feasibility/`(转发) | 方案/计划 → GO/NO-GO 评审 | 评审报告(走已装 plan-feasibility-review) |
| demo 设计 | `skills/pd-demo/` | 两段式:链路/四态草稿 → 确认 → 代码+埋点清单 | 代码 + `track-events.md` |
| 验证评估 | `skills/pd-eval/` | 主张→指标→数据→实验的验证链路 | `outputs/eval-plan.md` + 指标卡 |
| 变更/决策 | `skills/pd-change/` | 变更影响分析 + ADR 决策记录 | `outputs/change-impact-*.md` + `adr/ADR-*.md` |
| 写 PRD/汇报(须显式) | `skills/pd-deliverables/` | 既有资产组装成正式文档,零新数据 | `outputs/deliverables/` |

## 全局约定

1. **产出位置**:一律写当前工作区 `outputs/`,迭代另存时间戳版本(`outputs/_archive/`),不写技能安装目录。
2. **埋点耦合(灵魂规则)**:`pd-demo` 交付必须附 `track-events.md`(页面×交互×字段);`pd-eval` 开工必须先收到它——缺则先转 demo 补,禁止空转评估。
3. **显式触发分级**:生成可运行代码、产出对外文档,须用户明确点名该子技能;仅讨论想法时只分析不落码。
4. **两段式交付**:demo 先交草稿(链路图+四态矩阵),用户确认后再生成代码。
5. **脚本判读**:以退出码为准(0=过);stderr 不等于失败。机读前缀:`REQ_SCHEMA_JSON:` / `DEMO_GATE_JSON:` / `METRICS_JSON:`。Windows 下若 `python` 是应用商店占位符(**退出码 49 且无输出**即命中),改用系统真实 Python(Anaconda/官方安装均可: `where python` 找非 WindowsApps 路径),不要降级跳过校验。
6. **默认语言**:面向用户的产物用简体中文;脚本 JSON 字段名保持稳定。

## 留档钩子(soft nudge)

任一子技能执行完毕,检查 `cases/` 目录:有效案例(含三行标注)< 3 条时,在答复末尾加一句:"本次执行可留档为案例(模板见 cases/),是否保存?"——用户同意才写。

## 执行前核对

```
□ 已 Read 对应子技能 SKILL.md,未把本文件当子流程正文
□ 产出写在工作区 outputs/,迭代另存时间戳版本
□ demo 草稿未经确认未生成代码
□ eval 开工前已确认 track-events.md 存在
□ requirements/指标卡过脚本校验(exit 0)才交付
□ PRD/汇报仅显式点名时经 pd-deliverables 产出,且每个数字标注来源产物
□ 变更产生新时间戳版本,ADR 只追加不改写
□ 仅讨论想法时未擅自落码
```
