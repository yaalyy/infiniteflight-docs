---
id: airport-information
title: 获取机场信息
meta: Infinite Flight Live API 机场信息端点概览
order: 23
---

<a id="Get Airport Information"></a>
<a id="get airport information"></a>
<a id="get-airport-information"></a>
<a id="Get%20Airport%20Information"></a>
<a id="get%20airport%20information"></a>
<a id="Get Airport Information"></a>
<a id="get airport information"></a>
<a id="get-airport-information"></a>
<a id="Get%20Airport%20Information"></a>
<a id="get%20airport%20information"></a>
# 获取机场信息

获取某个机场的具体信息，包括位置数据和场景编辑元数据。

⚠️

: 此 API 仅用于模拟飞行，切勿用于真实飞行场景。

<a id="Resource"></a>
<a id="resource"></a>
<a id="Resource"></a>
<a id="resource"></a>
## 资源

**GET** `https://api.infiniteflight.com/public/v2/airport/{airportIcao}`

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

| Name          | Located in | Description                               | Required | Schema        |
| ------------- | ---------- | ----------------------------------------- | -------- | ------------- |
| `airportIcao` | query      | 要获取的机场 ICAO 代码                     | Yes      | string        |

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
        "icao": "KLAX",
        "iata": "LAX",
        "name": "Los Angeles Intl",
        "city": "Los Angeles",
        "state": "California",
        "country": {
            "id": 243,
            "name": "United States",
            "isoCode": "US"
        },
        "class": 3,
        "frequenciesCount": 16,
        "elevation": 125,
        "latitude": 33.9431209564209,
        "longitude": -118.40881633758545,
        "timezone": "UTC-08:00 America",
        "has3dBuildings": true,
        "hasJetbridges": true,
        "hasSafedockUnits": true,
        "hasTaxiwayRouting": true
    }
}
```

<a id="LiveAPIResponse"></a>
<a id="liveapiresponse"></a>
<a id="LiveAPIResponse"></a>
<a id="liveapiresponse"></a>
#### LiveAPIResponse

*响应类型:* `application/json`

| Name        | Type          | Description                                                  |
| ----------- | ------------- | ------------------------------------------------------------ |
| `errorCode` | integer       | _枚举:_ `"Ok = 0"`, `"UserNotFound = 1"`, `"MissingRequestParameters = 2"`, `"EndpointError = 3"`, `"NotAuthorized = 4"`, `"ServerNotFound = 5"`, `"FlightNotFound = 6"`, `"NoAtisAvailable = 7"` |
| `result`    | AirportInfo | 关于该机场的信息                                             |

<a id="AirportInfo"></a>
<a id="airportinfo"></a>
<a id="AirportInfo"></a>
<a id="airportinfo"></a>
#### AirportInfo

| Name                | Type    | Description                                                  |
| ------------------- | ------- | ------------------------------------------------------------ |
| `icao`              | string  | 机场的 ICAO 代码                                             |
| `iata`              | string  | 机场的 IATA 代码                                             |
| `name`              | string  | 机场的官方名称                                               |
| `city`              | string  | 机场所在城市                                                 |
| `state`             | string  | 机场所在州                                                   |
| `country`           | Country | 机场所在国家的信息                                           |
| `class`             | integer | 基于其特征和流量对机场进行的分类                             |
| `frequenciesCount`  | integer | 机场可用通信频率的数量                                       |
| `elevation`         | integer | 机场海拔高于海平面的高度（英尺）                             |
| `latitude`          | float   | 机场的地理纬度                                               |
| `longitude`         | float   | 机场的地理经度                                               |
| `timezone`          | string  | 机场时区                                                     |
| `has3dBuildings`    | boolean | 指示机场是否有 3D 建筑                                       |
| `hasJetbridges`     | boolean | 指示机场是否有登机桥                                         |
| `hasSafedockUnits`  | boolean | 指示机场是否有 Safedock 设备                                |
| `hasTaxiwayRouting` | boolean | 指示机场是否具备滑行道导航能力                               |

<a id="Country"></a>
<a id="country"></a>
<a id="Country"></a>
<a id="country"></a>
#### Country

| Name       | Type   | Description                                |
| ---------- | ------ | ------------------------------------------ |
| `id`       | integer| （请忽略，这项即将被移除）                   |
| `name`     | string | 国家名称                                   |
| `isoCode`  | string | 该国家的 ISO 代码                         |