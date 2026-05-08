---
id: 3d-airports
title: 获取 3D 机场
meta: Infinite Flight Live API 的 3D 机场端点概览
order: 25
---

<a id="Get 3D Airports"></a>
<a id="get 3d airports"></a>
<a id="get-3d-airports"></a>
<a id="Get%203D%20Airports"></a>
<a id="get%203d%20airports"></a>
<a id="Get 3D Airports"></a>
<a id="get 3d airports"></a>
<a id="get-3d-airports"></a>
<a id="Get%203D%20Airports"></a>
<a id="get%203d%20airports"></a>
# 获取 3D 机场

检索 Infinite Flight 中可用的 3D 机场列表，以及位置数据和场景编辑元数据。

⚠️

: 此 API 仅用于模拟飞行，绝不得用于真实飞行场景。

<a id="Resource"></a>
<a id="resource"></a>
<a id="Resource"></a>
<a id="resource"></a>
## 资源

**GET** `https://api.infiniteflight.com/public/v2/airports`

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

| 名称        | 类型          | 描述                                                      |
| ----------- | ------------- | ------------------------------------------------------------ |
| `errorCode` | integer       | _枚举：_ `"Ok = 0"`, `"UserNotFound = 1"`, `"MissingRequestParameters = 2"`, `"EndpointError = 3"`, `"NotAuthorized = 4"`, `"ServerNotFound = 5"`, `"FlightNotFound = 6"`, `"NoAtisAvailable = 7"` |
| `result`    | [AirportInfo] | AirportInfo 对象数组                                         |

<a id="AirportInfo"></a>
<a id="airportinfo"></a>
<a id="AirportInfo"></a>
<a id="airportinfo"></a>
#### AirportInfo

| 名称                | 类型    | 描述                                                  |
| ------------------- | ------- | ------------------------------------------------------------ |
| `icao`              | string  | 机场的 ICAO 代码                                          |
| `iata`              | string  | 机场的 IATA 代码                                          |
| `name`              | string  | 机场的官方名称                                            |
| `city`              | string  | 机场所在城市                                              |
| `state`             | string  | 机场所在州                                                |
| `country`           | Country | 关于机场所在国家的信息                                    |
| `class`             | integer | 基于其特征和流量对机场进行的分类                          |
| `frequenciesCount`  | integer | 机场可用通信频率数量                                      |
| `elevation`         | integer | 机场海拔高度（英尺）                                      |
| `latitude`          | float   | 机场的地理纬度                                            |
| `longitude`         | float   | 机场的地理经度                                            |
| `timezone`          | string  | 机场所在时区                                              |
| `has3dBuildings`    | boolean | 指示机场是否具有 3D 建筑                                  |
| `hasJetbridges`     | boolean | 指示机场是否具有廊桥                                      |
| `hasSafedockUnits`  | boolean | 指示机场是否具有 Safedock 设备                            |
| `hasTaxiwayRouting` | boolean | 指示机场是否具备滑行道路线规划能力                        |

<a id="Country"></a>
<a id="country"></a>
<a id="Country"></a>
<a id="country"></a>
#### Country

| 名称       | 类型   | 描述                                |
| ---------- | ------ | ------------------------------------------ |
| `id`       | integer| （请忽略，稍后会移除）                       |
| `name`     | string | 国家名称                                |
| `isoCode`  | string | 国家 ISO 代码                |