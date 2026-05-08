---
id: en-route
title: 航路中
meta: 了解如何在 Infinite Flight 中与 ATC 进行航路通信。
order: 5
contributor: babacar,lucaviness,planegeek,finn-14,Filipe_Samuel_Braine
---

<a id="En-Route"></a>
<a id="en-route"></a>
<a id="En-Route"></a>
<a id="en-route"></a>
# 航路中



<a id="En-Route Communication Summary"></a>
<a id="en-route communication summary"></a>
<a id="en-route-communication-summary"></a>
<a id="En-Route%20Communication%20Summary"></a>
<a id="en-route%20communication%20summary"></a>
<a id="En-Route Communication Summary"></a>
<a id="en-route communication summary"></a>
<a id="en-route-communication-summary"></a>
<a id="En-Route%20Communication%20Summary"></a>
<a id="en-route%20communication%20summary"></a>
## 航路通信摘要



步骤 1

: 如果你收到了“Frequency change approved, good day”，则说明你所在区域当前没有 Controller 在活动 - 我们建议直接点击“Tune out of [airport ICAO code] [facility]”离开当前频率，然后继续航路飞行。如果你被移交到一个活跃频率，你会看到两个选项，要么是“Send & Switch”（会回复并自动将你调至下一个频率），要么是“Send”（会回复，但之后你需要手动调至下一个频率）



![Send and Switch](../../../_images/manual/frames/send-and-switch.png)



步骤 2

: 一旦你调到 Radar Controller 的频率，下表概述了可以发送哪些请求： 



| 出发类型            | Check In [IFR] | Flight Following [VFR] |
| ------------------- | -------------- | ---------------------- |
| 有飞行计划          | 是             | 是                     |
| 无飞行计划          | 否             | 是                     |



![Initial Contact](../../../_images/manual/frames/initial-contact.png)



提示

: 确保一次只发出一个请求，多个传输会增加 Controller 的工作量，并且可能导致[违规](../../getting-started-guide/pilot-user-interface/violation-reasons.md#spamming-frequency---unnecessary-duplicate-requests)！



步骤 3

: 确保持续监控你所飞行的空域。如果你注意到自己即将进入一个活跃区域，或者收到了“On-Guard”消息，请调至相应频率。以下是不同设施的横向和纵向边界摘要：



| 设施               | 垂直管辖范围          | 横向边界                                           |
| ------------------ | --------------------- | -------------------------------------------------- |
| Tower             | SFC - 5000ft AAL      | 围绕机场的最近一圈/边界                              |
| Departure/Approach | SFC - 18,000ft/FL180  | 50nm                                              |
| Center             | SFC - 60,000ft/FL600  | 白色边界                                           |



注意：在特殊活动期间，空域参数和 ATC 管辖范围可能会因 NOTAM 和/或 TFR 而调整

![Image 5.1.1.1 - Airspace layout](../../../_images/manual/graphics/atc-airspace-layout.jpg)



<a id="En-Route Communication Table"></a>
<a id="en-route communication table"></a>
<a id="en-route-communication-table"></a>
<a id="En-Route%20Communication%20Table"></a>
<a id="en-route%20communication%20table"></a>
<a id="En-Route Communication Table"></a>
<a id="en-route communication table"></a>
<a id="en-route-communication-table"></a>
<a id="En-Route%20Communication%20Table"></a>
<a id="en-route%20communication%20table"></a>
## 航路通信表

下面列出了 Radar Controller 可以发送给飞行员的所有 ATC 指令，以及飞行员可以请求或回复的内容：



+++ 飞行员对 Radar Controller

| 请求/消息                  | 何时发送                                                      | 何时不要发送                                                 |
| ------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Request Approach         | 如果飞行员希望获得 ILS、GPS 或目视进近，就应请求进近。         | 其他任何情况。                                                |
| Request Flight Following | 如果飞行员希望在不接受进近的情况下飞入目的地，可以请求此项服务。如果获批，他们可以继续按照自己的飞行计划飞行，并自主决定高度。 | 在 Check In 之后不应再请求此项服务。                           |
| Request Radar Vectors    | 如果飞行员不想要 ILS、GPS 或目视进近，且尚未请求其他服务，可以请求雷达引导。ATC 会将其引导至 VFR 航线的相应航段，并在航线高度移交给 Tower/Unicom。 | 其他任何情况。                                                |
| Request Altitude Change   | 如果飞行员距离地形不到 1,000ft，或与另一架航空器在 3NM/1,000ft 范围内，则应请求此项。ATC 会检查周围环境，并在必要时采取行动。如果飞行员希望爬升超过初始巡航高度，也可以请求此项。 | 飞行员不应在起飞后立即请求此项。Check In 会让飞行员自行决定高度。 |
| Executing Missed Approach | 如果飞行员无法继续进近，可以通报复飞。如果正在复飞，这应在接触 Radar Controller 时发送。 | 其他任何情况。                                                |
| Check In                 | Check In 主要用于 Center 和 Departure。获批后，飞行员可以按照 FPL 中申报的横向和纵向航迹自行飞行。 | 飞行员不应向 approach 做 Check In。相反，他们只需请求进近即可。   |
| Request Descent via STAR | 如果飞行员距离 TOD 还有 1 分钟，并且已编入 STAR，就应请求此项。 | 如果 Radar 要求飞行员陈述其进近请求，则飞行员不应请求下降。       |
| Request Frequency Change  | 如果飞行员希望更换频率且尚未获得许可，应请求此项。            | 飞行员不应急躁地反复请求。频率切换并不总是会立即获准。            |
| Airport In Sight         | 如果飞行员在目视进近中已看见机场，可报告机场在视野中。        | 其他任何情况。                                                |

+++



+++ Radar Controller 对飞行员


| 指令/消息                                     | ATC 意图                                                      | 飞行员行动                                                     |
| -------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Continue As Filed                            | ATC 希望飞行员按其自行决定继续飞行。                           | 飞行员应按申报内容继续飞行；所有高度变化和方向变化都无需许可。         |
| Resume Own Navigation                        | ATC 希望飞行员自行导航。                                      | 飞行员应继续按其自行决定导航；所有方向变化都无需许可，所有高度变化都需要许可。 |
| Speed at Your Discretion                     | ATC 希望飞行员自行管理速度。                                  | 飞行员可在遵守速度限制的前提下，以任何安全速度飞行。                  |
| Maintain Present Speed                        | ATC 希望飞行员保持当前速度，直到另行通知。                    | 飞行员应检查自己的速度，并保持该速度，直到另行通知。                 |
| Maintain Slowest Practical Speed              | ATC 希望飞行员尽可能慢地安全飞行。                            | 飞行员应尽量降低速度。                                            |
| Maintain Best Forward Speed                   | ATC 希望飞行员尽可能快地安全飞行。                            | 飞行员应尽量提高速度。                                            |
| Adjust Speed to Follow Aircraft ahead.        | ATC 希望飞行员减速，以保持与前方航空器的间隔。                | 飞行员应调整速度，使其飞行速度不高于前方航空器。                     |
| Please Expedite Altitude Change               | ATC 希望飞行员加快高度变化。                                  | 飞行员应增加垂直速度，以尽快下降或爬升。                              |
| Amend Flight Plan to Include ATC Preferred STAR. | ATC 需要调节交通流量。                                       | 飞行员应在飞行计划中加入 ATC 首选 STAR。                           |

+++