---
id: notams
title: 获取 NOTAM
meta: Infinite Flight Live API 的 NOTAM 端点概览
order: 19
contributor: sqeezelemon
---

<a id="Get NOTAMs"></a>
<a id="get notams"></a>
<a id="get-notams"></a>
<a id="Get%20NOTAMs"></a>
<a id="get%20notams"></a>
<a id="Get NOTAMs"></a>
<a id="get notams"></a>
<a id="get-notams"></a>
<a id="Get%20NOTAMs"></a>
<a id="get%20notams"></a>
# 获取 NOTAM

检索某个会话的所有 NOTAM 列表。

⚠️

: 此 API 仅用于模拟飞行，不得用于真实世界的飞行场景。

<a id="Resource"></a>
<a id="resource"></a>
<a id="Resource"></a>
<a id="resource"></a>
## 资源

**GET** `https://api.infiniteflight.com/public/v2/sessions/{sessionId}/notams`

<a id="Authorization"></a>
<a id="authorization"></a>
<a id="Authorization"></a>
<a id="authorization"></a>
## 授权

通过以下任一方式包含你的 API 密钥 (`<apikey>`)：

- 添加 `apikey` 查询参数。例如，`?apikey=<apikey>`。
- 使用你的 API 密钥发送 bearer 授权头。例如，`Authorization: Bearer <apikey>`。

<a id="Parameters"></a>
<a id="parameters"></a>
<a id="Parameters"></a>
<a id="parameters"></a>
## 参数

| 名称        | 位于       | 描述                                                   | 必填 | Schema        |
| ----------- | ---------- | ------------------------------------------------------ | ---- | ------------- |
| `sessionId` | path       | 从 Sessions 端点返回的会话 ID                          | 是   | string (uuid) |

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
      "id": "53671e16-f937-47ca-a5db-c13b6a882851",
      "title": "Special Airport Procedures",
      "author": "Infinite Flight",
      "type": 0,
      "sessionId": "7e5dcd44-1fb5-49cc-bc2c-a9aab1f6a856",
      "radius": 3,
      "message": "Special Airport Procedures in Effect:\n\nNo straight in approached allowed RWY 13\n\nCC NDB 4500ft - 040° HDG Descending to SC NDB - Visual Right Turn Abeam Checkerboard to RWY 13\n\nPublished Approach Procedures (Found Online) Recommended",
      "longitude": 114.20680199460077,
      "latitude": 22.31646633312086,
      "icao": "VHHX",
      "floor": 0,
      "ceiling": 10000,
      "startTime": "2022-02-14T16:34:14.916",
      "endTime": "2100-01-01T16:34:00"
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
| ----------- | ------------- | ----------------------------------------------------- |
| `errorCode` | integer       | _枚举:_ `"Ok = 0"`, `"UserNotFound = 1"`, `"MissingRequestParameters = 2"`, `"EndpointError = 3"`, `"NotAuthorized = 4"`, `"ServerNotFound = 5"`, `"FlightNotFound = 6"`, `"NoAtisAvailable = 7"` |
| `result`    | [NotamResult] | FlightEntry 对象数组                                 |

<a id="NotamResult"></a>
<a id="notamresult"></a>
<a id="NotamResult"></a>
<a id="notamresult"></a>
#### NotamResult

| 名称                  | 类型          | 描述                                                  |
| --------------------- | ------------- | ----------------------------------------------------- |
| `id`            | string (uuid) | NOTAM 的唯一标识符                             |
| `title`              | string | NOTAM 的简短标题                               |
| `author`          | string | NOTAM 作者姓名                      |
| `type`            | NotamType | NOTAM 类型。 _枚举:_ `"NOTAM" = 0, "TFR" = 1`    |
| `sessionId`            | string (uuid)        | 发布该 NOTAM 的会话 ID。对所有会话为 `null`。 |
| `radius` | float        | NOTAM 的半径，单位为 NM |
| `message`            | string        | NOTAM 的主要内容                                      |
| `latitude`            | double        | NOTAM 中心点的十进制度纬度                     |
| `longitude`            | double        | NOTAM 中心点的十进制度经度                    |
| `icao`            | string        | 离 NOTAM 最近的机场 ICAO 代码                     |
| `floor`               | integer        | NOTAM 的最低高度，单位为英尺                 |
| `ceiling`       | integer        | NOTAM 的最高高度，单位为英尺             |
| `startTime`               | string (datetime)        | NOTAM 生效的时间                             |
| `endTime`             | string (datetime)         | NOTAM 失效的时间                           |