---
id: ndb-(non-directional-beacon)-navigation
title: NDB（无方向信标）导航
meta: 了解如何在 Infinite Flight 中使用 NDB 导航。
type: Advanced
order: 11
---

<a id="NDB (Non-Directional Beacon) Navigation"></a>
<a id="ndb (non-directional beacon) navigation"></a>
<a id="ndb-(non-directional-beacon)-navigation"></a>
<a id="ndb-non-directional-beacon-navigation"></a>
<a id="NDB%20%28Non-Directional%20Beacon%29%20Navigation"></a>
<a id="ndb%20%28non-directional%20beacon%29%20navigation"></a>
<a id="ndb-%28non-directional-beacon%29-navigation"></a>
<a id="NDB (Non-Directional Beacon) Navigation"></a>
<a id="ndb (non-directional beacon) navigation"></a>
<a id="ndb-(non-directional-beacon)-navigation"></a>
<a id="ndb-non-directional-beacon-navigation"></a>
<a id="NDB%20%28Non-Directional%20Beacon%29%20Navigation"></a>
<a id="ndb%20%28non-directional%20beacon%29%20navigation"></a>
<a id="ndb-%28non-directional-beacon%29-navigation"></a>
# NDB（无方向信标）导航



提示

: 使用 NDB 导航的原理与使用 VOR 非常相似，请务必查看我们的 [VOR Navigation](vor-(vhf-omni-directional-range)-navigation.md) 教程以获得更多帮助！



<a id="What is an NDB?"></a>
<a id="what is an ndb?"></a>
<a id="what-is-an-ndb?"></a>
<a id="what-is-an-ndb"></a>
<a id="What%20is%20an%20NDB%3F"></a>
<a id="what%20is%20an%20ndb%3F"></a>
<a id="what-is-an-ndb%3F"></a>
<a id="What is an NDB?"></a>
<a id="what is an ndb?"></a>
<a id="what-is-an-ndb?"></a>
<a id="what-is-an-ndb"></a>
<a id="What%20is%20an%20NDB%3F"></a>
<a id="what%20is%20an%20ndb%3F"></a>
<a id="what-is-an-ndb%3F"></a>
## 什么是 NDB？

Non-Directional Beacon，又称 NDB，是一种地面发射台，会发射无线电信号，并通过其专属频率和代码（通常是两个或三个字母）进行识别。配备 Automatic Direction Finder（ADF）的飞机可以解读这些信号，并将其用于导航。要使用 NDB 进行导航，你需要先 [调到正确频率](../../getting-started-guide/pilot-user-interface/navigation.md#tuning-to-a-vor-or-adf)，然后在 [座舱内显示它](../../getting-started-guide/pilot-user-interface/navigation.md#displaying-an-adf-in-your-aircraft)。



<a id="What is the Horizontal Situation Indicator (HSI)?"></a>
<a id="what is the horizontal situation indicator (hsi)?"></a>
<a id="what-is-the-horizontal-situation-indicator-(hsi)?"></a>
<a id="what-is-the-horizontal-situation-indicator-hsi"></a>
<a id="What%20is%20the%20Horizontal%20Situation%20Indicator%20%28HSI%29%3F"></a>
<a id="what%20is%20the%20horizontal%20situation%20indicator%20%28hsi%29%3F"></a>
<a id="what-is-the-horizontal-situation-indicator-%28hsi%29%3F"></a>
<a id="What is the Horizontal Situation Indicator (HSI)?"></a>
<a id="what is the horizontal situation indicator (hsi)?"></a>
<a id="what-is-the-horizontal-situation-indicator-(hsi)?"></a>
<a id="what-is-the-horizontal-situation-indicator-hsi"></a>
<a id="What%20is%20the%20Horizontal%20Situation%20Indicator%20%28HSI%29%3F"></a>
<a id="what%20is%20the%20horizontal%20situation%20indicator%20%28hsi%29%3F"></a>
<a id="what-is-the-horizontal-situation-indicator-%28hsi%29%3F"></a>
## 什么是水平位置指示器（HSI）？

水平位置指示器，简称 HSI，是 Infinite Flight 中用于导航的主要仪表。它由以下元素组成：



- 与当前飞机航向对齐的罗盘玫瑰
- 显示 [Autopilot FCU](../../getting-started-guide/pilot-user-interface/autopilot.md#autopilot) 设定航向的蓝色航向选择指示器
- 单个蓝色指针，表示 BRG（方位）1 - 当调到导航源（ILS、VOR 或 NDB）时，它会指向该导航设施
- 双蓝色指针，表示 BRG（方位）2 - 当调到导航源（ILS、VOR 或 NDB）时，它会指向该导航设施
- 航道偏差指示器（CDI），由航道指针和横向偏差条组成 - GPS 显示为品红色，NAV 1 和 NAV 2 显示为浅绿色

![HSI Elements](../../../_images/manual/graphics/hsi-elements.jpg)



<a id="How to Set Up your Horizontal Situation Indicator (HSI)"></a>
<a id="how to set up your horizontal situation indicator (hsi)"></a>
<a id="how-to-set-up-your-horizontal-situation-indicator-(hsi)"></a>
<a id="how-to-set-up-your-horizontal-situation-indicator-hsi"></a>
<a id="How%20to%20Set%20Up%20your%20Horizontal%20Situation%20Indicator%20%28HSI%29"></a>
<a id="how%20to%20set%20up%20your%20horizontal%20situation%20indicator%20%28hsi%29"></a>
<a id="how-to-set-up-your-horizontal-situation-indicator-%28hsi%29"></a>
<a id="How to Set Up your Horizontal Situation Indicator (HSI)"></a>
<a id="how to set up your horizontal situation indicator (hsi)"></a>
<a id="how-to-set-up-your-horizontal-situation-indicator-(hsi)"></a>
<a id="how-to-set-up-your-horizontal-situation-indicator-hsi"></a>
<a id="How%20to%20Set%20Up%20your%20Horizontal%20Situation%20Indicator%20%28HSI%29"></a>
<a id="how%20to%20set%20up%20your%20horizontal%20situation%20indicator%20%28hsi%29"></a>
<a id="how-to-set-up-your-horizontal-situation-indicator-%28hsi%29"></a>
## 如何设置你的水平位置指示器（HSI）

步骤 1

: 通过点击 [地图](../../getting-started-guide/pilot-user-interface/flight-planning.md#map) 或 [小地图](../../getting-started-guide/pilot-user-interface/flight-planning.md#mini-map) 上的 NDB，选择列表中显示的 NDB，然后点击 "Set ADF 1" 来 [调谐 NDB](../../getting-started-guide/pilot-user-interface/navigation.md#tuning-to-a-vor-or-adf)



步骤 2

: 通过在飞行界面点击 "NAV" 显示航空电子页面，来 [显示 NDB](../../getting-started-guide/pilot-user-interface/navigation.md#displaying-an-adf-in-your-aircraft)，并确保 BRG 1（或 2）已显示 ADF



<a id="How to Navigate using an NDB"></a>
<a id="how to navigate using an ndb"></a>
<a id="how-to-navigate-using-an-ndb"></a>
<a id="How%20to%20Navigate%20using%20an%20NDB"></a>
<a id="how%20to%20navigate%20using%20an%20ndb"></a>
<a id="How to Navigate using an NDB"></a>
<a id="how to navigate using an ndb"></a>
<a id="how-to-navigate-using-an-ndb"></a>
<a id="How%20to%20Navigate%20using%20an%20NDB"></a>
<a id="how%20to%20navigate%20using%20an%20ndb"></a>
## 如何使用 NDB 导航



步骤 1

: 通过确定飞行方向以及可用于辅助航线的导航设施（例如 NDB），来准备你的飞行计划



步骤 2

: 使用我们的分步指南提前做好规划，以帮助你 [调谐](../../getting-started-guide/pilot-user-interface/navigation.md#tuning-to-a-vor-or-adf) 并 [显示](../../getting-started-guide/pilot-user-interface/navigation.md#displaying-an-adf-in-your-aircraft) 所需的 NDB



提示

: 你只能为 NAV 1（或 2）和 GPS 显示 CDI，ADF 不支持 CDI



步骤 3

: 接下来，查看你相对于 NDB 所处的位置，并使用 HSI 上的蓝色方位指针来辅助判断。你也可以使用 [地图](../../getting-started-guide/pilot-user-interface/flight-planning.md#map) 和 [小地图](../../getting-started-guide/pilot-user-interface/flight-planning.md#mini-map)



步骤 4

: 规划你将如何切入该径向线，以及在接近时你预期会看到什么指示



提示

: 一个实用的经验法则是查看当前方位与期望方位之间、到/离信标的差值，并按该差值的两倍进行转向以建立航向，下面的示例会更清楚地说明这一点！



步骤 5

: 要切入特定径向线，可以想象 NDB 位于蓝色方位指针（箭头）的“头部”，而飞机位于蓝色方位指针的“尾部”。如果你是“飞向”信标，就需要朝着“尾部”方向转弯，把蓝色方位指针的尾部“拉”到新的位置；头部会开始向外“落开”，当它接近你想飞行的目标到信标方位时，你就可以再转回该方位。如果你是“背离”信标飞行，则需要通过远离“尾部”的方向转弯来“推”蓝色方位指针的头部。头部会开始向外“落开”并“拉”着尾部转动，当它接近你想飞行的目标离信标方位时，你就可以再转回该方位



| 到/离            | 转弯方向         | 结果                                      |
| --------------- | ---------------- | ----------------------------------------- |
| 飞向信标        | 朝向尾部         | 头部会“落开”并转到目标方位                |
| 背离信标        | 远离尾部         | 尾部会被“拉”到目标方位                    |



**示例：**

我们正从 PHNY 南侧向 Lanai（LLD）NDB 飞行，当前航向为 360 度。LLD NDB 已调谐到 ADF 1，并显示在 BRG（方位）1 上。今天，我们计划沿着 360 方位飞向信标（180 径向线），然而从下图可以看到，实际到信标方位为 350（或 170 径向线）。



![170 Radial](../../../_images/manual/frames/170-radial.png)



如果我们只是朝着信标转向（航向 350 度），就永远无法建立在 180 径向线上；相反，我们只会保持当前所在的 170 径向线。要飞到 180 径向线，我们需要确定到信标的“目标”方位与“当前”方位之间的差值——在这个例子里，差值是 10 度。为了切入目标径向线，我们建议将方位误差加倍作为经验法则——所以在这里，我们需要转 20 度。



![Heading 340](../../../_images/manual/frames/heading-340.png)



在上图中，你可以看到我们通过朝“尾部”方向转弯，将飞机航向从 360 改为 340 度。当前到信标方位仍然是 350，但现在我们已经改变了航向，蓝色方位指针的头部（箭头）会开始“落开”，当它接近到信标方位 360 度时，我们就可以再次向右转回 360 度航向。



![180 Radial](../../../_images/manual/frames/180-radial.png)



一旦到达目标方位，我们就可以监控蓝色方位指针，并根据风进行航向修正（确保我们沿着正确的径向线飞行）。



![Tracking 180 Radial](../../../_images/manual/frames/tracking-180-radial.png)



提示

: 使用 HSI 上的绿色虚线来帮助你理解在选择备用航向时风偏的影响