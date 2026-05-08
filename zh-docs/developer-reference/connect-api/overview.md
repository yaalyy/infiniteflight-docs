---
id: overview
title: 概览
meta: Infinite Flight Connect API 概览
order: 1
contributor: KaiM
---

<a id="Infinite Flight Connect API Overview"></a>
<a id="infinite flight connect api overview"></a>
<a id="infinite-flight-connect-api-overview"></a>
<a id="Infinite%20Flight%20Connect%20API%20Overview"></a>
<a id="infinite%20flight%20connect%20api%20overview"></a>
<a id="Infinite Flight Connect API Overview"></a>
<a id="infinite flight connect api overview"></a>
<a id="infinite-flight-connect-api-overview"></a>
<a id="Infinite%20Flight%20Connect%20API%20Overview"></a>
<a id="infinite%20flight%20connect%20api%20overview"></a>
# Infinite Flight Connect API 概览

Connect API 是我们用于获取特定数据并在飞行中执行操作的本地 TCP API。示例包括：

- 开关灯光
- 控制自动驾驶
- 控制网络摇杆

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

Connect API 有两个版本 - v1 和 v2 - 分别可通过端口 `10111` 和 `10112` 使用。版本 1 使用字符串形式的 JSON 对象，而版本 2 支持多种格式，并提供更多功能。

要使用 Connect API，用户必须先启用它。为此，用户可以按照以下步骤操作。

步骤 1
: 打开 Infinite Flight

步骤 2
: 进入 设置 > 常规

步骤 3
: 滚动到页面底部，找到“启用 Infinite Flight Connect”

步骤 4
: 如果尚未勾选，请勾选该复选框

请注意，Connect API 默认处于禁用状态。

<a id="API Keys"></a>
<a id="api keys"></a>
<a id="api-keys"></a>
<a id="API%20Keys"></a>
<a id="api%20keys"></a>
<a id="API Keys"></a>
<a id="api keys"></a>
<a id="api-keys"></a>
<a id="API%20Keys"></a>
<a id="api%20keys"></a>
## API 密钥

Connect API 不需要 API Key。

<a id="Prerequisites"></a>
<a id="prerequisites"></a>
<a id="Prerequisites"></a>
<a id="prerequisites"></a>
## 前提条件

本文档面向已了解以下内容的人：

- Transmission Control Protocol (TCP)
- 数据类型
- JSON
- Infinite Flight 操作

如果你对这些领域不熟悉，当然也欢迎继续浏览文档。你也可以查看以下资源来帮助学习。

- [什么是 TCP/IP？ | Cloudflare](https://www.cloudflare.com/learning/ddos/glossary/tcp-ip/)
- [W3Schools - C# 数据类型](https://www.w3schools.com/cs/cs_data_types.asp)
- [W3Schools - JSON 简介](https://www.w3schools.com/js/js_json_intro.asp)
- [Infinite Flight 飞行指南](../../flying-guide/index.md)