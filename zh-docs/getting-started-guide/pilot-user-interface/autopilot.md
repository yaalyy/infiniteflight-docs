---
id: autopilot
title: 自动驾驶
meta: 了解如何在 Infinite Flight 中使用自动驾驶。
order: 12
---

<a id="Autopilot"></a>
<a id="autopilot"></a>
<a id="Autopilot"></a>
<a id="autopilot"></a>
# 自动驾驶

![Autopilot](../../../_images/manual/frames/autopilot.png)



1. 通过点击自动驾驶（AP）图标，自动驾驶面板将出现，显示飞行控制单元（FCU）选项



步骤 1

: 要接通自动驾驶，请点击“AP OFF”按钮（必须在空中才能使自动驾驶功能正常工作）。该按钮会以橙色空心框高亮，并变为“AP ON”

步骤 2

: 基本模式会自动启用，即当前航向和垂直速度（VS）

步骤 3

: 高度（ALT）、垂直速度（VS）、高度预设（ALT PRESETS）、速度（SPD）、航向（HDG）、垂直导航（VNAV）、横向导航（LNAV GPS）和进近模式（APPR）都可以通过点击各自图标来接通或取消。按住任一图标（AP、ALT PRESETS、VNAV、LNAV 和 APPR 除外），然后上下移动手指即可更改数值。对于 ALT PRESETS，只需点击按钮，便会出现一个预设选项列表供选择（这将覆盖 ALT 窗口中当前设置的任何高度）

步骤 4

: 高度和航向选择会以青绿色 bug 的形式显示在 [HUD](hud.md) 上。这些数值可以在接通自动驾驶之前预先设置



<a id="Use of Approach Mode"></a>
<a id="use of approach mode"></a>
<a id="use-of-approach-mode"></a>
<a id="Use%20of%20Approach%20Mode"></a>
<a id="use%20of%20approach%20mode"></a>
<a id="Use of Approach Mode"></a>
<a id="use of approach mode"></a>
<a id="use-of-approach-mode"></a>
<a id="Use%20of%20Approach%20Mode"></a>
<a id="use%20of%20approach%20mode"></a>
## 进近模式的使用

@[vimeo](495491039)



某些飞机可能配备进近（APPR）模式，它允许自动驾驶截获 ILS，并在保持接通直到触地时执行自动着陆。在接通 APPR 模式之前，请确保 ILS 已经[调谐](navigation.md#tuning-to-an-ils)并已在你的飞机上[显示](navigation.md#displaying-an-ils-in-your-aircraft)。

提示

: 如果空速超过 250 节，或你的飞机超过最大着陆重量，则无法启用 APPR 模式




按下 APPR 按钮后，其下方会显示以下内容：

| 自动驾驶模式                                  | 含义                                                         |
| ---------------------------------------------- | ------------------------------------------------------------ |
| "LOC ALT"（琥珀色闪烁）                        | APPR 模式已预位                                                 |
| "LOC"（绿色常亮）和 "ALT"（琥珀色闪烁）        | APPR 模式正在截获或已经建立在 LOC 上，G/S 已预位，并且如果你低于 G/S，将会被捕获 |
| "LOC GS"（绿色常亮）                          | APPR 模式正在截获或已经建立在 LOC 和 G/S 上                   |

为了获得最佳效果，只有在你处于 [ILS 截获航向](../../flying-guide/descent-to-landing/instrument-landing-system-(ils)-approach.md#what-is-an-ils-approach%3F) 时才启用 APPR 模式（我们建议偏差不超过 30 度）。一旦接通，航向仍然可以调整。然而一旦 LOC 捕获开始，航向就不能再更改。 



提示

: 如果 LNAV 和 VNAV 已接通，而此时点击 APPR 按钮，飞机最后一次飞行的航向和垂直速度将会被保持，但这可能导致异常的自动驾驶行为