---
id: flight-plan
title: 获取飞行计划
meta: Infinite Flight Live API 飞行计划端点概览
order: 7

---

<a id="Get Detailed Flight Plan"></a>
<a id="get detailed flight plan"></a>
<a id="get-detailed-flight-plan"></a>
<a id="Get%20Detailed%20Flight%20Plan"></a>
<a id="get%20detailed%20flight%20plan"></a>
<a id="Get Detailed Flight Plan"></a>
<a id="get detailed flight plan"></a>
<a id="get-detailed-flight-plan"></a>
<a id="Get%20Detailed%20Flight%20Plan"></a>
<a id="get%20detailed%20flight%20plan"></a>
# 获取详细飞行计划

检索特定活动航班的飞行计划。

⚠️

: 此 API 仅用于模拟飞行，切勿用于真实飞行场景。

<a id="Resource"></a>
<a id="resource"></a>
<a id="Resource"></a>
<a id="resource"></a>
## 资源

**GET** `https://api.infiniteflight.com/public/v2/sessions/{sessionId}/flights/{flightId}/flightplan`

<a id="Authorization"></a>
<a id="authorization"></a>
<a id="Authorization"></a>
<a id="authorization"></a>
## 授权

通过以下任一方式包含你的 API 密钥 (`<apikey>`)：

- 添加 `apikey` 查询参数。例如，`?apikey=<apikey>`。
- 使用你的 API 密钥发送 bearer authorization header。例如，`Authorization: Bearer <apikey>`。

<a id="Parameters"></a>
<a id="parameters"></a>
<a id="Parameters"></a>
<a id="parameters"></a>
## 参数

| 名称        | 所在位置 | 描述                                                  | 必需 | Schema        |
| ---------- | -------- | ------------------------------------------------------------ | ---- | ------------- |
| `sessionId` | path       | 从 Sessions 端点返回的会话 ID | 是      | string (uuid) |
| `flightId` | path       | 航班 ID。该航班必须处于活动会话中，并且已提交飞行计划。 | 是      | string (uuid) |

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
  "result": {
      "flightPlanId": "4a57de08-a3b1-48ba-a081-adeff0a5b503",
      "flightId": "0b8cc273-d97d-4223-afac-907d09d8ca8b",
      "waypoints": [
        "AMAHE",
        "L12R"
      ],
      "lastUpdate": "2021-01-06 15:35:04Z",
      "flightPlanItems": [
        {
          "name": "AMAHE",
          "type": 0,
          "children": null,
          "identifier": null,
          "altitude": -1,
          "location": {
            "latitude": 26.92723722,
            "longitude": -77.47139889,
            "altitude": 0
          }
        },
        {
          "name": "L12R",
          "type": 2,
          "children": [
            {
              "name": "ZESTY",
              "type": 0,
              "children": null,
              "identifier": "ZESTY",
              "altitude": 4000,
              "location": {
                "latitude": 44.97196917,
                "longitude": -93.429735,
                "altitude": 0
              }
            },
            {
              "name": "RW12R",
              "type": 0,
              "children": null,
              "identifier": "RW12R",
              "altitude": -1,
              "location": {
                "latitude": 44.887794494628906,
                "longitude": -93.23413848876953,
                "altitude": 0
              }
            }
          ],
          "identifier": "L12R",
          "altitude": 0,
          "location": {
            "latitude": 0,
            "longitude": 0,
            "altitude": 0
          }
        }
      ]
    }
}
```

<a id="LiveAPIResponse"></a>
<a id="liveapiresponse"></a>
<a id="LiveAPIResponse"></a>
<a id="liveapiresponse"></a>
#### LiveAPIResponse

*响应类型:* `application/json`

| 名称        | 类型             | 描述                                                  |
| ----------- | ---------------- | ------------------------------------------------------------ |
| `errorCode` | integer          | _枚举:_ `"Ok = 0"`, `"UserNotFound = 1"`, `"MissingRequestParameters = 2"`, `"EndpointError = 3"`, `"NotAuthorized = 4"`, `"ServerNotFound = 5"`, `"FlightNotFound = 6"`, `"NoAtisAvailable = 7"` |
| `result`    | [FlightPlanInfo] | FlightPlanInfo 对象数组                              |

<a id="FlightPlanInfo"></a>
<a id="flightplaninfo"></a>
<a id="FlightPlanInfo"></a>
<a id="flightplaninfo"></a>
#### FlightPlanInfo

| 名称              | 类型             | 描述                                                  |
| ----------------- | ---------------- | ------------------------------------------------------------ |
| `flightPlanId`    | string (uuid)    | 飞行计划的唯一标识符                        |
| `flightId`        | string (uuid)    | 航班的唯一标识符。与 Get Flights 端点返回的响应关联 |
| `waypoints`       | [string]         | **已弃用**。航点名称数组。你可以将其与 [Airport Editing Project](https://github.com/infiniteflightairportediting/) 中的数据对应起来 |
| `lastUpdate`      | string           | 飞行计划的最后报告时间，格式如下：`YYYY-MM-DD HH:mm:ssZ` |
| `flightPlanItems` | [FlightPlanItem] | 包含飞行计划中航点和程序数据的 FlightPlanItem 数组。 |
|`flightPlanType`|integer|飞行计划类型。*枚举:* `VFR = 0`,`IFR = 1`|

<a id="FlightPlanItem"></a>
<a id="flightplanitem"></a>
<a id="FlightPlanItem"></a>
<a id="flightplanitem"></a>
#### FlightPlanItem

| 名称         | 类型             | 描述                                                  |
| ------------ | ---------------- | ------------------------------------------------------------ |
| `name`       | string           | 航点或程序的名称。在 `children` 数组中，这是程序内某个航点的名称。 |
| `type`       | integer          | 此项的程序类型。仅当 FlightPlanItem 的 `children` 字段已填充且不为 null 时使用此项。*枚举:* `"Sid = 0"`, `"STAR = 1"`,  `"Approach = 2"`, `"Track = 3"`, `"Unknown = 5"` |
| `children`   | [FlightPlanItem] | 包含某个程序的航点信息的 FlightPlanItem 数组。仅当此项定义了程序（SID/STAR/Approach/Track）时存在。如果没有，则可假定这是 Fix/VOR/自定义用户航点。 |
| `identifier` | string           | 航点或程序的标识符。它不是唯一的。 |
| `altitude`   | integer          | 此航点的高度，单位为英尺。由用户可选定义，若未设置则默认为 `-1`。 |
| `location`   | Coordinate       | 定义此航点位置的 Coordinate 对象。  |

<a id="Coordinate"></a>
<a id="coordinate"></a>
<a id="Coordinate"></a>
<a id="coordinate"></a>
#### Coordinate

| 名称        | 类型   | 描述                               |
| ----------- | ------ | ----------------------------------------- |
| `latitude`  | double | 飞机当前的十进制度纬度  |
| `longitude` | double | 飞机当前的十进制度经度 |
| `altitude`  | double | 飞机当前的十进制度高度  |