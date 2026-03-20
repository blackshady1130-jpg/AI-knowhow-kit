# Claude Code 终于不烦人了

Original 多头注意力 多头注意力 | 多头注意力

Claude Code 跟 ChatGPT 最大的区别在于，它不只是和你聊天，它真的会在你的电脑上执行命令。`rm -rf`、`git push --force`、`curl xxx | bash`——这些东西它都能干。虽然默认每条命令都要你手动确认，但如果你开启了自动审批来提升效率，安全就成了一个绕不开的问题。

## 确认疲劳

要求确认每一条命令，并不比不确认更安全。

这跟 Windows Vista 时代的 UAC 弹窗一样。刚上线时每个操作都弹一次"你确定要允许这个程序修改你的计算机吗？"，结果用户被训练成了条件反射式地点"是"。弹窗越多，每一次确认被认真对待的概率就越低。

Claude Code 的默认权限模式也有这个问题。它想读一个文件，弹确认；想搜索一下代码，弹确认；想看一下 git log，又弹确认。一个复杂任务下来，你可能要点几十次确认。到后面你的手指就会自动按 y，根本不看它要执行什么。

这就是确认疲劳。当安全机制本身变成了噪音，它就不再提供保护了。

## 现有方案够用吗

Claude Code 自带了几个权限模式，但每个都有明显的短板：

- **Auto accept edits**：只管文件编辑，Bash 命令照样弹确认
- **Bypass permissions**：所有操作零确认，包括 `rm -rf /`，官方只建议在沙箱环境里使用
- **默认模式**：每条命令都确认，确认疲劳导致安全只是幻觉

## 门卫的设计哲学

用 Claude Code 的 hook 机制写了一个 280 行的 Python 脚本做"门卫"。核心理念：把明确安全的放行，把明确危险的拦住，把拿不准的交给人。

三层逻辑：

**第一层：危险模式检测**。不管命令本身是什么，只要匹配到 fork bomb、pipe-to-shell、命令替换这类模式，直接拦截。

**第二层：黑名单**。`rm`、`sudo`、`kill`、`ssh`、`eval` 这些命令，无论参数是什么都不自动放行。

**第三层：白名单**。80 多个明确安全的命令——`ls`、`grep`、`cat`、`git log`、`curl`（只读模式）、`ps` 等。

## 同一个工具，读写分离

很多命令本身既能读也能写：

- `git`：`git log`、`git diff` 放行，`git push`、`git commit` 拦截
- `curl`：默认 GET 放行，加了 `-X POST`、`-d` 拦截
- `sed`：正常的 `sed 's/foo/bar/'` 放行，`sed -i` 拦截
- macOS `defaults`：`defaults read` 放行，`defaults write` 拦截

这种细粒度的读写分离，才是这个 hook 比简单的 allowlist 更实用的地方。

## 安全是个频谱

现在是 auto accept edits + hook 的组合。文件编辑和只读 Bash 命令都自动放行，只有真正有副作用的操作需要确认。这覆盖了日常 90% 以上的操作，同时把真正危险的 10% 留给了人类判断。

这跟管理一个团队其实很像。你不会要求一个资深工程师每写一行代码都来找你审批，也不会放任实习生直接往生产环境推代码。你会根据操作的风险等级来设定不同级别的自主权。

完整脚本：[approve_readonly_bash.py](https://gist.github.com/thuwyh/c1968ddd36bd8ea68f134be04570d371)

---
Source: https://mp.weixin.qq.com/s/iI7LubqcBmrSK6X3lzamgQ
