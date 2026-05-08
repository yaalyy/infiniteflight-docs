---
id: overview
title: 概述
meta: Infinite Flight Live API 概述
order: 1
---

<a id="Infinite Flight Live API Overview"></a>
<a id="infinite flight live api overview"></a>
<a id="infinite-flight-live-api-overview"></a>
<a id="Infinite%20Flight%20Live%20API%20Overview"></a>
<a id="infinite%20flight%20live%20api%20overview"></a>
<a id="Infinite Flight Live API Overview"></a>
<a id="infinite flight live api overview"></a>
<a id="infinite-flight-live-api-overview"></a>
<a id="Infinite%20Flight%20Live%20API%20Overview"></a>
<a id="infinite%20flight%20live%20api%20overview"></a>
# Infinite Flight Live API 概述

Live API 是我们用于从 Infinite Flight 服务器请求数据的 HTTP API。当前功能包括：

- 列出游戏内可用的飞行员和 ATC 服务器。
- 列出每个服务器上的活动航班。
- 列出每个服务器上的活动 ATC。
- 获取每个航班的飞行计划。
- 获取用户统计数据。

⚠️

: 此 API 仅用于模拟飞行，不得用于现实世界的飞行场景。

<a id="Obtaining an API key"></a>
<a id="obtaining an api key"></a>
<a id="obtaining-an-api-key"></a>
<a id="Obtaining%20an%20API%20key"></a>
<a id="obtaining%20an%20api%20key"></a>
<a id="Obtaining an API key"></a>
<a id="obtaining an api key"></a>
<a id="obtaining-an-api-key"></a>
<a id="Obtaining%20an%20API%20key"></a>
<a id="obtaining%20an%20api%20key"></a>
## 获取 API 密钥

使用 Live API 需要 API 密钥。请联系 [hello@infiniteflight.com](mailto:hello@infiniteflight.com)，告知我们你计划构建的内容并申请密钥。

<a id="How to use the API"></a>
<a id="how to use the api"></a>
<a id="how-to-use-the-api"></a>
<a id="How%20to%20use%20the%20API"></a>
<a id="how%20to%20use%20the%20api"></a>
<a id="How to use the API"></a>
<a id="how to use the api"></a>
<a id="how-to-use-the-api"></a>
<a id="How%20to%20use%20the%20API"></a>
<a id="how%20to%20use%20the%20api"></a>
## 如何使用 API

Live API 使用 HTTP，端点需要你向端点 URL 发起 GET 或 POST 请求。具体细节请参见各个端点的文档。

<a id="Conditions of Use"></a>
<a id="conditions of use"></a>
<a id="conditions-of-use"></a>
<a id="Conditions%20of%20Use"></a>
<a id="conditions%20of%20use"></a>
<a id="Conditions of Use"></a>
<a id="conditions of use"></a>
<a id="conditions-of-use"></a>
<a id="Conditions%20of%20Use"></a>
<a id="conditions%20of%20use"></a>
## 使用条件

- 如果应用没有被使用，所有应用都必须具备超时功能。我们不希望用户让应用运行数小时却无人查看。如果 15 分钟内没有任何操作，请让你的应用停止下载新内容，直到用户按下按钮为止（FlightRadar24 在其网站上就是这样做的）。

- Live API 数据只能存储在为支持你的应用所必需的临时缓存中。禁止永久存储、数据仓库、复制，或将 Live API 数据保留在你自己的数据库中。

- Infinite Flight 保留 Live API 数据的所有权。你不得使用 Live API 数据来训练、微调、评估、蒸馏、ground，或以其他方式改进 AI 或机器学习模型。

- 如果我们检测到被禁止的存储或 AI 训练用途，API 密钥及相关用户账户可能会被禁止访问 API。

  如果你需要 API 的其他功能，请联系我们。

- 在部署应用或将 API 与 LLM 集成之前，请先查看[使用和轮询最佳实践](best-practices.md)。

<a id="Prerequisites"></a>
<a id="prerequisites"></a>
<a id="Prerequisites"></a>
<a id="prerequisites"></a>
## 前提条件

本文档面向对以下内容有了解的人：

- HTTP
- JSON
- Infinite Flight System（等级、服务器等）

如果你对这些领域不熟悉，也欢迎浏览本文档。你还可以查看以下资源来帮助学习。

- [W3Schools - 什么是 HTTP？](https://www.w3schools.com/whatis/whatis_http.asp)
- [W3Schools - JSON 介绍](https://www.w3schools.com/js/js_json_intro.asp)
- [Infinite Flight 用户指南](../../getting-started-guide/home-user-interface/user-profile.md#the-grade-table)