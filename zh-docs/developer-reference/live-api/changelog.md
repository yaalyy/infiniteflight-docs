---
id: changelog
title: 变更日志
meta: 记录 Infinite Flight Live API 的更改
order: 2
---

<a id="Changelog"></a>
<a id="changelog"></a>
<a id="Changelog"></a>
<a id="changelog"></a>
# 变更日志

本文档记录 Infinite Flight Live API 的更改

<a id="2026-03-18"></a>
<a id="2026-03-18"></a>
## 2026-03-18
- 新增 [Get Flight Plans (Bulk)](flight-plans.md) 端点（`POST /v2/sessions/{sessionId}/flights/flightplans`）——可在单次请求中获取最多 25 个航班的详细 flight plan。
- 修复了一个问题：在缓存刷新周期内，Flights 端点偶尔会返回不完整的航班列表。

<a id="2026-03-17"></a>
<a id="2026-03-17"></a>
## 2026-03-17
- 将默认 Live API 速率限制下调为每个 API key 每分钟 30 次请求。
- 为与处于有效付费 Pro 订阅的用户关联的 API key 新增更高的默认速率限制：每分钟 100 次请求。
- 新增 [使用和轮询最佳实践](best-practices.md)，包括仅限临时缓存的存储规则，以及明确禁止将 Live API 数据用于 AI 训练。

<a id="2024-04-12"></a>
<a id="2024-04-12"></a>
## 2024-04-12
- 在 [Flights endpoint](flights.md) 中新增 `pilotState` 字段
  - 新的枚举字段用于指示飞行员状态：`Active = 0`、`AwayInFlight = 1`、`AwayParked = 2`、`InBackground = 3`
- 修复了 [ATC endpoint](atc.md) 中缺失的 `airportLatitude` 和 `airportLongitude`。