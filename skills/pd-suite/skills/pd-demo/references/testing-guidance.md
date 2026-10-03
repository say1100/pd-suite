# 测试规范·炼化版(testing-guidance)
> 来源:webapp-testing(官方)+ Playwright 官方 agent-cli skills + QA Skills.sh(设备仿真/网络节流)+ ui-ux-pro-max(UX 硬规则)。
> 用法:pd-demo D7(自检)与 pd-eval 数据采集验证的执行依据。

## 一、测试决策树(来源:webapp-testing 官方)

```
被测对象是静态 HTML?
├─ 是 → 直接读 HTML 找选择器 → 写 Playwright 脚本
│        (读不到/不完整 → 按动态处理)
└─ 否(动态应用)→ 服务已启动?
     ├─ 未启动 → python scripts/with_server.py --server "npm run dev" --port 5173 -- python 自动化脚本
     │           (双服务:--server 各写一条,自动管生命周期)
     └─ 已启动 → 侦察再行动:导航 → 等 networkidle → 截图/查 DOM
                → 从渲染态识别选择器 → 执行操作
```

铁律:chromium 一律 headless;先跑 `--help` 再用脚本(黑盒,不读源码污染上下文)。

## 二、升级路径:playwright-cli(来源:Playwright 官方 agent-cli)

裸写 Playwright 脚本的**命令驱动替代方案**(token 更省、流程更结构化):

```bash
playwright-cli install --skills=agents   # 装到 .agents/skills 布局(即本目录体系)
```

能力面:核心交互 / 快照与元素引用(refs)/ 会话管理(attach/detach)/ 请求 mock / 存储状态(cookies、localStorage)/ 测试生成与自愈 / tracing / 视频录制 / `run-code`(确需脚本时执行任意 Playwright 代码)。

采用建议:D7 自检先用快照+refs 的命令流;复杂断言才落到 `run-code`。

## 三、响应式与设备仿真(来源:QA Skills.sh + ui-ux-pro-max)

四态矩阵之外,补**第四维:屏宽**。每页至少三档核验:

| 档 | 视口 | 检查项 |
|---|---|---|
| 桌面 | 1280+ | 布局完整、无横向滚动 |
| 平板 | 768 | 栅格折叠正确、触控目标 ≥44px |
| 手机 | 375 | 单列、底部导航 ≤5 项、安全区、禁仅 hover、禁横向滚动/固定 px 容器 |

工具:Playwright 设备仿真(device emulation:视口/触屏/UA)+ **网络节流**(Slow 3G 下验证加载态/骨架屏真实出现)。

## 四、与 pd-demo/pd-eval 的对接

1. **四态核对**:每页 × (正常/空/错误/加载) 逐格截图,对照四态矩阵;
2. **P0 任务走查**:每条 P0 需求一条完整路径脚本(进入→操作→结果),存截图;
3. **控制台日志**:零报错才算过(有报错 = 回 D6 修,不是口头解释);
4. **产出台账**:截图 + 日志 + 通过/失败结论,归档到交付目录,供 check_demo_gate 与 pd-eval 引用;
5. **埋点验证**:问数操作时确认 track-events 事件真实发出(网络面板可见)——这是 demo↔eval 耦合的执行证据。
