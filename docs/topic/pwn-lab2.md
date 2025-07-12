# Pwn Lab 2：ROP / FSB

本节 Lab 由以下部分组成：

- [Task 1: 平台赛题 easyrop](#task-1-20)
- [Task 2: 平台赛题 stackpivot](#task-2-30)
- [Task 3: 思考题 ret2plt revenge](#task-3-20)
- [Task 4: 校巴赛题 Format String Bug_easy](#task-4-30)
- [Bonus: 非栈上格式化字符串 / fsb_heap](#bonus-15)

> Note: 如果你最终没能获取到题目 flag，也请在报告中附上你的 exp 以及你所获取到的地址泄露等对漏洞利用有帮助的信息，评分时会酌情给分

## Task 1 (20%)

题目名：`[lab2]easyrop`

提交的报告中**至少**需要包含以下内容：

- canary,程序基地址和libc基地址泄露的思路
- 构造rop链的思路
- 成功拿到 flag 的截图，以及在本次攻击中你所泄露出的内容
- 完整的 exp 代码

## Task 2 (30%)

题目名：`[lab2]stackpivot`

利用课上讲到的栈迁移技巧完成本题

提交的报告中**至少**需要包含以下内容：

- 构造栈迁移的思路
- 构造攻击rop链的思路
- 成功拿到 flag 的截图
- 完整的 exp 代码

## Task 3 (20%)

如果要使用ret2libc的技巧来解决课上的ret2plt一题，应该怎么做？请给出你的思路

提交的报告中**至少**需要包含以下内容：

- 完整的思路，包括泄露libc基地址，构造rop链，劫持控制流
- 攻击可以只通过一次rop完成吗？如果不能，如何在只有一次溢出的情况下多次进行rop？

## Task 4 (30%)

题目名：[Format String Bug_easy](https://zjusec.com/challenges/3)

> 本题使用的是32位环境，32位下函数参数全部通过栈传递，和课上讲到的略有不同。32位下地址为4字节。

<u>本题要求手动构造格式化字符串的payload，如果使用pwntools的fmtstr_payload函数只能得到15分</u>

提交的报告中**至少**需要包含以下内容：

- 完整的利用思路，包括如何构造格式化字符串，如何劫持控制流
- 成功拿到 flag 的截图
- 完整的 exp 代码

## Bonus (+15%)

在以下两个任务中任选一个完成

1. 对于格式化字符串不在栈上的情况，应该如何进行利用(任意地址读写)，请给出思路
2. 完成校巴赛题[fsb_heap](https://zjusec.com/challenges/77)，给出思路，成功拿到 flag 的截图及exp代码