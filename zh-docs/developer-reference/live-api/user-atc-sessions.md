---
id: user-atc-sessions
title: 获取用户 ATC 会话
meta: Infinite Flight Live API 用户 ATC 会话端点概览
order: 17
contributor: sqeezelemon
---

<a id="Get User ATC Sessions"></a>
<a id="get user atc sessions"></a>
<a id="get-user-atc-sessions"></a>
<a id="Get%20User%20ATC%20Sessions"></a>
<a id="get%20user%20atc%20sessions"></a>
<a id="Get User ATC Sessions"></a>
<a id="get user atc sessions"></a>
<a id="get-user-atc-sessions"></a>
<a id="Get%20User%20ATC%20Sessions"></a>
<a id="get%20user%20atc%20sessions"></a>
# 获取用户 ATC 会话

检索指定用户的 ATC 会话日志。

⚠️

: 此 API 仅用于模拟飞行，不得用于真实世界的飞行场景。

<a id="Resource"></a>
<a id="resource"></a>
<a id="Resource"></a>
<a id="resource"></a>
## 资源

**GET** `https://api.infiniteflight.com/public/v2/users/{userId}/atc`

<a id="Authorization"></a>
<a id="authorization"></a>
<a id="Authorization"></a>
<a id="authorization"></a>
## 授权

通过以下任一方式包含你的 API key (`<apikey>`)：

- 添加 `apikey` 查询参数。例如：`?apikey=<apikey>`。
- 使用你的 API key 发送 bearer authorization 头。例如：`Authorization: Bearer <apikey>`。

<a id="Parameters"></a>
<a id="parameters"></a>
<a id="Parameters"></a>
<a id="parameters"></a>
## 参数

| 名称     | 所在位置 | 描述            | 必填 | Schema        |
| -------- | -------- | --------------- | ---- | ------------- |
| `userId` | path     | 用户的 ID       | 是   | string (uuid) |
| `page`   | query    | 要检索的页索引  | 否，默认 `1` | integer |

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
    "pageIndex": 1,
    "totalPages": 80,
    "totalCount": 791,
    "hasPreviousPage": false,
    "hasNextPage": true,
    "data": [
      {
        "id": "857b1686-455d-481a-8bdf-c46cd7711691",
        "atcSessionGroupId": "1fcff4cb-48e6-46dc-8c87-4202bcdd7cc0",
        "facility": {
          "id": "4fda33c2-91b9-1a57-98f2-a765abd4c019",
          "airportIcao": "VRMM",
          "latitude": 4.191753387451172,
          "longitude": 73.52915954589844,
          "frequencyType": 4
        },
        "created": "2020-07-03T10:27:08.021137",
        "updated": "2020-07-03T10:37:49.026714",
        "operations": 9,
        "totalTime": 86.15142588333333,
        "worldType": 3,
        "server": "Expert",
        "violationsIssued": 2
      },
      ...
    ]
  }
}
```

<a id="LiveAPIResponse"></a>
<a id="liveapiresponse"></a>
<a id="LiveAPIResponse"></a>
<a id="liveapiresponse"></a>
#### LiveAPIResponse

*响应类型：* `application/json`

| 名称 | 类型 | 描述 |
| -- | -- | -- |
| `errorCode` | integer | _枚举：_ `"Ok = 0"`, `"UserNotFound = 1"`, `"MissingRequestParameters = 2"`, `"EndpointError = 3"`, `"NotAuthorized = 4"`, `"ServerNotFound = 5"`, `"FlightNotFound = 6"`, `"NoAtisAvailable = 7"` |
| `result` | PaginatedList | 日志簿中的一个页面。 |

<a id="Paginated List"></a>
<a id="paginated list"></a>
<a id="paginated-list"></a>
<a id="Paginated%20List"></a>
<a id="paginated%20list"></a>
<a id="Paginated List"></a>
<a id="paginated list"></a>
<a id="paginated-list"></a>
<a id="Paginated%20List"></a>
<a id="paginated%20list"></a>
#### 分页列表

| 名称 | 类型 | 描述 |
| -- | -- | -- |
| `pageIndex` | integer | 当前页的索引 |
| `totalPages` | integer | 可用的总页数 |
| `totalCount` | integer | 此数据集的总条目数 |
| `hasPreviousPage` | boolean | 是否存在前一页 |
| `hasNextPage` | boolean | 是否存在后一页 |
| `data` | [UserAtcSession] | 当前页中的条目 |

<a id="UserAtcSession"></a>
<a id="useratcsession"></a>
<a id="UserAtcSession"></a>
<a id="useratcsession"></a>
#### UserAtcSession

| 名称 | 类型 | 描述 |
| -- | -- | -- |
| `id` | string (uuid) | 会话的 ID |
| `atcSessionGroupId` | string (uuid) | 标识一组会话（当管制员在同一机场打开多个频率时） |
| `facility` | ATCFacility | 已开启的设施详情 |
| `created` | string (datetime) | 该频率首次开启的时间 |
| `updated` | string (datetime) | 最近一次收到报告的时间 |
| `operations` | integer | 本次会话中获得的操作次数 |
| `totalTime` | double | 会话持续时间，单位为分钟 |
| `worldType` | integer | 此会话开启所在服务器的类型。_枚举：_ `"Solo = 0"`, `"Casual = 1"`, `"Training = 2"`, `"Expert = 3"`, `"Private = 4"` |
| `server` | string | 此会话开启所在服务器的名称 | 
| `violationsIssued` | integer | 该用户在管制过程中发出的违规次数 |

<a id="ATCFacility"></a>
<a id="atcfacility"></a>
<a id="ATCFacility"></a>
<a id="atcfacility"></a>
#### ATCFacility

| 名称 | 类型 | 描述 |
| -- | -- | -- |
| `id` | string (uuid) | ATC 设施的 ID |
| `airportIcao` | string | 该设施所在机场的 ICAO 代码 |
| `latitude` | double | ATC 设施的纬度 |
| `longitude` | double | ATC 设施的经度 |
| `frequencyType` | ATCEntityType | ATC 设施类型。_枚举：_ `"Ground = 0"`, `"Tower = 1"`, `"Unicom = 2"`, `"Clearance = 3"`, `"Approach = 4"`, `"Departure = 5"`, `"Center = 6"`, `"ATIS = 7"`, `"Aircraft = 8"`, `"Recorded = 9"`, `"Unknown = 10"`, `"Unused = 11"` |