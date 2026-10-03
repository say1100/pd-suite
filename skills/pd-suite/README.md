# 产品 skill(pd-suite + plan-feasibility-review)

> 版本:pd-suite v0.2.0|安装位置:`~/.agents/skills/`(用户级技能路径,所有项目自动可用)
> 用途:**辅助产品设计全流程**——把一个模糊想法,沿"理需求 → 比方案 → 评可行性 → 做 Demo → 定验证"的决策链结构化走完,产出带校验的资产,直到"验证过能做"。不写工程代码,不管发布后增长。

## 组成(两个技能)

| 技能 | 角色 | 内容 |
|---|---|---|
| **pd-suite** | 产品设计全流程套件(路由层 + 7 场景) | 需求梳理/方案对比/可行性转发/Demo 设计/验证评估/变更与ADR/交付文档 |
| **plan-feasibility-review** | 独立评审技能 | 产品计划与方案的可行性评审:假设审计→因果链→pre-mortem→GO/NO-GO 报告(被 pd-suite 转发调用,也可单独触发) |

## pd-suite 的 7 个场景

| # | 场景 | 用户说 | 产出 | 把门 |
|---|---|---|---|---|
| 1 | pd-requirements 理需求 | "整理这些反馈""理一下需求" | schema 化需求清单(P0/P1/P2) | check_schema.py |
| 2 | pd-concept 方案对比 | "出几个方案""技术路线怎么选" | trade-off 矩阵(强制含最便宜验证方案) | P0 覆盖门禁 |
| 3 | pd-feasibility 可行性 | "靠谱吗""能成吗" | GO/NO-GO 评审报告 | 转发 #独立技能 |
| 4 | pd-demo Demo 设计 | "做个 demo""交互流程" | 链路图+四态矩阵草稿 →确认→ 代码+埋点清单 | check_demo_gate.py |
| 5 | pd-eval 验证评估 | "怎么验证""定指标" | 验证链路+指标卡+kill criteria | check_metrics.py |
| 6 | pd-change 变更记录 | "改定位了,影响什么""记下这个决定" | 变更影响单 + ADR | 只追加不改写 |
| 7 | pd-deliverables 交付文档 | 显式点名"写 PRD/出汇报" | PRD/汇报/评审材料(零新数据,数字全带来源) | 来源标注自检 |

**触发方式**:自然语言即用(理需求/做 demo/怎么验证…);仅 pd-deliverables 须显式点名;可行性评审请求由独立技能承接,无双重触发。

## 骨架规则(整套的灵魂)

1. **埋点耦合**:pd-demo 交付必附埋点清单;pd-eval 凭此开工,没有就拒收转回——设计与验证硬闭环;
2. **两段式交付**:demo 先草稿(链路图+四态矩阵),用户确认后才生成代码;
3. **脚本把门**:需求清单/指标卡/交付物过校验脚本(exit 0)才准交付,模糊词直接拦截;
4. **变更纪律**:不改历史产物(新时间戳版本),ADR 只追加,推翻假设必须回流重验;
5. **零新数据**:交付文档是资产视图,每个数字标注来源产物。

## 测试与质量

- **触发测试**:`pd-suite/tests/trigger-cases.md` —— 11 条(6 召回 + 4 边界 + 1 重叠探测)全 PASS,含一次"写 PRD 误触发"的修复记录;
- **门禁实测**:模糊词指标卡拦截、缺埋点拒收、"跳过确认直接写代码"被规则顶回——对抗压测通过;
- **黄金集**:`plan-feasibility-review/tests/`(GC1–GC5 + 答案 key,冒烟通过,跑分待做);
- **失灵处理**:原话记入 `pd-suite/inbox.md` → 修 description → 全量回归。

## 版本历史

- v0.1.0(10-01):路由层 + 5 场景 + 3 校验脚本;专利包 5 机制移植(子技能不可触发/步骤即 prompts/两段式/软留档钩子/退出码纪律)
- v0.1.1(10-02):触发测评首轮,修复"写 PRD 误触发"边界
- v0.2.0(10-02):新增 pd-change、pd-deliverables,触发测试 11/11 PASS

## 依赖与环境

- 校验脚本需 Python:本机用 `S:\Anaconda\anaconda\python.exe`(PATH 里的 WindowsApps python 是占位符,退出码 49)
- pd-demo 的代码生成与自检可选联动官方技能:frontend-design / theme-factory / web-artifacts-builder / webapp-testing
- 文档转 Word/PPT 联动官方 docx / pptx 技能

## 数据飞轮(怎么让它越用越准)

1. 每次真实使用 → 按模板留档 `cases/`(输入/输出/三行标注);
2. 失灵(该醒没醒/不该醒乱醒)→ 原话进 `pd-suite/inbox.md` → 修 description → 回归;
3. 案例攒到 ≥3 条 → 升格进黄金测试集;
4. 改任何 SKILL.md → 全量重跑 trigger-cases → 通过才算改完。
