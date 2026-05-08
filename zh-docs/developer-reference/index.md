---
id: index
title: 介绍
meta: Infinite Flight Live 和 Connect API 参考
---

<a id="Developer Reference"></a>
<a id="developer reference"></a>
<a id="developer-reference"></a>
<a id="Developer%20Reference"></a>
<a id="developer%20reference"></a>
<a id="Developer Reference"></a>
<a id="developer reference"></a>
<a id="developer-reference"></a>
<a id="Developer%20Reference"></a>
<a id="developer%20reference"></a>
# 开发者参考



<a id="Guide Version: 25.1.0"></a>
<a id="guide version: 25.1.0"></a>
<a id="guide-version:-25.1.0"></a>
<a id="guide-version-2510"></a>
<a id="Guide%20Version%3A%2025.1.0"></a>
<a id="guide%20version%3A%2025.1.0"></a>
<a id="guide-version%3A-25.1.0"></a>
<a id="Guide Version: 25.1.0"></a>
<a id="guide version: 25.1.0"></a>
<a id="guide-version:-25.1.0"></a>
<a id="guide-version-2510"></a>
<a id="Guide%20Version%3A%2025.1.0"></a>
<a id="guide%20version%3A%2025.1.0"></a>
<a id="guide-version%3A-25.1.0"></a>
## 指南版本：25.1.0



Infinite Flight 为开发者提供了两个用于与我们的平台交互的 API，本节提供这些 API 的文档和参考指南。



<a id="Infinite Flight Live API"></a>
<a id="infinite flight live api"></a>
<a id="infinite-flight-live-api"></a>
<a id="Infinite%20Flight%20Live%20API"></a>
<a id="infinite%20flight%20live%20api"></a>
<a id="Infinite Flight Live API"></a>
<a id="infinite flight live api"></a>
<a id="infinite-flight-live-api"></a>
<a id="Infinite%20Flight%20Live%20API"></a>
<a id="infinite%20flight%20live%20api"></a>
## Infinite Flight Live API

Live API 是我们用于从 Infinite Flight 请求数据的 HTTP API。当前功能包括：

- 列出游戏中飞行员和 ATC 可用的服务器。
- 列出每个服务器上的活跃航班。
- 列出每个服务器上的活跃 ATC。
- 获取每个航班的飞行计划。
- 获取每个用户的统计数据。

需要 API 密钥，可通过发送电子邮件至 [hello@infiniteflight.com](mailto:hello@infiniteflight.com) 申请。文档请参见[概览](live-api/overview.md)。

在基于 Live API 开发之前，请阅读[使用和轮询最佳实践](live-api/best-practices.md)。Live API 数据只能用于临时缓存，必须不得持久化，也不得用于训练 AI 模型。

<a id="Infinite Flight Connect API"></a>
<a id="infinite flight connect api"></a>
<a id="infinite-flight-connect-api"></a>
<a id="Infinite%20Flight%20Connect%20API"></a>
<a id="infinite%20flight%20connect%20api"></a>
<a id="Infinite Flight Connect API"></a>
<a id="infinite flight connect api"></a>
<a id="infinite-flight-connect-api"></a>
<a id="Infinite%20Flight%20Connect%20API"></a>
<a id="infinite%20flight%20connect%20api"></a>
## Infinite Flight Connect API

Connect API 是我们用于与本地网络上运行的 Infinite Flight 设备交互的本地 TCP API。

- 发送命令以控制飞机系统或模拟器。
- 获取有关模拟的数据，包括飞机状态、ATC 指令等。

不需要 API 密钥。文档可在[这里](connect-api/overview.md)查看。

<a id="Which one should I use?"></a>
<a id="which one should i use?"></a>
<a id="which-one-should-i-use?"></a>
<a id="which-one-should-i-use"></a>
<a id="Which%20one%20should%20I%20use%3F"></a>
<a id="which%20one%20should%20i%20use%3F"></a>
<a id="which-one-should-i-use%3F"></a>
<a id="Which one should I use?"></a>
<a id="which one should i use?"></a>
<a id="which-one-should-i-use?"></a>
<a id="which-one-should-i-use"></a>
<a id="Which%20one%20should%20I%20use%3F"></a>
<a id="which%20one%20should%20i%20use%3F"></a>
<a id="which-one-should-i-use%3F"></a>
## 我应该使用哪一个？

**如果你正在构建一个用于查看某个服务器上 Live 数据的工具**，请使用 Live API。示例用途包括：

- 航班跟踪器
- ATC 状态网站
- 显示用户统计数据（等级、违规等）
- 查看飞行计划

**如果你正在构建一个用于与模拟器交互的工具**，请使用 Connect API。示例用途包括：

- 移动地图（如 ForeFlight）
- 本地交通查看器
- 自动检查单
- 在收到 ATC 指令时自动更新航向/高度