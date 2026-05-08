---
id: atis-pushback-and-taxi
title: ATIS、Pushback 和 Taxi
meta: 了解如何在 Infinite Flight 中与 ATC 交流 Pushback 和 Taxi 指令。
order: 2
contributor: babacar,lucaviness,planegeek,John370,KaiM
---

<a id="ATIS, Pushback and Taxi"></a>
<a id="atis, pushback and taxi"></a>
<a id="atis,-pushback-and-taxi"></a>
<a id="atis-pushback-and-taxi"></a>
<a id="ATIS%2C%20Pushback%20and%20Taxi"></a>
<a id="atis%2C%20pushback%20and%20taxi"></a>
<a id="atis%2C-pushback-and-taxi"></a>
<a id="ATIS, Pushback and Taxi"></a>
<a id="atis, pushback and taxi"></a>
<a id="atis,-pushback-and-taxi"></a>
<a id="atis-pushback-and-taxi"></a>
<a id="ATIS%2C%20Pushback%20and%20Taxi"></a>
<a id="atis%2C%20pushback%20and%20taxi"></a>
<a id="atis%2C-pushback-and-taxi"></a>
# ATIS、Pushback 和 Taxi



<a id="ATIS Communication Summary"></a>
<a id="atis communication summary"></a>
<a id="atis-communication-summary"></a>
<a id="ATIS%20Communication%20Summary"></a>
<a id="atis%20communication%20summary"></a>
<a id="ATIS Communication Summary"></a>
<a id="atis communication summary"></a>
<a id="atis-communication-summary"></a>
<a id="ATIS%20Communication%20Summary"></a>
<a id="atis%20communication%20summary"></a>
## ATIS 通信摘要

一旦生成，若当前由管制员值守，飞行员将自动调至 ATIS 频率。当前 ATIS 将继续播报，直到飞行员切离该频率。



![调至 ATIS](../../../_images/manual/frames/tuned-to-atis.png)



1. 当 ATIS 播报时，它会显示在屏幕顶部。

    

2. 会出现一条屏幕通知，告知你已自动调至一个处于活动状态的频率。你可以轻点将其关闭。

    

3. 可点击通信按钮（耳机图标）来更改频率、发送/回复 ATC 消息，以及查看消息日志。

    


![ATIS 通信框](../../../_images/manual/frames/atis-communication-box.png)



1. 通信框左上角显示相应管制员所播发的机场、高度以及管制员频率。第二行显示该管制员所属席位及其显示名称，第三行显示机场的 METAR。

    

2. 返回按钮可用于选择其他频率或切离当前频率。

    

3. ATC 先前发布的最后一次高度、航向、速度和跑道分配会作为提醒显示出来（在发布指令前这里会为空白）。

   

4. 消息日志显示全部通信历史，双击可仅显示你与 ATC 的通信。




提示

: 在收听 ATIS 时，请根据当前位置以及起飞时正在使用的跑道，提前规划你最可能会被指派到的滑行路线。提前规划滑行路线有助于减轻操作负担，并降低地面移动出错的可能性！



<a id="ATIS Definitions"></a>
<a id="atis definitions"></a>
<a id="atis-definitions"></a>
<a id="ATIS%20Definitions"></a>
<a id="atis%20definitions"></a>
<a id="ATIS Definitions"></a>
<a id="atis definitions"></a>
<a id="atis-definitions"></a>
<a id="ATIS%20Definitions"></a>
<a id="atis%20definitions"></a>
## ATIS 定义

下面有两张表，说明 ATIS 广播中可能出现的所有 REMARKS 和 NOTAMS 的含义：



+++ REMARKS

| REMARKS                           | ATC 意图                                                | 飞行员操作                                                |
| :-------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| No Intersection Departures        | ATC 要求飞行员使用跑道全长。     | 飞行员应在跑道尽头等待。        |
| No Pattern Work                   | ATC 不接受航线盘旋飞行。                           | 飞行员不应尝试在机场进行航线盘旋飞行，这不包括进场执行 touch & go 但随后离开空域的飞行。 |
| Gate Hold                         | ATC 需要冻结所有出港地面移动。            | 飞行员应在机位等待，直到该限制解除，不要重复发送 pushback 请求。 |
| No Light Aircraft                 | 轻型飞机（XCub、C172、P38、SR22 和 Spitfire）不允许进入该空域或停靠该机场。 | 如果飞行员驾驶的是轻型飞机，必须改降或在其他机场重新生成。 |
| Rolling Departures                | ATC 希望加快起飞流程。                       | 获准起飞后，飞行员应立即进入跑道并开始起飞滑跑。 |
| Flight Plan Required              | ATC 希望飞行员在 pushback/taxi 前先提交飞行计划。 | 飞行员必须在请求 pushback 前提交飞行计划。 |
| Straight Out Departures           | ATC 希望航空器在达到起飞许可中给定的高度且确保无交通冲突之前保持跑道航向。 | 飞行员应一直保持直飞，直到达到指定高度且避开所有交通后，才可进行任何方向改变。 |
| Multiple Frequencies in Use       | 管制员正使用多个频率来管理交通。 | 飞行员应查看 ATIS 以确认应从当前位置联系的频率，并随时准备切换频率。 |
| Check Forum for Event Information | ATC 正将飞行员引导至 IFC 页面上的特别说明（例如 FNF、VARB Summit） | 飞行员在飞行前应查看论坛。              |
| SID/STAR Use Recommended          | SID/STAR 的使用对交通管理并非必需，但建议使用。 | 飞行员应在飞行计划中添加 SID/STAR。       |
| SID/STAR Use Required             | SID/STAR 的使用对交通管理或活动至关重要。  | 飞行员必须在飞行计划中添加 ATC 首选的 SID/STAR。 |

+++



+++ NOTAMS

| NOTAMS                     | ATC 意图                                     | 飞行员操作                                                |
| :------------------------- | :------------------------------------------------ | :----------------------------------------------------------- |
| Event in Progress          | 正在进行活动。                          | 飞行员可能会遇到延误，或者根据活动规则，可能不允许参与。 |
| Size Restrictions in Place | 该机场无法接纳某些尺寸的航空器。 | 飞行员应考虑自己航空器的尺寸是否适合该机场。 |
| Low Visibility             | 已报告低能见度。                 | 飞行员应预期低能见度。                      |

+++



<a id="Pushback Communication Summary"></a>
<a id="pushback communication summary"></a>
<a id="pushback-communication-summary"></a>
<a id="Pushback%20Communication%20Summary"></a>
<a id="pushback%20communication%20summary"></a>
<a id="Pushback Communication Summary"></a>
<a id="pushback communication summary"></a>
<a id="pushback-communication-summary"></a>
<a id="Pushback%20Communication%20Summary"></a>
<a id="pushback%20communication%20summary"></a>
## Pushback 通信摘要

步骤 1

: 选择当前可用的 Ground 频率



![当前 Ground 频率](../../../_images/manual/frames/active-ground-frequency.png)



步骤 2

: 点击 "Request Pushback"



![请求 Pushback](../../../_images/manual/frames/request-pushback.png)



提示

: 如果你所在的机位不需要 pushback，或者所驾驶的航空器不支持 pushback，那么准备好后请直接请求 taxi！



步骤 3

: 点击 "Send" 或 "Request Specific Runway"（如果你确实要请求特定跑道，可供选择的跑道会显示出来，点击所需跑道即可发送请求）



![发送 Pushback 请求](../../../_images/manual/frames/send-pushback-request.png)



提示

: 如果你要请求特定跑道，请先确认它正在 ATIS 中被使用！



步骤 4

: 当你收到 pushback 放行（或来自管制员的其他通信）时，通信按钮会闪烁琥珀色，消息会显示在屏幕顶部，点击通信按钮即可对该消息 "Reply"



![回复 Pushback 放行](../../../_images/manual/frames/reply-to-pushback-clearance.png)



提示

: 当你收到 pushback 放行时，可能会被告知预计使用某条特定跑道 - 请确保以能让你顺利滑行到相应跑道的方向完成 pushback！



<a id="Taxi Communication Summary"></a>
<a id="taxi communication summary"></a>
<a id="taxi-communication-summary"></a>
<a id="Taxi%20Communication%20Summary"></a>
<a id="taxi%20communication%20summary"></a>
<a id="Taxi Communication Summary"></a>
<a id="taxi communication summary"></a>
<a id="taxi-communication-summary"></a>
<a id="Taxi%20Communication%20Summary"></a>
<a id="taxi%20communication%20summary"></a>
## Taxi 通信摘要

步骤 1

: 点击 "Request Taxi"



![请求 Taxi](../../../_images/manual/frames/request-taxi.png)



步骤 2

: 点击 "Active Runway" 发送消息，或点击 "Request Specific Runway"（如果你确实要请求特定跑道，可供选择的跑道会显示出来，点击所需跑道即可发送请求）



![发送 Taxi 请求](../../../_images/manual/frames/send-taxi-request.png)



提示

: 如果你要请求特定跑道，请先确认它正在 ATIS 中被用于起飞！



步骤 3

: 当你收到 taxi 放行（或来自管制员的其他通信）时，通信按钮会闪烁琥珀色，消息会显示在屏幕顶部，点击通信按钮即可对该消息 "Reply"



![回复 Taxi 放行](../../../_images/manual/frames/reply-to-taxi-clearance.png)



<a id="Pushback and Taxi Communication Tables"></a>
<a id="pushback and taxi communication tables"></a>
<a id="pushback-and-taxi-communication-tables"></a>
<a id="Pushback%20and%20Taxi%20Communication%20Tables"></a>
<a id="pushback%20and%20taxi%20communication%20tables"></a>
<a id="Pushback and Taxi Communication Tables"></a>
<a id="pushback and taxi communication tables"></a>
<a id="pushback-and-taxi-communication-tables"></a>
<a id="Pushback%20and%20Taxi%20Communication%20Tables"></a>
<a id="pushback%20and%20taxi%20communication%20tables"></a>
## Pushback 和 Taxi 通信表

下面列出了地面管制员可以向飞行员发出的所有 ATC 指令，以及飞行员可以请求或回复的内容：



+++ 飞行员对地面管制员

| 请求/消息                   | 何时发送                                                 | 何时不发送                                             |
| --------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 请求前往活动跑道的 Taxi  | 当飞行员没有跑道偏好时发送。       | 飞行员在正进行 pushback 时不应发送此请求。 |
| 请求前往特定跑道的 Taxi | 当飞行员有跑道偏好时发送。                 | 飞行员不应请求当前 ATIS 判定为未使用的跑道。 |
| 请求 Pushback                  | 当飞行员希望进行 pushback 时，应请求 pushback 放行。 | 如果用户驾驶的航空器不具备 pushback 能力（C172、C208、TBM-930、SR22、XCub、F18、F22、F16、F14、A-10、Spitfire 或 P-38），或所处机位不需要 pushback，则不应请求此项。 |
| 请求穿越跑道           | 如果飞行员的滑行路线需要穿越跑道，必须请求穿越许可。所请求的跑道应与当前使用跑道相同。 | 其他任何情况下都不应请求。                                   |
| 请求频率切换          | 如果飞行员希望切换频率且尚未获得切换许可，应请求频率切换。 | 飞行员在正滑行前往跑道时，不应向 Ground 请求频率切换。频率切换已包含在滑行指令中（“ready 时联系 Tower”）。 |

+++



+++ 地面管制员对飞行员 

| 指令/消息                      | ATC 意图                                                | 飞行员操作                                                |
| ---------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Taxi to Runway, Contact Tower when Ready | ATC 已允许飞行员滑行至跑道 XX。              | 飞行员应开始滑行至分配的跑道。       |
| Pushback Approved                        | ATC 已给予飞行员 pushback 放行。               | 飞行员应 pushback 到滑行道上。                  |
| Hold Position                            | ATC 希望飞行员立即停止航空器。      | 如果在机位，飞行员应等待直到获得 pushback 放行。如果飞行员正在滑行，应将航空器完全停下，并等待 “Continue Taxi” 指令。 |
| Continue Taxi                            | ATC 已解除 “Hold Position” 指令。            | 飞行员可以继续滑行。                              |
| Hold Short of Runway                     | ATC 希望飞行员在跑道前等待。             | 飞行员应将整架航空器停在等待线后方。 |
| Cross Runway                             | ATC 已允许飞行员穿越跑道。               | 飞行员应穿越跑道。如果包含 “Please Expedite”，飞行员应加速完成穿越。 |
| Give Way to Aircraft                     | ATC 希望飞行员让行给另一架航空器。         | 飞行员应让行给相应航空器。           |
| Expect Progressive Taxi Instructions     | ATC 将使用渐进式滑行指令。                  | 在收到进一步指令前，飞行员应按常规继续。 |
| Turn Left/Right Next Taxiway             | ATC 希望飞行员在下一个滑行道左转/右转（分别对应）。 | 飞行员应在下一个滑行道左转/右转（分别对应），并继续滑行，直到收到进一步指令。 |
| Continue Straight Ahead                  | ATC 希望飞行员在当前滑行道上继续直行。 | 飞行员应保持在该滑行道上，直到收到进一步指令。 |
| Make a 180                               | ATC 希望飞行员完成 180º 转弯。                     | 飞行员应掉头并等待进一步指令。 |
| Follow Aircraft Ahead                    | ATC 希望飞行员跟随前方航空器。            | 飞行员应跟随前方航空器，直到收到进一步指令。 |
| Continue Taxi at your Discretion         | ATC 希望告知飞行员，他们不再受渐进式滑行指令约束。 | 飞行员可以自行决定继续滑行。如果给出了其他滑行指令，则应遵循那些指令。 |

+++