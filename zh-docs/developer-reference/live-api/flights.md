---
id: flights
title: 获取航班
meta: Infinite Flight Live API 航班端点概览
order: 4
---

<a id="Get Flights"></a>
<a id="get flights"></a>
<a id="get-flights"></a>
<a id="Get%20Flights"></a>
<a id="get%20flights"></a>
<a id="Get Flights"></a>
<a id="get flights"></a>
<a id="get-flights"></a>
<a id="Get%20Flights"></a>
<a id="get%20flights"></a>
# 获取航班

检索某个会话的所有航班列表。

⚠️

: 此 API 仅用于模拟飞行，不得用于真实飞行场景。

<a id="Resource"></a>
<a id="resource"></a>
<a id="Resource"></a>
<a id="resource"></a>
## 资源

**GET** `https://api.infiniteflight.com/public/v2/sessions/{sessionId}/flights`

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

| 名称         | 所在位置 | 描述                                              | 必需 | Schema        |
| ------------ | -------- | ------------------------------------------------- | ---- | ------------- |
| `sessionId`  | path     | 从 Sessions endpoint 返回的会话 ID                 | 是   | string (uuid) |

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
      "username": "Cameron",
      "callsign": "EC-CAM",
      "latitude": 30.123479009207056,
      "longitude": 31.413340256981044,
      "altitude": 597.8003749797689,
      "speed": 185.3844049009562,
      "verticalSpeed": 2167.31591796875,
      "track": 162.13836669921875,
      "lastReport": "2020-10-02 00:46:19Z",
      "flightId": "348d1ba8-1e60-48ca-8278-42f019147de8",
      "userId": "3f8b28bf-bbb1-4024-80ae-2a0ea9b30685",
      "aircraftId": "de510d3d-04f8-46e0-8d65-55b888f33129",
      "liveryId": "c875c0e9-19c2-420d-8fb4-32c151bd797c",
      "heading": 159.33542,
      "virtualOrganization": "IFATC [IFATC]",
      "pilotState": 0,
      "isConnected": true
    }
  ]
}
```

<a id="LiveAPIResponse"></a>
<a id="liveapiresponse"></a>
<a id="LiveAPIResponse"></a>
<a id="liveapiresponse"></a>
#### LiveAPIResponse

*响应类型：* `application/json`

| 名称         | 类型           | 描述                                                                 |
| ------------ | -------------- | -------------------------------------------------------------------- |
| `errorCode`  | integer        | _枚举：_ `"Ok = 0"`, `"UserNotFound = 1"`, `"MissingRequestParameters = 2"`, `"EndpointError = 3"`, `"NotAuthorized = 4"`, `"ServerNotFound = 5"`, `"FlightNotFound = 6"`, `"NoAtisAvailable = 7"` |
| `result`     | [FlightEntry]  | FlightEntry 对象数组                                                 |

<a id="FlightEntry"></a>
<a id="flightentry"></a>
<a id="FlightEntry"></a>
<a id="flightentry"></a>
#### FlightEntry

| 名称                  | 类型           | 描述                                                                 |
| --------------------- | -------------- | -------------------------------------------------------------------- |
| `flightId`            | string (uuid)  | 航班的唯一标识符                                                      |
| `userId`              | string (uuid)  | 用户的唯一标识符                                                      |
| `aircraftId`          | string (uuid)  | 机型的唯一标识符                                                      |
| `liveryId`            | string (uuid)  | 涂装与机型组合的唯一标识符。                                          |
| `username`            | string         | 若账户已关联，则为该用户的论坛用户名。若账户未关联，则为 null         |
| `virtualOrganization` | string         | 若已关联，则为该用户论坛账户的虚拟组织。若未设置，则可为 null          |
| `callsign`            | string         | 航班呼号                                                            |
| `latitude`            | double         | 当前飞机的十进制度纬度                                               |
| `longitude`           | double         | 当前飞机的十进制度经度                                               |
| `altitude`            | double         | 当前飞机高度，单位为英尺                                              |
| `speed`               | double         | 当前飞机地速，单位为节                                                 |
| `verticalSpeed`       | double         | 当前飞机垂直速度，单位为英尺/分钟                                      |
| `track`               | double         | 飞机航迹，单位为度                                                    |
| `heading`             | float          | 飞机航向，单位为度                                                    |
| `lastReport`          | string         | 航班最后一次位置报告时间，格式如下：`YYYY-MM-DD HH:mm:ssZ`            |
| `pilotState`          | integer        | 飞行员当前状态。_枚举：_ `"Active = 0"`, `"AwayInFlight = 1"`, `"AwayParked = 2"`, `"InBackground = 3"`。**注意：**此字段需要 Infinite Flight 25.1 或更高版本才能正常工作。 |
| `isConnected`         | boolean        | 指示飞行员当前是否已连接到服务器。**注意：**此字段需要 Infinite Flight 25.1 或更高版本才能正常工作。 |