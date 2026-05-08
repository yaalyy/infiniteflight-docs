---
id: airport-status
title: 获取机场状态
meta: Infinite Flight Live API 机场状态端点概览
order: 12
contributor: sqeezelemon
---

<a id="Get Airport Status"></a>
<a id="get airport status"></a>
<a id="get-airport-status"></a>
<a id="Get%20Airport%20Status"></a>
<a id="get%20airport%20status"></a>
<a id="Get Airport Status"></a>
<a id="get airport status"></a>
<a id="get-airport-status"></a>
<a id="Get%20Airport%20Status"></a>
<a id="get%20airport%20status"></a>
# 获取机场状态

检索机场的当前 ATC 状态信息，以及进港和出港航空器数量。

⚠️

: 此 API 仅用于模拟飞行，不得用于真实世界的飞行情境。

<a id="Resource"></a>
<a id="resource"></a>
<a id="Resource"></a>
<a id="resource"></a>
## 资源

**GET** `https://api.infiniteflight.com/public/v2/sessions/{sessionId}/airport/{airportIcao}/status`

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

| 名称          | 位置       | 描述                                   | 必需 | Schema        |
| ------------- | ---------- | -------------------------------------- | ---- | ------------- |
| `airportIcao` | query      | 要获取状态的机场 ICAO                 | 是   | string        |
| `sessionId`   | query      | Live Server 的会话（服务器）ID        | 是   | string (uuid) |

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
    "airportIcao": "VTBS",
    "airportName": "Suvarnabhumi Airport",
    "inboundFlightsCount": 40,
    "inboundFlights": [
      "4f559855-fecc-4a8a-a95e-1d097eed9b72",
	  ...
    ],
    "outboundFlightsCount": 19,
    "outboundFlights": [
      "59e9509b-214a-4f8c-9d45-29c4f7ea01d7",
	  ...
    ],
    "atcFacilities": [
      {
        "frequencyId": "23bea566-20a0-2858-a40e-179d0699afc1",
        "userId": "05328fc4-b651-45e9-8e1f-328095329484",
        "username": "Rhys_V",
        "virtualOrganization": null,
        "airportName": "VTBS",
        "type": 4,
        "latitude": 13.680815,
        "longitude": 100.74768,
        "startTime": "2021-02-08 09:59:58Z"
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

_响应类型：_ `application/json`

| 名称        | 类型    | 描述                                                                                                                                                                                       |
| ----------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `errorCode` | integer | _枚举：_ `"Ok = 0"`, `"UserNotFound = 1"`, `"MissingRequestParameters = 2"`, `"EndpointError = 3"`, `"NotAuthorized = 4"`, `"ServerNotFound = 5"`, `"FlightNotFound = 6"`, `"NoAtisAvailable = 7"` |
| `result`    | string  | 一个 `AirportStatus` 对象                                                                                                                                                                         |

<a id="Airport Status"></a>
<a id="airport status"></a>
<a id="airport-status"></a>
<a id="Airport%20Status"></a>
<a id="airport%20status"></a>
<a id="Airport Status"></a>
<a id="airport status"></a>
<a id="airport-status"></a>
<a id="Airport%20Status"></a>
<a id="airport%20status"></a>
#### 机场状态

| 名称                   | 类型                | 描述                                                                                                       |
| ---------------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `airportIcao`          | string              | 机场的 ICAO 代码                                                                                               |
| `airportName`          | string              | 机场名称                                          |
| `inboundFlightsCount`  | integer             | 进港到该机场的航空器数量（飞行计划中的最终航点必须设置为该机场 ICAO）      |
| `inboundFlights`       | [string (uuid)]     | 进港到该机场的航班标识符列表。可用于获取飞行计划或航线信息    |
| `outboundFlightsCount` | integer             | 从该机场出发的航空器数量（飞行计划中的第一个航点必须设置为该机场 ICAO）       |
| `outboundFlights`      | [string (uuid)]     | 从该机场出港的航班标识符列表。可用于获取飞行计划或航线信息 |
| `atcFacilities`        | [ActiveATCFacility] | ActiveATCFacility 对象数组                                                                                |

<a id="ActiveATCFacility"></a>
<a id="activeatcfacility"></a>
<a id="ActiveATCFacility"></a>
<a id="activeatcfacility"></a>
#### ActiveATCFacility

| 名称                  | 类型          | 描述                                                                                                                                                                                                                                                                    |
| --------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `frequencyId`         | string (uuid) | 开放频率的唯一标识符                                                                                                                                                                                                                                       |
| `userId`              | string (uuid) | 控制该频率用户的唯一标识符                                                                                                                                                                                                                       |
| `username`            | string        | 如果账户已关联，则为用户的论坛用户名；如果账户未关联，则为 `null`                                                                                                                                                                             |
| `virtualOrganization` | string        | _(当前未使用)_                                                                                                                                                                                                                                                       |
| `airportName`         | string        | 机场的 4 字符 ICAO 标识符。中心频率为 `null`                                                                                                                                                                                                             |
| `type`                | integer       | 已开放的频率类型 - 并非全部都在使用中。_枚举：_ `"Ground = 0"`, `"Tower = 1"`, `"Unicom = 2"`, `"Clearance = 3"`, `"Approach = 4"`, `"Departure = 5"`, `"Center = 6"`, `"ATIS = 7"`, `"Aircraft = 8"`, `"Recorded = 9"`, `"Unknown = 10"`, `"Unused = 11"` |
| `latitude`            | float         | 机场的十进制度纬度                                                                                                                                                                                                                                                |
| `longitude`           | float         | 机场的十进制度经度                                                                                                                                                                                                                                               |
| `startTime `          | string        | 频率开启时间，格式如下：`YYYY-MM-DD HH:mm:ssZ`                                                                                                                                                                                        |