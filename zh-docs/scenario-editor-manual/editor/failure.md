---
id: failure
title: 失败条件
meta: Scenario Editor 工具快速概览
order: 2
---

<a id="Failure Conditions"></a>
<a id="failure conditions"></a>
<a id="failure-conditions"></a>
<a id="Failure%20Conditions"></a>
<a id="failure%20conditions"></a>
<a id="Failure Conditions"></a>
<a id="failure conditions"></a>
<a id="failure-conditions"></a>
<a id="Failure%20Conditions"></a>
<a id="failure%20conditions"></a>
# 失败条件

失败条件用于在用户离开某些参数时使场景失败。例如，你可以在以下情况判定失败：

 - 用户在直线平飞教程中把机头压向地面。
 - 用户使飞机失速
 - 等等

你可以添加任意数量的失败条件，每个条件都可以有自己特定的消息显示给用户。

<a id="Example"></a>
<a id="example"></a>
<a id="Example"></a>
<a id="example"></a>
## 示例

例如，我们来在用户失速时让场景失败。

步骤 1

: 点击“添加失败条件”

步骤 2

: 在 `States` 列表中，搜索 `Is Stalling` 状态。将其设置为 `equals` 和 `true` 以启用它。

步骤 3

: 设置一条要显示给用户的消息，例如“你使飞机失速了”

步骤 3

: 点击每个状态旁边的勾选标记以保存更改。