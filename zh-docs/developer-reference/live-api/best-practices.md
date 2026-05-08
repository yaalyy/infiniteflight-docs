---
id: best-practices
title: 使用和轮询最佳实践
meta: Infinite Flight Live API 的速率限制、轮询频率、缓存以及禁止的存储和 AI 训练规则
order: 2
---

<a id="Usage and Polling Best Practices"></a>
<a id="usage and polling best practices"></a>
<a id="usage-and-polling-best-practices"></a>
<a id="Usage%20and%20Polling%20Best%20Practices"></a>
<a id="usage%20and%20polling%20best%20practices"></a>
<a id="Usage and Polling Best Practices"></a>
<a id="usage and polling best practices"></a>
<a id="usage-and-polling-best-practices"></a>
<a id="Usage%20and%20Polling%20Best%20Practices"></a>
<a id="usage%20and%20polling%20best%20practices"></a>
# 使用和轮询最佳实践

在部署 Live API 集成之前，请遵循以下规则。

<a id="Rate Limits"></a>
<a id="rate limits"></a>
<a id="rate-limits"></a>
<a id="Rate%20Limits"></a>
<a id="rate%20limits"></a>
<a id="Rate Limits"></a>
<a id="rate limits"></a>
<a id="rate-limits"></a>
<a id="Rate%20Limits"></a>
<a id="rate%20limits"></a>
## 速率限制

- 默认限制：每个 API 密钥每分钟 30 次请求。
- 当 API 密钥关联到拥有有效付费 Pro 订阅的用户账户时，默认限制提高到每分钟 100 次请求。
- 如果关联的 Pro 订阅失效，该密钥将恢复为免费层默认限制。
- 如果由于应用人气过高而无法遵守速率限制（恭喜！），请联系 hello@infiniteflight.com，我们会评估是否提高你的速率限制。
- 超出限制时会返回 HTTP `429 Too Many Requests`。

<a id="Polling Guidance"></a>
<a id="polling guidance"></a>
<a id="polling-guidance"></a>
<a id="Polling%20Guidance"></a>
<a id="polling%20guidance"></a>
<a id="Polling Guidance"></a>
<a id="polling guidance"></a>
<a id="polling-guidance"></a>
<a id="Polling%20Guidance"></a>
<a id="polling%20guidance"></a>
## 轮询建议

不要把 Live API 当作流式数据源来轮询。请使用尽可能慢、但仍能满足你的产品需求的频率。

| 端点 | 建议的最小间隔 | 说明 |
| --- | --- | --- |
| `GET /sessions` | 10 分钟 | 这些数据会在服务器端缓存 10 分钟，而且变化不频繁。 |
| `GET /sessions/{sessionId}` | 10 分钟 | 除非用户明确刷新，否则将会话元数据与会话列表按同样方式处理。 |
| `GET /sessions/{sessionId}/flights` | 15 秒 | 航班列表是短生命周期的缓存数据，不需要每 15 秒以下轮询。 |
| `GET /sessions/{sessionId}/flights/{flightId}` | 15 秒 | 如有可能，重复利用列表响应，而不是反复获取单个航班。 |
| `GET /sessions/{sessionId}/atc` | 15 秒 | 谨慎轮询，并且只在用户正在主动查看数据时轮询。 |
| `GET /sessions/{sessionId}/airport/{icao}/status` | 15 秒 | 除非 UI 可见，否则避免并行轮询多个机场视图。 |
| 用户历史端点 | 5 分钟或更长 | 历史和个人资料类数据应当尽量积极缓存。 |

<a id="Caching Expectations"></a>
<a id="caching expectations"></a>
<a id="caching-expectations"></a>
<a id="Caching%20Expectations"></a>
<a id="caching%20expectations"></a>
<a id="Caching Expectations"></a>
<a id="caching expectations"></a>
<a id="caching-expectations"></a>
<a id="Caching%20Expectations"></a>
<a id="caching%20expectations"></a>
## 缓存要求

- 允许且预期使用临时缓存。
- 会话数据至少缓存 10 分钟。
- 航班和 ATC 数据至少缓存 15 秒。
- 当应用处于空闲状态时停止轮询。如果 15 分钟内没有任何用户操作，就停止下载新内容，直到用户恢复交互。

<a id="Prohibited Data Use"></a>
<a id="prohibited data use"></a>
<a id="prohibited-data-use"></a>
<a id="Prohibited%20Data%20Use"></a>
<a id="prohibited%20data%20use"></a>
<a id="Prohibited Data Use"></a>
<a id="prohibited data use"></a>
<a id="prohibited-data-use"></a>
<a id="Prohibited%20Data%20Use"></a>
<a id="prohibited%20data%20use"></a>
## 禁止的数据使用

- 不得将 Live API 数据持久化到短生命周期的运行时缓存之外。
- 不得将 Live API 数据复制到你自己的长期数据库、分析仓库或训练语料库中。
- 不得使用 Live API 数据训练、微调、评估、蒸馏、作为检索增强上下文，或以其他方式改进 AI 或机器学习模型。
- Infinite Flight 保留 Live API 返回数据的所有权。

如果我们检测到被禁止的存储、抓取或 AI 训练用途，API 密钥及相关账户可能会被禁止使用该 API。

<a id="LLM Integrations"></a>
<a id="llm integrations"></a>
<a id="llm-integrations"></a>
<a id="LLM%20Integrations"></a>
<a id="llm%20integrations"></a>
<a id="LLM Integrations"></a>
<a id="llm integrations"></a>
<a id="llm-integrations"></a>
<a id="LLM%20Integrations"></a>
<a id="llm%20integrations"></a>
## LLM 集成

如果你在运行时向 LLM 提供 Live API 数据：

- 只发送回答当前用户请求所需的最少数据。
- 在获取新数据前，遵守上面的轮询间隔。
- 不要保留 Live API 响应用于后续模型训练、调优、评估或数据集创建。
- 优先为用户总结当前结果，而不是重复重新获取同一端点。

你也可以向 LLM 提供一份 Live API 参考文档的单个 llms.txt 作为上下文：[下载 Live API llms.txt](/llms.txt)。