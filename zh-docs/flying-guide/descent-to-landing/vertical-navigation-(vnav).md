---
id: vertical-navigation-(vnav)
title: 垂直导航（VNAV）
meta: 了解如何在 Infinite Flight 中使用 VNAV。
order: 2
contributor: deercrusher
---

<a id="Vertical Navigation (VNAV)"></a>
<a id="vertical navigation (vnav)"></a>
<a id="vertical-navigation-(vnav)"></a>
<a id="vertical-navigation-vnav"></a>
<a id="Vertical%20Navigation%20%28VNAV%29"></a>
<a id="vertical%20navigation%20%28vnav%29"></a>
<a id="vertical-navigation-%28vnav%29"></a>
<a id="Vertical Navigation (VNAV)"></a>
<a id="vertical navigation (vnav)"></a>
<a id="vertical-navigation-(vnav)"></a>
<a id="vertical-navigation-vnav"></a>
<a id="Vertical%20Navigation%20%28VNAV%29"></a>
<a id="vertical%20navigation%20%28vnav%29"></a>
<a id="vertical-navigation-%28vnav%29"></a>
# 垂直导航（VNAV）


@[vimeo](422519684)


<a id="What is VNAV?"></a>
<a id="what is vnav?"></a>
<a id="what-is-vnav?"></a>
<a id="what-is-vnav"></a>
<a id="What%20is%20VNAV%3F"></a>
<a id="what%20is%20vnav%3F"></a>
<a id="what-is-vnav%3F"></a>
<a id="What is VNAV?"></a>
<a id="what is vnav?"></a>
<a id="what-is-vnav?"></a>
<a id="what-is-vnav"></a>
<a id="What%20is%20VNAV%3F"></a>
<a id="what%20is%20vnav%3F"></a>
<a id="what-is-vnav%3F"></a>
## 什么是 VNAV？

VNAV 代表 Vertical Navigation，是一种自动驾驶功能，允许飞机调整垂直速度，以在指定航路点达到预定高度。所有 SID、STAR 和进近都有必须满足的高度限制；VNAV 可用（当前仅支持下降）来帮助满足这些限制并减轻你的工作负担。 



只要你的飞行计划中至少有一个带高度限制的航路点，VNAV 就会计算出合适的爬升/下降率，并根据条件变化进行调整。以下参数用于此计算：



- 地速
- 到下一个航路点的距离
- 以及初始高度与目标/最终高度之间的高度差



<a id="What does Top of Descent (TOD) mean?"></a>
<a id="what does top of descent (tod) mean?"></a>
<a id="what-does-top-of-descent-(tod)-mean?"></a>
<a id="what-does-top-of-descent-tod-mean"></a>
<a id="What%20does%20Top%20of%20Descent%20%28TOD%29%20mean%3F"></a>
<a id="what%20does%20top%20of%20descent%20%28tod%29%20mean%3F"></a>
<a id="what-does-top-of-descent-%28tod%29-mean%3F"></a>
<a id="What does Top of Descent (TOD) mean?"></a>
<a id="what does top of descent (tod) mean?"></a>
<a id="what-does-top-of-descent-(tod)-mean?"></a>
<a id="what-does-top-of-descent-tod-mean"></a>
<a id="What%20does%20Top%20of%20Descent%20%28TOD%29%20mean%3F"></a>
<a id="what%20does%20top%20of%20descent%20%28tod%29%20mean%3F"></a>
<a id="what-does-top-of-descent-%28tod%29-mean%3F"></a>
## 什么是下降顶点（TOD）？

下降顶点，也称为 TOD，是从巡航高度开始下降到另一个高度、为飞行进近阶段做准备的点。TOD 会以时间显示，距离可以在两个位置找到，分别是：



- [自动驾驶](../../getting-started-guide/pilot-user-interface/autopilot.md#autopilot) 飞行控制单元（FCU）中的 VNAV 按钮内
- 以及如果已选择该选项，也会显示在 [状态栏](../../getting-started-guide/pilot-user-interface/status-bar.md#status-bar) 中



你也可以手动计算 TOD，点击 [这里](descent-planning.md#manually-calculating-top-of-descent-(tod)) 了解方法。



<a id="How do I use VNAV?"></a>
<a id="how do i use vnav?"></a>
<a id="how-do-i-use-vnav?"></a>
<a id="how-do-i-use-vnav"></a>
<a id="How%20do%20I%20use%20VNAV%3F"></a>
<a id="how%20do%20i%20use%20vnav%3F"></a>
<a id="how-do-i-use-vnav%3F"></a>
<a id="How do I use VNAV?"></a>
<a id="how do i use vnav?"></a>
<a id="how-do-i-use-vnav?"></a>
<a id="how-do-i-use-vnav"></a>
<a id="How%20do%20I%20use%20VNAV%3F"></a>
<a id="how%20do%20i%20use%20vnav%3F"></a>
<a id="how-do-i-use-vnav%3F"></a>
## 如何使用 VNAV？



步骤 1

: 检查你的飞行计划，确保你即将执行的程序中包含高度限制，你需要这些限制才能让 VNAV 正常工作



步骤 2

: 在接近 TOD 时，如果有启用的 ATC，请务必[请求高度变更](../atc-communication/descent-and-approach.md#descent-communication-summary)



步骤 3

: 一旦获得许可并确认周围安全，进入 [自动驾驶](../../getting-started-guide/pilot-user-interface/autopilot.md#autopilot) FCU 并点击 VNAV 以准备该功能。你的高度和 VS 会变为品红色，表示 VNAV 已准备就绪



提示

: 在进行任何高度变更之前，检查周围环境以确保安全，使用 [摄像机](../../getting-started-guide/pilot-user-interface/cameras.md#camera) 和 [小地图](../../getting-started-guide/pilot-user-interface/flight-planning.md#mini-map) 可帮助你



步骤 4

: 无需输入高度和 VS，VNAV 现在会自动调整你的垂直速度，以满足飞行计划中设定的高度限制



提示

: VNAV 的目标飞行路径角（FPA）为 2 度，不过如果你较晚开始下降，VNAV 可能会增加该角度以满足限制。VNAV 无法超过每分钟 3000 英尺（fpm），因此在这种情况下，可能需要手动干预以满足高度限制。此外，TOD 计算器会开始显示负值，这是因为你在开始下降前已经越过了 TOD 点



步骤 5

: 在下降过程中，地图上会显示一个高度弧线，表示飞机预计在当前自动驾驶 FCU ALT 按钮中显示的高度上保持平飞的位置。如果该弧线不在理想位置，VNAV 可能没有正常工作，可能需要手动干预



<a id="What happens once I'm level?"></a>
<a id="what happens once i'm level?"></a>
<a id="what-happens-once-i'm-level?"></a>
<a id="what-happens-once-im-level"></a>
<a id="What%20happens%20once%20I%27m%20level%3F"></a>
<a id="what%20happens%20once%20i%27m%20level%3F"></a>
<a id="what-happens-once-i%27m-level%3F"></a>
<a id="What happens once I'm level?"></a>
<a id="what happens once i'm level?"></a>
<a id="what-happens-once-i'm-level?"></a>
<a id="what-happens-once-im-level"></a>
<a id="What%20happens%20once%20I%27m%20level%3F"></a>
<a id="what%20happens%20once%20i%27m%20level%3F"></a>
<a id="what-happens-once-i%27m-level%3F"></a>
## 一旦保持平飞会发生什么？



当 VNAV 捕获到目标高度后，它会执行以下两种操作之一：



- 自动驾驶会保持平飞，并显示新的到 TOD 距离（如果该飞行计划段中还有更多已编程的高度限制，则表示你的下一个 TOD 在何处）
- 或者，如果自动驾驶判断你到达该高度时将处于或高于 2 度飞行路径角（FPA），它会继续下降



<a id="What do I do when I’m being Vectored?"></a>
<a id="what do i do when i’m being vectored?"></a>
<a id="what-do-i-do-when-i’m-being-vectored?"></a>
<a id="what-do-i-do-when-im-being-vectored"></a>
<a id="What%20do%20I%20do%20when%20I%E2%80%99m%20being%20Vectored%3F"></a>
<a id="what%20do%20i%20do%20when%20i%E2%80%99m%20being%20vectored%3F"></a>
<a id="what-do-i-do-when-i%E2%80%99m-being-vectored%3F"></a>
<a id="What do I do when I’m being Vectored?"></a>
<a id="what do i do when i’m being vectored?"></a>
<a id="what-do-i-do-when-i’m-being-vectored?"></a>
<a id="what-do-i-do-when-im-being-vectored"></a>
<a id="What%20do%20I%20do%20when%20I%E2%80%99m%20being%20Vectored%3F"></a>
<a id="what%20do%20i%20do%20when%20i%E2%80%99m%20being%20vectored%3F"></a>
<a id="what-do-i-do-when-i%E2%80%99m-being-vectored%3F"></a>
## 当我被雷达引导时该怎么办？

通常，雷达管制员会尽量让你按所选程序飞行，因为这样能减轻他们的工作负担，不过他们可能仍需要给出引导向量（在进近阶段几乎是必然的）。当你收到引导向量和/或高度指令时，重要的是遵照执行：



步骤 1

: 使用 [通信](../atc-communication/descent-and-approach.md#approach-communication-summary) 按钮确认发给你的指令



步骤 2

: 进入 [自动驾驶](../../getting-started-guide/pilot-user-interface/autopilot.md#autopilot) FCU 并点击 VNAV 以取消准备该功能



步骤 3

: 根据 ATC 的要求调整你的航向、高度和/或速度



步骤 4

: 确保你的导航台已调谐到你预期执行的进近方式



提示

: 持续检查周围环境以确保安全，并在规划时（尤其是在下降过程中），使用 [摄像机](../../getting-started-guide/pilot-user-interface/cameras.md#camera) 和 [小地图](../../getting-started-guide/pilot-user-interface/flight-planning.md#mini-map) 来帮助你