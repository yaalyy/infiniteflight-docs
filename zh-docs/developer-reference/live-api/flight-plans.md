---
id: flight-plans
title: 获取航班计划
meta: Infinite Flight Live API 批量航班计划端点概览
order: 8

---

<a id="Get Flight Plans (Bulk)"></a>
<a id="get flight plans (bulk)"></a>
<a id="get-flight-plans-(bulk)"></a>
<a id="get-flight-plans-bulk"></a>
<a id="Get%20Flight%20Plans%20%28Bulk%29"></a>
<a id="get%20flight%20plans%20%28bulk%29"></a>
<a id="get-flight-plans-%28bulk%29"></a>
<a id="Get Flight Plans (Bulk)"></a>
<a id="get flight plans (bulk)"></a>
<a id="get-flight-plans-(bulk)"></a>
<a id="get-flight-plans-bulk"></a>
<a id="Get%20Flight%20Plans%20%28Bulk%29"></a>
<a id="get%20flight%20plans%20%28bulk%29"></a>
<a id="get-flight-plans-%28bulk%29"></a>
# 获取航班计划（批量）

在单个请求中获取最多 25 个活跃航班的详细航班计划。与为每个航班单独调用 [获取航班计划](flight-plan.md) 端点相比，这种方式更高效。

⚠️

: 此 API 仅用于模拟飞行，切勿用于真实飞行场景。

<a id="Resource"></a>
<a id="resource"></a>
<a id="Resource"></a>
<a id="resource"></a>
## 资源

**POST** `https://api.infiniteflight.com/public/v2/sessions/{sessionId}/flights/flightplans`

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

| 名称        | 位置       | 描述                                             | 必填 | Schema        |
| ----------- | ---------- | ------------------------------------------------------ | -------- | ------------- |
| `sessionId` | path       | 从 Sessions 端点返回的会话 ID  | 是      | string (uuid) |

<a id="Body"></a>
<a id="body"></a>
<a id="Body"></a>
<a id="body"></a>
## 请求体

发送一个包含要查询航班 ID 数组的 JSON 对象。

```json
{
  "flightIds": [
    "0b8cc273-d97d-4223-afac-907d09d8ca8b",
    "1c9dd384-e8e8-5334-bgbd-018e1e9db9bc"
  ]
}
```

| 名称        | 类型         | 描述                                                                       | 必填 |
| ----------- | ------------- | --------------------------------------------------------------------------------- | -------- |
| `flightIds` | [string (uuid)] | 要检索航班计划的航班 ID 数组。每个请求最多 **10** 个 ID。 | 是      |

<a id="Response"></a>
<a id="response"></a>
<a id="Response"></a>
<a id="response"></a>
## 响应

结果会按请求中的 `flightIds` 顺序返回。如果对应航班没有提交航班计划，或者未找到该航班 ID，则该条目为 `null`。

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
        }
      ],
      "flightPlanType": 1
    },
    null
  ]
}
```

<a id="LiveAPIResponse"></a>
<a id="liveapiresponse"></a>
<a id="LiveAPIResponse"></a>
<a id="liveapiresponse"></a>
#### LiveAPIResponse

*响应类型:* `application/json`

| 名称         | 类型                  | 描述                                                  |
| ------------ | --------------------- | ------------------------------------------------------------ |
| `errorCode` | integer               | _枚举:_ `"Ok = 0"`, `"UserNotFound = 1"`, `"MissingRequestParameters = 2"`, `"EndpointError = 3"`, `"NotAuthorized = 4"`, `"ServerNotFound = 5"`, `"FlightNotFound = 6"`, `"NoAtisAvailable = 7"`, `"AirportNotFound = 8"`, `"ExceededMaximumRequestSize = 9"` |
| `result`    | [FlightPlanInfo\|null] | 按请求顺序返回的 FlightPlanInfo 对象数组。对于没有提交航班计划的航班为 `null`。 |

<a id="FlightPlanInfo"></a>
<a id="flightplaninfo"></a>
<a id="FlightPlanInfo"></a>
<a id="flightplaninfo"></a>
#### FlightPlanInfo

| 名称              | 类型             | 描述                                                  |
| ----------------- | ---------------- | ------------------------------------------------------------ |
| `flightPlanId`    | string (uuid)    | 航班计划的唯一标识符                        |
| `flightId`        | string (uuid)    | 航班的唯一标识符。与 Get Flights 端点的响应关联使用 |
| `waypoints`       | [string]         | **已弃用**。航路点名称数组。可将其与 [Airport Editing Project](https://github.com/infiniteflightairportediting/) 中的数据对应起来 |
| `lastUpdate`      | string           | 航班计划的最后报告时间，格式如下：`YYYY-MM-DD HH:mm:ssZ` |
| `flightPlanItems` | [FlightPlanItem] | 包含航路点和程序数据的 FlightPlanItem 数组，用于表示航班计划中的各个点。 |
| `flightPlanType`  | integer          | 航班计划类型。*枚举:* `VFR = 0`, `IFR = 1`           |

<a id="FlightPlanItem"></a>
<a id="flightplanitem"></a>
<a id="FlightPlanItem"></a>
<a id="flightplanitem"></a>
#### FlightPlanItem

| 名称         | 类型             | 描述                                                  |
| ------------ | ---------------- | ------------------------------------------------------------ |
| `name`       | string           | 航路点或程序的名称。在 `children` 数组中，这是某个程序内航路点的名称。 |
| `type`       | integer          | 此项所对应程序的类型。仅当 FlightPlanItem 的 `children` 字段已填充且不为 null 时才使用此字段。*枚举:* `"Sid = 0"`, `"STAR = 1"`, `"Approach = 2"`, `"Track = 3"`, `"Unknown = 5"` |
| `children`   | [FlightPlanItem] | 包含某个程序航路点信息的 FlightPlanItem 数组。仅当此项定义了程序（SID/STAR/Approach/Track）时才存在。如果没有，则应假定这是一个 Fix/VOR/自定义用户航路点。 |
| `identifier` | string           | 航路点或程序的标识符。此字段不唯一。 |
| `altitude`   | integer          | 此航路点的高度，单位为英尺。可由用户可选定义，如果未设置则默认为 `-1`。 |
| `location`   | Coordinate       | 定义此航路点位置的 Coordinate 对象。  |

<a id="Coordinate"></a>
<a id="coordinate"></a>
<a id="Coordinate"></a>
<a id="coordinate"></a>
#### Coordinate

| 名称        | 类型   | 描述                               |
| ----------- | ------ | ----------------------------------------- |
| `latitude`  | double | 航机当前的十进制度纬度  |
| `longitude` | double | 航机当前的十进制度经度 |
| `altitude`  | double | 航机当前的十进制度高度  |