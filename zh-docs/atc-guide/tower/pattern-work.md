---
id: pattern-work
title: 航线作业
meta: 如何在 Infinite Flight 中于塔台席位执勤时管理航线、过渡飞行和 Flight of XX。
order: 4
---



<a id="Pattern Work"></a>
<a id="pattern work"></a>
<a id="pattern-work"></a>
<a id="Pattern%20Work"></a>
<a id="pattern%20work"></a>
<a id="Pattern Work"></a>
<a id="pattern work"></a>
<a id="pattern-work"></a>
<a id="Pattern%20Work"></a>
<a id="pattern%20work"></a>
# 航线作业

traffic pattern 是飞机在起飞和降落时，在保持与机场目视接触的情况下遵循的标准飞行航线。在 Infinite Flight 中，螺旋桨飞机的航线高度为 1000ft AAL（above aerodrome level，机场标高以上），喷气飞机为 1500ft AAL。它由多个航段组成，每一段之间通过 90 度转弯连接，如下图所示：



![标准航线](../../../_images/manual/graphics/atc-traffic-pattern.jpg)



手册

: 只有在存在目视气象条件（VMC）、飞机**必须**{.red}能够飞标准航线，并且交通量需要可控时，才**允许**{.red}进行航线作业。[更多信息？](../../atc-manual/3.-tower/3.4-pattern-work-transitions-flight-of-xx.md#3.4.1) 



要查看如何发布航线加入、排序和放行的逐步指南，请务必查看 [进场](inbounds.md) 页面。



+++ 情景 - 重新排序

::: scenario-heading
情景
:::

::: scenario
*I-DRUM* 和 *N1DC* 都已经完成排序并获准用于 RWY05L。随着两架飞机继续沿顺风腿飞行，*I-DRUM* 的顺风腿比管制员预期更长。
::: 

![](../../../_images/manual/screens/atcg-pw-downwind.png){.scenario}

| 方法 1                                                  |
| ------------------------------------------------------------ |
| 1: 将 *N1DC* 重新排序为 1 号                               |
| 2: 将 *I-DRUM* 重新排序为 2 号                          |
| 3: 如果你担心间隔，可以让 *I-DRUM* 说“延长顺风腿，我会叫你转基线”来缓解这一点 |

{.technique}

| 方法 1       | 优点或缺点？                                                |
| ------------------------------------------------------------ | -------------------------- |
| :fa-check-circle: | 高效                                                  |
| :fa-check-circle: | 飞行员满意度更高                                 |
| :fa-times-circle: | 可能会增加工作量，因为你需要发送多条指令 |

{.prosandcons}




| 方法 2                                          |
| ---------------------------------------------------- |
| 1: 指示 *I-DRUM* “转基线”                  |
| 2: 这会迫使 *I-DRUM* 飞出更紧凑的航线 |

{.technique}

| 方法 2       | 优点或缺点？                                                  |
| ------------------------------------------------------------ | ---------------------------- |
| :fa-check-circle: | 可能很高效                                             |
| :fa-times-circle: | 某些飞行员/机型可能无法飞出这么紧凑的航线 |

{.prosandcons}

+++



<a id="Transitions"></a>
<a id="transitions"></a>
<a id="Transitions"></a>
<a id="transitions"></a>
## 过渡飞行

当飞机未与雷达席位接管、并且正在穿越塔台管制员空域时，可以请求过渡飞行。对于 Infinite Flight，塔台空域被定义为机场周围最紧邻的环状/边界区域，并向上延伸至 5000ft AAL（因此，如果机场标高为 1000ft，则塔台空域为 1000ft - 6000ft）。



手册

: 过渡飞行**必须**{.red}仅在塔台空域内批准（因此在上例中，不得高于 6000ft）。如果塔台管制员在航线中已有飞机，则**必须**{.red}应用间隔。[更多信息？](../../atc-manual/3.-tower/3.4-pattern-work-transitions-flight-of-xx.md#3.4.2)



@[vimeo](563250409)



步骤 1

: 当飞机请求过渡飞行时，飞机图标以及飞行进度条上的呼号都会以琥珀色闪烁



步骤 2

: 点击地图上的飞机（然后选择 "Other Message"），或者点击飞行进度条，打开通信菜单



步骤 3

: 确定一个既能让飞机保持在塔台空域内、又能与航线中可能存在的其他交通保持间隔的高度



步骤 4

: 点击 "Respond to Transition > [select <10,000ft / >=10,000ft ] > [select altitude]"



提示

: VFR 交通之间至少需要 500ft 间隔，不过我们建议给出能提供至少 1000ft 间隔的过渡飞行，以便同时满足 IFR 要求！



<a id="Flight of XX"></a>
<a id="flight of xx"></a>
<a id="flight-of-xx"></a>
<a id="Flight%20of%20XX"></a>
<a id="flight%20of%20xx"></a>
<a id="Flight of XX"></a>
<a id="flight of xx"></a>
<a id="flight-of-xx"></a>
<a id="Flight%20of%20XX"></a>
<a id="flight%20of%20xx"></a>
## Flight of XX



手册

: 当使用 "Flight of XX" 呼号管制飞机时，你**必须**{.red}只向领机发送指令，并将 Flight of XX 视作一架飞机。[更多信息？](../../atc-manual/3.-tower/3.4-pattern-work-transitions-flight-of-xx.md#3.4.5)



@[vimeo](563261625)



步骤 1

: 当领机提出请求时，飞机图标以及飞行进度条上的呼号都会以琥珀色闪烁



步骤 2

: 点击地图上的飞机（然后选择 "Other Message"），或者点击飞行进度条，打开通信菜单 



提示

: 使用飞行进度条可能更容易，因为多架编队飞行的飞机会让点击地图上的飞机变得有些困难！