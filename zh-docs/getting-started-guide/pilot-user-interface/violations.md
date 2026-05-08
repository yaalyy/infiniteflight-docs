---
id: violations
title: 违规
meta: 了解 Infinite Flight 中违规机制的运作方式。
order: 15
---

<a id="Violations"></a>
<a id="violations"></a>
<a id="Violations"></a>
<a id="violations"></a>
# 违规



<a id="What are Violations?"></a>
<a id="what are violations?"></a>
<a id="what-are-violations?"></a>
<a id="what-are-violations"></a>
<a id="What%20are%20Violations%3F"></a>
<a id="what%20are%20violations%3F"></a>
<a id="what-are-violations%3F"></a>
<a id="What are Violations?"></a>
<a id="what are violations?"></a>
<a id="what-are-violations?"></a>
<a id="what-are-violations"></a>
<a id="What%20are%20Violations%3F"></a>
<a id="what%20are%20violations%3F"></a>
<a id="what-are-violations%3F"></a>
## 什么是违规？


违规可以由系统自动生成（1 级）或由 ATC 签发（2 级或 3 级），用于管理 [Training and Expert Servers](../home-user-interface/mode.md#servers) 上的飞行员行为。**1 级**违规可在两个服务器上收到，而 **2 级** 和 **3 级** 违规只能在 Expert Server 上签发。每个服务器都有各自的规则和最低 [grade](../home-user-interface/user-profile.md#the-grade-table) 要求，但 Expert Server 仅面向认真使用的用户。如果没有遵守服务器规则和程序，ATC 将严格执行，飞行员可能会收到违规。 

 

**1 级**违规会在飞行员违反以下任一设定条件时自动生成：

 


| 规则                       | 违规条件                                                     |
| -------------------------- | ------------------------------------------------------------ |
| 地面超速                   | 在地面上地速超过 35 kts GS（地速），不包括跑道 |
| 飞行超速                   | 在 10,000 英尺以下 IAS（指示空速）超过 250 kts / 超过最大速度警告（VMO/MMO）- 不适用于军用飞机 |
| 空域内特技飞行             | 在 5,000 英尺以下且距机场 5 海里内进行特技飞行 |
| 跑道停留                   | 未经 ATC 放行，在跑道上静止停留超过 60 秒 |



提示

: 最常见的 1 级违规是飞行超速 - 请务必在接近 10,000 英尺之前就将速度降到 250kts IAS 以下，以避免触发。我们还建议不要在 10,000 英尺巡航时将速度保持在（或接近）250kts IAS 以上，因为启用 Autopilot 时高度可能会波动，从而导致违规！



<a id="What happens if I get a Violation?"></a>
<a id="what happens if i get a violation?"></a>
<a id="what-happens-if-i-get-a-violation?"></a>
<a id="what-happens-if-i-get-a-violation"></a>
<a id="What%20happens%20if%20I%20get%20a%20Violation%3F"></a>
<a id="what%20happens%20if%20i%20get%20a%20violation%3F"></a>
<a id="what-happens-if-i-get-a-violation%3F"></a>
<a id="What happens if I get a Violation?"></a>
<a id="what happens if i get a violation?"></a>
<a id="what-happens-if-i-get-a-violation?"></a>
<a id="what-happens-if-i-get-a-violation"></a>
<a id="What%20happens%20if%20I%20get%20a%20Violation%3F"></a>
<a id="what%20happens%20if%20i%20get%20a%20violation%3F"></a>
<a id="what-happens-if-i-get-a-violation%3F"></a>
## 如果我收到违规会怎样？

 

为了确保所有飞行员都能获得愉快的体验（在 Expert Server 上则是更真实的体验），违规都会被记录，并对飞行员产生以下影响：



1 级违规

: 如果飞行员在一次飞行中收到 3 次或更多 1 级违规，将会被自动移出服务器，并且必须重新开始一次飞行



2 级违规（琥珀色）

: 飞行员会与服务器断开连接，但可以离线继续飞行。只要 2 级和 3 级违规数量仍低于服务器允许上限，飞行员即可通过开始新飞行立即返回 Expert Server


![2 级违规](../../../_images/manual/frames/violation-level2.png) 


1. 通常在你收到违规时会提供简要摘要，不过你也可以在[这里](violation-reasons.md#violation-reasons)查看更详细的原因。如果你仍然不确定，可以在论坛上联系管制员：[community.infiniteflight.com](https://community.infiniteflight.com/)，或者按照[下面的步骤](violations.md#appealing-a-level-2-or-3-violation)提出申诉

 

2. “用户指南”按钮会结束你当前的飞行，并直接带你进入我们的指南页面，在那里你可以找到更多信息

 

3. “结束飞行”按钮会结束你的飞行，提供你的飞行摘要，然后带你返回在线飞行界面

 

4. 你还可以选择“继续离线”，但这样你将对其他玩家不可见，也将无法再看到 ATC 或空中交通



3 级违规（红色）

: 飞行员会与服务器断开连接，但可以离线继续飞行。飞行结束后，飞行员将无法返回 Expert Server；自此起 7 天内将被限制访问


![3 级违规](../../../_images/manual/frames/violation-level3.png) 


此外，违规会保留在飞行员记录中，因此如果飞行员持续收到违规（仅限 **2 级** 和 **3 级**），对 Expert Server 的访问限制时间会更长。目前，在任意 365 天滚动周期内，收到的 **2 级** 和/或 **3 级** 违规不得超过五次，才能访问该服务器。



<a id="How to prevent Violations"></a>
<a id="how to prevent violations"></a>
<a id="how-to-prevent-violations"></a>
<a id="How%20to%20prevent%20Violations"></a>
<a id="how%20to%20prevent%20violations"></a>
<a id="How to prevent Violations"></a>
<a id="how to prevent violations"></a>
<a id="how-to-prevent-violations"></a>
<a id="How%20to%20prevent%20Violations"></a>
<a id="how%20to%20prevent%20violations"></a>
## 如何避免违规

 

避免违规的最佳方式是：

 

* 熟悉 [infiniteflight.com](/guide) 提供的官方教程和指南

* 加入我们的社区 [community.infiniteflight.com](https://community.infiniteflight.com/) 并提问，那里有很多飞行员和管制员愿意提供帮助

* 一旦你的等级足够高，可以加入 Expert Server，请放慢节奏，遵循所有 ATC 指令，并礼貌对待其他飞行员

 

如果你仍然收到违规，请尝试找出原因，并从中吸取经验教训。



提示

: 需要注意的是，管制员并不总是能够在违规之前发出警告（或多次警告），尤其是在非常繁忙时段，或对于显而易见的违规行为！



<a id="Appealing a Level 2 or 3 Violation"></a>
<a id="appealing a level 2 or 3 violation"></a>
<a id="appealing-a-level-2-or-3-violation"></a>
<a id="Appealing%20a%20Level%202%20or%203%20Violation"></a>
<a id="appealing%20a%20level%202%20or%203%20violation"></a>
<a id="Appealing a Level 2 or 3 Violation"></a>
<a id="appealing a level 2 or 3 violation"></a>
<a id="appealing-a-level-2-or-3-violation"></a>
<a id="Appealing%20a%20Level%202%20or%203%20Violation"></a>
<a id="appealing%20a%20level%202%20or%203%20violation"></a>
## 申诉 2 级或 3 级违规



我们建议你只对 **3 级** 违规提出申诉，因为它们会阻止你访问 Expert Server；而 **2 级** 违规则允许你开始新飞行（前提是你没有超过允许的违规总数）。不过，如果你认为违规是误发的，你可以在违规发出后 **7 天内** 按照以下步骤提出申诉：

 

步骤 1

: 打开你的 [logbook](../home-user-interface/logbook.md)

 

步骤 2

: 在 Live Flights 下的 Notes 列中，你可以看到所有导致报告的飞行。点按该备注，然后在屏幕底部选择“View Flight Details”。这样你就能看到举报你的管制员的 IFC 用户名，以便你提出申诉

 

步骤 3

: [在我们的社区论坛发送私信](https://community.infiniteflight.com)给该管制员，并附上你的呼号、违规日期以及尽可能详细的事件说明。如果你找不到该管制员，或者你是新用户，你也可以改为[将申诉发送给我们的 @appeals 组](https://community.infiniteflight.com/new-message?groupname=appeals&title=Violation%20Appeal&body=%23%23%20Violation%20Appeal%20Process%0A%0AThank%20you%20for%20taking%20the%20time%20to%20find%20out%20how%20to%20Appeal%20a%20recent%20Level%202%20or%203%20Violation.%20Please%20fill%20in%20the%20template%20below%20with%20as%20much%20detail%20as%20possible%20-%20%2A%2Awithout%20this%20information%20we%20won%27t%20be%20able%20to%20help%20you.%2A%2A%0A%0A%2APlease%20note%20that%20you%20cannot%20appeal%20Level%201%20Violations%2C%20these%20are%20automatically%20generated%20based%20on%20your%20flying%2C%20for%20more%20information%20please%20click%20%5Bhere%5D%28https%3A%2F%2Finfiniteflight.com%2Fguide%2Fgetting-started-guide%2Fpilot-user-interface%2Fviolations%23what-are-violations%253F%29.%2A%0A%0A%23%23%20What%20is%20your%20callsign%3F%0A_Type%20your%20response%20next%20to%20the%20%60%3E%60.%20Make%20sure%20you%20give%20us%20your%20current%20callsign%20%28as%20well%20as%20the%20callsign%20you%20used%20when%20you%20received%20a%20violation_%0A%3E%0A---%0A%23%23%20When%20did%20you%20get%20the%20violation%3F%0A%3E%0A---%0A%23%23%20What%20was%20the%20name%20of%20the%20controller%3F%0A%3E%0A---%0A---%0A%23%23%20What%27s%20the%20link%20to%20your%20replay%20file%3F%0A_Upload%20your%20replay%20to%20%5Bsharemyinfiniteflight.com%5D%28https%3A%2F%2Fsharemyinfiniteflight.com%2F%29%20and%20paste%20the%20link%20below_%0A%3E%0A---%0A%23%23%20Additional%20Details%3A%0A_Let%20us%20know%20additional%20details%20so%20we%20can%20investigate%20as%20quickly%20as%20possible_%0A%3E) instead

 

步骤 4

: 为了帮助团队处理你的申诉，你很可能会被要求[提供你的飞行回放](../home-user-interface/logbook.md)



步骤 5

: 请耐心等待，我们会尽力协助你完成整个流程

 

