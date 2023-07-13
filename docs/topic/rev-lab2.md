# Rev Lab 2: CrackMe & Malware

本节 Lab 由以下两部分组成：

- [Task 1: 课堂例题++](#task-1)（60分）
    - CrackMe 部分 (30分)
    - Malware 部分 (30分)
- [Task 2: 简单的勒索软件](#task-2)（40分）

## Task 1

### Part 1 (30 points)

课上我们讲解了如何把 010 Editor 变为 Freeware，请回顾课上讲解的内容，复现这一过程并提交 Writeup

### Part 2 (30 points)

[题目下载链接](https://raw.githubusercontent.com/team-s2/summer_course_2023/master/src/topic/rev-lab2/Evil_Panda.zip)

课上我们分析了使用 Go 语言编写的低配版“熊猫烧香”，请回顾课上讲解的内容，回答以下问题：

1. 在程序启动后，它使用了什么方法来隐藏自己？ (5 points)
2. 该软件是如何实现持久化的？（5 points）
3. 程序对哪些目标文件有恶意行为，分别做了什么操作？（10 points）
4. 如果我的系统不幸被该软件感染，应该如何恢复？请编写一个恢复程序，对编程语言不做要求 （10 points）

## Task 2

[题目下载链接](https://raw.githubusercontent.com/team-s2/summer_course_2023/master/src/topic/rev-lab2/baby_ransomware.zip)

非常友好的一个程序，甚至感觉不到丝毫威胁，完成该题目并提交：

1. flag 内容及 Writeup (40 points)

### Hint

1. 该题目的年代较为久远，如果无法运行（如提示缺少 dll）也无需担心，静态分析就足以解出这道题目
2. 你可能需要了解一下什么是壳，这个程序用到了什么壳进行保护，以及是否有对应的脱壳工具