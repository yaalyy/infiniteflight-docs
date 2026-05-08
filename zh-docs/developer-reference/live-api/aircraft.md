---
id: aircraft
title: 获取飞机
meta: Infinite Flight Live API 的飞机端点概览
order: 20
---

<a id="Get Aircraft"></a>
<a id="get aircraft"></a>
<a id="get-aircraft"></a>
<a id="Get%20Aircraft"></a>
<a id="get%20aircraft"></a>
<a id="Get Aircraft"></a>
<a id="get aircraft"></a>
<a id="get-aircraft"></a>
<a id="Get%20Aircraft"></a>
<a id="get%20aircraft"></a>
# 获取飞机

检索所有飞机型号的列表。

⚠️

: 此 API 仅用于模拟飞行，且不得用于真实飞行情境。

<a id="Resource"></a>
<a id="resource"></a>
<a id="Resource"></a>
<a id="resource"></a>
## 资源

**GET** `https://api.infiniteflight.com/public/v2/aircraft`

<a id="Authorization"></a>
<a id="authorization"></a>
<a id="Authorization"></a>
<a id="authorization"></a>
## 授权

通过以下任一方式包含你的 API 密钥（`<apikey>`）：

- 添加 `apikey` 查询参数。例如，`?apikey=<apikey>`。
- 使用你的 API 密钥发送 bearer authorization header。例如，`Authorization: Bearer <apikey>`。

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
      "id": "81d9ccd4-9c03-493a-811e-8fad3e57bd05",
      "name": "A-10"
    },
    ...
  ]
}
```

<a id="LiveAPIResponse"></a>
<a id="liveapiresponse"></a>
<a id="LiveAPIResponse"></a>
<a id="liveapiresponse"></a>
#### LiveAPIResponse

*响应类型:* `application/json`

| 名称        | 类型          | 描述                                                  |
| ----------- | ------------- | ------------------------------------------------------------ |
| `errorCode` | integer       | _枚举：_ `"Ok = 0"`, `"UserNotFound = 1"`, `"MissingRequestParameters = 2"`, `"EndpointError = 3"`, `"NotAuthorized = 4"`, `"ServerNotFound = 5"`, `"FlightNotFound = 6"`, `"NoAtisAvailable = 7"` |
| `result`    | [AircraftPackage] | AircraftPackage 对象数组                                 |

<a id="AircraftPackage"></a>
<a id="aircraftpackage"></a>
<a id="AircraftPackage"></a>
<a id="aircraftpackage"></a>
#### AircraftPackage

| 名称   | 类型          | 描述                     |
| ------ | ------------- | ------------------------------- |
| `id`   | string (uuid) | 该型号的唯一标识符 |
| `name` | string        | 飞机名称            |