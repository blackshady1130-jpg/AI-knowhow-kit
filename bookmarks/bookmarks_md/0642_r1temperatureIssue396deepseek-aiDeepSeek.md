---
url: https://github.com/deepseek-ai/DeepSeek-R1/issues/396
title: "r1的temperature参数是否生效？ · Issue #396 · deepseek-ai/DeepSeek-R1"
description: "官方文档（https://api-docs.deepseek.com/zh-cn/guides/reasoning_model ）提到r1不支持temperature参数， 但仓库readme对于r1的评估又有temperature值说明使用的0.6评估。 经测试发现，传不同的temperature确实有不一样的回答影响（长度、回答质量）。"
captured_at: "2026-03-08T12:44:15.098Z"
---

# r1的temperature参数是否生效？ · Issue #396 · deepseek-ai/DeepSeek-R1

[deepseek-ai](https://github.com/deepseek-ai) / **[DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1)** Public

-   [Notifications](https://github.com/login?return_to=%2Fdeepseek-ai%2FDeepSeek-R1) You must be signed in to change notification settings
-   [Fork 11.8k](https://github.com/login?return_to=%2Fdeepseek-ai%2FDeepSeek-R1)
-   [Star 91.9k](https://github.com/login?return_to=%2Fdeepseek-ai%2FDeepSeek-R1)

# r1的temperature参数是否生效？ #396

[New issue](https://github.com/login?return_to=https://github.com/deepseek-ai/DeepSeek-R1/issues/396)

Copy link

[New issue](https://github.com/login?return_to=https://github.com/deepseek-ai/DeepSeek-R1/issues/396)

Copy link

Closed as not planned

Closed as not planned

[r1的temperature参数是否生效？](https://github.com/deepseek-ai/DeepSeek-R1/issues/396#top)#396

Copy link

Labels

[closed-as-stale](https://github.com/deepseek-ai/DeepSeek-R1/issues?q=state%3Aopen%20label%3A%22closed-as-stale%22)[stale](https://github.com/deepseek-ai/DeepSeek-R1/issues?q=state%3Aopen%20label%3A%22stale%22)

## Description

[lena-777](https://github.com/lena-777)

opened [on Feb 13, 2025](https://github.com/deepseek-ai/DeepSeek-R1/issues/396#issue-2851007501)

Issue body actions

官方文档（[https://api-docs.deepseek.com/zh-cn/guides/reasoning\_model](https://api-docs.deepseek.com/zh-cn/guides/reasoning_model) ）提到r1不支持temperature参数，
但仓库readme对于r1的评估又有temperature值说明使用的0.6评估。

经测试发现，传不同的temperature确实有不一样的回答影响（长度、回答质量）。

👀React with 👀3freeorca, fangxy926 and MonkeyLeeT

## Activity

### cht619 commented on Feb 17, 2025

[cht619](https://github.com/cht619)

[on Feb 17, 2025](https://github.com/deepseek-ai/DeepSeek-R1/issues/396#issuecomment-2661712309)

More actions

在request上设置么

### lena-777 commented on Feb 17, 2025

[lena-777](https://github.com/lena-777)

[on Feb 17, 2025](https://github.com/deepseek-ai/DeepSeek-R1/issues/396#issuecomment-2661840131)

Author

More actions

> 在request上设置么

是的，测试的时候同样的请求体，temperature=0,0.6**连续**请求20次，=0时think字符数平均值是2600，=0.7时think字符数平均值是6300。此外其他变量都一致。
此外，还测试了多种不一样的问题，temperature值都会对think字符数有影响。

但是，将temperature值运用到实际请求中后，又发现字符数没变化。

### github-actions commented on Mar 22, 2025

[github-actions](https://github.com/apps/github-actions)bot

[on Mar 22, 2025](https://github.com/deepseek-ai/DeepSeek-R1/issues/396#issuecomment-2744707973) – with [GitHub Actions](https://help.github.com/en/actions)

More actions

This issue has been automatically marked as stale because it has not had recent activity. It will be closed if no further activity occurs. If you believe this issue is still relevant, please leave a comment to keep it open. Thank you for your contributions!

[![](https://avatars.githubusercontent.com/in/15368?s=64&v=4)github-actions](https://github.com/apps/github-actions)

added

[stale](https://github.com/deepseek-ai/DeepSeek-R1/issues?q=state%3Aopen%20label%3A%22stale%22)

[on Mar 22, 2025](https://github.com/deepseek-ai/DeepSeek-R1/issues/396#event-16937137856)

[![](https://avatars.githubusercontent.com/in/15368?s=64&v=4)github-actions](https://github.com/apps/github-actions)

removed

[stale](https://github.com/deepseek-ai/DeepSeek-R1/issues?q=state%3Aopen%20label%3A%22stale%22)

[on Apr 27, 2025](https://github.com/deepseek-ai/DeepSeek-R1/issues/396#event-17419767609)

### github-actions commented on May 30, 2025

[github-actions](https://github.com/apps/github-actions)bot

[on May 30, 2025](https://github.com/deepseek-ai/DeepSeek-R1/issues/396#issuecomment-2920855565) – with [GitHub Actions](https://help.github.com/en/actions)

More actions

This issue has been automatically marked as stale because it has not had recent activity. It will be closed if no further activity occurs. If you believe this issue is still relevant, please leave a comment to keep it open. Thank you for your contributions!

[![](https://avatars.githubusercontent.com/in/15368?s=64&v=4)github-actions](https://github.com/apps/github-actions)

added

[stale](https://github.com/deepseek-ai/DeepSeek-R1/issues?q=state%3Aopen%20label%3A%22stale%22)

[on May 30, 2025](https://github.com/deepseek-ai/DeepSeek-R1/issues/396#event-17876765123)

### github-actions commented on Jun 13, 2025

[github-actions](https://github.com/apps/github-actions)bot

[on Jun 13, 2025](https://github.com/deepseek-ai/DeepSeek-R1/issues/396#issuecomment-2968525393) – with [GitHub Actions](https://help.github.com/en/actions)

More actions

false

[![](https://avatars.githubusercontent.com/in/15368?s=64&v=4)github-actions](https://github.com/apps/github-actions)

added

[closed-as-stale](https://github.com/deepseek-ai/DeepSeek-R1/issues?q=state%3Aopen%20label%3A%22closed-as-stale%22)

[on Jun 13, 2025](https://github.com/deepseek-ai/DeepSeek-R1/issues/396#event-18124462021)

[![](https://avatars.githubusercontent.com/in/15368?s=64&v=4)github-actions](https://github.com/apps/github-actions)

closed this as [not planned](https://github.com/deepseek-ai/DeepSeek-R1/issues?q=is%3Aissue%20state%3Aclosed%20archived%3Afalse%20reason%3Anot-planned)[on Jun 13, 2025](https://github.com/deepseek-ai/DeepSeek-R1/issues/396#event-18124462155)

[Sign up for free](https://github.com/signup?return_to=https://github.com/deepseek-ai/DeepSeek-R1/issues/396) **to join this conversation on GitHub.** Already have an account? [Sign in to comment](https://github.com/login?return_to=https://github.com/deepseek-ai/DeepSeek-R1/issues/396)

## Metadata

## Metadata

### Assignees

No one assigned

### Labels

[closed-as-stale](https://github.com/deepseek-ai/DeepSeek-R1/issues?q=state%3Aopen%20label%3A%22closed-as-stale%22)[stale](https://github.com/deepseek-ai/DeepSeek-R1/issues?q=state%3Aopen%20label%3A%22stale%22)

### Type

No type

### Projects

No projects

### Milestone

No milestone

### Relationships

None yet

### Development

Code with agent mode

Select code repository

No branches or pull requests

### Participants

## Issue actions