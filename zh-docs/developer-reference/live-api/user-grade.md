---
id: user-grade
title: 获取用户等级
meta: Infinite Flight Live API 用户等级端点概览
order: 10
contributor: KaiM,sqeezelemon,Ethan_C
---

<a id="Get User Grade"></a>
<a id="get user grade"></a>
<a id="get-user-grade"></a>
<a id="Get%20User%20Grade"></a>
<a id="get%20user%20grade"></a>
<a id="Get User Grade"></a>
<a id="get user grade"></a>
<a id="get-user-grade"></a>
<a id="Get%20User%20Grade"></a>
<a id="get%20user%20grade"></a>
# 获取用户等级

检索某个用户的完整等级表和详细统计信息。

⚠️

: 此 API 仅适用于模拟飞行，不得用于真实世界飞行场景。

<a id="Resource"></a>
<a id="resource"></a>
<a id="Resource"></a>
<a id="resource"></a>
## 资源

**GET** `https://api.infiniteflight.com/public/v2/users/{userId}`

<a id="Authorization"></a>
<a id="authorization"></a>
<a id="Authorization"></a>
<a id="authorization"></a>
## 授权

通过以下任一方式包含你的 API 密钥（`<apikey>`）：

-   添加 `apikey` 查询参数。例如，`?apikey=<apikey>`。
-   使用你的 API 密钥发送 bearer authorization 头。例如，`Authorization: Bearer <apikey>`。

<a id="Parameters"></a>
<a id="parameters"></a>
<a id="Parameters"></a>
<a id="parameters"></a>
## 参数

| 名称     | 所在位置   | 描述         | 必填 | Schema        |
| -------- | ---------- | ------------ | ---- | ------------- |
| `userId` | path       | 用户的 ID     | 是   | string (uuid) |

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
    "totalXP": 217242,
    "total12MonthsViolations": 4,
    "gradeDetails": {
        "grades": [...],
        "gradeIndex": 2,
        "ruleDefinitions": [...]
    },
    "atcOperations": 14641,
    "atcRank": 3,
    "lastLevel1ViolationDate": "2020-12-16T03:20:10.283484",
    "lastLevel2ViolationDate": "0001-01-01T00:00:00",
    "lastLevel3ViolationDate": "2018-07-01T17:44:05.345678",
    "lastReportViolationDate": "2018-07-01T17:44:05.345678",
    "violationCountByLevel": {
      "level1": 9,
      "level2": 0,
      "level3": 0
    },
    "roles": [
      41,
      43,
      53,
      61,
      64,
      68
    ],
    "userId": "b0018209-e010-40a0-afe1-00ecd5856c5e",
    "virtualOrganization": "IFATC [IFATC]",
    "discourseUsername": "KaiM",
    "groups": [
      "df0f6341-5f6a-40ef-8b73-087a0ec255b5"
    ],
    "errorCode": 0
  }
}
```

<a id="LiveAPIResponse"></a>
<a id="liveapiresponse"></a>
<a id="LiveAPIResponse"></a>
<a id="liveapiresponse"></a>
#### LiveAPIResponse

_响应类型:_ `application/json`

| 名称        | 类型      | 描述                                                                                                                                                                                       |
| ----------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `errorCode` | integer   | _枚举:_ `"Ok = 0"`, `"UserNotFound = 1"`, `"MissingRequestParameters = 2"`, `"EndpointError = 3"`, `"NotAuthorized = 4"`, `"ServerNotFound = 5"`, `"FlightNotFound = 6"`, `"NoAtisAvailable = 7"` |
| `result`    | GradeInfo | GradeInfo 对象                                                                                                                                                                                  |

<a id="GradeInfo"></a>
<a id="gradeinfo"></a>
<a id="GradeInfo"></a>
<a id="gradeinfo"></a>
#### GradeInfo

| 名称                      | 类型               | 描述                                                                                                                       |
| ------------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| `userId`                  | string (uuid)      | 用户的唯一标识符                                                                                                            |
| `virtualOrganization`     | string             | 如果已关联，则为该用户论坛账号所属的虚拟组织；若未设置，可为 null                                            |
| `discourseUsername`       | string             | 如果账号已关联，则为该用户的论坛用户名；如果账号未关联，则为 null                                |
| `groups`                  | [string (uuid)]    | **已弃用 - 即将移除。** 用户可能所属的组列表。                                                |
| `roles`                   | [integer]          | 用户被分配的角色列表。有关主要角色列表，请参见下文。                                                     |
| `errorCode`               | integer            | 用户查询状态码。此端点未使用。                                                                          |
| `gradeDetails`            | GradeConfiguration | 完整等级表                                                                                                                  |
| `violationCountByLevel`   | dict               | 按级别拆分的用户违规次数字典（Level 1/2/3）。                                     |
| `totalXP`                 | double             | 多人模式中获得的总 XP                                                                                                  |
| `atcOperations`           | integer           | ATC 操作总数。                                                                                                   |
| `atcRank`                 | integer           | Expert Server 上的 ATC 等级。有关等级请参见下文。若用户不是 IFATC 管制员，则可为 null。                            |
| `total12MonthsViolations` | integer           | 最近 12 个月内收到的 Level 1、2 和 3 违规总数                                                       |
| `lastLevel1ViolationDate` | string (datetime)  | 用户最后一次 Level 1 违规的日期。若用户没有任何 Level 1 违规，则默认为 `0001-01-01T00:00:00`。 |                                                                                         |
| `lastLevel2ViolationDate` | string (datetime)  | 用户最后一次 Level 2 违规的日期。若用户没有任何 Level 2 违规，则默认为 `0001-01-01T00:00:00`。 |                                                                                        |
| `lastLevel3ViolationDate` | string (datetime)  | 用户最后一次 Level 3 违规（report）的日期。若用户没有任何 Level 3 违规（reports），则默认为 `0001-01-01T00:00:00`。 |                                                                                        |
| `lastReportViolationDate` | string (datetime)  | 用户最后一次 Level 2 或 3 违规（report）的日期。若用户没有任何 reports，则默认为 `0001-01-01T00:00:00`。 |

<a id="Roles"></a>
<a id="roles"></a>
<a id="Roles"></a>
<a id="roles"></a>
#### 角色

主要角色如下。

| ID  | 名称                  |
| --- | --------------------- |
| 1   | Infinite Flight Staff |
| 2   | Moderators            |
| 64  | IFATC Members         |

<a id="Groups"></a>
<a id="groups"></a>
<a id="Groups"></a>
<a id="groups"></a>
#### 组

主要组如下。

| ID                                   | 名称          |
| ------------------------------------ | ------------- |
| d07afad8-79df-4363-b1c7-a5a1dde6e3c8 | Staff         |
| 8c93a113-0c6c-491f-926d-1361e43a5833 | Moderators    |
| df0f6341-5f6a-40ef-8b73-087a0ec255b5 | IFATC Members |

<a id="GradeConfiguration"></a>
<a id="gradeconfiguration"></a>
<a id="GradeConfiguration"></a>
<a id="gradeconfiguration"></a>
#### GradeConfiguration

| 名称              | 类型                  | 描述                                            |
| ----------------- | --------------------- | ----------------------------------------------- |
| `grades`          | [Grade]               | 包含所有等级的数组                            |
| `gradeIndex`      | integer               | 用户所持有的 `grades` 属性索引 |
| `ruleDefinitions` | [GradeRuleDefinition] | 每个等级所需规则的定义        |

<a id="Grade"></a>
<a id="grade"></a>
<a id="Grade"></a>
<a id="grade"></a>
#### Grade

| 名称    | 类型        | 描述                                                                    |
| ------- | ----------- | ----------------------------------------------------------------------- |
| `rules` | [GradeRule] | 达到该等级所需满足的规则                                            |
| `index` | integer     | `GradeConfiguration` 对象中 `grades` 属性里的等级索引 |
| `name`  | string      | 等级名称                                                              |
| `state` | integer     | _枚举:_ `"Fail = 0"`, `"OK = 1"`, `"Warning = 2"`                              |

<a id="GradeRule"></a>
<a id="graderule"></a>
<a id="GradeRule"></a>
<a id="graderule"></a>
#### GradeRule

| 名称                   | 类型                | 描述                                                     |
| ---------------------- | ------------------- | -------------------------------------------------------- |
| `ruleIndex`            | integer             | `Grade` 对象中 `rules` 属性里的规则索引 |
| `referenceValue`       | double              | 要求值                                           |
| `userValue`            | double              | 用户在该属性上的值                         |
| `state`                | integer             | _枚举:_ `"Fail = 0"`, `"OK = 1"`, `"Warning = 2"`               |
| `userValueString`      | string              | 用户的值，格式化后显示                         |
| `referenceValueString` | string              | 要求值，格式化后显示                         |
| `definition`           | GradeRuleDefinition | 规则定义                                          |

<a id="GradeRuleDefinition"></a>
<a id="graderuledefinition"></a>
<a id="GradeRuleDefinition"></a>
<a id="graderuledefinition"></a>
#### GradeRuleDefinition

| 名称          | 类型    | 描述                                                                                                                                  |
| ------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `name`        | string  | 规则名称                                                                                                                             |
| `description` | string  | 规则描述                                                                                                                      |
| `property`    | string  | `GradeInfo` 对象中该规则关联的属性                                                                                   |
| `operator`    | integer | _枚举:_ `"GreaterThan = 0"`, `"LesserThan = 1"`, `"GreaterThanOrEqual = 2"`, `"LesserThanOrEqual = 3"`, `"Equal = 4"`, `"DifferentThan = 5"` |
| `period`      | double  | 必须满足该规则的时间周期                                                                                                    |
| `order`       | integer | `Grade` 对象中 `rules` 属性内规则的顺序                                                                          |
| `group`       | integer | 此端点未使用。                                                                                                                |

<a id="ViolationEntry"></a>
<a id="violationentry"></a>
<a id="ViolationEntry"></a>
<a id="violationentry"></a>
#### ViolationEntry

| 名称   | 类型   | 描述                     |
| ------ | ------ | ------------------------ |
| `type` | double | 违规类型               |
| `date` | string | 收到违规的日期 |

<a id="ReportEntry"></a>
<a id="reportentry"></a>
<a id="ReportEntry"></a>
<a id="reportentry"></a>
#### ReportEntry

| 名称           | 类型          | 描述                                 |
| -------------- | ------------- | ------------------------------------ |
| `type`         | integer       | 报告类型                              |
| `creationTime` | string        | 报告创建时间                 |
| `creatorId`    | string (uuid) | 报告发布者的用户 ID                |
| `description`  | string        | 报告原因                       |
| `flightId`     | string (uuid) | 接收该报告时的航班 ID |