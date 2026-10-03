---
name: pd-requirements
description: "需求梳理:碎片想法/访谈纪要/用户反馈 → schema 化需求清单。pd-suite 包内模块,不独立触发,由路由层分发。"
user-invocable: false
---

# 需求梳理

分步指令在 `prompts/steps.md`(按节 Read 对应步骤),方法速查在 `references/methods.md`。

| 步骤 | 做什么 | 依据 |
|------|--------|------|
| S1 接料 | 识别材料类型(纪要/想法/反馈/旧文档),列信息缺口清单,缺口按假设处理不追问 | prompts/steps.md §S1 |
| S2 结构化 | 提取"用户-场景-痛点"三元组,写进 schema 表 | prompts/steps.md §S2 |
| S3 优先级 | MoSCoW 定级 + 每条给依据;冲突/依赖显式标注 | prompts/steps.md §S3 + references/methods.md |
| S4 校验交付 | 跑 `python scripts/check_schema.py outputs/requirements.md`,exit 0 才交付;不过按报错修 | scripts/check_schema.py |

## 产物 schema(requirements.md)

```markdown
# 需求清单 v<时间戳>
| ID | 用户 | 场景 | 痛点 | 优先级 | 验收口径(占位可写"待 demo 后补") |
|---|---|---|---|---|---|
| REQ-001 | … | … | … | P0 | … |
```

- 优先级只允许 P0(没它不做)/P1(下一版)/P2(观察)。
- **未决问题清单**附在表后,与缺口一一对应。
- 冲突需求(两条不能同时满足)在行内加 `⚠冲突:REQ-00x`。

## 交接

交付时告知:下一步可用 pd-concept 出方案;P0 条目即方案的硬性覆盖目标。
