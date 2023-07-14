# Rev Lab 1: Baby Reverse

本节 Lab 由以下两部分组成：

- [Task 1: 课堂例题++](#task-1)（70分）
    - 课上练习题复现 (40分)
    - 修改后的练习题 (30分)
- [Task 2: 伪随机？](#task-2)（30分）

## Task 1

### Part 1 (40 points)

[题目下载链接](https://raw.githubusercontent.com/team-s2/summer_course_2023/master/src/intro/rev-lab1/practice)

课上作为练习的 `practice` 赛题，请回顾课上讲解的内容，完成题目并回答课上提出的 5 个问题：

1. 在题目中有一个函数是**加密**相关的函数，请找出这个函数的**地址**（Hex 格式作答，5 points）
2. 当你找到了这个加密函数，请找出程序在加密过程中所使用到的**密钥** （5 points）
3. 在这个题目中，程序简单封装了**短字符串**类型，请在 IDA 中恢复它的**结构体** （截图或用 C 语言表示该结构， 15 points）
4. 给出你解答的 flag 内容及 Writeup （15 points）

### Part 2 (30 points)

[题目下载链接](https://raw.githubusercontent.com/team-s2/summer_course_2023/master/src/intro/rev-lab1/rc4.tar.gz)

在 `practice` 赛题的基础上，该题目稍有修改，请你稍加探索完成题目并回答以下问题：

1. 程序中加密函数用到的的**密钥**是什么，你是如何找到它的（10 points）
2. 给出你解答的 flag 内容及 Writeup（20 points）

## Task 2

[题目下载链接](https://raw.githubusercontent.com/team-s2/summer_course_2023/master/src/intro/rev-lab1/pseudo.tar.gz)

看似随机却并不随机，看似模糊却又清晰，请你耐心分析并提交：

1. flag 内容及 Writeup (30 points)

### Hint

- 对于相同的输入，输出也是不一样的，但这并不影响我们对 flag 的求解（flag 内容为有意义的字符串）