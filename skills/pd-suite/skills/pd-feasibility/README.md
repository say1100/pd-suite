# pd-feasibility(转发件)

本子技能**不重复实现**评审逻辑,转发到已装技能:

- 技能:`plan-feasibility-review`(安装于 `~/.agents/skills/plan-feasibility-review/`)
- 转发方式:把用户方案/计划 + pd-suite 上下文(目标用户、竞品、来自 requirements 的 P0 清单、来自 tradeoff-matrix 的推荐方案)作为输入,按该技能的流程(含黄金测试集口径)执行评审。
- 触发词:可行性 / 靠谱 / 能不能成 / 评估这个方案。
- 产出沿用其报告模板(GO/有条件 GO/PIVOT/NO-GO + 关键假设 + Kill criteria + 下一步)。

PIVOT/NO-GO 时回到 pd-concept 换候选方案;GO 时进入 pd-demo。
