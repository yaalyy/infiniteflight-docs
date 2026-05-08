---
id: air-traffic-control
title: 空中交通管制
meta: 了解如何在 Infinite Flight 上开始一个空中交通管制会话。
order: 2
---

<a id="Air Traffic Control"></a>
<a id="air traffic control"></a>
<a id="air-traffic-control"></a>
<a id="Air%20Traffic%20Control"></a>
<a id="air%20traffic%20control"></a>
<a id="Air Traffic Control"></a>
<a id="air traffic control"></a>
<a id="air-traffic-control"></a>
<a id="Air%20Traffic%20Control"></a>
<a id="air%20traffic%20control"></a>
# 空中交通管制



![ATC 页面](../../../_images/manual/frames/air-traffic-control-page-233.png)



1. 搜索功能可让您轻松找到想要的机场。如果您知道 ICAO 四字代码（例如圣弗朗西斯科国际机场的 KSFO），则可以输入其中的部分或全部内容，随后会显示一个选项列表。或者，直接输入城市/机场名称的部分或全部内容。

2. 您也可以使用地图来查找所选机场。只需用手指在地球仪上移动，使用捏合手势放大和缩小，然后点按您想要的机场。

3. 已添加建筑物的机场会标有“3D”符号

4. 红色圆锥表示该跑道有 ILS 进近，白色圆锥表示可用的其他进近类型

5. 设备右侧会显示一张卡片，包含与所选机场相关的所有信息，包括：

   - 入境交通数量

   - 您计划管制的预计时长

   - 频率

   - 天气

6. 您可以在此点按以选择要管制的服务器（Training 或 Expert）



<a id="Frequency Selection"></a>
<a id="frequency selection"></a>
<a id="frequency-selection"></a>
<a id="Frequency%20Selection"></a>
<a id="frequency%20selection"></a>
<a id="Frequency Selection"></a>
<a id="frequency selection"></a>
<a id="frequency-selection"></a>
<a id="Frequency%20Selection"></a>
<a id="frequency%20selection"></a>
## 频率选择

选择机场后，您可以使用卡片来选择要管制的频率。



![频率选择](../../../_images/manual/frames/frequency-selection-233.png)



1. 点按某个频率即可选中。已选中的频率会在其周围显示琥珀色圆环

    

2. 以绿色高亮的频率表示已被另一位管制员使用

    

3. 如果机场有其他管制员在岗，当前可用的服务会以绿色高亮显示，若已发布 ATIS 也会一并显示

    

4. 您可以在此选择计划管制的时长（您可以随时退出，但应尽量至少管制到所选时长）

    

5. 地图上的机场符号中心会有一个彩色圆点，用来表示当前天气状况：

   | 指示                                        | 含义                         |
   | ------------------------------------------- | ---------------------------- |
   | ![](../../../_images/manual/tables/weather-vfr.png)  | 目视飞行规则                 |
   | ![](../../../_images/manual/tables/weather-mvfr.png) | 边际目视飞行规则             |
   | ![](../../../_images/manual/tables/weather-ifr.png)  | 仪表飞行规则                 |

   

7. 跑道颜色代码可帮助您了解风向，并辅助判断应使用哪些跑道：

   | 指示                                          | 含义                                                         |
   | --------------------------------------------- | ------------------------------------------------------------ |
   | ![](../../../_images/manual/tables/weather-green.png)  | 顺风超过 3kts（或风速低于 3kts 时任意方向来风）- 建议使用该跑道 |
   | ![](../../../_images/manual/tables/weather-orange.png) | 横风超过 3kts                                              |
   | ![](../../../_images/manual/tables/weather-red.png)    | 逆风超过 3kts - 不建议使用该跑道                           |

   

8. 准备开始管制了吗？点按 [Control 按钮](../atc-user-interface/ground-tower-radar.md) 即可开始

   


<a id="Servers"></a>
<a id="servers"></a>
<a id="Servers"></a>
<a id="servers"></a>
## 服务器

当选择 Multi Player 时，会显示可用的各个实时服务器。每个服务器都有自己的一套规则和最低等级要求，在尝试加入之前请务必查看这些要求！



| 服务器   | 描述                                                  | 最低 [等级](user-profile.md#the-grade-table) |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Training | 此服务器用于练习飞行员和 ATC 技能。所有 ATC 设施（ATIS 除外）都可使用，且程序将通过 [违规](../pilot-user-interface/violations.md#violations) 进行强制执行 | 2                                                            |
| Expert*  | 此服务器要求遵守已发布的规则。所有程序都由 ATC 严格执行。违规可能会导致发放 [违规](../pilot-user-interface/violations.md#violations) | 3**                                                          |

**要在 Expert 服务器上执管，您必须接受正式培训 - 更多信息可在 [Infinite Flight Community Forum](https://community.infiniteflight.com/t/infinite-flight-atc-recruiting/564656) 上找到*

***除最低等级要求外，1 级违规总数必须至少比总着陆次数少 50%，并且飞行员在最近 365 天内不得有 [5 次或以上 2 级或 3 级违规](../pilot-user-interface/violations.md#what-happens-if-i-get-a-violation%3F)*