# GUI 将死，CLI 才是一切

Original J0hn J0hn | AGI Hunt

GUI 赢了上一个十年，但它的时代快到头了。

CLI 正在赢下一个十年，只不过这次，CLI 的用户不再是开发者，而是 Agent。

这个判断听起来有点反直觉，毕竟 CLI 是计算机世界里最古老的交互方式之一了。但回头看这半年的趋势，Claude Code 是 CLI，Codex 是 CLI，OpenClaw 也是 CLI。

Agent 操控计算机的方式，正在从「看屏幕点鼠标」转向「读文档敲命令」。

## CLI-Anything

有个项目叫 CLI-Anything，来自香港大学的 HKUDS 团队，已经拿到了 15000 颗星。

该项目并不复杂：给任意软件自动生成一套 CLI 接口，让 AI Agent 能直接用命令行操控 GIMP、Blender、Audacity、LibreOffice……几乎你能想到的桌面软件，它都能包一层。

## 为什么是 CLI

GUI 本质上是一个翻译层。人类花了 40 年给计算机套上图形界面，是因为人类不擅长记命令。

但 Agent 不需要图形界面。Agent 天生就是说命令行语言的。你让它点按钮、拖滑块、填表单……那是在强迫一个天生会说 API 的实体，去学一门它根本不需要的语言。

CLI-Anything 做的事情，本质上就是把那层「翻译层」给剥掉了，让 Agent 直接和软件的底层对话。

## 怎么做到的

CLI-Anything 的实现分七步，全自动：扫描源码，把 GUI 操作映射到底层 API。设计命令结构和状态模型。用 Python Click 框架生成 CLI。自动写测试。自动写文档。最后打包安装到系统 PATH。

整个过程只需要一条命令：`/cli-anything:cli-anything ./gimp`

生成出来的 CLI 有几个特点：每个命令都支持 `--json` 输出；每个命令都有 `--help`；还有 undo/redo 和持久化的项目状态。

目前已经通过测试的软件有 GIMP、Blender、OBS Studio、Audacity、Kdenlive、Inkscape、Draw.io、LibreOffice、Zoom 等等，1508 个测试全部通过。

## 组合拳

与其让 Agent 在 context 里塞满工具描述（MCP 的做法），不如让它直接写代码调用。

而 CLI + Skill 的组合，其实是这个思路的自然延伸：

- Skill 是知识，是「怎么干」
- CLI 是接口，是「用什么干」

二者组合起来，Agent 只需要读一份简短的 SKILL.md（几百 tokens），就知道该调哪些命令、参数怎么传、结果怎么解析。

## 真正的问题

当 Agent 能直接操控 Blender 渲染、Audacity 处理音频、LibreOffice 生成 PDF 的时候……权限边界在哪里，谁来兜底呢？

CLI 解决的是 Agent「能不能干」的问题。但「该不该干」「谁说了算」，这些问题才刚刚浮出水面。

## 接下来会怎样

CLI 会成为 Agent 时代的标准交互协议。不是因为 CLI 本身有多先进。恰恰相反，它是计算机最古老的交互方式之一。但它天然适合 Agent：文本输入，结构化输出，可组合，可发现，确定性强。

人类花了 40 年给计算机加上 GUI 这层翻译层。现在 Agent 来了，它不需要这层翻译。

就像当年 USB 统一了硬件接口一样，CLI 正在成为 Agent 世界的「通用插口」。

---
Source: https://mp.weixin.qq.com/s/yBzf0CCj2FiJKQyK9j2t7A?scene=1
