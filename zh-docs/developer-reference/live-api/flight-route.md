---
id: flight-route
title: 获取航线
meta: Infinite Flight Live API 航线端点概览
order: 5
---

<a id="Get Flight Route"></a>
<a id="get flight route"></a>
<a id="get-flight-route"></a>
<a id="Get%20Flight%20Route"></a>
<a id="get%20flight%20route"></a>
<a id="Get Flight Route"></a>
<a id="get flight route"></a>
<a id="get-flight-route"></a>
<a id="Get%20Flight%20Route"></a>
<a id="get%20flight%20route"></a>
# 获取航线

检索特定航班在不同时间点的飞行航线，包括位置信息、高度、速度和航向信息。

请注意，目前仅在 Expert Server 和 Training Server 上受支持。

⚠️

: 此 API 仅用于模拟飞行，不得用于真实世界的飞行场景。

<a id="Resource"></a>
<a id="resource"></a>
<a id="Resource"></a>
<a id="resource"></a>
## 资源

**GET** `https://api.infiniteflight.com/public/v2/sessions/{sessionId}/flights/{flightId}/route`

<a id="Authorization"></a>
<a id="authorization"></a>
<a id="Authorization"></a>
<a id="authorization"></a>
## 授权

通过以下任一方式包含你的 API 密钥（`<apikey>`）：

- 添加 `apikey` 查询参数。例如，`?apikey=<apikey>`。
- 使用你的 API 密钥发送 bearer authorization header。例如，`Authorization: Bearer <apikey>`。

<a id="Parameters"></a>
<a id="parameters"></a>
<a id="Parameters"></a>
<a id="parameters"></a>
## 参数

| 名称        | 所在位置 | 描述                                                     | 必填 | Schema        |
| ----------- | -------- | -------------------------------------------------------- | ---- | ------------- |
| `sessionId` | path     | 从 Sessions 端点返回的 session ID                       | 是   | string (uuid) |
| `flightId`  | path     | 航班的 ID。该航班必须位于活动的 session 中。            | 是   | string (uuid) |

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
      "latitude": 25.52992361245416,
      "longitude": -80.33701239710909,
      "altitude": 18429.91132829714,
      "track": 75.00002,
      "groundSpeed": 194.6716372048416,
      "date": "2021-01-06T16:20:27.3275657Z"
    },
    {
      "latitude": 25.59595843191219,
      "longitude": -79.96882929194611,
      "altitude": 27448.993829140254,
      "track": 77.0936,
      "groundSpeed": 229.58654094765924,
      "date": "2021-01-06T16:23:27.4572883Z"
    },
    {
      "latitude": 25.621774462118506,
      "longitude": -79.56246802075516,
      "altitude": 30999.01751208178,
      "track": 110.30767,
      "groundSpeed": 235.4484678810845,
      "date": "2021-01-06T16:26:27.5268907Z"
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

| 名称         | 类型             | 描述                                                     |
| ------------ | ---------------- | -------------------------------------------------------- |
| `errorCode`  | integer          | _枚举:_ `"Ok = 0"`, `"UserNotFound = 1"`, `"MissingRequestParameters = 2"`, `"EndpointError = 3"`, `"NotAuthorized = 4"`, `"ServerNotFound = 5"`, `"FlightNotFound = 6"`, `"NoAtisAvailable = 7"` |
| `result`     | [PositionReport] | PositionReport 对象数组                                  |

<a id="PositionReport"></a>
<a id="positionreport"></a>
<a id="PositionReport"></a>
<a id="positionreport"></a>
#### PositionReport

| 名称          | 类型   | 描述                                                     |
| ------------- | ------ | -------------------------------------------------------- |
| `latitude`    | double | 此位置上飞机的十进制度纬度。                               |
| `longitude`   | double | 此位置上飞机的十进制度经度。                               |
| `altitude`    | double | 飞机高度，单位为英尺。                                     |
| `track`       | double | 飞机的航迹 / 航向，单位为度。                               |
| `groundSpeed` | double | 飞机地速，单位为节。                                       |
| `date`        | string | 航班的位置报告时间，格式如下：`YYYY-MM-DD HH:mm:ssZ` |