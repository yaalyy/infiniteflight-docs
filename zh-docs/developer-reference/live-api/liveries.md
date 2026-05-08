---
id: liveries
title: 获取涂装
meta: Infinite Flight Live API 涂装端点概览
order: 22
---

<a id="Get All Liveries"></a>
<a id="get all liveries"></a>
<a id="get-all-liveries"></a>
<a id="Get%20All%20Liveries"></a>
<a id="get%20all%20liveries"></a>
<a id="Get All Liveries"></a>
<a id="get all liveries"></a>
<a id="get-all-liveries"></a>
<a id="Get%20All%20Liveries"></a>
<a id="get%20all%20liveries"></a>
# 获取所有涂装

检索所有飞机涂装的列表。

⚠️

: 此 API 仅用于模拟飞行，不得用于现实世界的飞行场景。

<a id="Resource"></a>
<a id="resource"></a>
<a id="Resource"></a>
<a id="resource"></a>
## 资源

**GET** `https://api.infiniteflight.com/public/v2/aircraft/liveries`

<a id="Authorization"></a>
<a id="authorization"></a>
<a id="Authorization"></a>
<a id="authorization"></a>
## 授权

通过以下任一方式包含你的 API 密钥（`<apikey>`）：

- 添加 `apikey` 查询参数。例如，`?apikey=<apikey>`。
- 使用你的 API 密钥发送 bearer 授权头。例如，`Authorization: Bearer <apikey>`。

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
      "id": "1d7dff42-46a5-4c47-a46c-bd39ab9cea8d",
      "aircraftID": "982dd974-5be7-4369-90c6-bd92863632ba",
      "aircraftName": "Airbus A318",
      "liveryName": "Generic"
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

| 名称        | 类型          | 描述                                                     |
| ----------- | ------------- | -------------------------------------------------------- |
| `errorCode` | integer       | _枚举:_ `"Ok = 0"`, `"UserNotFound = 1"`, `"MissingRequestParameters = 2"`, `"EndpointError = 3"`, `"NotAuthorized = 4"`, `"ServerNotFound = 5"`, `"FlightNotFound = 6"`, `"NoAtisAvailable = 7"` |
| `result`    | [LiveryData] | LiveryData 对象数组                                      |

<a id="LiveryData"></a>
<a id="liverydata"></a>
<a id="LiveryData"></a>
<a id="liverydata"></a>
#### LiveryData

| 名称           | 类型          | 描述                 |
| -------------- | ------------- | -------------------- |
| `id`           | string (uuid) | 涂装的唯一标识符     |
| `aircraftID`   | string (uuid) | 飞机机型的 ID        |
| `aircraftName` | string        | 飞机机型的名称       |
| `liveryName`   | string        | 涂装名称             |