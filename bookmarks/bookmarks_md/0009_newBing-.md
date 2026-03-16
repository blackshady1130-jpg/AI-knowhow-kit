---
url: https://www.ruancan.com/p/126327.html
title: "[技巧] 修复浏览器访问new Bing报错问题"
description: "软餐获悉，这几天，大量中文互联网用户在访问new Bing时，似乎正在遇到新的报错。 报错信息如下： Sorry, looks like your network settings are preventing access to…"
author: "安亚"
published: "2023-03-27T00:46:38+08:00"
captured_at: "2026-03-08T10:06:21.780Z"
---

# [技巧] 修复浏览器访问new Bing报错问题

## \[技巧\] 修复浏览器访问 new Bing 报错问题

[安亚](https://www.ruancan.com/i/72) • 2023-03-27 00:46 • [网络应用](https://www.ruancan.com/p/category/pc-soft/wangluo)

软餐获悉，这几天，大量中文互联网用户在访问 new Bing 时，似乎正在遇到新的报错。

报错信息如下：

> *Sorry, looks like your network settings are preventing access to this feature.* 
>
> *抱歉，看起来您的网络设置正在阻止访问此功能。*

显然，这阻断了对 new Bing 的使用。

一个新的解决方法正在社交媒体上流传，读者可以一试。本文发出时，我们实测该方法是有效的。

1\. 从 Chrome 网上应用店[下载](https://chrome.google.com/webstore/detail/modheader-modify-http-hea/idgpnmonknjnojddfkpgkljpfnnfcklj?hl=zh-CN)“ModHeader” 扩展。
2\. 通过浏览器访问 new Bing，点击浏览器工具栏上的 “ModHeader” 图标，点加号按钮，按如下填写参数。

“Name” 处填入：`X-Forwarded-For`
“Value” 处填入：`1.1.1.1`

3\. 点击扩展的空白处以保存设置。
4\. 重启浏览器。重新访问 new Bing 。应该又可以重新和 new Bing 愉快聊天了。

---

**又讯：**

-   微软在周末刚刚[再次上调了 new Bing 的提问配额](https://www.ruancan.com/p/126307.html)。现在允许用户每天向 new Bing 提问 200 个问题（话题），每个问题可互动 20 个回合。
-   读者还可尝试[通过 Skype 应用程序来访问 new Bing](https://www.ruancan.com/p/126243.html)，这相比浏览器更稳定、更方便，遇到莫名其妙的异常的概率也更小。

赞 (3)