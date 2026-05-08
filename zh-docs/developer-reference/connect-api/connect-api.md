---
id: version-2
title: Connect API
meta: Infinite Flight Connect API 版本 2 的参考文档
order: 3
contributor: likeablegeek,KaiM,tomthetank
---

<a id="Connect API v2"></a>
<a id="connect api v2"></a>
<a id="connect-api-v2"></a>
<a id="Connect%20API%20v2"></a>
<a id="connect%20api%20v2"></a>
<a id="Connect API v2"></a>
<a id="connect api v2"></a>
<a id="connect-api-v2"></a>
<a id="Connect%20API%20v2"></a>
<a id="connect%20api%20v2"></a>
# Connect API v2

此版本的 API 首次包含于 Infinite Flight 19.4 中。

<a id="Table of Contents"></a>
<a id="table of contents"></a>
<a id="table-of-contents"></a>
<a id="Table%20of%20Contents"></a>
<a id="table%20of%20contents"></a>
<a id="Table of Contents"></a>
<a id="table of contents"></a>
<a id="table-of-contents"></a>
<a id="Table%20of%20Contents"></a>
<a id="table%20of%20contents"></a>
## 目录

- [Connect API v2](#connect-api-v2)
  - [目录](#table-of-contents)
  - [关于 API](#about-the-api)
  - [启用 API](#enabling-the-api)
  - [连接到 API](#connecting-to-the-api)
      - [查找 Infinite Flight 设备](#finding-an-infinite-flight-device)
  - [使用 API](#using-the-api)
      - [API 清单](#the-api-manifest)
      - [API 请求的结构](#the-structure-of-api-requests)
      - [获取清单](#obtaining-the-manifest)
      - [数据类型](#data-types)
        - [小端序](#little-endian)
      - [从 API 获取状态](#retrieving-states-from-the-api)
      - [通过 API 设置状态](#setting-states-with-the-api)
      - [通过 API 运行命令](#running-commands-through-the-api)
      - [从 Infinite Flight v22.1 处理飞行计划](#working-with-flight-plans-from-infinite-flight-v221)

<a id="About the API"></a>
<a id="about the api"></a>
<a id="about-the-api"></a>
<a id="About%20the%20API"></a>
<a id="about%20the%20api"></a>
<a id="About the API"></a>
<a id="about the api"></a>
<a id="about-the-api"></a>
<a id="About%20the%20API"></a>
<a id="about%20the%20api"></a>
## 关于 API

Connect API v2 的设计目标是提供一种高性能方式，用于查询飞机和 Infinite Flight 的状态、修改这些状态，并向 Infinite Flight 发出命令。该 API 经过设计，具有很高的响应速度，因此可用于多种用途，包括在航班进行中以“实时”方式控制 Infinite Flight 的某些方面，以及创建能够迅速响应飞机状态变化的应用程序。

因此，传统基于 HTTP 的 REST API 并不合适，因为它需要在网络上传输更多数据，并且在建立和协商 HTTP 连接时会产生开销，不适合这类应用。

相反，Connect API v2 是一个 [TCP socket](https://www.easytechjunkie.com/what-is-a-tcpip-socket.htm) API。TCP socket 是一种网络级机制，用于在 TCP/IP 网络上的两个设备之间直接通信。它允许设备之间进行原始形式的通信，任意字节序列都可以从一个设备发送到另一个设备。

通过这种方式，Connect API v2 能够在客户端与 Infinite Flight 设备之间使用紧凑、简洁的通信格式，从而以尽可能短的时间交换尽可能多的数据。

简单来说，这意味着命令或请求会以字节序列的形式发送到 API，并按照本文档中概述的结构进行组织。对于需要返回数据的 API，它也会以字节序列的形式返回，随后这些字节需要被“解码”以获得实际传输的信息。

<a id="Enabling the API"></a>
<a id="enabling the api"></a>
<a id="enabling-the-api"></a>
<a id="Enabling%20the%20API"></a>
<a id="enabling%20the%20api"></a>
<a id="Enabling the API"></a>
<a id="enabling the api"></a>
<a id="enabling-the-api"></a>
<a id="Enabling%20the%20API"></a>
<a id="enabling%20the%20api"></a>
## 启用 API

你可以在 Infinite Flight 中启用或禁用 Connect API。在尝试使用 API 连接到 Infinite Flight 设备之前，请前往 Infinite Flight 的 `Settings > General`，并确保已勾选 `Enable Infinite Flight Connect`。

<a id="Connecting to the API"></a>
<a id="connecting to the api"></a>
<a id="connecting-to-the-api"></a>
<a id="Connecting%20to%20the%20API"></a>
<a id="connecting%20to%20the%20api"></a>
<a id="Connecting to the API"></a>
<a id="connecting to the api"></a>
<a id="connecting-to-the-api"></a>
<a id="Connecting%20to%20the%20API"></a>
<a id="connecting%20to%20the%20api"></a>
## 连接到 API

要连接到 Connect API v2，请使用设备的 IP 地址，通过端口 `10112` 与 Infinite Flight 设备建立 TCP socket 连接。

具体方式取决于你用于连接 API 的语言或平台。

可用于建立 TCP socket 连接的常见模块/包示例包括：

* JavaScript (Node): Node 的 [`net` 模块](https://nodejs.org/api/net.html)
* C#: [`TcpClient`](https://docs.microsoft.com/en-us/dotnet/api/system.net.sockets.tcpclient?view=net-6.0)
* Python: [`socket` 模块](https://docs.python.org/3/library/socket.html)
* Swift: [SwiftSocket](https://github.com/swiftsocket/SwiftSocket)
* Kotlin: [`java.net.socket`](https://sylhare.github.io/2020/04/07/Kotlin-tcp-socket-example.html)

<a id="Finding an Infinite Flight Device"></a>
<a id="finding an infinite flight device"></a>
<a id="finding-an-infinite-flight-device"></a>
<a id="Finding%20an%20Infinite%20Flight%20Device"></a>
<a id="finding%20an%20infinite%20flight%20device"></a>
<a id="Finding an Infinite Flight Device"></a>
<a id="finding an infinite flight device"></a>
<a id="finding-an-infinite-flight-device"></a>
<a id="Finding%20an%20Infinite%20Flight%20Device"></a>
<a id="finding%20an%20infinite%20flight%20device"></a>
#### 查找 Infinite Flight 设备

如果要连接的设备 IP 地址未知，可以使用 UDP 在同一本地网络中发现现有的 Infinite Flight 设备。Infinite Flight 会在端口 `15000` 上广播 [UDP](https://www.cloudflare.com/en-gb/learning/ddos/glossary/user-datagram-protocol-udp/) 数据包，其中提供了设备的 IP 地址以及其他详细信息。Infinite Flight 发出的 UDP 广播示例如下：

```json
{
    "state": "Playing",
    "port": 10111,
    "deviceId": "iPad7",
    "aircraft": "Cessna 172",
    "version": "19.4.7354.25209",
    "deviceName": "Thomas’s iPad",
    "addresses": ["fe80::1c79:baf4:f9f1:dd59%3", "192.168.1.26"],
    "livery": "Civil Air Patrol"
}
```

根据这些信息，可以提取设备的 IPv4 或 IPv6 地址，以及当前使用的 Infinite Flight 版本、当前飞机和涂装，以及设备类型。这里显示的端口将是 `10111`，这是 [Connect API v1](https://infiniteflight.com/guide/developer-reference/connect-api/version-1) 的端口。**要连接 v2 API，请按照上文“[连接到 API](#connecting-to-the-api)”中的说明连接到端口 `10112`。**

如何接收这些 UDP 数据包广播取决于所使用的语言或平台。

可用于监听并接收这些 UDP 数据包广播的常见模块/包示例包括：

* JavaScript (Node): Node 的 [`dgram` 模块](https://nodejs.org/api/dgram.html)
* C#: [`UdpClient`](https://docs.microsoft.com/en-us/dotnet/api/system.net.sockets.udpclient?view=net-6.0)
* Python: [`socket` 模块](https://docs.python.org/3/library/socket.html)
* Swift: [Swift 的 `NWListener` 类](https://developer.apple.com/documentation/network/nwlistener)
* Kotlin: [`java.net.DatagramSocket`](https://docs.oracle.com/javase/7/docs/api/java/net/DatagramSocket.html)

<a id="Using the API"></a>
<a id="using the api"></a>
<a id="using-the-api"></a>
<a id="Using%20the%20API"></a>
<a id="using%20the%20api"></a>
<a id="Using the API"></a>
<a id="using the api"></a>
<a id="using-the-api"></a>
<a id="Using%20the%20API"></a>
<a id="using%20the%20api"></a>
## 使用 API

Connect API v2 提供了两种与 Infinite Flight 交互的机制：

* **状态**：状态用于获取或设置航班、飞机或 Infinite Flight 当前活动状态的特定方面。这些内容分为几个组：
    * `aircraft`：从飞机的高度、航向、坡度和俯仰，到襟翼位置、飞机涂装，以及自动驾驶设置的所有内容。
    * `infiniteflight`：与 Infinite Flight 本身状态相关的设置，例如当前的摄像机视角和角度，以及当前使用的 Infinite Flight 版本。
    * `api_joystick`：与 Infinite Flight 手柄支持相关的一组状态。
    * 其他：与 `environment`（例如风速）或 `atmosphere`（用于空气密度）、`simulator` 本身（例如当前飞行时长）以及其他一次性状态相关的其他零散状态。
* **命令**：命令用于复现通常在 Infinite Flight 用户界面中执行的操作，例如切换停机刹车、移动摄像机、启动和停止发动机、移动襟翼、放下起落架等。

<a id="The API Manifest"></a>
<a id="the api manifest"></a>
<a id="the-api-manifest"></a>
<a id="The%20API%20Manifest"></a>
<a id="the%20api%20manifest"></a>
<a id="The API Manifest"></a>
<a id="the api manifest"></a>
<a id="the-api-manifest"></a>
<a id="The%20API%20Manifest"></a>
<a id="the%20api%20manifest"></a>
#### API 清单

每种飞机提供的状态和命令集合都不同。在使用这些状态或命令之前，连接后先从 API 获取清单非常重要，因为成功向 API 发出请求需要用到它。

清单是一长串文本，由一系列条目组成，每个条目对应一个命令或状态。每个条目之间用换行符分隔。

每个条目包含三个以逗号分隔的字段：

* 一个用于通过 API 获取、设置状态或执行命令的数值 ID（32 位整数）。对于任意给定的状态或命令，这些数值 ID 可能会因飞机不同而不同。
* 一个指示该状态所用数据类型的 32 位整数（见下文的“[数据类型](#data-types)”）。对于命令，这一字段将是 `-1`，而不是表示数据类型的整数。
* 命令或状态的名称，以便于理解的方式表达命令意图。即使可用的状态和命令集合可能不同，或者数值 ID 不同，这些名称在不同飞机之间也会保持一致。

下面是一个典型清单的摘录，展示了若干状态的格式：

```markup
    632,4,aircraft/0/flightplan/route\n
    539,2,aircraft/0/groundspeed\n
    548,2,aircraft/0/heading_magnetic\n
    556,0,aircraft/0/is_on_ground\n
    554,3,aircraft/0/latitude\n
    555,3,aircraft/0/longitude\n
```

> *在这个示例中，为了便于阅读，文本在每个换行符（`\n`）后进行了拆分。实际文本不会在换行符后额外包含一个换行。*

例如，在上面的第一条记录中，该状态的详细信息如下：

* 数值 ID：`632`
* 数据类型：`4`（参见下方的“[数据类型](#data-types)”以了解它对应什么类型，在这里是字符串）
* 命令名称：`aircraft/0/flightplan/route`

值得注意的是，所有状态名称都采用由斜杠（`/`）分隔的一系列术语，表示该状态所处的上下文。在这个示例中，这表示：

* `aircraft`：该状态指的是飞机本身
* `flightplan`：该状态指的是当前飞行计划
* `route`：该状态指的是飞行计划中定义的航线

下面的示例说明了命令在清单中的显示方式：

```markup
    1048649,-1,commands/AutoStart\n
    1048628,-1,commands/BeaconLights\n
    1048613,-1,commands/Brakes\n
```

值得注意的是，清单中的命令与状态有几个关键区别：

1. 数值 ID 会大于 1,000,000，而状态的数值 ID 都是较小的数值
2. 数据类型会被指定为 `-1`，这并不是实际的数据类型
3. 名称都采用 `commands/...` 的格式，没有任何状态名称会以 `commands` 开头

> 需要注意的是，目前有些命令无法使用，具体来说，是那些需要传入数据的命令。举例来说，`commands/ParkingBrakes` 这个命令只是一个简单的切换：发出命令后，停机刹车会在关闭和开启之间切换。但其他命令显然不是这样。例如，`commands/FlightPlan.AddWaypoints` 需要提供一系列航点，但目前 API 中没有机制来完成这一点，因此这些命令实际上当前无法使用。预计未来 Infinite Flight 会启用这些命令。

<a id="The Structure of API Requests"></a>
<a id="the structure of api requests"></a>
<a id="the-structure-of-api-requests"></a>
<a id="The%20Structure%20of%20API%20Requests"></a>
<a id="the%20structure%20of%20api%20requests"></a>
<a id="The Structure of API Requests"></a>
<a id="the structure of api requests"></a>
<a id="the-structure-of-api-requests"></a>
<a id="The%20Structure%20of%20API%20Requests"></a>
<a id="the%20structure%20of%20api%20requests"></a>
#### API 请求的结构

对 API 的所有请求都采用统一格式，由以下字节序列组成：

* 一个 32 位整数，表示所请求的状态或命令的数值 ID。
* 一个字节的布尔值，表示请求是否包含要发送的数据：`true`（用 `1` 表示）表示状态/命令后面跟随要发送的数据，`false`（用 `0` 表示）表示后面没有数据。
* 请求中可选携带的数据，仅在通过 API 设置状态时使用。

实际上，这意味着要获取某个状态或执行清单中的某个命令，只需发送数值 ID 后再跟一个 `0`。要设置某个状态，则发送数值 ID，后跟 `1`，再后跟一些数据。

例如，参照上面的清单示例，如果要获取当前飞机纬度，可以使用 `aircraft/0/latitude`，它的数值 ID 是 `554`。这意味着发送一个 32 位整数 `554`，后跟一个字节 `0`。

这意味着需要发送以下五个字节：

```markup
    2A 02 00 00 00
```

> 这一串字节以十六进制表示，每个字节范围从 `00` 到 `FF`。

这里，前四个字节表示一个 32 位整数（使用小端序表示法，后文在“[数据类型](#data-types)”中会进一步说明）。这意味着实际的十六进制 32 位整数是 `0000022A`，而十六进制 `22A` 对应十进制的 `554`。第五个字节表示 `0` 或 `false` 标记。

当 API 返回数据时，它会按如下方式返回一系列字节：

* 一个 32 位整数，表示正在返回的状态的数值 ID。
* 一个字节的布尔值 `false`（表示为 `0`）。
* 一个或多个字节组成的数据序列，表示该状态返回的数据（具体长度和格式取决于命令的数据类型，参见下方的“[数据类型](#data-types)”）。

需要注意的是，使用 TCP socket 意味着与 API 的交互并不是顺序的发送-接收模式。例如，当我们使用 HTTP 获取某个 REST API 端点时，HTTP 事务是完整的顺序往返流程：

1. 通过 HTTP 连接到 API 端点
2. 发送请求
3. 接收响应
4. 断开连接

但使用 TCP socket 时，请求与响应是分离的。完全可能在 API 发送任何响应之前，就连续发送两个响应，因此可能需要在客户端将响应与相应请求关联起来。由于 API 会提供返回状态的数值 ID，如果需要，应用程序就可以在客户端端管理并关联请求和 API 响应。

下面在讨论如何 [获取](#retrieving-states-from-the-api) 和 [设置](#setting-states-with-the-api) 状态，以及 [运行](#running-commands-through-the-api) 命令时，会提供更具体的示例。

<a id="Obtaining the Manifest"></a>
<a id="obtaining the manifest"></a>
<a id="obtaining-the-manifest"></a>
<a id="Obtaining%20the%20Manifest"></a>
<a id="obtaining%20the%20manifest"></a>
<a id="Obtaining the Manifest"></a>
<a id="obtaining the manifest"></a>
<a id="obtaining-the-manifest"></a>
<a id="Obtaining%20the%20Manifest"></a>
<a id="obtaining%20the%20manifest"></a>
#### 获取清单

通常，在成功连接到 TCP socket 之后，第一件事就是获取清单。

这可以通过发送特殊命令 `-1`，后跟 `false`（或 `0`）来完成，表示请求中没有携带数据。`-1` 命令是 API 用于请求清单的命令。

实际上，这意味着要发送以下字节序列：

```markup
    ff ff ff ff 00
```

这里，`ff ff ff ff` 是 `-1` 的 32 位小端序十六进制表示，而第五个字节是 `0` 标记。

API 会按以下方式返回清单：

* `-1` 表示 API 正在返回清单数据，随后是
* 一个 32 位 [小端序](#little-endian) 整数，表示返回数据的总长度
* 清单数据本身按如下方式拆分：
    * 一个 32 位整数，表示字符串本身的字节长度
    * 字符串数据本身，以字节序列形式返回

例如，下面是 API 返回的清单前 50 个字节：

```markup
    ff ff ff ff 13 b7 00 00 0f b7
    00 00 35 31 35 2c 32 2c 61 69
    72 63 72 61 66 74 2f 30 2f 73
    79 73 74 65 6d 73 2f 6e 61 76
    5f 73 6f 75 72 63 65 73 2f 61
    64 66 2f 32 2f 64 69 73 74 61
```

将其拆解如下，数据结构是这样的：

* `ff ff ff ff`：这是整数 `-1` 的表示，表明这是对清单请求的响应。
* `13 b7 00 00`：这是返回总数据大小的 32 位 [小端序](#little-endian) 整数。在本例中，十六进制数 `0000b713` 表示后续返回的总数据为 46,867 字节。
* `0f b7 00 00 35 31 35 2c ...`：清单本身分为两部分：
    * `0f b7 00 00`：这是清单数据的第一部分，一个 32 位 [小端序](#little-endian) 整数，表示后续清单字符串的长度。在本例中，十六进制数 `0000b70f` 表示清单字符串长度为 46,863 字节。
    * `35 31 35 2c 32 2c 61 69 72 63 72 61 66 74 2f 30 2f 73 ...`：这是清单字符串实际字节的开始。这些字节是 ASCII 字符的十六进制表示，在这里这些字节是 `515,2,aircraft/0/s ...`，显然是清单中某个条目的开头部分。

一个重要的点是，整个清单不会作为单个大消息一次性返回。它很可能会以多个消息返回，因此需要将这些消息追加到清单数据末尾，直到接收到第三个整数所指示的完整字符串长度为止（本例中是 `0f b7 00 00`）。

具体如何完成这一步取决于所使用的语言和平台，但基本逻辑相同：持续将消息追加到清单末尾，直到接收到所指示的完整长度。

<a id="Data Types"></a>
<a id="data types"></a>
<a id="data-types"></a>
<a id="Data%20Types"></a>
<a id="data%20types"></a>
<a id="Data Types"></a>
<a id="data types"></a>
<a id="data-types"></a>
<a id="Data%20Types"></a>
<a id="data%20types"></a>
#### 数据类型

如前所述，清单中的每个状态都带有一个由 32 位整数值表示的关联数据类型。共有六种数据类型：

| 整数 | 类型 | 说明 |
|---------|------|-------------|
| 0 | 布尔值 | 单字节，`true` 用 `01` 表示，`false` 用 `00` 表示。 |
| 1 | 整数（32 位） | 32 位整数，以 4 个字节的小端序格式表示（参见下方的 [小端序](#little-endian)）。可存储范围为 -2,147,483,648 到 2,147,483,647 的数值。 |
| 2 | 浮点数 | 浮点数，以 4 个字节的小端序格式表示。可表示 6 到 7 位小数。 |
| 3 | 双精度浮点数 | 浮点数，以 8 个字节的小端序格式表示。可表示 15 位十进制数字。 |
| 4 | 字符串 | 字符串以一个 32 位整数（4 个字节）表示其字节长度，随后跟随字符串本身的字节序列。 |
| 5 | 长整数 | 64 位整数，以 8 个字节的小端序格式表示（参见下方的“[小端序](#little-endian)”）。可存储范围为 -9,223,372,036,854,775,808 到 9,223,372,036,854,775,807。 |

<a id="Little-Endian"></a>
<a id="little-endian"></a>
<a id="Little-Endian"></a>
<a id="little-endian"></a>
##### 小端序

*[字节序](https://en.wikipedia.org/wiki/Endianness)* 指的是数据以数字形式表示时的排列方式。就十六进制数而言，数字可以是 *大端序*（BE）或 *小端序*（LE）。

考虑这个表示 32 位整数 1,210,590 的十六进制数：

```markup
    001278DE
```

*大端序* 表示字节从左到右按从最高有效字节到最低有效字节排列，如下：

```markup
    00 12 78 DE
```

相比之下，*小端序* 会将顺序反转为：

```markup
    DE 78 12 00
```

Connect v2 API 以小端序格式表示数字，因此在发送请求时，将状态或命令表示为 32 位小端序整数非常重要。例如，如果被请求的状态数值 ID 是 `535`，那么它的十六进制值是 `217`，作为 32 位小端序整数表示为：

```markup
    17 02 00 00
```

同样，如果被请求的命令数值 ID 是 `1048616`，那么它的十六进制值是 `100028`，作为 32 位 *小端序* 整数表示为：

```markup
    28 00 10 00
```

所有数字类型都使用小端序，包括 *Float*、*Double* 和 *Long* 数据类型。

<a id="Retrieving States from the API"></a>
<a id="retrieving states from the api"></a>
<a id="retrieving-states-from-the-api"></a>
<a id="Retrieving%20States%20from%20the%20API"></a>
<a id="retrieving%20states%20from%20the%20api"></a>
<a id="Retrieving States from the API"></a>
<a id="retrieving states from the api"></a>
<a id="retrieving-states-from-the-api"></a>
<a id="Retrieving%20States%20from%20the%20API"></a>
<a id="retrieving%20states%20from%20the%20api"></a>
#### 从 API 获取状态

要从 API 获取某个状态，请按如下方式发送 `GetState` 请求：

* 一个 32 位整数，表示正在发送的状态数值 ID。
* 一个字节的布尔值 `false`（表示为 `0`）。

例如，假设清单中包含以下状态：

```markup
    522,4,aircraft/0/livery
```

这表示 `aircraft/0/livery` 状态的数值 ID 为 `522`，并返回 `String` 数据类型。

要获取该状态，可以发送以下内容：

```markup
    0a 02 00 00 00
```

其拆解如下：

* `0a 02 00 00`：`522` 的 32 位小端序整数表示，其十六进制值为 `20A`。
* `00`：表示 `false` 的单字节。

当 API 响应时，它会返回如下所示的响应：

```markup
    0a 02 00 00 0e 00 00 00 0a 00 00 00 41 65 72 20 4c 69 6e 67 75 73
```

其拆解如下：

* `0a 02 00 00`：状态数值 ID `522` 的 32 位 [小端序](#little-endian) 整数表示。
* `0e 00 00 00`：返回数据长度的 32 位 [小端序](#little-endian) 整数表示。在本例中，十六进制值 `0000000e` 为 `14`，表示数据长度为 14 字节。
* `0a 00 00 00 41 65 72 20 ....`：该状态返回的实际数据。由于这个状态是字符串，数据分为两部分：
    * `0a 00 00 00`：一个 32 位 [小端序](#little-endian) 整数，表示字符串长度。在本例中，`0000000a` 为 `10`，表示字符串长度为 10 字节。
    * `41 65 72 20 4c 69 6e 67 75 73`：由单字节字符组成的 10 字节字符串，表示 `Aer Lingus`，即此时飞机涂装的名称。

无论数据类型是什么，这种请求与响应结构都适用。

再看一个 32 位整数数据类型的示例：

```markup
    622,1,aircraft/0/systems/flaps/state
```

要获取该状态，请发送以下内容：

```markup
    6e 02 00 00 00
```

其拆解如下：

* `63 02 00 00`：`622` 的 32 位 [小端序](#little-endian) 整数表示，其十六进制值为 `26E`。
* `00`：表示 `false` 的单字节。

当 API 响应时，它会返回如下所示的响应：

```markup
    6e 02 00 00 04 00 00 00 00 00 00 00
```

其拆解如下：

* `6e 02 00 00`：状态数值 ID `622` 的 32 位 [小端序](#little-endian) 整数表示。
* `04 00 00 00`：返回数据长度的 32 位 [小端序](#little-endian) 整数表示。在本例中，十六进制值 `00000004` 为 `4`，表示数据长度为 4 字节，因为 32 位整数由 4 个字节表示。
* `00 00 00 00`：该状态返回的实际数据。由于这个状态是 32 位 [小端序](#little-endian) 整数，因此返回值是 `0`。

<a id="Setting States with the API"></a>
<a id="setting states with the api"></a>
<a id="setting-states-with-the-api"></a>
<a id="Setting%20States%20with%20the%20API"></a>
<a id="setting%20states%20with%20the%20api"></a>
<a id="Setting States with the API"></a>
<a id="setting states with the api"></a>
<a id="setting-states-with-the-api"></a>
<a id="Setting%20States%20with%20the%20API"></a>
<a id="setting%20states%20with%20the%20api"></a>
#### 通过 API 设置状态

可以通过 API 发送 `SetState` 请求来设置状态，也就是为其赋予新值，方法如下。

不过，并非所有状态都可以设置，清单也不会指示哪些状态可以设置、哪些不可以。判断的唯一方法是反复尝试并结合一些常识。

例如，像 `aircraft/0/livery` 这样的状态不能设置，因为它表示飞机当前实际的涂装。同样，`aircraft/0/latitude` 也不能设置，因为它反映的是某一时刻飞机的实际位置。

相比之下，像 `aircraft/0/systems/flaps/state` 这样的状态可以设置，通过将该状态设为代表目标襟翼状态的数字（不同飞机会不同）来改变襟翼位置。

为说明这一点，我们使用 API 将襟翼状态设为 `1`。为此，需要生成一个 `SetState` 请求，发送：

* 表示该状态数值 ID 的 32 位 [小端序](#little-endian) 整数
* 一个由单字节值 `1` 表示的布尔值 `true`
* 实际数据本身，在这里是数字 `1`，以 32 位 [小端序](#little-endian) 整数表示

与前面获取同一状态的示例一样，如果该状态的数值 ID 是 `622`，那么发送以下内容即可将状态设为 `1`：

```markup
    6e 02 00 00 01 01 00 00 00
```

其拆解如下：

* `6e 02 00 00`：状态数值 ID `622` 的 32 位 [小端序](#little-endian) 整数表示。
* `01`：表示 `true` 的单字节。
* `01 00 00 00`：要为该状态设置的值的 32 位 [小端序](#little-endian) 整数表示（在本例中为 `1`）。

与获取状态一样，如何表示要设置的值将遵循各个 [数据类型](#data-types) 的表示方式。

例如，下面这个状态的数据类型是 `String`：

```markup
    605,4,aircraft/0/systems/comm_radios/com_1/atc_name
```

要将该值设置为 `Bob the Pilot`，请向 API 发送以下请求：

```markup
    5d 02 00 00 01 0d 00 00 00 42 6f 62 20 74 68 65 20 50 69 6c 6f 74
```

其拆解如下：

* `5d 02 00 00`：状态数值 ID `605` 的 32 位 [小端序](#little-endian) 整数表示。
* `01`：表示 `true` 的单字节。
* `0d 00 00 00 42 6f 62 20 ...`：字符串数据分为两部分：
    * `0d 00 00 00`：一个 32 位 [小端序](#little-endian) 整数，表示字符串长度。在本例中，`0000000d` 为 `13`，表示字符串长度为 13 字节（即 `Bob the Pilot` 的字符数）。
    * `42 6f 62 20 74 68 65 20 50 69 6c 6f 74`：由单字节字符组成的 13 字节字符串，表示 `Bob the Pilot`。

在发送设置状态的请求后，API 不会返回任何响应来表明状态是否已成功设置。确认请求是否成功的唯一方法，是随后 [从 API 获取该状态](#retrieving-states-from-the-api)。

<a id="Running Commands through the API"></a>
<a id="running commands through the api"></a>
<a id="running-commands-through-the-api"></a>
<a id="Running%20Commands%20through%20the%20API"></a>
<a id="running%20commands%20through%20the%20api"></a>
<a id="Running Commands through the API"></a>
<a id="running commands through the api"></a>
<a id="running-commands-through-the-api"></a>
<a id="Running%20Commands%20through%20the%20API"></a>
<a id="running%20commands%20through%20the%20api"></a>
#### 通过 API 运行命令

要通过 API 执行命令，请按如下方式发送 `RunCommand` 请求：

* 一个 32 位 [小端序](#little-endian) 整数，表示正在执行的命令的数值 ID。
* 一个字节的布尔值 `false`（表示为 `0`）。

例如，假设清单中包含以下命令：

```markup
    1048614,-1,commands/ParkingBrakes
```

这表示 `commands/ParkingBrakes` 状态的数值 ID 为 `1048614`。

要执行此命令，请发送以下内容：

```markup
    26 00 10 00 00
```

其拆解如下：

* `26 00 10 00`：`1048614` 的 32 位 [小端序](#little-endian) 整数表示，其十六进制值为 `100026`。
* `00`：表示 `false` 的单字节。

这将执行该命令并切换停机刹车的开/关状态，用户会在 Infinite Flight 中看到这一变化。

与设置状态一样，在发送执行命令的请求后，API 不会返回任何响应来表明命令已成功执行。确认请求是否成功的唯一方法，是随后 [从 API 获取适当的状态](#retrieving-states-from-the-api)，或直接在 Infinite Flight 中进行视觉确认。

例如，在切换停机刹车状态后，如上所示，获取 `aircraft/0/systems/parking_brake/state` 状态以验证命令是否成功。

如前文在“[API 清单](#the-api-manifest)”中提到的，目前清单中返回的一些命令无法使用，因为它们需要传入数据。当前 API 没有提供执行这一点的机制，因此这些命令实际上目前无法使用。预计未来 Infinite Flight 会启用这些命令。

例如，`commands/ParkingBrakes` 这个命令只是一个简单的切换：发出命令后，停机刹车会在关闭和开启之间切换。但其他命令显然不是这样。例如，`commands/FlightPlan.AddWaypoints` 需要提供一系列航点，而目前无法做到这一点。

<a id="Working with Flight Plans from Infinite Flight v22.1"></a>
<a id="working with flight plans from infinite flight v22.1"></a>
<a id="working-with-flight-plans-from-infinite-flight-v22.1"></a>
<a id="working-with-flight-plans-from-infinite-flight-v221"></a>
<a id="Working%20with%20Flight%20Plans%20from%20Infinite%20Flight%20v22.1"></a>
<a id="working%20with%20flight%20plans%20from%20infinite%20flight%20v22.1"></a>
<a id="Working with Flight Plans from Infinite Flight v22.1"></a>
<a id="working with flight plans from infinite flight v22.1"></a>
<a id="working-with-flight-plans-from-infinite-flight-v22.1"></a>
<a id="working-with-flight-plans-from-infinite-flight-v221"></a>
<a id="Working%20with%20Flight%20Plans%20from%20Infinite%20Flight%20v22.1"></a>
<a id="working%20with%20flight%20plans%20from%20infinite%20flight%20v22.1"></a>
#### 从 Infinite Flight v22.1 处理飞行计划

随着 Infinite Flight v22.1 的发布，`aircraft/0/flightplan/full_info` 状态返回飞行计划数据的方式发生了变化。此前数据是以简单字符串返回的，而从 v22.1 开始，Connect v2 API 返回的是 JSON 格式字符串，这与 Infinite Flight v22.1 中 Connect v1 API 返回的 JSON 格式一致。

该字符串的格式如下：

```json
{
  "Result": 0,
  "Type": "Fds.IFAPI.APIFlightPlan",
  "Bearing": 1.988517,
  "DesiredTrack": 1.59089124,
  "DetailedInfo": {
    "AlternateDestinations": null,
    "Altitude": 0,
    "Altitudes": null,
    "DepartureAirportCode": "LEMD",
    "DepartureTime": "/Date(-62135596800000+0000)/",
    "DestinationAirportCode": "IMR",
    "EntityID": "00000000-0000-0000-0000-000000000000",
    "EstimatedTimeEnroute": "PT0S",
    "FlightID": "00000000-0000-0000-0000-000000000000",
    "FlightPlanItems": [
      {
        "Altitude": -1,
        "Children": null,
        "Identifier": "LEMD",
        "Length": 0,
        "Location": {
          "Altitude": 608.9904,
          "Latitude": 40.495345592498779,
          "Longitude": -3.5602057874202728
        },
        "Name": "Adolfo Suárez Madrid-Barajas",
        "StartIndex": 0,
        "Type": 0
      },
      {
        "Altitude": -1,
        "Children": null,
        "Identifier": null,
        "Length": 0,
        "Location": {
          "Altitude": 0,
          "Latitude": 40.71944583,
          "Longitude": -3.5575025
        },
        "Name": "D001O",
        "StartIndex": 0,
        "Type": 0
      },
      {
        "Altitude": -1,
        "Children": null,
        "Identifier": "IMR",
        "Length": 0,
        "Location": {
          "Altitude": 0,
          "Latitude": 40.519747222222222,
          "Longitude": -3.5736333333333334
        },
        "Name": "MADRID BARAJAS",
        "StartIndex": 0,
        "Type": 0
      }
    ],
    "FlightPlanType": 0,
    "FuelOnBoard": "PT0S",
    "LastUpdate": "/Date(1645012763298)/",
    "Remarks": null,
    "Speed": 0,
    "Waypoints": ["LEMD", "D001O", "IMR"]
  },
  "DistanceToDestination": 26.87741,
  "DistanceToNext": 14.8649006,
  "ETAToDestination": 1.32894981e17,
  "ETAToNext": 1.32894938e17,
  "ETEToDestination": 171.8713,
  "ETEToNext": 95.05565,
  "ICAO": null,
  "NextWaypointLatitude": 40.7194443,
  "NextWaypointLongitude": -3.55750251,
  "TotalDistance": 25.4681568,
  "Track": 323.766663,
  "WaypointName": "D001O"
}
```

> 感谢 [@carmichaelalonso](https://github.com/carmichaelalonso) 在 GitHub 上发布了这个 JSON 示例 [这里](https://gist.github.com/carmichaelalonso/6f2b82bae992e81b24b93df6842c3cee)。

如果你的应用依赖 `aircraft/0/flightplan/full_info` 状态，你应该使用 `infiniteflight/app_version` 状态检查 Infinite Flight 版本，并据此相应地处理 `aircraft/0/flightplan/full_info` 的数据。