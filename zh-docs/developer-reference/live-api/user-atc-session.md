---
id: user-atc-session
title: 获取用户 ATC 会话
meta: Infinite Flight Live API 用户 ATC 会话端点概览
order: 18
contributor: sqeezelemon
---

<a id="Get User ATC Session"></a>
<a id="get user atc session"></a>
<a id="get-user-atc-session"></a>
<a id="Get%20User%20ATC%20Session"></a>
<a id="get%20user%20atc%20session"></a>
<a id="Get User ATC Session"></a>
<a id="get user atc session"></a>
<a id="get-user-atc-session"></a>
<a id="Get%20User%20ATC%20Session"></a>
<a id="get%20user%20atc%20session"></a>
# 获取用户 ATC 会话

从指定用户的日志中检索一个 ATC 会话。

⚠️

: 此 API 仅用于模拟飞行，不得用于真实世界飞行情境。

<a id="Resource"></a>
<a id="resource"></a>
<a id="Resource"></a>
<a id="resource"></a>
## 资源

**GET** `https://api.infiniteflight.com/public/v2/users/{userId}/atc/{atcSessionId}`

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

| Name     | Located in | Description    | Required | Schema        |
| -------- | ---------- | -------------- | -------- | ------------- |
| `userId` | path       | 用户 ID | Yes      | string (uuid) |
| `atcSessionId` | path | ATC 会话 ID | Yes | string (uuid) |

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
  }
}
```

<a id="LiveAPIResponse"></a>
<a id="liveapiresponse"></a>
<a id="LiveAPIResponse"></a>
<a id="liveapiresponse"></a>
#### LiveAPIResponse

*响应类型:* `application/json`

| Name | Type | Description |
| -- | -- | -- |
| `errorCode` | integer | _枚举:_ `"Ok = 0"`, `"UserNotFound = 1"`, `"MissingRequestParameters = 2"`, `"EndpointError = 3"`, `"NotAuthorized = 4"`, `"ServerNotFound = 5"`, `"FlightNotFound = 6"`, `"NoAtisAvailable = 7"` |
| `result` | UserAtcSession | 来自日志的一个 ATC 会话。 |

<a id="UserAtcSession"></a>
<a id="useratcsession"></a>
<a id="UserAtcSession"></a>
<a id="useratcsession"></a>
#### UserAtcSession

| Name | Type | Description |
| -- | -- | -- |
| `id` | string (uuid) | 会话 ID |
| `atcSessionGroupId` | string (uuid) | 标识一组会话（用于控制员在同一机场开启多个频率时） |
| `facility` | ATCFacility | 已开启设施的详细信息 |
| `created` | string (datetime) | 该频率首次开启的时间 |
| `updated` | string (datetime) | 最近一次收到报告的时间 |
| `operations` | integer | 本次会话中获得的操作数 |
| `totalTime` | double | 会话时长，单位为分钟 |
| `worldType` | integer | 此会话开启所在服务器的类型。_枚举:_ `"Solo = 0"`, `"Casual = 1"`, `"Training = 2"`, `"Expert = 3"`, `"Private = 4"` |
| `server` | string | 此会话开启所在服务器的名称 | 
| `violationsIssued` | integer | 该用户在管制过程中发出的违规次数 |

<a id="ATCFacility"></a>
<a id="atcfacility"></a>
<a id="ATCFacility"></a>
<a id="atcfacility"></a>
#### ATCFacility

| Name | Type | Description |
| -- | -- | -- |
| `id` | string (uuid) | ATC 设施 ID |
| `airportIcao` | string | 该设施所在机场的 ICAO 代码 |
| `latitude` | double | ATC 设施纬度 |
| `longitude` | double | ATC 设施经度 |
| `frequencyType` | ATCEntityType | ATC 设施类型。_枚举:_ `"Ground = 0"`, `"Tower = 1"`, `"Unicom = 2"`, `"Clearance = 3"`, `"Approach = 4"`, `"Departure = 5"`, `"Center = 6"`, `"ATIS = 7"`, `"Aircraft = 8"`, `"Recorded = 9"`, `"Unknown = 10"`, `"Unused = 11"` |