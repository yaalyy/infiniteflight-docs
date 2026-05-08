---
id: atis
title: 获取 ATIS
meta: Infinite Flight Live API 的 ATIS 端点概览
order: 11
contributor: KaiM
---

<a id="Get Airport ATIS"></a>
<a id="get airport atis"></a>
<a id="get-airport-atis"></a>
<a id="Get%20Airport%20ATIS"></a>
<a id="get%20airport%20atis"></a>
<a id="Get Airport ATIS"></a>
<a id="get airport atis"></a>
<a id="get-airport-atis"></a>
<a id="Get%20Airport%20ATIS"></a>
<a id="get%20airport%20atis"></a>
# 获取机场 ATIS

如果机场的 ATIS 处于活动状态，则检索特定服务器上的该 ATIS。

⚠️

: 此 API 仅用于模拟飞行，不得用于真实世界飞行情境。

<a id="Resource"></a>
<a id="resource"></a>
<a id="Resource"></a>
<a id="resource"></a>
## 资源

**GET** `https://api.infiniteflight.com/public/v2/sessions/{sessionId}/airport/{airportIcao}/atis`

<a id="Authorization"></a>
<a id="authorization"></a>
<a id="Authorization"></a>
<a id="authorization"></a>
## 授权

通过以下任一方式包含你的 API 密钥（`<apikey>`）：

- 添加 `apikey` 查询参数。例如，`?apikey=<apikey>`。
- 使用你的 API 密钥发送 bearer 授权头。例如，`Authorization: Bearer <apikey>`。

<a id="Parameters"></a>
<a id="parameters"></a>
<a id="Parameters"></a>
<a id="parameters"></a>
## 参数

| 名称           | 位于       | 描述                                 | 必需 | Schema        |
| -------------- | ---------- | ------------------------------------ | ---- | ------------- |
| `airportIcao`  | query      | 要获取 ATIS 的机场 ICAO              | 是   | string        |
| `sessionId`    | query      | Live Server 的会话（服务器）ID       | 是   | string (uuid) |

<a id="Response"></a>
<a id="response"></a>
<a id="Response"></a>
<a id="response"></a>
## 响应

<a id="Sample Response"></a>
<a id="sample response"></a>
<a id="sample-response"></a>
<a id="Sample%20Response"></a>
<a id="sample%20response"></a>
<a id="Sample Response"></a>
<a id="sample response"></a>
<a id="sample-response"></a>
<a id="Sample%20Response"></a>
<a id="sample%20response"></a>
#### 示例响应

```json
{
    "errorCode":0,
    "result":"Manchester Airport, ATIS information DELTA, time 2355 ZULU, Wind 350 at 6 Visibility 21, Temperature 2, Dew Point 0, QNH 1024. Remarks, no pattern work allowed, no light aircraft accepted at this time. Landing Runways 05L and 05R, Departing Runways 05L and 05R. Advise on initial contact, you have information DELTA."
}
```

<a id="LiveAPIResponse"></a>
<a id="liveapiresponse"></a>
<a id="LiveAPIResponse"></a>
<a id="liveapiresponse"></a>
#### LiveAPIResponse

*响应类型:* `application/json`

| 名称        | 类型    | 描述                                                         |
| ----------- | ------- | ------------------------------------------------------------ |
| `errorCode` | integer | _枚举:_ `"Ok = 0"`, `"UserNotFound = 1"`, `"MissingRequestParameters = 2"`, `"EndpointError = 3"`, `"NotAuthorized = 4"`, `"ServerNotFound = 5"`, `"FlightNotFound = 6"`, `"NoAtisAvailable = 7"` |
| `result`    | string  | ATIS；如果不可用则为 `null`                                    |