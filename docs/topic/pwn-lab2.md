# Pwn Lab 2：ROP

本节 Lab 分为必做题目和选做题目。

- 如有疑问优先考虑合理提问 AI，若无果，欢迎向助教寻求帮助
- 如果提问人数比较多会考虑放出hint
- 报告需要体现人类参与工作的痕迹，若明显由 AI 完成则将酌情扣分
- 完成后需要提交报告和 exp 代码

> Note: 如果你最终没能获取到题目 flag，也请附上你的 exp 以及你所获取到的地址泄露等对漏洞利用有帮助的信息，评分时会酌情给分

> 没有思路时多看看每题报告的提交要求

## 必做部分 (80 pts)

### 例题复现 (30 pts)

复现，并完成课上讲解的三道例题

[[lab 2] passkey](https://ctf.zjusec.net/games/7/challenges#378)  
[[lab 2] ret2plt](https://ctf.zjusec.net/games/7/challenges#379)  
[[lab 2] rop1](https://ctf.zjusec.net/games/7/challenges#380)

提交的报告中**至少**需要包含以下内容：

- 信息泄露的思路(如有)
- 构造rop链的思路
- 成功拿到 flag 的截图

### easyrop (25 pts)

[[lab 2] easyrop](https://ctf.zjusec.net/games/7/challenges#381)

提交的报告中**至少**需要包含以下内容：

- canary，pie基地址和libc基地址泄露的思路
- 构造rop链的思路
- 成功拿到 flag 的截图

### stackpivot (25 pts)

[[lab 2] stackpivot](https://ctf.zjusec.net/games/7/challenges#382)

利用课上讲到的栈迁移技巧完成本题

提交的报告中**至少**需要包含以下内容：

- 构造栈迁移的思路
- 构造攻击rop链的思路
- 成功拿到 flag 的截图

## 选做部分 (至多 35 pts)

### back to future (20 pts)

[[lab 2] ret2plt](https://ctf.zjusec.net/games/7/challenges#379) 

使用ret2libc的技巧完成课上的ret2plt一题

提交的报告中**至少**需要包含以下内容：

- 完整的思路，包括泄露libc基地址，构造rop链，劫持控制流
- 成功拿到 flag 的截图
- 你只用一次rop就完成了攻击吗？如果不是，请说明你是如何达成多次rop的

### orw (20 pts)

[[lab 2] rop1](https://ctf.zjusec.net/games/7/challenges#380)

使用orw的技巧完成课上的rop1一题，直接system("/bin/sh")不得分

提交的报告中**至少**需要包含以下内容：

- 完整的利用思路
- 成功拿到 flag 的截图

### feedback (5~15 pts)

谈谈你对本节课的感受、意见或建议（请畅所欲言，视真诚程度 5 ~ 15 pts）