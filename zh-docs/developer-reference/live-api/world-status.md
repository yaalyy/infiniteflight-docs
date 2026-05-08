---
id: world-status
title: 获取世界状态
meta: Infinite Flight Live API 世界状态端点概览
order: 13
contributor: sqeezelemon
---

<a id="Get World Status"></a>
<a id="get world status"></a>
<a id="get-world-status"></a>
<a id="Get%20World%20Status"></a>
<a id="get%20world%20status"></a>
<a id="Get World Status"></a>
<a id="get world status"></a>
<a id="get-world-status"></a>
<a id="Get%20World%20Status"></a>
<a id="get%20world%20status"></a>
# 获取世界状态

获取所有在特定服务器上有活动的机场的当前 ATC 状态信息，以及入站/出站航空器信息。

⚠️

: 此 API 仅用于模拟飞行，绝不得用于真实世界的飞行场景。

<a id="Resource"></a>
<a id="resource"></a>
<a id="Resource"></a>
<a id="resource"></a>
## 资源

**GET** `https://api.infiniteflight.com/public/v2/sessions/{sessionId}/world`

<a id="Authorization"></a>
<a id="authorization"></a>
<a id="Authorization"></a>
<a id="authorization"></a>
## 授权

通过以下任一方式包含你的 API 密钥（`<apikey>`）：

- 添加 `apikey` 查询参数。例如：`?apikey=<apikey>`。
- 使用你的 API 密钥发送 bearer 授权头。例如：`Authorization: Bearer <apikey>`。

<a id="Parameters"></a>
<a id="parameters"></a>
<a id="Parameters"></a>
<a id="parameters"></a>
## 参数

| 名称        | 所在位置 | 描述                             | 必需 | 模式          |
| ----------- | -------- | -------------------------------- | ---- | ------------- |
| `sessionId` | query      | Live Server 的 Session（服务器）ID | 是   | string (uuid) |

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
      "airportIcao": "KLAX",
      "airportName": "洛杉矶国际机场",
      "inboundFlightsCount": 103,
      "inboundFlights": [
        "e1cf6c27-6f18-43a0-8bf8-cec5406e93a0",
        ...
      ],
      "outboundFlightsCount": 39,
      "outboundFlights": [
        "e2ded8f8-ff70-454a-911b-f193eb47636f",
        ...
      ],
      "atcFacilities": [
        {
          "frequencyId": "ee835f12-6cf5-eaa1-04bf-2018c7c01ae0",
          "userId": "51f94d83-54e8-4674-ae2d-046a42c04f7a",
          "username": "Manav_Suri",
          "virtualOrganization": null,
          "airportName": "KLAX",
          "type": 0,
          "latitude": 33.943123,
          "longitude": -118.40881,
          "startTime": "2021-02-09 09:53:02Z"
        },
        ...
      ]
    },
  ]
}
```

<a id="LiveAPIResponse"></a>
<a id="liveapiresponse"></a>
<a id="LiveAPIResponse"></a>
<a id="liveapiresponse"></a>
#### LiveAPIResponse

*响应类型：* `application/json`

| 名称        | 类型            | 描述                                                  |
| ----------- | --------------- | ------------------------------------------------------------ |
| `errorCode` | integer         | _枚举：_ `"Ok = 0"`, `"UserNotFound = 1"`, `"MissingRequestParameters = 2"`, `"EndpointError = 3"`, `"NotAuthorized = 4"`, `"ServerNotFound = 5"`, `"FlightNotFound = 6"`, `"NoAtisAvailable = 7"` |
| `result`    | [AirportStatus] | `AirportStatus` 对象数组                          |

<a id="AirportStatus"></a>
<a id="airportstatus"></a>
<a id="AirportStatus"></a>
<a id="airportstatus"></a>
#### AirportStatus

| 名称                   | 类型                | 描述                                                  |
| ---------------------- | ------------------- | ------------------------------------------------------------ |
| `airportIcao`          | string              | 机场的 ICAO 代码                                          |
| `airportName`          | string              | 机场名称                                          |
| `inboundFlightsCount`  | integer             | 进入该机场的航空器数量（航路计划中的最后一个航点必须设置为该机场的 ICAO） |
| `inboundFlights`       | [string (uuid)]     | 进入该机场的航班标识符列表。可用于获取航班计划或航线信息 |
| `outboundFlightsCount` | integer             | 从该机场起飞的航空器数量（航路计划中的第一个航点必须设置为该机场的 ICAO） |
| `outboundFlights`      | [string (uuid)]     | 从该机场出发的航班标识符列表。可用于获取航班计划或航线信息 |
| `atcFacilities`        | [ActiveATCFacility] | `ActiveATCFacility` 对象数组                           |

<a id="ActiveATCFacility"></a>
<a id="activeatcfacility"></a>
<a id="ActiveATCFacility"></a>
<a id="activeatcfacility"></a>
#### ActiveATCFacility

| 名称                  | 类型          | 描述                                                  |
| --------------------- | ------------- | ------------------------------------------------------------ |
| `frequencyId`         | string (uuid) | 开放频率的唯一标识符                     |
| `userId`              | string (uuid) | 控制该频率的用户唯一标识符     |
| `username`            | string        | 如果账号已关联，则为用户的论坛用户名；如果账号未关联，则为 `null` |
| `virtualOrganization` | string        | *(当前未使用)*                                     |
| `airportName`         | string        | 机场的 4 位字符 ICAO 标识符。中心台为 `null` |
| `type`                | integer       | 已开放频率的类型 - 并非所有类型都在使用中。*枚举：* `"Ground = 0"`, `"Tower = 1"`, `"Unicom = 2"`, `"Clearance = 3"`, `"Approach = 4"`, `"Departure = 5"`, `"Center = 6"`, `"ATIS = 7"`, `"Aircraft = 8"`, `"Recorded = 9"`, `"Unknown = 10"`, `"Unused = 11"` |
| `latitude`            | float         | 机场的十进制度纬度                              |
| `longitude`           | float         | 机场的十进制度经度                             |
| `startTime `          | string        | 频率开放时间，格式如下：`YYYY-MM-DD HH:mm:ssZ` |