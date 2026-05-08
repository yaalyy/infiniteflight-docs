---
id: user-flights
title: 获取用户航班
meta: Infinite Flight Live API 用户航班端点概览
order: 15
contributor: sqeezelemon
---

<a id="Get User Flights"></a>
<a id="get user flights"></a>
<a id="get-user-flights"></a>
<a id="Get%20User%20Flights"></a>
<a id="get%20user%20flights"></a>
<a id="Get User Flights"></a>
<a id="get user flights"></a>
<a id="get-user-flights"></a>
<a id="Get%20User%20Flights"></a>
<a id="get%20user%20flights"></a>
# 获取用户航班

检索指定用户的在线飞行日志。

⚠️

: 此 API 仅用于模拟飞行，切勿在真实飞行场景中使用。

<a id="Resource"></a>
<a id="resource"></a>
<a id="Resource"></a>
<a id="resource"></a>
## 资源

**GET** `https://api.infiniteflight.com/public/v2/users/{userId}/flights`

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

| 名称 | 位置 | 描述 | 必填 | Schema |
| ---- | ---- | ---- | ---- | ------ |
| `userId` | path | 用户的 ID | 是 | string (uuid) |
| `page` | query | 要检索的页索引 | 否，默认 `1` | integer |

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
    "totalCount": 799,
    "hasPreviousPage": false,
    "hasNextPage": true,
    "data": [
      {
        "id": "9aeb16a3-ac69-41d3-9dd4-d62be72b1525",
        "created": "2022-01-10T10:37:41.965626",
        "userId": "b0018209-e010-40a0-afe1-00ecd5856c5e",
        "aircraftId": "849366e1-cb11-4d72-9034-78b11cd026b0",
        "liveryId": "a071518d-995a-4b3c-b65b-656da0d6ed86",
        "callsign": "VH-KAI",
        "server": "Casual Server",
        "dayTime": 2.5355167,
        "nightTime": 0,
        "totalTime": 2.5355167,
        "landingCount": 0,
        "originAirport": "YTYA",
        "destinationAirport": "YTYA",
        "xp": 25,
        "worldType": 1,
        "violations": [
          {
            "issuedBy": {
                "id": "2a11e620-1cc1-4ac6-90d1-18c4ed9cb913",
                "username": "Cameron",
                "callsign": "EC-CAM",
                "discourseUser": {
                    "userId": 4,
                    "username": "Cameron",
                    "virtualOrganization": "",
                    "avatarTemplate": "/user_avatar/community.infiniteflight.com/cameron/{size}/886772_2.png"
                }
            },
            "level": 1,
            "type": "Ground Overspeed",
            "description": "Ground Overspeed",
            "created": "2023-10-31T16:34:51.014366+00:00"
          }
        ]
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

*响应类型:* `application/json`

| 名称 | 类型 | 描述 |
| -- | -- | -- |
| `errorCode` | integer | _枚举:_ `"Ok = 0"`, `"UserNotFound = 1"`, `"MissingRequestParameters = 2"`, `"EndpointError = 3"`, `"NotAuthorized = 4"`, `"ServerNotFound = 5"`, `"FlightNotFound = 6"`, `"NoAtisAvailable = 7"` |
| `result` | PaginatedList | 日志中的一个分页。 |

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
#### Paginated List

| 名称 | 类型 | 描述 |
| -- | -- | -- |
| `pageIndex` | integer | 当前页的索引 |
| `totalPages` | integer | 可用的总页数 |
| `totalCount` | integer | 此数据集的总条目数 |
| `hasPreviousPage` | boolean | 是否存在前一页 |
| `hasNextPage` | boolean | 是否存在后一页 |
| `data` | [UserFlight] | 当前页中的条目 |

<a id="UserFlight"></a>
<a id="userflight"></a>
<a id="UserFlight"></a>
<a id="userflight"></a>
#### UserFlight

| 名称 | 类型 | 描述 |
| -- | -- | -- |
| `id` | string (uuid) | 航班的 ID |
| `created` | string (datetime) | 航班创建时间 |
| `userId` | string (uuid) | 执行该航班的用户 ID |
| `aircraftId` | string (uuid) | 所飞行的飞机 ID |
| `liveryId` | string (uuid) | 所飞行的涂装 ID。**当前仅支持 Casual 服务器** |
| `callsign` | string | 用户在本次航班中的 callsign |
| `server` | string | 执行该航班的服务器名称 |
| `dayTime` | float | 白天飞行时间，单位为分钟 |
| `nightTime` | float | 夜间飞行时间，单位为分钟 |
| `totalTime` | float | 航班总飞行时间，单位为分钟 |
| `landingCount` | integer | 本次航班中的着陆次数 |
| `originAirport` | string | 出发机场的 ICAO 代码。可以为 null |
| `destinationAirport` | string | 到达机场的 ICAO 代码。可以为 null |
| `xp` | integer | 本次航班获得的 XP 数量 |
| `worldType` | integer | 执行该航班的服务器类型。_枚举:_ `"Solo = 0"`, `"Casual = 1"`, `"Training = 2"`, `"Expert = 3"`, `"Private = 4"` |
| `violations` | [Violation] | 用户在本次航班中收到的违规记录数组。 |

<a id="Violation"></a>
<a id="violation"></a>
<a id="Violation"></a>
<a id="violation"></a>
#### Violation

| 名称 | 类型 | 描述 |
| ---- | ---- | ---- |
| `issuedBy` | Issuer | 发出该违规的人员信息 |
| `level` | integer | 违规严重等级 |
| `type` | string | 所犯违规的类型 |
| `description` | string | 违规的详细描述 |
| `created` | string (datetime) | 记录该违规的时间 |

<a id="Issuer"></a>
<a id="issuer"></a>
<a id="Issuer"></a>
<a id="issuer"></a>
#### Issuer

| 名称 | 类型 | 描述 |
| ---- | ---- | ---- |
| `id` | string (uuid) | 发出者的 ID |
| `username` | string | 发出者的用户名 |
| `callsign` | string | 发出者的 callsign |
| `discourseUser` | DiscourseUser | 发出者 Discourse 账号的信息，如可用 |

<a id="DiscourseUser"></a>
<a id="discourseuser"></a>
<a id="DiscourseUser"></a>
<a id="discourseuser"></a>
#### DiscourseUser

| 名称 | 类型 | 描述 |
| ---- | ---- | ---- |
| `userId` | integer | Discourse 平台上的用户 ID |
| `username` | string | Discourse 平台上的用户名 |
| `virtualOrganization` | string | 与该用户关联的虚拟组织（如有） |
| `avatarTemplate` | string | 该用户在 Discourse 上的头像 URL 模板 |