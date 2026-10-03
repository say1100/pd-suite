# 安装指南

## 这是什么

两个用于产品设计的 Agent Skills:

- **pd-suite** —— 产品设计全流程套件:需求梳理 → 方案对比 → 可行性评审 → Demo 设计 → 验证评估 → 变更记录 → 交付文档
- **plan-feasibility-review** —— 独立的可行性评审技能(被 pd-suite 调用,也可单独触发)

兼容所有支持 Agent Skills 标准的工具(Claude Code、Codex CLI、Gemini CLI、Cursor 等发现路径相同的工具)。

## 安装(三种方式任选)

### 方式 A:复制安装(通用)

把仓库里的两个技能文件夹完整复制到你的用户级技能目录:

- Windows: `C:\Users\<你>\.agents\skills\`(本仓库的 `skills/` 下两个文件夹)
- macOS / Linux: `~/.agents/skills/`

> 目标目录不存在就新建。想要只对某个项目生效,则复制到 `<项目>/.agents/skills/`。

### 方式 B:git clone

```bash
cd ~/.agents/skills        # Windows: cd C:\Users\<你>\.agents\skills
git clone <本仓库地址> pd-suite-repo
# 然后把 pd-suite-repo/skills/pd-suite 与 plan-feasibility-review 拷到上一级,或直接保留引用
```

### 方式 C:逐文件复制后验证

安装后新开会话,输入:"帮我看看这个计划靠不靠谱:……(随便一个产品想法)"
→ 若技能被触发并输出结构化评审报告,即安装成功。

## 依赖

| 组件 | 是否必需 | 说明 |
|---|---|---|
| Python 3.9+ | 推荐(校验脚本用) | Windows 注意:应用商店占位符 python 会以退出码 49 报错,请安装真实 Python |
| pip 包 | 无(校验脚本纯标准库) | — |
| 配套技能(可选) | 否 | frontend-design / theme-factory / web-artifacts-builder / webapp-testing(Anthropic 官方仓库)增强 demo 能力;docx/pptx(文档技能)增强交付能力 |

## 使用 60 秒上手

| 你说 | 触发 |
|---|---|
| "帮我看看这个计划靠不靠谱……" | plan-feasibility-review 评审 |
| "帮我把这些反馈整理成需求清单" | pd-suite → 需求梳理 |
| "这两个方案帮我对比一下" | pd-suite → 方案对比 |
| "做个 demo,交互流程帮我设计" | pd-suite → Demo 设计(两段式:先草稿确认再代码) |
| "这个功能怎么验证?定一下指标" | pd-suite → 验证评估 |
| "改成 XX 了,影响哪些东西?" | pd-suite → 变更影响 + ADR |
| "写一份 PRD / 出份汇报"(需显式) | pd-suite → 交付文档(零新数据) |

## 已知限制

- 触发词按中文口吻优化(含部分英文),纯英文交流触发率可能降低——可自行改各 SKILL.md 的 description;
- Demo 阶段的可视化自检需要安装 Playwright(`pip install playwright && playwright install`);
- 欢迎提 Issue 反馈触发失灵(误触发/漏触发),原话即可——这直接帮助改进触发边界。
