# Pwn Lab 1: 代码注入与栈溢出

本节 Lab 由以下部分组成：

- [Task 1: nocrash 赛题](#task-1)
- [Task 2: login_me 赛题](#task-2)
- [Task 3: inject_me 赛题](#task-3)
- [Task 4: sbofsc 赛题](#task-4)
- [Bonus](#bonus)

## Task 1 (10%)

课上作为引子的 `nocrash` 赛题，请通过其熟悉远程攻击，取得 flag

- `[lec1] pwn nocrash` 题目位于[比赛平台](https://ctf.zjusec.com/games/3/challenges)上

请在报告中附上漏洞分析以及做法，给出成功拿到 flag 的截图，并将攻击代码以附件形式上传

## Task 2 (30%)

复现，并完成课上讲解的 `login_me` 赛题，取得远程的 flag

- `[lec1] pwn login_me` 题目位于[比赛平台](https://ctf.zjusec.com/games/3/challenges)上

请在报告中附上漏洞分析以及做法，给出成功拿到 flag 的截图，并将攻击代码以附件形式上传

## Task 3 (30%)

课上讲解的 `inject_me` 赛题，请实现

1. 按题目要求实现 5 种功能的 `delegate` 代码，完成后取得flag第一部分 (15 points)
2. 学习 shellcode (5 points) 并通过 shellcode 攻击拿到远程的 shell，并得到另外的 flag 内容 (15 points)

- `[lec1] pwn inject_me` 题目位于[比赛平台](https://ctf.zjusec.com/games/3/challenges)上

请在报告中附上漏洞分析以及做法，给出对于你使用的 shellcode 代码的分析（这个代码到底干了啥），给出成功拿到 flag 的截图，并将攻击代码以附件形式上传

## Task 4 (30%)

（课上稍微预告的）题目 `sbofsc` 是栈上缓冲区溢出 + shellcode 的组合题目，请完成该赛题

- `[lab1] pwn sbofsc` 题目位于[比赛平台](https://ctf.zjusec.com/games/3/challenges)上

## Bonus (+15%)

位于校巴的“超老” shellcode 赛题，在完成以上的基础后，做它一定是砍瓜切菜

- [题目信息](https://zjusec.com/challenges/7)

> 注：这个题是 32 位架构的 shellcode 哦，不要弄错了

请在报告中附上漏洞分析以及做法，给出成功拿到 flag 的截图，并将攻击代码以附件形式上传