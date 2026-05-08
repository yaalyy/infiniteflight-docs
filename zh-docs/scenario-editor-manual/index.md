---
id: index
title: 简介
meta: 通过我们的在线文档了解如何使用 Infinite Flight 场景编辑器。
---

<a id="Welcome to the Scenario Editor overview!"></a>
<a id="welcome to the scenario editor overview!"></a>
<a id="welcome-to-the-scenario-editor-overview!"></a>
<a id="welcome-to-the-scenario-editor-overview"></a>
<a id="Welcome%20to%20the%20Scenario%20Editor%20overview%21"></a>
<a id="welcome%20to%20the%20scenario%20editor%20overview%21"></a>
<a id="welcome-to-the-scenario-editor-overview%21"></a>
<a id="Welcome to the Scenario Editor overview!"></a>
<a id="welcome to the scenario editor overview!"></a>
<a id="welcome-to-the-scenario-editor-overview!"></a>
<a id="welcome-to-the-scenario-editor-overview"></a>
<a id="Welcome%20to%20the%20Scenario%20Editor%20overview%21"></a>
<a id="welcome%20to%20the%20scenario%20editor%20overview%21"></a>
<a id="welcome-to-the-scenario-editor-overview%21"></a>
# 欢迎查看场景编辑器概览！

本文旨在带你了解 Infinite Flight 场景编辑器的基础知识。

重要
: 这个工具仍在开发中，我们非常欢迎你在使用过程中提供反馈！如果你有具体反馈或任何疑问，请联系 Cameron 或 Laura。

<a id="What is a scenario?"></a>
<a id="what is a scenario?"></a>
<a id="what-is-a-scenario?"></a>
<a id="what-is-a-scenario"></a>
<a id="What%20is%20a%20scenario%3F"></a>
<a id="what%20is%20a%20scenario%3F"></a>
<a id="what-is-a-scenario%3F"></a>
<a id="What is a scenario?"></a>
<a id="what is a scenario?"></a>
<a id="what-is-a-scenario?"></a>
<a id="what-is-a-scenario"></a>
<a id="What%20is%20a%20scenario%3F"></a>
<a id="what%20is%20a%20scenario%3F"></a>
<a id="what-is-a-scenario%3F"></a>
## 什么是场景？

场景是 Infinite Flight 中具有特定目标或一组目标的一个会话。它可以是：

 - 飞行训练课程（例如，如何降落飞机）
 - 挑战（例如，降落航天飞机）
 - 任务（例如，飞行一条特定航线）

场景编辑器的创建，旨在帮助你在 Infinite Flight 中构建交互式体验。你可以访问 Infinite Flight 中所有模拟器状态来构建场景，这些场景可以提示用户执行特定操作，然后根据他们的输入执行更多操作。

<a id="Accessing The Scenario Editor"></a>
<a id="accessing the scenario editor"></a>
<a id="accessing-the-scenario-editor"></a>
<a id="Accessing%20The%20Scenario%20Editor"></a>
<a id="accessing%20the%20scenario%20editor"></a>
<a id="Accessing The Scenario Editor"></a>
<a id="accessing the scenario editor"></a>
<a id="accessing-the-scenario-editor"></a>
<a id="Accessing%20The%20Scenario%20Editor"></a>
<a id="accessing%20the%20scenario%20editor"></a>
## 访问场景编辑器

要使用场景编辑器，你必须由 Infinite Flight 团队成员注册。此功能目前仅限邀请使用。如果你无法访问，请联系你在 Infinite Flight 的联系人。

步骤 1

: 找到你设备的 IP 地址。在 iOS 和 Android 上，这可以在“设置 -> WiFi”中找到，位于你的本地 WiFi 网络下。

步骤 2

: 打开你通过 TestFlight 收到的 Infinite Flight 测试版最新版本。

步骤 3

: 保持 Infinite Flight 在你的手机或平板上运行，并在另一台电脑上在浏览器中打开以下地址：`http://[DEVICE IP]:4090`。例如，如果你的设备 IP 是 `192.168.0.5`，你应打开 `http://192.168.0.5:4090`。

步骤 4

: 场景编辑器应在你的网页浏览器中打开，左侧边栏应显示 `已连接` 图标

<a id="Troubleshooting"></a>
<a id="troubleshooting"></a>
<a id="Troubleshooting"></a>
<a id="troubleshooting"></a>
#### 故障排查

如果你无法打开编辑器，请检查以下内容：

 - 你的 Infinite Flight 设备是否已登录？
 - 两台设备是否连接到同一个 WiFi 网络？
 - 你是否确实正在使用 Infinite Flight 测试版？

如有疑问，请联系 Cameron 获取更多帮助。

<a id="Scenario Editor Overview"></a>
<a id="scenario editor overview"></a>
<a id="scenario-editor-overview"></a>
<a id="Scenario%20Editor%20Overview"></a>
<a id="scenario%20editor%20overview"></a>
<a id="Scenario Editor Overview"></a>
<a id="scenario editor overview"></a>
<a id="scenario-editor-overview"></a>
<a id="Scenario%20Editor%20Overview"></a>
<a id="scenario%20editor%20overview"></a>
## 场景编辑器概览

场景编辑器由顶部工具栏和一个主编辑窗口组成，工具栏包含常用操作。它有 3 个主要选项卡 - 查看各子页面以获取更具体的信息：

 - **配置场景**：元数据和配置
 - **步骤**：定义操作和完成条件
 - **失败条件**：会导致场景失败的场景级操作