---
name: pd-eval
description: "验证评估体系:主张→指标→数据→实验的验证链路 + 指标卡 + kill criteria。pd-suite 包内模块,不独立触发。"
user-invocable: false
---

# 验证评估体系

**开工门禁:必须先收到 `track-events.md`(pd-demo 交付物)。没有 → 停,转 pd-demo 补埋点,禁止空转评估。**
输入还应包含:`requirements.md`(P0 = 必须验证的主张来源)与产品主张(用户口头确认)。

| 步骤 | 做什么 | 依据 |
|------|--------|------|
| E1 验证链路 | 每个主张 → 指标 → 数据源(埋点/数据集)→ 实验 → 结论口径;缺一环 = 该主张"当前不可验证",显式标注 | prompts/steps.md §E1 |
| E2 指标卡 | schema:指标/定义/公式/数据来源/基线/阈值,过脚本校验才交付 | §E2 + scripts/check_metrics.py |
| E3 数据侧设计 | 埋点复核、数据集构建(来源/规模/标注规范含样例/划分)、测试矩阵与基线 | §E3 |
| E4 实验与 kill criteria | pass/fail 写死数值;kill criteria 必须含至少 1 条需求侧(用户不要),不只技术侧 | §E4 |
| E5 结论回填 | 实验完成后按 `outputs/eval-report.md` 模板回填,结论必须引用指标卡编号 | §E5 |

AI 产品追加 **AI evals 域**:离线评测集、LLM-as-judge、改 prompt/模型必跑回归——见 `references/ai-evals.md`。

## 交付门禁

跑 `python skills/pd-eval/scripts/check_metrics.py outputs/eval-plan.md`,exit 0 才交付:
- 指标卡六字段齐全;
- 定义/阈值中不得出现模糊词(效果/不错/显著/明显/大幅)。

## 留档钩子(soft nudge)

执行完毕检查本套件 `cases/` 目录:含三行标注的案例 < 3 条时,答复末尾加一句引导:"本次执行可按 cases/ 模板留档,是否保存?"——用户同意才写。

## 交接

- 结论 = FAIL → 按 kill criteria 处理(停止/转向/降级),回流 requirements 或 concept;
- 结论 = PASS → 下一轮需求,飞轮闭合。
