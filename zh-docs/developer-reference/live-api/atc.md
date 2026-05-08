---
id: atc
title: 获取 ATC
meta: Infinite Flight Live API 中 ATC 端点概览
order: 8
contributor: KaiM,sqeezelemon
---

<a id="Get Active ATC Frequencies"></a>
<a id="get active atc frequencies"></a>
<a id="get-active-atc-frequencies"></a>
<a id="Get%20Active%20ATC%20Frequencies"></a>
<a id="get%20active%20atc%20frequencies"></a>
<a id="Get Active ATC Frequencies"></a>
<a id="get active atc frequencies"></a>
<a id="get-active-atc-frequencies"></a>
<a id="Get%20Active%20ATC%20Frequencies"></a>
<a id="get%20active%20atc%20frequencies"></a>
# 获取活动 ATC 频率

检索某个会话中当前处于活动状态的空中交通管制频率

⚠️

: 此 API 仅用于模拟飞行，严禁用于真实世界的飞行场景。

<a id="Resource"></a>
<a id="resource"></a>
<a id="Resource"></a>
<a id="resource"></a>
## 资源

**GET** `https://api.infiniteflight.com/public/v2/sessions/{sessionId}/atc`

<a id="Authorization"></a>
<a id="authorization"></a>
<a id="Authorization"></a>
<a id="authorization"></a>
## 授权

通过以下任一方式包含你的 API 密钥（`<apikey>`）：

-   添加 `apikey` 查询参数。例如，`?apikey=<apikey>`。
-   使用你的 API 密钥发送 bearer 授权头。例如，`Authorization: Bearer <apikey>`。

<a id="Parameters"></a>
<a id="parameters"></a>
<a id="Parameters"></a>
<a id="parameters"></a>
## 参数

| 名称        | 位置       | 描述                                           | 必填 | 模式          |
| ----------- | ---------- | ---------------------------------------------- | ---- | ------------- |
| `sessionId` | path       | 从 Sessions 端点返回的会话 ID                 | 是   | string (uuid) |

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
            "frequencyId": "c2d7decc-2803-c905-5d88-81bc07626b1f",
            "userId": "3f8b28bf-bbb1-4024-80ae-2a0ea9b30685",
            "username": "Cameron",
            "virtualOrganization": null,
            "airportName": "LEPA",
            "type": 1,
            "latitude": 39.551575,
            "longitude": 2.736811,
            "startTime": "2020-10-02 15:47:25Z"
        }
    ]
}
```

<a id="LiveAPIResponse"></a>
<a id="liveapiresponse"></a>
<a id="LiveAPIResponse"></a>
<a id="liveapiresponse"></a>
#### LiveAPIResponse

_响应类型：_ `application/json`

| 名称         | 类型                | 描述                                                                                                                                                                                       |
| ------------ | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `errorCode`  | integer             | _枚举：_ `"Ok = 0"`, `"UserNotFound = 1"`, `"MissingRequestParameters = 2"`, `"EndpointError = 3"`, `"NotAuthorized = 4"`, `"ServerNotFound = 5"`, `"FlightNotFound = 6"`, `"NoAtisAvailable = 7"` |
| `result`     | [ActiveATCFacility] | ActiveATCFacility 对象数组                                                                                                                                                                 |

<a id="ActiveATCFacility"></a>
<a id="activeatcfacility"></a>
<a id="ActiveATCFacility"></a>
<a id="activeatcfacility"></a>
#### ActiveATCFacility

| 名称                  | 类型          | 描述                                                                                                                                                                                                                                                                    |
| --------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `frequencyId`         | string (uuid) | 已开启频率的唯一标识符                                                                                                                                                                                                                                                  |
| `userId`              | string (uuid) | 控制该频率的用户的唯一标识符                                                                                                                                                                                                                                            |
| `username`            | string        | 如果账户已关联，则为用户的论坛用户名。若账户未关联，则为 null                                                                                                                                                                                                          |
| `virtualOrganization` | string        | _(当前未使用)_                                                                                                                                                                                                                                                          |
| `airportName`         | string        | 机场的 4 字符 ICAO 标识符。`center` 时为 `null`                                                                                                                                                                                                                         |
| `type`                | integer       | 已开启频率的类型 - 并非所有类型都在使用中。_枚举：_ `"Ground = 0"`, `"Tower = 1"`, `"Unicom = 2"`, `"Clearance = 3"`, `"Approach = 4"`, `"Departure = 5"`, `"Center = 6"`, `"ATIS = 7"`, `"Aircraft = 8"`, `"Recorded = 9"`, `"Unknown = 10"`, `"Unused = 11"` |
| `latitude`            | float         | 机场的十进制度纬度                                                                                                                                                                                                                                                       |
| `longitude`           | float         | 机场的十进制度经度                                                                                                                                                                                                                                                       |
| `startTime `          | string        | 频率开启时间，格式如下：`YYYY-MM-DD HH:mm:ssZ`                                                                                                                                                                                                                           |