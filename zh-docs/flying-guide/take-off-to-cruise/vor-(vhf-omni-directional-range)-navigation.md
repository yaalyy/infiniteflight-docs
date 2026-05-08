---
id: vor-(vhf-omni-directional-range)-navigation
title: VOR（甚高频全向信标）导航
meta: 了解如何在 Infinite Flight 中使用 VOR 进行导航。
type: Advanced
order: 10
---

<a id="VOR (VHF Omni-Directional Range) Navigation"></a>
<a id="vor (vhf omni-directional range) navigation"></a>
<a id="vor-(vhf-omni-directional-range)-navigation"></a>
<a id="vor-vhf-omni-directional-range-navigation"></a>
<a id="VOR%20%28VHF%20Omni-Directional%20Range%29%20Navigation"></a>
<a id="vor%20%28vhf%20omni-directional%20range%29%20navigation"></a>
<a id="vor-%28vhf-omni-directional-range%29-navigation"></a>
<a id="VOR (VHF Omni-Directional Range) Navigation"></a>
<a id="vor (vhf omni-directional range) navigation"></a>
<a id="vor-(vhf-omni-directional-range)-navigation"></a>
<a id="vor-vhf-omni-directional-range-navigation"></a>
<a id="VOR%20%28VHF%20Omni-Directional%20Range%29%20Navigation"></a>
<a id="vor%20%28vhf%20omni-directional%20range%29%20navigation"></a>
<a id="vor-%28vhf-omni-directional-range%29-navigation"></a>
# VOR（甚高频全向信标）导航



@[vimeo](455590960)



<a id="What is a VOR?"></a>
<a id="what is a vor?"></a>
<a id="what-is-a-vor?"></a>
<a id="what-is-a-vor"></a>
<a id="What%20is%20a%20VOR%3F"></a>
<a id="what%20is%20a%20vor%3F"></a>
<a id="what-is-a-vor%3F"></a>
<a id="What is a VOR?"></a>
<a id="what is a vor?"></a>
<a id="what-is-a-vor?"></a>
<a id="what-is-a-vor"></a>
<a id="What%20is%20a%20VOR%3F"></a>
<a id="what%20is%20a%20vor%3F"></a>
<a id="what-is-a-vor%3F"></a>
## 什么是 VOR？

VHF（Very High Frequency，甚高频）Omni-Directional Range，也称为 VOR，是一种地面发射器，会发射无线电信号，并通过其自身的频率和三字母代码进行识别。装备了 VHF 导航接收机的飞机就可以解释这些信号，并将其用于导航。要使用 VOR 进行导航，你需要[调谐到正确的频率](../../getting-started-guide/pilot-user-interface/navigation.md#tuning-to-a-vor-or-adf)，然后[在驾驶舱中显示它](../../getting-started-guide/pilot-user-interface/navigation.md#displaying-a-vor-in-your-aircraft)。

 

除此之外，以下定义对于理解 VOR 导航背后的原理至关重要：



| 术语   | 定义                                         |
| ------ | -------------------------------------------------- |
| Radial | radial 总是指**从**信标指向外的方位 |
| To     | **指向**信标的磁方位                          |
| From   | **从**信标指向外的磁方位                    |



![径向线与 To/From](../../../_images/manual/graphics/vor-radials.jpg)



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
## 什么是水平情况指示器（HSI）？

水平情况指示器，或 HSI，是 Infinite Flight 中用于导航的主要仪表。它由以下部分组成：



- 罗盘玫瑰，随当前飞机航向对准
- 蓝色航向旋钮，显示 [自动驾驶 FCU](../../getting-started-guide/pilot-user-interface/autopilot.md#autopilot) 设定的航向
- 单蓝色指针表示 BRG（方位）1 - 当调谐到某个导航源（ILS、VOR 或 NDB）时，它会指向该导航台
- 双蓝色指针表示 BRG（方位）2 - 当调谐到某个导航源（ILS、VOR 或 NDB）时，它会指向该导航台
- 航向偏差指示器（CDI），由航向指针和侧向偏差条组成 - GPS 显示为品红色，NAV 1 和 NAV 2 显示为浅绿色

![HSI 元素](../../../_images/manual/graphics/hsi-elements.jpg)




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
## 如何设置你的水平情况指示器（HSI）

步骤 1

: 通过从你的[地图](../../getting-started-guide/pilot-user-interface/flight-planning.md#map)或[小地图](../../getting-started-guide/pilot-user-interface/flight-planning.md#mini-map)中点选 VOR，在显示的列表里选择该 VOR，然后点击“Set NAV 1 (or 2)”来[调谐 VOR](../../getting-started-guide/pilot-user-interface/navigation.md#tuning-to-a-vor-or-adf)



步骤 2

: 通过在飞行界面中点击“NAV”来显示航空电子页面，并确保 BRG 1（或 2）中显示的是 NAV 1（或 2），以此来[显示 VOR](../../getting-started-guide/pilot-user-interface/navigation.md#displaying-a-vor-in-your-aircraft)（取决于你将 VOR 调谐到哪个 NAV）



步骤 3

: 最后，在航空电子页面中，根据需要将“SOURCE”更改为 NAV 1（或 2），然后将相应的航向（CRS 1 或 2）调整为你希望飞行的目标磁方位



<a id="How to Navigate using a VOR"></a>
<a id="how to navigate using a vor"></a>
<a id="how-to-navigate-using-a-vor"></a>
<a id="How%20to%20Navigate%20using%20a%20VOR"></a>
<a id="how%20to%20navigate%20using%20a%20vor"></a>
<a id="How to Navigate using a VOR"></a>
<a id="how to navigate using a vor"></a>
<a id="how-to-navigate-using-a-vor"></a>
<a id="How%20to%20Navigate%20using%20a%20VOR"></a>
<a id="how%20to%20navigate%20using%20a%20vor"></a>
## 如何使用 VOR 导航



步骤 1

: 通过确定飞行方向以及可用于辅助航线的导航台（如 VOR），来准备你的飞行计划



步骤 2

: 确保你已经使用我们的分步指南提前做好规划，以帮助你-[调谐](../../getting-started-guide/pilot-user-interface/navigation.md#tuning-to-a-vor-or-adf)和[显示](../../getting-started-guide/pilot-user-interface/navigation.md#displaying-a-vor-in-your-aircraft)所需的 VOR，调整 CRS 到你希望截获的目标磁方位，最后将 SOURCE 设置为 NAV 1（或按需设置为 NAV 2）



提示

: 你只能显示 NAV 1 或 NAV 2 的 CDI，不过你仍然可以用相同或不同的 VOR 和/或 CRS 来设置 NAV 1 和 NAV 2，这样在空中时可以减轻你的工作负担！



步骤 3

: 接下来，查看你相对于 VOR 的位置，并使用 HSI 上的方位指针（蓝色）来帮助判断。你也可以使用你的[地图](../../getting-started-guide/pilot-user-interface/flight-planning.md#map)和[小地图](../../getting-started-guide/pilot-user-interface/flight-planning.md#mini-map)



步骤 4

: 计划你将如何截获预设航向，以及在接近时你预计指示器会显示什么



提示

: 我们建议截获角不大于 45 度，不过如果你离 VOR 很近，可能需要更小的角度，否则在截获过程中你可能会穿过目标航线！



步骤 5

: 当你接近截获点时，CDI 的侧向偏差条会“活跃”起来，利用它来帮助判断转向到目标航向的时机



提示

: 侧向偏差条可能会“活跃”得非常快，尤其是在你离 VOR 很近时 - 注意蓝色方位指针，它会始终显示到信标的当前磁方位，用它来在接近你想飞行的航线时提前做好准备！



**示例：**

我们已从雅典（LGAV）的 03R 号跑道起飞，并执行右侧下风航段离场，打算截获 ATV VOR 的 090 径向线，并据此以 270 的磁方位飞向该信标。



![VOR 示例](../../../_images/manual/graphics/vor-radial-example.jpg)



在起飞前，我们已经调谐并显示了 ATV VOR（本例中为 NAV 1），选择了 270 的 CRS，并确保 SOURCE 设置为 NAV 1。

![航空电子设置](../../../_images/manual/frames/avionics-set-up.png)

当我们起飞并右转进入下风航段后，航向将为 210，这是一个 60 度的截获角，因此我们将航向调整为 240 度，以便在离 VOR 不远的情况下获得稍微缓一些的截获角。

![右侧下风航段](../../../_images/manual/frames/right-downwind.png)

在 240 度航向下，我们可以看到蓝色方位指针（表示 VOR 所在方向）开始移动；当它接近 270 时，我已经开始预判何时需要转向至 270 度航向。

![调整后的截获航向](../../../_images/manual/frames/adjusted-intercept-heading.png)

当侧向偏差条“活跃”起来时，我开始转弯，以 270 的磁方位飞向该信标。 

![CDI 活跃](../../../_images/manual/frames/cdi-alive.png)

一旦我们转到这个航向，就可以继续微调，以确保我们沿着指向信标的 090 径向线飞行（同时考虑风偏）。

![航向 270](../../../_images/manual/frames/heading-270.png)



提示

: 使用 HSI 上的绿色虚线，帮助你理解在选择备用航向时风偏的影响

![沿 090 径向线跟踪](../../../_images/manual/frames/tracking-090-radial.png)