---
id: oceanic-tracks
title: 获取海洋航线
meta: Infinite Flight Live API 海洋航线端点概览
order: 14
---

<a id="Get Oceanic Tracks"></a>
<a id="get oceanic tracks"></a>
<a id="get-oceanic-tracks"></a>
<a id="Get%20Oceanic%20Tracks"></a>
<a id="get%20oceanic%20tracks"></a>
<a id="Get Oceanic Tracks"></a>
<a id="get oceanic tracks"></a>
<a id="get-oceanic-tracks"></a>
<a id="Get%20Oceanic%20Tracks"></a>
<a id="get%20oceanic%20tracks"></a>
# 获取海洋航线

检索 Infinite Flight 多人会话中处于激活状态的海洋航线列表。

⚠️

: 此 API 仅用于模拟飞行，不得用于真实世界的飞行场景。

<a id="Resource"></a>
<a id="resource"></a>
<a id="Resource"></a>
<a id="resource"></a>
## 资源

**GET** `https://api.infiniteflight.com/public/v2/tracks`

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

*无需参数。*

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
  "errorCode": 0,
  "result": [
    {
      "name": "A",
      "path": [
        "DINIM",
        "51/20",
        "51/30",
        "50/40",
        "49/50",
        "JOOPY"
      ],
      "eastLevels": null,
      "westLevels": [
        350,
        370,
        390
      ],
      "type": "North Atlantic Tracks",
      "lastSeen": "2021-01-06T18:49:33.6300772Z"
    }
  ]
}
```

<a id="LiveAPIResponse"></a>
<a id="liveapiresponse"></a>
<a id="LiveAPIResponse"></a>
<a id="liveapiresponse"></a>
#### LiveAPIResponse

*响应类型:* `application/json`

| 名称        | 类型          | 描述                                                     |
| ----------- | ------------- | -------------------------------------------------------- |
| `errorCode` | integer       | _枚举:_ `"Ok = 0"`、`"UserNotFound = 1"`、`"MissingRequestParameters = 2"`、`"EndpointError = 3"`、`"NotAuthorized = 4"`、`"ServerNotFound = 5"`、`"FlightNotFound = 6"`、`"NoAtisAvailable = 7"` |
| `result`    | [OceanicTrack] | 在 Infinite Flight 中处于激活状态的航线数组。           |

<a id="OceanicTrack"></a>
<a id="oceanictrack"></a>
<a id="OceanicTrack"></a>
<a id="oceanictrack"></a>
#### OceanicTrack

| 名称         | 类型      | 描述                                                     |
| ------------ | --------- | -------------------------------------------------------- |
| `name`       | string    | 航线名称。通常以字母表示。                               |
| `path`       | [string]  | 你可以将这些与 [Airport Editing Project](https://github.com/infiniteflightairportediting/) 中的数据进行对应。 |
| `eastLevels` | [integer] | 可使用此航线向东飞行的飞行高度层数组。                   |
| `westLevels` | [integer] | 可使用此航线向西飞行的飞行高度层数组。                   |
| `type`       | string    | 海洋航线类型。Infinite Flight 除了支持活动定义的自定义航线外，还支持 `North Atlantic Tracks`。 |
| `lastSeen`   | string    | 海洋航线最后一次更新时间，格式如下：`YYYY-MM-DDTHH:mm:ssZ` |