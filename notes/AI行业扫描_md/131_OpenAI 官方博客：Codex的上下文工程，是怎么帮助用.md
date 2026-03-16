---
url: https://mp.weixin.qq.com/s/8xgKUybdmEO21QX8K1lAXw
title: "OpenAI 官方揭秘：Codex 是怎么一步步完成任务的"
description: "OpenAI 开发者团队把 Codex CLI 的「内核」给拆开了"
author: "OpenAI"
captured_at: "2026-03-09T03:36:39.419Z"
---

# OpenAI 官方揭秘：Codex 是怎么一步步完成任务的

刚刚，OpenAI 开发者团队发了一篇博客，**直接把 Codex CLI 的「内核」给拆开了。**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/M3PrhSUICnFaLluanJarZfwhBQBfVf4ZjjGWA7RGQxu3wqI9keAqC0Xlgdsia2a0M2icegYBiaKUH6fdHUOswW64A/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

文章完整讲解了从用户输入到最终响应的全过程，包括 prompt 构建、模型推理、工具调用、上下文管理等核心细节。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/M3PrhSUICnFaLluanJarZfwhBQBfVf4ZnVHF0SWV9z9QT8SwPwZMsicxE8T8XxOz8Lt6CkHcBuIveyRCMIPnxXA/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

对于想了解 AI 编程助手底层机制的开发者、正在构建自己 Agent 系统的工程师、以及对 Codex 感兴趣的用户来说，本文值得一读。

### 全文如下

你有没有想过，当你给 Codex 发一条指令，到它给你返回结果之间，到底发生了什么？

每一轮对话都会经历：**组装输入、运行推理、执行工具、把结果喂回上下文**。

如此循环，直到任务完成。

这是 OpenAI 关于 Codex 技术揭秘系列的第一篇，且 OpenAI 承诺后续还会有更多内容放出。

## 什么是 Agent Loop

Agent Loop（智能体循环）是 Codex CLI 的核心逻辑，**负责协调用户、模型和工具之间的交互**。

简单来说，流程是这样的：

![Agent loop diagram](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Agent loop diagram

Agent 接收用户的**输入**，把它组装成发给模型的指令（也就是 prompt）。

下一步是**推理**（inference）：把 prompt 发给模型，让它生成响应。在推理过程中，文本 prompt 首先被转换成一串 token（整数索引），然后模型基于这些 token 采样，产生新的 token 序列。

输出的 token 再转回文本，就是模型的响应。因为 token 是逐个生成的，所以很多 LLM 应用都支持流式输出。你能看到回答一个字一个字蹦出来。

推理结束后，模型要么（1）直接给出最终答案，要么（2）请求执行一个**工具调用**（比如「跑一下 `ls` 命令然后告诉我结果」）。如果是后者，Agent 就去执行工具，把输出拼到原来的 prompt 后面，然后重新查询模型。

**这个过程会一直循环**，直到模型不再请求工具调用，而是产出一条给用户的消息（在 OpenAI 的术语里叫 assistant message）。

这条消息可能直接回答了用户的问题，也可能是向用户追问。

从**用户输入**到 **Agent 响应**，这个过程叫做一「轮」对话（turn）。在 Codex 里叫「thread」。

虽然是一轮对话，但可能包含多次「模型推理 → 工具调用」的迭代。

![Multi-turn agent loop](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Multi-turn agent loop

每当用户向已有对话发送新消息时，之前的对话历史（包括之前的消息和工具调用）都会作为新一轮的 prompt 的一部分。

**这意味着对话越长，prompt 也越长。**

这很关键，因为每个模型都有**上下文窗口**（context window），也就是单次推理能处理的最大 token 数。注意这个窗口包括输入和输出的 token。

一个 Agent 可能在一轮对话里调用几百次工具，很容易就把上下文撑爆了。

所以，**上下文窗口管理**是 Agent 的重要职责之一。

## 模型推理

Codex CLI 通过向 Responses API 发送 HTTP 请求来运行模型推理。

Codex CLI 使用的 Responses API 端点是**可配置的**，所以它可以兼容任何实现了 Responses API 的端点：

-   使用 ChatGPT 登录时，端点是 `https://chatgpt.com/backend-api/codex/responses`

-   使用 API key 认证时，端点是 `https://api.openai.com/v1/responses`

-   使用 `--oss` 参数跑 gpt-oss 时（配合 ollama 0.13.4+ 或 LM Studio 0.3.39+），默认用本地的 `http://localhost:11434/v1/responses`

-   也可以用 Azure 等云服务商托管的 Responses API

### 构建初始 Prompt

作为用户，你不需要自己写完整的 prompt。

你只需要在请求里指定各种输入，Responses API 服务器会决定怎么把这些信息组装成模型能理解的 prompt。

你可以把 prompt 想象成一个「列表」。

初始 prompt 里的每个条目都有一个 **role**，表示这段内容的权重高低，从高到低依次是：`system`、`developer`、`user`、`assistant`。

Responses API 接受的 JSON 里有很多参数，最关键的是这三个：

-   **`instructions`**：插入到模型上下文的 system（或 developer）消息

-   **`tools`**：模型可以调用的工具列表

-   **`input`**：发给模型的文本、图片或文件输入列表

在 Codex 里，`instructions` 字段来自 `~/.codex/config.toml` 里的 `model_instructions_file`，如果没配置，就用模型自带的 `base_instructions`。

不同模型的指令文件打包在 CLI 里（比如 `gpt-5.2-codex_prompt.md`）。

`tools` 字段是一个工具定义列表，包括 Codex CLI 自带的工具、Responses API 提供的工具，以及用户通过 MCP server 配置的工具：

```
[
```

`input` 字段是一个条目列表。在添加用户消息之前，Codex 会先插入以下内容：

**1\. 一条 `role=developer` 的消息**，描述沙箱环境，但**仅适用于 Codex 自带的 `shell` 工具**。也就是说，MCP server 提供的工具不受 Codex 沙箱保护，需要自行实现安全机制。

这条消息用模板生成，核心内容来自打包在 CLI 里的 Markdown 文件（如 `workspace_write.md` 和 `on_request.md`）：

```
<permissions instructions>
```

**2.（可选）一条 `role=developer` 的消息**，内容是用户 `config.toml` 里的 `developer_instructions`。

**3.（可选）一条 `role=user` 的消息**，即「用户指令」。这不是来自单一文件，而是从多个来源聚合而来。越具体的指令出现得越靠后：

-   `$CODEX_HOME` 目录下的 `AGENTS.override.md` 和 `AGENTS.md` 内容

-   从 Git/项目根目录到当前目录的每个文件夹里（受 32 KiB 限制），查找 `AGENTS.override.md`、`AGENTS.md` 或 `project_doc_fallback_filenames` 指定的文件

-   如果配置了 skills：

-   一段关于 skills 的简短说明

-   每个 skill 的元数据

-   关于如何使用 skills 的说明

**4\. 一条 `role=user` 的消息**，描述 Agent 当前运行的本地环境，包括当前工作目录和用户的 shell：

```
<environment_context>
```

上述计算完成后，Codex 把用户消息追加到 `input` 里，开始对话。

每个 `input` 元素都是一个 JSON 对象，包含 `type`、`role` 和 `content`：

```
{
```

Codex 构建好完整的 JSON 后，就向 Responses API 发送 HTTP POST 请求（带上 `Authorization` header，以及配置中指定的其他 header 和参数）。

当 OpenAI 的 Responses API 服务器收到请求后，会按如下方式从 JSON 构建 prompt：

![Snapshot 1](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Snapshot 1

可以看到，**前三项的顺序由服务器决定，而非客户端**。

不过在这三项中，只有 system message 的内容也由服务器控制，`tools` 和 `instructions` 都是客户端决定的。之后是 JSON 里的 `input`，构成完整的 prompt。

有了 prompt，就可以采样模型了。

### 第一轮对话

向 Responses API 发送的 HTTP 请求启动了 Codex 对话的第一「轮」。服务器以 Server-Sent Events（SSE）流的形式返回响应。每个事件的 `data` 是一个 JSON，`type` 以 `response` 开头，可能像这样：

```
data: {"type":"response.reasoning_summary_text.delta","delta":"ah ", ...}
```

Codex 消费这些事件流，把它们重新发布为内部事件对象供客户端使用。像 `response.output_text.delta` 这样的事件用来支持 UI 的流式显示，而 `response.output_item.added` 这样的事件会被转换成对象，追加到后续 Responses API 调用的 `input` 里。

假设第一次请求返回了两个 `response.output_item.done` 事件：一个 `type=reasoning`，一个 `type=function_call`。当我们再次查询模型时，这些事件必须在 `input` 里体现出来：

```
[
```

后续查询的 prompt 会变成这样：

![Snapshot 2](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Snapshot 2

注意，**旧 prompt 是新 prompt 的精确前缀**。这是故意设计的,这样后续请求就能利用 **prompt 缓存**，大幅提升效率（后面会讲）。

回顾我们最开始的 Agent Loop 图，推理和工具调用之间可能有很多次迭代。Prompt 会不断增长，直到我们最终收到一条 assistant message，标志着这一轮结束：

```
data: {"type":"response.output_text.done","text": "I added a diagram to explain...", ...}
```

在 Codex CLI 里，我们把 assistant message 展示给用户，并聚焦到输入框，表示现在轮到用户继续对话了。如果用户回复，上一轮的 assistant message 和用户的新消息都要追加到新请求的 `input` 里：

```
[
```

因为是在继续对话，发给 Responses API 的 `input` 长度会持续增加：

![Snapshot 3](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

Snapshot 3

## 性能考量

你可能会问：「等等，这个 Agent Loop 在整个对话过程中发送的 JSON 量不是**平方级**增长吗？」

没错。虽然 Responses API 支持可选的 `previous_response_id` 参数来缓解这个问题，但 Codex 目前不用它，**主要是为了保持请求完全无状态，以及支持零数据保留（ZDR）配置**。

避免使用 `previous_response_id` 简化了 Responses API 提供方的实现，因为每个请求都是无状态的。这也让支持 ZDR 客户变得简单：存储支持 `previous_response_id` 所需的数据会与 ZDR 相矛盾。ZDR 客户仍然可以受益于之前轮次的专有推理消息，因为相关的 `encrypted_content` 可以在服务器端解密。（OpenAI 保留 ZDR 客户的解密密钥，但不保留他们的数据。）

一般来说，**采样模型的成本远超网络传输成本**，所以采样是效率优化的主要目标。这就是为什么 **prompt 缓存**如此重要：它能让我们复用之前推理调用的计算。

当缓存命中时，**采样模型是线性的而非平方级的**。

OpenAI 的 prompt 缓存文档这样解释：

> 缓存命中只对 prompt 内精确的前缀匹配有效。要实现缓存收益，把静态内容（如指令和示例）放在 prompt 开头，把可变内容（如用户特定信息）放在末尾。图片和工具也是如此，它们必须在不同请求之间完全一致。

考虑到这点，哪些操作可能导致 Codex 的「缓存未命中」呢？

-   在对话中途改变可用的 `tools`

-   改变 Responses API 请求的目标 `model`（实际上这会改变原始 prompt 的第三项，因为它包含模型特定的指令）

-   改变沙箱配置、审批模式或当前工作目录

Codex 团队在引入可能影响 prompt 缓存的新功能时必须谨慎。举个例子，最初支持 MCP 工具时有一个 bug，**工具枚举顺序不一致**，导致缓存未命中。MCP 工具特别棘手，因为 MCP server 可以通过 `notifications/tools/list_changed` 通知动态改变工具列表。在长对话中途响应这个通知可能导致昂贵的缓存未命中。

在可能的情况下，我们通过在 `input` 后面**追加新消息**来处理对话中途的配置变更，而不是修改之前的消息：

-   如果沙箱配置或审批模式变更，我们插入一条新的 `role=developer` 消息，格式与原来的 `<permissions instructions>` 相同

-   如果当前工作目录变更，我们插入一条新的 `role=user` 消息，格式与原来的 `<environment_context>` 相同

我们竭尽全力确保缓存命中以提升性能。还有另一个关键资源需要管理：**上下文窗口**。

我们避免上下文窗口耗尽的通用策略是：当 token 数超过某个阈值时，**压缩对话**。具体来说，我们用一个更小的、能代表原对话的条目列表替换 `input`，让 Agent 能带着对已发生内容的理解继续工作。

早期的压缩实现需要用户手动执行 `/compact` 命令，它会用已有对话加上自定义的摘要指令查询 Responses API，然后用返回的 assistant message 作为后续对话轮次的新 `input`。

后来，Responses API 演进出了专门的 `/responses/compact` 端点来更高效地执行压缩。它返回一个条目列表，可以替代之前的 `input` 继续对话，同时释放上下文窗口。这个列表包含一个特殊的 `type=compaction` 条目，带有不透明的 `encrypted_content`，保留了模型对原始对话的隐式理解。现在，当超过 `auto_compact_limit` 时，Codex 会自动使用这个端点压缩对话。

## 后续计划

OpenAI 介绍了 Codex 的 Agent Loop，并详细讲解了 Codex 在查询模型时如何构建和管理上下文。同时也分享了一些对任何在 Responses API 上构建 Agent Loop 的人都适用的实践考量和最佳实践。

虽然 Agent Loop 是 Codex 的基础，但这只是开始。在后续文章中，他们会深入探讨 CLI 的架构、工具使用的实现，以及 Codex 的沙箱模型。

**相关链接：**

-   原文博客：https://openai.com/index/unrolling-the-codex-agent-loop/

-   Codex CLI 开源仓库：https://github.com/openai/codex

-   Codex 开发者文档：https://developers.openai.com/codex/cli

-   Responses API 文档：https://platform.openai.com/docs/api-reference/responses