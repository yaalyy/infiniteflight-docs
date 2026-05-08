---
id: steps
title: 步骤
meta: 场景编辑器工具快速概览
order: 2
---

<a id="Steps"></a>
<a id="steps"></a>
<a id="Steps"></a>
<a id="steps"></a>
# 步骤

“步骤”选项卡是配置场景大部分内容的地方。

每个步骤都代表场景中的一个点，在这个点会执行某个动作。动作可以是：

 - 向用户显示一条消息（带文本转语音音频）
 - 配置 Autopilot
 - 显示一个 UI 辅助提示，在用户屏幕上闪烁某个特定按钮。

<a id="The Timeline"></a>
<a id="the timeline"></a>
<a id="the-timeline"></a>
<a id="The%20Timeline"></a>
<a id="the%20timeline"></a>
<a id="The Timeline"></a>
<a id="the timeline"></a>
<a id="the-timeline"></a>
<a id="The%20Timeline"></a>
<a id="the%20timeline"></a>
## 时间轴

时间轴是 Steps 选项卡顶部的部分。这里会显示你**所有现有的步骤**，并且可以轻松添加新步骤。你可以执行以下操作：

 - **选择步骤：** 只需在时间轴中点按该步骤
 - **添加新步骤：** 可以按 `Add Step` 在末尾添加，或者右键在其他步骤之间插入一步。
 - **删除步骤：** 右键并按 Delete。
 - **复制步骤：** 右键并按 Duplicate。这会复制所有消息、完成条件等内容。
 - **重新排序步骤：** 按住任意步骤进入类似 iPhone 的“抖动模式”。完成后重新排列，并按 `Stop Ordering`。

<a id="When does a step advance to the next one?"></a>
<a id="when does a step advance to the next one?"></a>
<a id="when-does-a-step-advance-to-the-next-one?"></a>
<a id="when-does-a-step-advance-to-the-next-one"></a>
<a id="When%20does%20a%20step%20advance%20to%20the%20next%20one%3F"></a>
<a id="when%20does%20a%20step%20advance%20to%20the%20next%20one%3F"></a>
<a id="when-does-a-step-advance-to-the-next-one%3F"></a>
<a id="When does a step advance to the next one?"></a>
<a id="when does a step advance to the next one?"></a>
<a id="when-does-a-step-advance-to-the-next-one?"></a>
<a id="when-does-a-step-advance-to-the-next-one"></a>
<a id="When%20does%20a%20step%20advance%20to%20the%20next%20one%3F"></a>
<a id="when%20does%20a%20step%20advance%20to%20the%20next%20one%3F"></a>
<a id="when-does-a-step-advance-to-the-next-one%3F"></a>
## 步骤何时推进到下一步？

主要有 3 种方式：
 
  - 当 Briefing Message 已由文本转语音系统完整读出后
  - 当满足某个完成条件时
  - 当在步骤配置中设置了超时

<a id="Step Configuration"></a>
<a id="step configuration"></a>
<a id="step-configuration"></a>
<a id="Step%20Configuration"></a>
<a id="step%20configuration"></a>
<a id="Step Configuration"></a>
<a id="step configuration"></a>
<a id="step-configuration"></a>
<a id="Step%20Configuration"></a>
<a id="step%20configuration"></a>
## 步骤配置

在每个步骤内部，你会看到以下选项卡和配置项：

<a id="State"></a>
<a id="state"></a>
<a id="State"></a>
<a id="state"></a>
#### 状态

用于配置模拟器或飞机的状态。举个例子，假设我们要在航向 90 度时启用 HDG autopilot。

步骤 1

: 点按 Add Action

步骤 2

: 在 `States` 列表中，搜索 `Systems → Autopilot → Hdg → On` 状态。将其设为 `true` 以启用它。

步骤 3

: 在 `States` 列表中，搜索 `Systems → Autopilot → Hdg → Target` 状态。将其设为 `1.5708` 来设置航向。注意：目前航向使用弧度表示，我们正在改进这一点。

步骤 4

: 点按每个状态旁边的对勾以保存更改。


<a id="Briefing Message"></a>
<a id="briefing message"></a>
<a id="briefing-message"></a>
<a id="Briefing%20Message"></a>
<a id="briefing%20message"></a>
<a id="Briefing Message"></a>
<a id="briefing message"></a>
<a id="briefing-message"></a>
<a id="Briefing%20Message"></a>
<a id="briefing%20message"></a>
#### 简报消息

这是用户到达此步骤时会看到的消息。可用于提供指令，或为用户提供额外背景信息。

在你上传更改并编辑简报消息之后，可以听到每种语言对应的音频。

<a id="Completion Conditions"></a>
<a id="completion conditions"></a>
<a id="completion-conditions"></a>
<a id="Completion%20Conditions"></a>
<a id="completion%20conditions"></a>
<a id="Completion Conditions"></a>
<a id="completion conditions"></a>
<a id="completion-conditions"></a>
<a id="Completion%20Conditions"></a>
<a id="completion%20conditions"></a>
#### 完成条件

如果满足这些条件，场景将推进到下一步。

完成条件有两种类型：

 - **状态条件：** 其工作方式与 `State` 选项卡相同，只不过它是在查找某个值是否与状态匹配。
 - **位置条件：** 在这里，飞机需要位于某个纬度和经度的半径范围内。如果你希望用户飞经某个特定区域，可以使用这个条件。

需要注意的事项：
 - **容差：** 如果该值是数字，你可以提供一个容差作为误差范围。也就是说，如果你期望值为 100，但容差为 25，我们会接受 75 到 125 之间的任何状态。
 - **最短时间：** 状态必须在这段时间内一直符合这些值。这样我们就不会立即推进到下一步。我们建议 5 秒。

<a id="Configuration"></a>
<a id="configuration"></a>
<a id="Configuration"></a>
<a id="configuration"></a>
#### 配置

如果用户没有完成所需条件，可以在这里设置超时。例如，如果他们忽略了指令，你可以在 10 秒后推进到下一步。

**Continue button title** 允许你自定义 Mission Brief 中用户可以点按以继续到下一步的按钮标题。

**Wait for confirmation** 要求用户点按 mission brief，否则场景会一直等待输入。