---
id: sessions
title: 获取会话
meta: Infinite Flight Live API 的会话端点概览
order: 3
---

<a id="Get Sessions"></a>
<a id="get sessions"></a>
<a id="get-sessions"></a>
<a id="Get%20Sessions"></a>
<a id="get%20sessions"></a>
<a id="Get Sessions"></a>
<a id="get sessions"></a>
<a id="get-sessions"></a>
<a id="Get%20Sessions"></a>
<a id="get%20sessions"></a>
# 获取会话

检索 Infinite Flight 中的活动会话（服务器）。

⚠️

: 此 API 仅用于模拟飞行，且不得用于真实世界的飞行场景。

<a id="Resource"></a>
<a id="resource"></a>
<a id="Resource"></a>
<a id="resource"></a>
## 资源

**GET** `https://api.infiniteflight.com/public/v2/sessions`

<a id="Authorization"></a>
<a id="authorization"></a>
<a id="Authorization"></a>
<a id="authorization"></a>
## 授权

通过以下任一方式包含你的 API 密钥 (`<apikey>`)：

- 添加 `apikey` 查询参数。例如，`?apikey=<apikey>`。
- 使用你的 API 密钥发送 bearer 授权标头。例如，`Authorization: Bearer <apikey>`。

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
      "maxUsers": 1000,
      "id": "89573c7f-d398-4281-bcc0-3e9b7f6b8492",
      "name": "Sample Server",
      "userCount": 187,
      "type": 0,
      "worldType": 0,
      "minimumGradeLevel": 2,
      "minimumAppVersion": "24.3",
      "maximumAppVersion": null
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

| 名称         | 类型          | 描述                                                     |
| ------------ | ------------- | -------------------------------------------------------- |
| `errorCode`  | integer       | _枚举:_ `"Ok = 0"`, `"UserNotFound = 1"`, `"MissingRequestParameters = 2"`, `"EndpointError = 3"`, `"NotAuthorized = 4"`, `"ServerNotFound = 5"`, `"FlightNotFound = 6"`, `"NoAtisAvailable = 7"` |
| `result`     | [SessionInfo] | SessionInfo 对象数组                                      |

<a id="SessionInfo"></a>
<a id="sessioninfo"></a>
<a id="SessionInfo"></a>
<a id="sessioninfo"></a>
#### SessionInfo

| 名称                | 类型    | 描述                                                     |
| ------------------- | ------- | -------------------------------------------------------- |
| `id`                | string  | 服务器的唯一标识符。用于请求航班和 ATC 数据              |
| `name`              | string  | 服务器名称                                               |
| `maxUsers`          | integer | 服务器可接受的最大用户数                                 |
| `userCount`         | integer | 连接到服务器的用户数                                     |
| `type`              | integer | _枚举:_ `"Unrestricted = 0"`, `"Restricted = 1"`         |
| `worldType`         | integer | _枚举:_ `"Solo = 0"`, `"Casual = 1"`, `"Training = 2"`, `"Expert = 3"`, `"Private = 4"` |
| `minimumGradeLevel` | integer | 访问服务器所需的最低等级索引。加 1 可得到等级名称（即索引 0 为 1 级） |
| `minimumAppVersion` | string  | 能够连接到此服务器的 Infinite Flight 最低版本            |
| `maximumAppVersion` | string  | 能够连接到此服务器的 Infinite Flight 最低版本            |