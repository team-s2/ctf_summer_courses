# Pwn Lab 1: Code Injection

本节 Lab 由以下两部分组成：

- 基础部分
    - 课上题目的复现 (80分)
    - 校巴上的 shellcode 赛题 (20分)
- bonus部分 (extra 20分)

## Task 1 (30 points)

课上作为引子的 `hello` 赛题，请通过其熟悉 pwntools 的使用，并完成攻击远程，取得 flag1 (15 points) 与 flag2 (points)

- [题目附件](https://github.com/team-s2/summer_course_2023/tree/master/src/intro/pwn-lab1/hello)
- 题目部署在 IP: `116.62.247.145`, Port: `10100`

请在报告中附上漏洞分析以及做法，给出成功拿到 flag 的截图，并将攻击代码以附件形式上传

## Task 2 (25 points)

课上讲解的 `injection1` 赛题，请逆向分析程序，并实现对其中Code Injection漏洞的攻击，取得位于远程服务器上的 flag (25 points)

- [题目附件](https://github.com/team-s2/summer_course_2023/tree/master/src/intro/pwn-lab1/injection1)
- 题目部署在 IP: `116.62.247.145`, Port: `10101`

请在报告中附上漏洞分析以及做法，给出成功拿到 flag 的截图，并将攻击代码以附件形式上传

> 注：路径穿越不给分哦 :-)

## Task 3 (25 points)

课上讲解的 `injection2` 赛题，请实现

1. 按题目要求实现 5 种功能的 `delegate` 代码，完成后取得 FLAG (10 points)
2. 学习 shellcode (5 points) 并通过 shellcode 攻击拿到远程的 shell，并得到另外的 flag 内容 (10 points)

- [题目附件](https://github.com/team-s2/summer_course_2023/tree/master/src/intro/pwn-lab1/injection2)
- 题目部署在 IP: `116.62.247.145`, Port: `10102`

请在报告中附上漏洞分析以及做法，给出对于你使用的 shellcode 代码的分析（这个代码到底干了啥），给出成功拿到 flag 的截图，并将攻击代码以附件形式上传

## Task 4 (20 points)

位于校巴的“超老” shellcode 赛题，在完成以上的基础后，做它一定是砍瓜切菜

- [题目信息](https://zjusec.com/challenges/7)

> 注：这个题是 32 位架构的 shellcode 哦，不要弄错了

请在报告中附上漏洞分析以及做法，给出成功拿到 flag 的截图，并将攻击代码以附件形式上传

## Bonus (extra 20 points)

在 Task 3 的基础上，`injection3` 赛题对于输入的代码做了一些限制，你还能成功攻击么？请完成

1. 分析 `injection3` 和 `injection2` 的不同，实现了怎样的检查？(5 points)
2. 绕过该检查，完成远程弹 shell，并取得 flag (15 points)

- [题目附件](https://github.com/team-s2/summer_course_2023/tree/master/src/intro/pwn-lab1/injection3)
- 题目部署在 IP: `116.62.247.145`, Port: `10103`

请在报告中给出你的分析结果，并附上漏洞分析以及做法，给出成功拿到 flag 的截图，并将攻击代码以附件形式上传
