<a id="Infinite Flight Documentation"></a>
<a id="infinite flight documentation"></a>
<a id="infinite-flight-documentation"></a>
<a id="Infinite%20Flight%20Documentation"></a>
<a id="infinite%20flight%20documentation"></a>
<a id="Infinite Flight Documentation"></a>
<a id="infinite flight documentation"></a>
<a id="infinite-flight-documentation"></a>
<a id="Infinite%20Flight%20Documentation"></a>
<a id="infinite%20flight%20documentation"></a>
# Infinite Flight 文档



<a id="Overview"></a>
<a id="overview"></a>
<a id="Overview"></a>
<a id="overview"></a>
## 概述



我们的文档使用 Markdown 编写，托管在 GitHub 上，并通过我们网站上的文档组件进行渲染。为便于组织，所有指南都被划分为不同的类别，定义如下：

| 类别 | 定义                                                   | 仓库定义 |
| -------- | ------------------------------------------------------------ | --------------------- |
| 指南    | 将显示在导航侧边栏中的主类别 | 文件夹                |
| 部分    | 每个指南内会包含一系列部分，在导航侧边栏中点击某个指南时会显示这些部分 | 子文件夹            |
| 页面     | 页面位于某个部分内，涵盖特定主题，同样可通过在导航侧边栏中点击某个部分来访问，以显示该部分下包含的所有页面 | 文件                  |



> 关于 markdown，一个有用的参考是 [Markdown Cheatsheet]( https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet )



<a id="Community Contribution"></a>
<a id="community contribution"></a>
<a id="community-contribution"></a>
<a id="Community%20Contribution"></a>
<a id="community%20contribution"></a>
<a id="Community Contribution"></a>
<a id="community contribution"></a>
<a id="community-contribution"></a>
<a id="Community%20Contribution"></a>
<a id="community%20contribution"></a>
## 社区贡献

社区可以通过点击每个指南页面底部的 “Contribute on GitHub” 链接来为任意指南做出贡献。在对指南进行任何更改时，应同时查阅 IFC 上的公告以及本 ReadMe 文档，以确保符合要求。 



>  当前不支持本地化（即提供其他语言版本的指南），因此目前只接受美式英文编辑



<a id="Setting up an Editing Environment"></a>
<a id="setting up an editing environment"></a>
<a id="setting-up-an-editing-environment"></a>
<a id="Setting%20up%20an%20Editing%20Environment"></a>
<a id="setting%20up%20an%20editing%20environment"></a>
<a id="Setting up an Editing Environment"></a>
<a id="setting up an editing environment"></a>
<a id="setting-up-an-editing-environment"></a>
<a id="Setting%20up%20an%20Editing%20Environment"></a>
<a id="setting%20up%20an%20editing%20environment"></a>
## 搭建编辑环境



<a id="Programs to Install"></a>
<a id="programs to install"></a>
<a id="programs-to-install"></a>
<a id="Programs%20to%20Install"></a>
<a id="programs%20to%20install"></a>
<a id="Programs to Install"></a>
<a id="programs to install"></a>
<a id="programs-to-install"></a>
<a id="Programs%20to%20Install"></a>
<a id="programs%20to%20install"></a>
### 需要安装的程序

需要以下程序：

- [Typora]( https://www.typora.io/ ) 用于 Markdown 编辑
- [GitHub Desktop]( https://desktop.github.com/ ) 用于与 GitHub 同步更改



<a id="GitHub Set Up"></a>
<a id="github set up"></a>
<a id="github-set-up"></a>
<a id="GitHub%20Set%20Up"></a>
<a id="github%20set%20up"></a>
<a id="GitHub Set Up"></a>
<a id="github set up"></a>
<a id="github-set-up"></a>
<a id="GitHub%20Set%20Up"></a>
<a id="github%20set%20up"></a>
### GitHub 设置

可按以下步骤设置 GitHub：



步骤 1

: 为此仓库创建一个 `Fork`。这会创建一个仓库副本，允许你在将更改合并回主仓库之前先进行修改。该仓库将命名为 `[你的 GitHub 用户名]/infiniteflight-docs`

![image-20191119155543647](../_images/image-20191119155543647.png)



步骤 2

: 将你的 `Fork` 克隆到本地电脑。选择你分叉后的仓库（此处为 `carmichaelalonso/infiniteflight-docs`），然后点击底部的 “Clone”。设置你偏好的 `local path`，即仓库保存在本地电脑上的位置，默认选项为 `Documents\GitHub\infiniteflight-docs`

![image-20191119155947062](../_images/image-20191119155947062.png)

<a id="Typora Set Up"></a>
<a id="typora set up"></a>
<a id="typora-set-up"></a>
<a id="Typora%20Set%20Up"></a>
<a id="typora%20set%20up"></a>
<a id="Typora Set Up"></a>
<a id="typora set up"></a>
<a id="typora-set-up"></a>
<a id="Typora%20Set%20Up"></a>
<a id="typora%20set%20up"></a>
### Typora 设置

可按以下步骤设置 Typora：



步骤 1

: 在 Typora 中打开已克隆的文件夹

![image-20191119160444608](../_images/image-20191119160444608.png)

​	

步骤 2

: 在这种情况下，选择 `Documents\GitHub\infiniteflight-docs` 文件夹，它会显示为如下所示

​	![image-20191119160558562](../_images/image-20191119160558562.png)



步骤 3

: 切换 Tree View。Tree View 允许你按仓库中的章节结构查看所有文件。选择任意文件即可打开，它会显示在右侧编辑窗格中

![image-20191119160941433](../_images/image-20191119160941433.png)

步骤 3

: 开始编写，并参考下方的样式指南。你也可以在编辑窗格中右键以选择格式选项，或插入特定的 Markdown 元素



步骤 4

: 定期保存文件，并在推送到 GitHub 前保存一次。可使用 `Ctrl + s` 或 `File -> Save`。



<a id="Creating a New Guide"></a>
<a id="creating a new guide"></a>
<a id="creating-a-new-guide"></a>
<a id="Creating%20a%20New%20Guide"></a>
<a id="creating%20a%20new%20guide"></a>
<a id="Creating a New Guide"></a>
<a id="creating a new guide"></a>
<a id="creating-a-new-guide"></a>
<a id="Creating%20a%20New%20Guide"></a>
<a id="creating%20a%20new%20guide"></a>
### 创建新指南

步骤 1

: 右键单击 `infiniteflight-docs` 文件夹



步骤 2

: 创建一个 `New Folder`



步骤 3

: 名称必须与指南名称一致，全部使用小写，空格使用 `-` 替代



<a id="Creating a New Section"></a>
<a id="creating a new section"></a>
<a id="creating-a-new-section"></a>
<a id="Creating%20a%20New%20Section"></a>
<a id="creating%20a%20new%20section"></a>
<a id="Creating a New Section"></a>
<a id="creating a new section"></a>
<a id="creating-a-new-section"></a>
<a id="Creating%20a%20New%20Section"></a>
<a id="creating%20a%20new%20section"></a>
### 创建新部分

步骤 1

: 右键单击 `guide` 文件夹



步骤 2

: 创建一个 `New Folder`



步骤 3

: 名称必须与部分名称一致，全部使用小写，空格使用 `-` 替代



<a id="Creating a New Page"></a>
<a id="creating a new page"></a>
<a id="creating-a-new-page"></a>
<a id="Creating%20a%20New%20Page"></a>
<a id="creating%20a%20new%20page"></a>
<a id="Creating a New Page"></a>
<a id="creating a new page"></a>
<a id="creating-a-new-page"></a>
<a id="Creating%20a%20New%20Page"></a>
<a id="creating%20a%20new%20page"></a>
### 创建新页面

步骤 1

: 右键单击某个部分文件夹



步骤 2

: 创建一个 `New File`



步骤 3

: 名称必须与页面名称一致，全部使用小写，空格使用 `-` 替代



<a id="Pushing to GitHub"></a>
<a id="pushing to github"></a>
<a id="pushing-to-github"></a>
<a id="Pushing%20to%20GitHub"></a>
<a id="pushing%20to%20github"></a>
<a id="Pushing to GitHub"></a>
<a id="pushing to github"></a>
<a id="pushing-to-github"></a>
<a id="Pushing%20to%20GitHub"></a>
<a id="pushing%20to%20github"></a>
### 推送到 GitHub

步骤 1

: 确保你已同步最新更改。点击顶部菜单栏中的 `Fetch Origin`，查看是否有新更改

![image-20191119161354615](../_images/image-20191119161354615.png)



> 如果有更改，它会在 `Pull Changes` 旁显示提交数量。请在继续之前先执行此操作（如果存在文件冲突，这可能会产生一些错误，如有需要，请联系 Cam 寻求帮助）



步骤 2

: 提交你的更改。确保所有已更改的文件都被选中（参见上图左侧的复选框）。编写一段更改摘要（应简短但有信息量，以便我们将来查看文件历史时能快速理解），然后点击 `Commit`

![image-20191119161735977](../_images/image-20191119161735977.png)



步骤 3

: 推送你的更改。点击 `Push origin` 将提交推送到 GitHub

![image-20191119162015898](../_images/image-20191119162015898.png)



<a id="GitHub Definitions"></a>
<a id="github definitions"></a>
<a id="github-definitions"></a>
<a id="GitHub%20Definitions"></a>
<a id="github%20definitions"></a>
<a id="GitHub Definitions"></a>
<a id="github definitions"></a>
<a id="github-definitions"></a>
<a id="GitHub%20Definitions"></a>
<a id="github%20definitions"></a>
### GitHub 定义

| GitHub 术语 | 定义                                                   |
| ------------------ | ------------------------------------------------------------ |
| Commit             | 保存到本地仓库的一组更改。可以包含多个文件的修改、添加、删除等。 |
| Pushing a commit   | 将本地仓库与 GitHub 同步。其本质上意味着把你的更改推送到我们的公共仓库 |



<a id="Style Guide"></a>
<a id="style guide"></a>
<a id="style-guide"></a>
<a id="Style%20Guide"></a>
<a id="style%20guide"></a>
<a id="Style Guide"></a>
<a id="style guide"></a>
<a id="style-guide"></a>
<a id="Style%20Guide"></a>
<a id="style%20guide"></a>
## 样式指南

有关如何为新页面设置样式的示例，请参见 `_template.md`。



<a id="Language"></a>
<a id="language"></a>
<a id="Language"></a>
<a id="language"></a>
### 语言

文档必须使用美式英文。



<a id="Metadata"></a>
<a id="metadata"></a>
<a id="Metadata"></a>
<a id="metadata"></a>
### 元数据

每个文件顶部都必须包含一个元数据部分，其样式必须如下：



| 元数据 | 描述                                                  |
| -------- | ------------------------------------------------------------ |
| id:      | 与文件名相同（例如 `"flight-planning"`）               |
| title:   | 与文件名相同，不过它会显示在导航栏中，因此可按需要使用空格和大写字母（例如 `"Flight Planning"`） |
| meta:    | 对页面内容的描述，也用于 SEO |
| order:   | 该页面在该部分中显示的顺序（例如 `"2"`） |
| hidden:  | 如果该页面需要隐藏，仅供 IFC 上对应群组访问，则应添加 `"true"` |



**示例：** 

```markdown
id: flight-planning
title: Flight Planning
meta: 了解如何在 Infinite Flight 中为飞行做准备。
order: 2
```



<a id="Headings"></a>
<a id="headings"></a>
<a id="Headings"></a>
<a id="headings"></a>
### 标题

可通过在文本前放置一系列 `#` 符号来添加标题：

| 标题类型 | Markdown 格式 | 用途                                                          |
| ------------ | ------------------- | ------------------------------------------------------------ |
| 一级标题    | #                   | 用于页面名称                                |
| 二级标题    | ##                   | 用于页面内所需的任何副标题，以将内容拆分为逻辑部分 |
| 三级标题    | ###                 | 在手册中为每个段落添加编号参考的一系列数字/字母（不用于指南） |



**指南示例：**

```markdown
# 飞行计划
```



```markdown
## 重量与平衡
```



**手册示例：**

> 手册中的章节将按顺序编号，并在章节名称中包含这一编号（例如 1 Introduction、2 Ground 等）。每个章节内的页面也会在章节编号后按顺序编号（例如 2.1 Runway Selection and Pushback、2.2 Taxi and Use of Give Way 等）。在每个页面中，每个段落也会在章节编号和页面编号之后按顺序编号（例如 2.1.1、2.1.2、2.1.3 等）。



```markdown
# 2.1 Runway Selection & Pushback
```



```markdown
## Runway Selection
```



```markdown
### 2.1.1
```



```markdown
### 2.1.2
```



```markdown
### 2.1.3
```



<a id="Emphasis"></a>
<a id="emphasis"></a>
<a id="Emphasis"></a>
<a id="emphasis"></a>
### 强调

可使用多种强调方式来吸引对特定内容的注意：



```markdown
Emphasis, aka italics, with *asterisks* or _underscores_.

Strong emphasis, aka bold, with **asterisks** or __underscores__.

Combined emphasis with **asterisks and _underscores_**.

Strikethrough uses two tildes. ~~Scratch this.~~
```



**示例：**

>强调，即斜体，使用 *asterisks* 或 _underscores_。
>
>强强调，即粗体，使用 **asterisks** 或 __underscores__。
>
>组合强调使用 **asterisks and _underscores_**。
>
>删除线使用两个波浪号。~~Scratch this.~~



<a id="Bullet Points"></a>
<a id="bullet points"></a>
<a id="bullet-points"></a>
<a id="Bullet%20Points"></a>
<a id="bullet%20points"></a>
<a id="Bullet Points"></a>
<a id="bullet points"></a>
<a id="bullet-points"></a>
<a id="Bullet%20Points"></a>
<a id="bullet%20points"></a>
### 项目符号

项目符号列表可用于列出信息块（应先用一句话描述该项目符号列表包含的内容，随后使用分号，再接项目符号列表，且不应使用句号）。

**示例：**

```markdown
临时飞行限制（Temporary Flight Restriction），简称 TFR，是一块已实施限制的空域。在现实中，这可能由多种因素造成，例如：

- 政府官员活动
- 自然灾害
- 或其他特殊事件
```



<a id="Blockquotes"></a>
<a id="blockquotes"></a>
<a id="Blockquotes"></a>
<a id="blockquotes"></a>
### 引用块

引用块用于 “notes”，使用以下 markdown：

```markdown
> 插入说明
```



**示例：**

> 插入说明



<a id="Step by Step Guides"></a>
<a id="step by step guides"></a>
<a id="step-by-step-guides"></a>
<a id="Step%20by%20Step%20Guides"></a>
<a id="step%20by%20step%20guides"></a>
<a id="Step by Step Guides"></a>
<a id="step by step guides"></a>
<a id="step-by-step-guides"></a>
<a id="Step%20by%20Step%20Guides"></a>
<a id="step%20by%20step%20guides"></a>
### 分步指南

分步指南用于展示一个流程及其完成方式。



**示例：**

```markdown
步骤 1
: 返回设备主屏幕并找到 Infinite Flight 图标

步骤 2
: 点击该图标
        
步骤 3
: 欢迎来到 Infinite Flight，祝你玩得愉快！
```

![image-20191119152902493](../_images/image-20191119152902493.png)



<a id="Hyperlinks"></a>
<a id="hyperlinks"></a>
<a id="Hyperlinks"></a>
<a id="hyperlinks"></a>
### 超链接

到指南其他部分的链接定义为 `/guide/guide-name/section-name/file-name`。

**示例：**

```markdown
有关更多信息，请参见 [android 安装指南](getting-started-guide/installing-the-app/android.md)。
```

> 有关更多信息，请参见 [android 安装指南](getting-started-guide/installing-the-app/android.md)。



到其他页面的链接，例如社区页面，使用该页面的 URL 定义。

**示例：**

```markdown
请参见 IFC 上的 [教程](https://community.infiniteflight.com/t/infinite-flight-faq/288495)。
```

>请参见 IFC 上的 [教程](https://community.infiniteflight.com/t/infinite-flight-faq/288495)。



手册中指向手册其他部分的任何链接都应始终引用 “heading 3”。

**示例：**

```markdown
*(见下方 [3.2.3](atc-manual/3.-tower/3.2-departures.md#3.2.3))*
```

>*(见下方 [3.2.3](atc-manual/3.-tower/3.2-departures.md#3.2.3))*



<a id="Images"></a>
<a id="images"></a>
<a id="Images"></a>
<a id="images"></a>
### 图片

图片需要包含在 `_images` 目录中，这样它们才会被推送到仓库，并在文档中通过相对路径引用（即 `_images/`，后跟图片名称）。此外，还需要提供 `Alternative Text`，用几个词概括图片内容，方便视力受限用户使用（因为屏幕阅读器可以朗读它）。如果图片不可用，它也会显示出来。

```markdown
![Alternative Text](../_images/image-20191119152902493.png "Alternative Text")
```

> ![Alternative Text](../_images/image-20191119152902493.png "Alternative Text")



步骤 1：

如果你使用 Typora，建议先粘贴一张图片，然后使用 `Copy Image To...` 功能（在粘贴图片时会显示，或通过右键单击图片显示）



![image-20191119154554666](../_images/image-20191119154554666.png)



步骤 2

: 确保路径以 `_images/` 开头



<a id="Tables"></a>
<a id="tables"></a>
<a id="Tables"></a>
<a id="tables"></a>
### 表格

表格用于使用以下 markdown 对任何数据进行制表：



```markdown
| 类别        | 飞机类型                  | 速度范围 (M) |
| --------------- | ------------------------------- | --------------- |
| 涡桨      | 例如 TBM-930、Dash-8 Q400 等   | .51 - .53       |
| 窄体喷气机 | 例如 CRJ、E-Jet、A320、B737 等 | .75 - .80       |
| 宽体喷气机   | 例如 A330、B777、MD-11 等      | .82 - .85       |
```



**示例：**

| 类别        | 飞机类型                  | 速度范围 (M) |
| --------------- | ------------------------------- | --------------- |
| 涡桨      | 例如 TBM-930、Dash-8 Q400 等   | .51 - .53       |
| 窄体喷气机 | 例如 CRJ、E-Jet、A320、B737 等 | .75 - .80       |
| 宽体喷气机   | 例如 A330、B777、MD-11 等      | .82 - .85       |



<a id="Hidden Section"></a>
<a id="hidden section"></a>
<a id="hidden-section"></a>
<a id="Hidden%20Section"></a>
<a id="hidden%20section"></a>
<a id="Hidden Section"></a>
<a id="hidden section"></a>
<a id="hidden-section"></a>
<a id="Hidden%20Section"></a>
<a id="hidden%20section"></a>
### 隐藏部分

可添加隐藏部分，以防页面加载时立即显示所有信息，读者可在需要时再打开。可使用以下 markdown 实现：



```markdown
+++ CYTZ (Toronto City Billy Bishop)

不允许大于 Dash-8 Q400 的飞机。禁止喷气式交通。较大的飞机必须备降。

| 参数 | 限制 |
| ---------- | ------------ |
| 类型       | NOTAM        |
| 状态     | ACTIVE       |
| 下限      | SFC          |
| 上限    | 10,000ft     |

+++

+++ EGKK (London Gatwick)

RWY 08L/26R 关闭。RWY08L/26R 仅可作为滑行道使用。

| 参数 | 限制 |
| ---------- | ------------ |
| 类型       | NOTAM        |
| 状态     | ACTIVE       |
| 下限      | SFC          |
| 上限    | 10,000ft     |

+++
```



**示例：**

+++ CYTZ (Toronto City Billy Bishop)

不允许大于 Dash-8 Q400 的飞机。禁止喷气式交通。较大的飞机必须备降。

| 参数 | 限制 |
| ---------- | ------------ |
| 类型       | NOTAM        |
| 状态       | ACTIVE       |
| 下限       | SFC          |
| 上限       | 10,000ft     |

+++



+++ EGKK (London Gatwick)

RWY 08L/26R 关闭。RWY08L/26R 仅可作为滑行道使用。

| 参数 | 限制 |
| ---------- | ------------ |
| 类型       | NOTAM        |
| 状态       | ACTIVE       |
| 下限       | SFC          |
| 上限       | 10,000ft     |

+++



<a id="FontAwesome Icons"></a>
<a id="fontawesome icons"></a>
<a id="fontawesome-icons"></a>
<a id="FontAwesome%20Icons"></a>
<a id="fontawesome%20icons"></a>
<a id="FontAwesome Icons"></a>
<a id="fontawesome icons"></a>
<a id="fontawesome-icons"></a>
<a id="FontAwesome%20Icons"></a>
<a id="fontawesome%20icons"></a>
### FontAwesome 图标

可使用 FontAwesome 图标，可在 [FontAwesome](https://fontawesome.com/icons) 中找到。例如，[Clipboard Check](https://fontawesome.com/icons/clipboard-check?style=solid) 图标的 class 属性为 `fas fa-clipboard-check`。在文档中使用时，请采用以下 markdown：

```markdown
:fa-clipboard-check:
```



<a id="Scenarios"></a>
<a id="scenarios"></a>
<a id="Scenarios"></a>
<a id="scenarios"></a>
### 场景

可通过用 `:::` 包裹内容来添加 HTML 容器（div）。场景通常包含在隐藏部分中，以确保明确哪些内容适用于该场景。对于场景，会使用 `scenario-heading` 和 `scenario` 来添加场景样式：

```markdown
::: scenario-heading
场景
:::

::: scenario
插入对该场景的简要描述。
:::
```



随后是带有类属性 `{.technique}` 和 `{.prosandcons}` 的表格。只要中间没有额外的段落断行，这样就能创建关联表格。它们会应用特殊的表格样式以便于查看：

```markdown
| 技巧 1                                                 |
| ------------------------------------------------------------|
| 1. 插入步骤 1 | 
| 2. 插入步骤 2 |
{.technique}
| 技巧 1                                                  | 优点还是缺点？                       |
| ------------------------------------------------------------ | --------------------------------- |
| :fa-check-circle: | 插入优点 |
| :fa-times-circle: | 插入缺点 |
{.prosandcons}
```



<a id="Task Lists"></a>
<a id="task lists"></a>
<a id="task-lists"></a>
<a id="Task%20Lists"></a>
<a id="task%20lists"></a>
<a id="Task Lists"></a>
<a id="task lists"></a>
<a id="task-lists"></a>
<a id="Task%20Lists"></a>
<a id="task%20lists"></a>
### 任务列表

任务列表可使用以下 markdown 添加：

```markdown
- [ ] 第一项
- [ ] 第二项
- [x] 第三项，默认已勾选
```



<a id="Special Page Properties"></a>
<a id="special page properties"></a>
<a id="special-page-properties"></a>
<a id="Special%20Page%20Properties"></a>
<a id="special%20page%20properties"></a>
<a id="Special Page Properties"></a>
<a id="special page properties"></a>
<a id="special-page-properties"></a>
<a id="Special%20Page%20Properties"></a>
<a id="special%20page%20properties"></a>
## 特殊页面属性

<a id="Hiding Pages from the Side Menu"></a>
<a id="hiding pages from the side menu"></a>
<a id="hiding-pages-from-the-side-menu"></a>
<a id="Hiding%20Pages%20from%20the%20Side%20Menu"></a>
<a id="hiding%20pages%20from%20the%20side%20menu"></a>
<a id="Hiding Pages from the Side Menu"></a>
<a id="hiding pages from the side menu"></a>
<a id="hiding-pages-from-the-side-menu"></a>
<a id="Hiding%20Pages%20from%20the%20Side%20Menu"></a>
<a id="hiding%20pages%20from%20the%20side%20menu"></a>
### 从侧边菜单隐藏页面

可隐藏单个页面，使其不显示在侧边菜单导航中，但仍可通过直接 URL 访问。这对于以下内容很有用：
- 内部文档页面
- 开发中的页面
- 不需要出现在主导航中的补充内容
- 仅在特定上下文中相关的特殊用途页面

要隐藏页面，请在 markdown 文件的 frontmatter 中添加 `hideFromSideMenu: true` 属性：

```markdown
---
id: your-page-id
title: Your Page Title
meta: Your page description
hideFromSideMenu: true
---
```

该页面仍可通过直接 URL 访问，并可从其他页面链接到，但不会出现在侧边栏导航中。

可作为起点使用的隐藏页面模板位于 `_hidden_page_template.md`。