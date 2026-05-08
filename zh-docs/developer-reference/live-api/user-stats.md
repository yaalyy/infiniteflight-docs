---
id: user-stats
title: 获取用户统计
meta: Infinite Flight Live API 用户统计端点概览
order: 9
contributor: sqeezelemon
---

<a id="Get User Stats"></a>
<a id="get user stats"></a>
<a id="get-user-stats"></a>
<a id="Get%20User%20Stats"></a>
<a id="get%20user%20stats"></a>
<a id="Get User Stats"></a>
<a id="get user stats"></a>
<a id="get-user-stats"></a>
<a id="Get%20User%20Stats"></a>
<a id="get%20user%20stats"></a>
# 获取用户统计

一次最多检索 25 位用户的统计信息，包括他们的等级、飞行时间和用户名。

⚠️

: 此 API 仅用于模拟飞行，不能用于真实世界的飞行场景。

<a id="Resource"></a>
<a id="resource"></a>
<a id="Resource"></a>
<a id="resource"></a>
## 资源

**POST** `https://api.infiniteflight.com/public/v2/users`

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

*请求 Content-Type:* `application/json`

| 名称             | 位于             | 描述                                                     | 必需 | Schema          |
| ---------------- | ---------------- | -------------------------------------------------------- | ---- | --------------- |
| `userIds`        | POST 请求体      | 从其他端点检索到的用户 ID 字符串数组                       | 否\* | [string (uuid)] |
| `discourseNames` | POST 请求体      | IFC 用户名数组。不区分大小写。                            | 否\* | [string]        |
| `userHashes`     | POST 请求体      | 从应用内或其他端点检索到的用户哈希数组。所有字母必须为大写。 | 否\* | [string]        |

*\*至少需要一个搜索参数*

<a id="Sample Body"></a>
<a id="sample body"></a>
<a id="sample-body"></a>
<a id="Sample%20Body"></a>
<a id="sample%20body"></a>
<a id="Sample Body"></a>
<a id="sample body"></a>
<a id="sample-body"></a>
<a id="Sample%20Body"></a>
<a id="sample%20body"></a>
#### 示例请求体

```json
{
  "userIds": [
    "2a11e620-1cc1-4ac6-90d1-18c4ed9cb913",
    "5917d076-88a5-40e7-95e0-8818748f8e99"
  ],
  "discourseNames": [
      "KaiM",
      "Laura"
  ],
  "userHashes": [
      "F0081CAA",
      "E2087C9F"
  ],
}
```

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
      "onlineFlights": 2449,
      "violations": 102,
      "xp": 572128,
      "landingCount": 898,
      "flightTime": 45983,
      "atcOperations": 548,
      "atcRank": 7,
      "grade": 5,
      "hash": "5F0973A9",
      "violationCountByLevel": {
        "level1": 102,
        "level2": 0,
        "level3": 0
      },
      "roles": [
        1,
        2,
        64
      ],
      "userId": "2a11e620-1cc1-4ac6-90d1-18c4ed9cb913",
      "virtualOrganization": null,
      "discourseUsername": "Cameron",
      "groups": [
        "8c93a113-0c6c-491f-926d-1361e43a5833",
        "d07afad8-79df-4363-b1c7-a5a1dde6e3c8",
        "df0f6341-5f6a-40ef-8b73-087a0ec255b5"
      ],
      "errorCode": 0
    },
    {
      "onlineFlights": 21,
      "violations": 0,
      "xp": 29984,
      "landingCount": 24,
      "flightTime": 2717,
      "atcOperations": 0,
      "atcRank": null,
      "grade": 1,
      "hash": "56099EA4",
      "userId": "66e362c0-894b-495b-93a6-75f9befa502d",
      "virtualOrganization": null,
      "discourseUsername": null,
       "violationCountByLevel": {
        "level1": 22,
        "level2": 0,
        "level3": 0
      },
      "roles": [
        64
      ],
      "groups": [],
      "errorCode": 0
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

| 名称        | 类型        | 描述                                                     |
| ----------- | ----------- | -------------------------------------------------------- |
| `errorCode` | integer     | _枚举:_ `"Ok = 0"`, `"UserNotFound = 1"`, `"MissingRequestParameters = 2"`, `"EndpointError = 3"`, `"NotAuthorized = 4"`, `"ServerNotFound = 5"`, `"FlightNotFound = 6"`, `"NoAtisAvailable = 7"` |
| `result`    | [UserStats] | UserStats 对象数组                                       |



<a id="UserStats"></a>
<a id="userstats"></a>
<a id="UserStats"></a>
<a id="userstats"></a>
#### UserStats

| 名称                    | 类型            | 描述                                                     |
| ----------------------- | --------------- | -------------------------------------------------------- |
| `userId`                | string (uuid)   | 用户的唯一标识符                                           |
| `virtualOrganization`   | string          | 如果已关联，则为用户论坛账户所属的虚拟组织。未设置时可为 null |
| `discourseUsername`     | string          | 如果账户已关联，则为用户的论坛用户名；如果未关联，则为 null |
| `groups`                | [string (uuid)] | **已弃用 - 将在未来更新中移除** 用户可能所属的组列表。      |
| `roles`                 | [integer]       | 用户被分配到的角色列表。下面有主要角色列表。                |
| `errorCode`             | integer         | 用户查询状态码。此端点未使用。                             |
| `onlineFlights`         | integer         | 多人模式中完成的飞行次数                                     |
| `violations`            | integer         | 用户在多人模式中收到的 1、2 和 3 级违规次数                  |
| `violationCountByLevel` | dict            | 按级别（1/2/3 级）拆分的用户违规次数字典。                  |
| `xp`                    | double          | 多人模式中获得的总 XP                                      |
| `landingCount`         | integer         | 多人模式中完成的总着陆次数                                   |
| `flightTime`           | double          | 多人模式中的总飞行时间（分钟）                               |
| `atcOperations`        | integer         | ATC 操作总数。                                             |
| `atcRank`              | integer         | Expert Server 上的 ATC 等级。下面有等级列表。如果用户不是 IFATC 管制员，则可为 null。 |
| `grade`                | integer         | 用户的等级，范围为 1 到 5。                                 |
| `hash`                 | string          | 简短形式的用户标识符，在应用中用于识别匿名用户。            |

<a id="Roles"></a>
<a id="roles"></a>
<a id="Roles"></a>
<a id="roles"></a>
#### 角色

主要角色如下。

| ID   | 名称                  |
| ---- | --------------------- |
| 1    | Infinite Flight Staff |
| 2    | Moderators            |
| 64   | IFATC Members         |

<a id="ATC Ranks"></a>
<a id="atc ranks"></a>
<a id="atc-ranks"></a>
<a id="ATC%20Ranks"></a>
<a id="atc%20ranks"></a>
<a id="ATC Ranks"></a>
<a id="atc ranks"></a>
<a id="atc-ranks"></a>
<a id="ATC%20Ranks"></a>
<a id="atc%20ranks"></a>
#### ATC 等级

ATC 等级如下。

| ID   | 名称           |
| ---- | -------------- |
| 0    | Observer       |
| 1    | ATC Trainee    |
| 2    | ATC Apprentice |
| 3    | ATC Specialist |
| 4    | ATC Officer    |
| 5    | ATC Supervisor |
| 6    | ATC Recruiter  |
| 7    | ATC Manager    |