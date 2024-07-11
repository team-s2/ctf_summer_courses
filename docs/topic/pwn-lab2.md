# Pwn Lab 2：ROP与格式化字符串漏洞

本节 Lab 由以下部分组成：

- [Task 1: ropbasic 赛题](#task-1-20)
- [Task 2: onerop 赛题](#task-2-20)
- [Task 3: onefsb 赛题](#task-3-25)
- [Task 4: fsb-stack 赛题](#task-4-35)
- [Bonus: nosbofrop 赛题](#bonus-15)

以上题目均已部署在比赛平台上。拿到附件后先 checksec 一下是做 pwn 题的好习惯，看清楚程序保护的开关情况有助于你思考如何进行漏洞利用

> Note: 如果你最终没能获取到题目 flag，也请在报告中附上你的 exp 以及你所获取到的地址泄露等对漏洞利用有帮助的信息，评分时会酌情给分

## Task 1 (20%)

题目名：`[lab2] ropbasic`

课件中没有演示过，但给了思路的题目，请编写 exp 获取 flag

本题有特殊要求：

- 靶机上的 flag 文件名叫做 "flag.txt"，希望你在 exp 中通过 "orw"（即 open、read、write 这三个函数）来实现打开 flag 文件、读取 flag 内容并输出 flag 的效果。C代码示例 orw-demo.c 已在附件中给出

- <u>如果 exp 是通过执行 system("/bin/sh") 等方式拿到 shell 后执行 cat flag 命令获取到 flag 的话，本题只给 10 分</u>

提交的报告中**至少**需要包含以下内容：

- canary 和 libc 地址泄露的思路
- 成功拿到 flag 的截图，以及在本次攻击中你所泄露出的 canary 值与 libc 基地址值
- 完整的 exp 代码

## Task 2 (20%)

题目名：`[lab2] onerop`

分析附件程序，编写 exp 获取 flag

提交的报告中**至少**需要包含以下内容：

- 地址泄露的思路
- 成功拿到 flag 的截图，以及在本次攻击中你所泄露出的 libc 基地址值
- 完整的 exp 代码

## Task 3 (25%)

题目名：`[lab2] onefsb`

分析附件程序，编写 exp 获取 flag

提交的报告中**至少**需要包含以下内容：

- 完整的利用思路，包括如何进行地址泄露、如何劫持控制流等
- 如果你在利用时用到了 "$" 符号，请简要描述你确认该控制符对应参数的位置的过程
- 成功拿到 flag 的截图，以及在本次攻击中你所泄露出的 libc 基地址值
- 完整的 exp 代码

## Task 4 (35%)

题目名：`[lab2] fsb-stack`

分析附件程序，编写 exp 获取 flag

提交的报告中**至少**需要包含以下内容：

- 完整的利用思路，包括如何进行地址泄露、如何劫持控制流等
- 成功拿到 flag 的截图，以及在本次攻击中你所泄露出的 libc 基地址值
- 完整的 exp 代码

## Bonus (+15%)

题目名：`[lab2] nosbofrop`

分析附件程序，编写 exp 获取 flag

提交的报告中**至少**需要包含以下内容：

- 完整的利用思路
- 你所用到的所有 gadget
- 成功拿到 flag 的截图
- 完整的 exp 代码