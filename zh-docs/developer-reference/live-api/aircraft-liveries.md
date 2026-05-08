---
id: aircraft-liveries
title: 获取机型涂装
meta: Infinite Flight Live API 机型涂装端点概览
order: 21
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
# 获取机型涂装

获取某一机型的全部涂装列表。

⚠️

: 本 API 仅适用于模拟飞行，不得用于真实世界飞行场景。


<a id="Resource"></a>
<a id="resource"></a>
<a id="Resource"></a>
<a id="resource"></a>
## 资源

**GET** `https://api.infiniteflight.com/public/v2/aircraft/{aircraftId}/liveries`

<a id="Authorization"></a>
<a id="authorization"></a>
<a id="Authorization"></a>
<a id="authorization"></a>
## 授权

通过以下任一方式包含你的 API 密钥（`<apikey>`）：

- 添加 `apikey` 查询参数。例如，`?apikey=<apikey>`。
- 发送带有你的 API 密钥的 bearer authorization header。例如，`Authorization: Bearer <apikey>`。

<a id="Parameters"></a>
<a id="parameters"></a>
<a id="Parameters"></a>
<a id="parameters"></a>
## 参数

| 名称         | 所在位置 | 描述                                          | 必填 | Schema        |
| ------------ | -------- | --------------------------------------------- | ---- | ------------- |
| `aircraftId` | path     | 从 aircraft 端点返回的机型 ID                | 是   | string (uuid) |

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
      "id": "701c826b-a160-4b1a-a89f-08d0afb4af1b",
      "aircraftID": "710c84ae-6fdc-4c4a-ac3b-4031c3036e98",
      "aircraftName": "Airbus A220-300",
      "liveryName": "airBaltic"
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

*响应类型：* `application/json`

| 名称        | 类型          | 描述                                                  |
| ----------- | ------------- | ----------------------------------------------------- |
| `errorCode` | integer       | _枚举：_ `"Ok = 0"`, `"UserNotFound = 1"`, `"MissingRequestParameters = 2"`, `"EndpointError = 3"`, `"NotAuthorized = 4"`, `"ServerNotFound = 5"`, `"FlightNotFound = 6"`, `"NoAtisAvailable = 7"` |
| `result`    | [LiveryData] | LiveryData 对象数组                                  |

<a id="LiveryData"></a>
<a id="liverydata"></a>
<a id="LiveryData"></a>
<a id="liverydata"></a>
#### LiveryData

| 名称           | 类型          | 描述                      |
| -------------- | ------------- | ------------------------- |
| `id`           | string (uuid) | 涂装的唯一标识符          |
| `aircraftID`   | string (uuid) | 机型 ID                  |
| `aircraftName` | string        | 机型名称                 |
| `liveryName`   | string        | 涂装名称                 |