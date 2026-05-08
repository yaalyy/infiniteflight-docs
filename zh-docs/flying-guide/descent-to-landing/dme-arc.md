---
id: dme-arc
title: DME 弧线
meta: 了解如何在 Infinite Flight 中飞行 DME 弧线。
order: 6
type: Advanced
contributor: deercrusher
---

<a id="DME Arc"></a>
<a id="dme arc"></a>
<a id="dme-arc"></a>
<a id="DME%20Arc"></a>
<a id="dme%20arc"></a>
<a id="DME Arc"></a>
<a id="dme arc"></a>
<a id="dme-arc"></a>
<a id="DME%20Arc"></a>
<a id="dme%20arc"></a>
# DME 弧线



<a id="What is a DME Arc?"></a>
<a id="what is a dme arc?"></a>
<a id="what-is-a-dme-arc?"></a>
<a id="what-is-a-dme-arc"></a>
<a id="What%20is%20a%20DME%20Arc%3F"></a>
<a id="what%20is%20a%20dme%20arc%3F"></a>
<a id="what-is-a-dme-arc%3F"></a>
<a id="What is a DME Arc?"></a>
<a id="what is a dme arc?"></a>
<a id="what-is-a-dme-arc?"></a>
<a id="what-is-a-dme-arc"></a>
<a id="What%20is%20a%20DME%20Arc%3F"></a>
<a id="what%20is%20a%20dme%20arc%3F"></a>
<a id="what-is-a-dme-arc%3F"></a>
## 什么是 DME 弧线？

距离测量设备（Distance Measuring Equipment，简称 DME）最常与 VOR 之类的导航台（NAVAID）配合使用，用于提供到或离该台的距离。DME 弧线是一条与其中某个 NAVAID 保持恒定距离的弯曲航线，其中弧线距离本质上就是以该 NAVAID 为圆心的圆半径。 



DME 弧线最常见于进近初始段，用于引导飞机从初始进近定位点（IAF）进入最后进近航向，从而开始中间进近和最后进近段。 



在弧线周围会有一系列由该 NAVAID 发布的径向线，用于指示弧线的开始位置、何时可以继续下降，以及何时可以开始转弯以截获最后进近航向。



下面是航图上 DME 弧线的一个示例；在这个特定案例中，它通过 ALANA IAF 引导飞机进入檀香山（PHNL）RWY04R 的最后进近航向：

![PHNL Chart](../../../_images/manual/graphics/phnl-chart.jpg)



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



- 与当前飞机航向对正的罗盘玫瑰
- 显示 [Autopilot FCU](../../getting-started-guide/pilot-user-interface/autopilot.md#autopilot) 设定航向的蓝色航向 bug
- 单个蓝色指针表示 BRG（bearing）1 - 当调谐到导航源（ILS、VOR 或 NDB）时，它会指向该导航台
- 双蓝色指针表示 BRG（bearing）2 - 当调谐到导航源（ILS、VOR 或 NDB）时，它会指向该导航台
- 航道偏差指示器（CDI），由航道指针和横向偏差条组成 - GPS 时显示为品红色，NAV 1 和 NAV 2 时显示为浅绿色

![HSI Elements](../../../_images/manual/graphics/hsi-elements.jpg)



<a id="DME Arc Flying Technique"></a>
<a id="dme arc flying technique"></a>
<a id="dme-arc-flying-technique"></a>
<a id="DME%20Arc%20Flying%20Technique"></a>
<a id="dme%20arc%20flying%20technique"></a>
<a id="DME Arc Flying Technique"></a>
<a id="dme arc flying technique"></a>
<a id="dme-arc-flying-technique"></a>
<a id="DME%20Arc%20Flying%20Technique"></a>
<a id="dme%20arc%20flying%20technique"></a>
## DME 弧线飞行技巧

进入弧线时，飞机通常需要沿某条径向线飞入，这意味着它们是以 90 度角接近弧线。90 度转弯需要提前量，我们建议用地速的 1% 作为开始转弯的参考，除非航图另有指定距离。



提示

: 例如，如果你以 180kt 飞行，那么应在距离剩余 1.8 英里时开始转弯！



一旦建立在弧线上，并且要沿着弯曲轨迹保持相同的 DME 距离，飞机航向在无风条件下就应始终与该导航台成 90 度。然而，要真正这样飞并匹配转弯半径，飞机需要根据风对地速的影响持续调整坡度角。这在实际操作中并不现实，因此最佳技巧是把弧线拆分成一系列受控的航向变化，每次都稍微切过弧线。



需要预先设定一个航向变化幅度；下面的示例使用 10 度，但如果你愿意，也可以更大！一旦建立在弧线上（即与 DME 弧线公布的距离正确，且相对方位为 90 度）就可以进行一次 10 度转弯来“切过”弧线。此时方位指针会显示在 90 度线以上 5 度（实际相对方位为 85 度），飞机将开始切过弧线。随着飞机再次接近弧线，方位指针会开始移动，直到它降到 90 度线以下 5 度（实际相对方位现在为 95 度）；这时可以再做一次 10 度切过，重复该技巧，直到完成整个弧线。



![DME Arc Flying Technique](../../../_images/manual/graphics/dme-arc.jpg)



在上面的“HSI 1”中，你可以看到飞机已做出 10 度转弯，开始切过弧线（方位指针现在位于 90 度相对方位线以上 5 度）。在“HSI 2”中，飞机已经到达这次切过的末端（方位指针现在位于 90 度相对方位线以下 5 度）。在“HSI 3”中，飞机又做出一次 10 度转弯，以切过弧线的下一个区段（方位指针现在位于 90 度相对方位线以上 5 度）。



提示

: 每次完成一次切过时，DME 一开始会显示公布的弧线距离。随后当飞机“切角”时，这个距离会略微减小，但应在下一次转弯之前开始回到公布的弧线距离。



如果在接近 90 度相对方位线时，DME 距离与公布的弧线距离不符，则需要采取以下修正措施：

| DME 距离                             | 修正措施                                                   |
| ------------------------------------ | ---------------------------------------------------------- |
| 低于公布的弧线距离                    | 保持当前航向更久，直到距离回到设定值，再进行下一次切过转弯 |
| 高于公布的弧线距离                    | 需要做更大的切过转弯，以重新建立在弧线上                   |



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

: 通过在你的[地图](../../getting-started-guide/pilot-user-interface/flight-planning.md#map)或[小地图](../../getting-started-guide/pilot-user-interface/flight-planning.md#mini-map)中点击 NAVAID，选择显示列表中的 VOR/NDB，然后点击“Set NAV 1 (or 2)”来[调谐 NAVAID](../../getting-started-guide/pilot-user-interface/navigation.md#tuning-to-a-vor-or-adf)



步骤 2

: 通过在 Fly Screen 上点击“NAV”来显示航空电子设备选项卡，从而[显示 VOR](../../getting-started-guide/pilot-user-interface/navigation.md#displaying-a-vor-in-your-aircraft)或[NDB](../../getting-started-guide/pilot-user-interface/navigation.md#displaying-an-adf-in-your-aircraft)，并确保 BRG 1（或 2）显示的是 NAV 1（或 2）或 ADF（取决于你调谐的是哪个 NAVAID）



<a id="How to Fly a DME Arc"></a>
<a id="how to fly a dme arc"></a>
<a id="how-to-fly-a-dme-arc"></a>
<a id="How%20to%20Fly%20a%20DME%20Arc"></a>
<a id="how%20to%20fly%20a%20dme%20arc"></a>
<a id="How to Fly a DME Arc"></a>
<a id="how to fly a dme arc"></a>
<a id="how-to-fly-a-dme-arc"></a>
<a id="How%20to%20Fly%20a%20DME%20Arc"></a>
<a id="how%20to%20fly%20a%20dme%20arc"></a>
## 如何飞行 DME 弧线



步骤 1

: 查看进近航图，确认所需的 NAVAID、DME 弧线的起止位置，以及需要飞行的距离



步骤 2

: 设置你的[水平位置指示器（HSI）](dme-arc.md#what-is-the-horizontal-situation-indicator-(hsi)%3F)以帮助飞行 DME 弧线。如果你在 DME 弧线结束时要截获精密/非精密进近的最后进近航向，若条件允许，也请确保将其调好



提示

: 虽然不是必需的，但把一些[航路点](../../getting-started-guide/pilot-user-interface/flight-planning.md#flight-plan)或[进近程序](../../getting-started-guide/pilot-user-interface/flight-planning.md#selecting-departure%2C-arrival-and-approach-procedures)加入你的飞行计划，会很有助于你保持位置感



步骤 3

: 规划你将以什么速度执行该程序。在进入弧线入口点时，使用地速来判断何时转入第一个航向（我们建议使用地速的 1%，所以如果你的 GS 为 180kt，就应在距离弧线 1.8 海里时开始转弯）



提示

: 我们建议飞行 DME 弧线时不要超过 180kt IAS，这样可以减轻你的工作负荷；不过，具体速度也可能取决于机型。无论如何，都要确保遵守所有高度/速度限制！



步骤 4

: 弧线上的初始航向应使飞机与导航台成 90 度，使用方位指针来帮助你判断



步骤 5

: 将航向调整 10 度，以“切过”弧线，方位指针应显示相对导航台 85 度的相对方位



步骤 6

: 监控方位指针，当它接近 95 度相对方位时，再转 10 度，重新“切过”弧线



步骤 7

: 确保持续监控 DME，并确认其数值大致与公布的 DME 距离一致；如果不同，可能需要[进行修正](dme-arc.md#dme-arc-flying-technique)



步骤 8

: 当你通过航图上标示的最后一条径向线后，继续转弯以截获最后进近航向