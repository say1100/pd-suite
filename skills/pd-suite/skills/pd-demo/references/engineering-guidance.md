# 工程规范·炼化版(engineering-guidance)
> 来源:web-artifacts-builder(官方)+ theme-factory(tokens)+ ui-ux-pro-max(tokens 三层/冲突检测)+ Impeccable(全原子提交)。
> 用法:pd-demo 阶段二 D5(tokens)与 D6(生成代码)的工程决策依据。

## 一、脚手架决策树

```
这个 demo 有多页面 / 状态管理 / 需要 shadcn 组件吗?
├─ 否(单页演示)→ 单 HTML 文件(内联 CSS/JS),零工程
└─ 是 → web-artifacts-builder 脚手架:
    bash scripts/init-artifact.sh <项目名>     # React18+TS+Vite+Tailwind+shadcn
    (40+ shadcn/ui 组件预装、@/ 路径别名、Parcel 打包配置、Node18+ 自动钉 Vite 版本)
    …开发…
    bash scripts/bundle-artifact.sh            # 打成单 HTML 交付
```

## 二、tokens 三层纪律(来源:ui-ux-pro-max + theme-factory)

1. **三层架构**:primitive(原始色板/字号)→ semantic(语义映射:primary/成功/危险)→ component(组件级引用)。**组件内禁裸 hex**——所有颜色/字号/间距必须引用 semantic 层;
2. **主题来源**:先从 theme-factory 的 10 套预设选一套改(不自创配色);主题选定时展示 theme-showcase.pdf 并等用户确认;
3. **同步与冲突检测**:品牌规范文件(brands/*.md)变更 → tokens 自动同步,检测到与组件硬编码冲突即报;
4. 配套:硬编码值扫描(全局搜裸 hex/px 字面量),命中即回 tokens 层。

## 三、代码工程纪律(来源:web-artifacts-builder + Impeccable)

1. **不造轮子**:shadcn 40 个组件现成的先用手搓;引入新依赖前先查工程内已有等价物;
2. **全原子提交**(Impeccable):导航/按钮/输入框全部使用新设计词汇——残留默认组件即失误;
3. **禁 AI slop 代码味**:官方点名规避:过度居中布局、紫色渐变、统一圆角、Inter 默认字体(细则见 design-guidance.md §五);
4. **Node 18+ 兼容**:脚手架自动检测并钉住 Vite 版本,不手动升级依赖;
5. **交付定义**:bundle 通过 + 页面无控制台报错,才算"代码完成"。

## 四、产物与路径

| 阶段 | 产物 | 位置 |
|---|---|---|
| 初始化 | React 工程 | 工作区 `<项目名>/` |
| 开发 | 组件/页面代码 | 工程内 src/ |
| 打包 | 单 HTML | `outputs/`(交付物) |
| 配套 | track-events.md | 与代码同目录(check_demo_gate 检查) |
