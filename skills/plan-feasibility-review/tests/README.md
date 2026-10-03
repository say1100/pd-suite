# 测试资产总览(plan-feasibility-review)

> 搜集日期:2026-09-30|状态:✅ 已搜集,⬜ 待检测/待回填

## 一、资产清单(四类)

| 类别 | 文件 | 内容 | 状态 |
|---|---|---|---|
| ① 执行黄金集 | [golden-cases.md](golden-cases.md) | 5 用例正文:GC1 埋雷SaaS / GC2 埋雷硬件 / GC3 埋雷AI医疗 / GC4 好计划 / GC5 缺料 | ✅ 已搜集,⬜ 未跑分 |
| ① 答案 key | [golden-answers.md](golden-answers.md) | 埋雷点 6+6+6 逐条、GC4 观察项边界、GC5 期望行为、评分口径、封版线 | ✅(检测时才看) |
| ② 触发测试集 | [trigger-cases.md](trigger-cases.md) | 召回组 R1–R5 + 边界组 B1–B7,共 12 条,含预期 | ✅ R1–R2/B1–B3 已实测 PASS;⬜ R3–R5/B4–B7 待测 |
| ③ 案例库 | [../cases/](../cases/) | 用例留档(含通用模板);首次使用从模板开始 | ✅ 模板就绪 |
| ④ 范例(few-shot) | [../references/examples/范例清单.md](../references/examples/范例清单.md) | 3 份结构要点(BP要素链/尽调骨架/PRD验收写法)+ 待补清单 | ✅ 结构版;⬜ 真实范例待你确认 |

## 二、你检测的三步(每步约 10 分钟)

1. **测执行(核心)**:新会话 → 把 golden-cases.md 里任一用例的引文原文粘贴发送 → 报告对照 golden-answers.md 打分(命中/误报/结构/证据四栏)。五个用例都跑或先跑 GC3(最难)+GC4(误报);
2. **测触发**:新会话发 trigger-cases.md 里 R3–R5、B4–B7 任一口吻 → 看是否按预期触发/不触发;
3. **验案例**:CASE-0001 标注两行回填;范例清单"待补"处丢一份你认可的真实文档路径。

## 三、失灵处理规矩

任何一步出现误报/漏报/边界失守:**原话原封不动**记到 trigger-cases.md 的"失灵记录"区 → 通知我修 SKILL.md → 全量回归(①+②所有用例重跑)→ 通过才封版。

## 四、这份测试集的第二个用途

它是 `pd-suite` 四个子技能(pd-requirements / pd-concept / pd-demo / pd-eval)测试集的**结构模板**:每个照抄"用例正文 / 答案key / 触发口吻 / 案例库"四件套即可,埋雷思路不变,领域内容换成各自的。
