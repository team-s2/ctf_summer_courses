# Lab 0：基础知识及技能

本课程的 Lab 0 由两部分组成:

- [Prerequisite](#prerequisite) 部分以及
- [Misc](#misc), [Reverse](#reverse), [Pwn](#pwn), [Web](#web), [Crypto](#crypto) 部分**五选一**

> 鼓励多选，探索自己感兴趣的方向！

完成的报告请命名为 `lab0_姓名_学号.pdf` 与**6月11日中午12点前**，以邮件附件的形式提交到 <team-aaa@zju.edu.cn>；并于邮件中提供个人的联系方式～

lab过程中遇到的问题或者任何与课程相关的问题欢迎加入课程交流群进行讨论，QQ 群号 704639399。

## Prerequisite

### Challange 1

**Linux 环境的搭建与简单使用**

参考难度：★

后续课程的许多内容都将在 Linux 操作系统的平台上完成，为了方便，本次课程提供了 ubuntu 虚拟机供下载

> 下载[链接](https://pan.baidu.com/s/1lg4JZoYJwKj6ImuKdtv_Nw?pwd=AAAA)（其中用户名为 ctfer，密码为 aaa）

虚拟机中预装了课程中将要用到的各类工具及环境。

> 当然，如果你已经拥有了熟悉的 Linux 环境，请放心大胆使用。

具备 Linux 后，请观看 [Shell 基础及 CLI 工具推荐 - 2023 春夏计算机学院朋辈辅学](https://www.bilibili.com/video/BV1T84y1w7wB/) 课程视频，并在实验报告中给出***任意4个*** shell 命令的用法介绍以及在 Linux 环境下的实操截图。

hint: 

- Linux 环境的准备可以参考[去年的课程内容](https://github.com/team-s2/ctf_summer_courses/blob/main/homework/trivial/01_linux_hw.pdf)


### Challenge 2

**基础的 python 编程**

参考难度：★

后续的课程中不乏通过编程来：

1. 节省人力成本
2. 解决特定问题

掌握脚本语言 python 会让这些事半功倍。请完成如下任务，并在实验报告中给出你的代码：

> 当然，即使你没有学习过 python 也无需慌张；你可以通过如[菜鸟教程](https://www.runoob.com/python3/python3-tutorial.html)和各类慕课进行简单的学习。你无需成为一个 python master，基本的代码阅读能力以及编程能力足以使你通过此课。

1. 请阅读和执行如下 python 程序，在实验报告中并解释其功能:
```py
#!/usr/bin/python3

data = input("give me your string: ")
print("length of string:", len(data))

data_old = data
data_new = ""
for d in data:
    if d in 'abcdefghijklmnopqrstuvwxyz':
        data_new += chr(ord(d) - 32)
    elif d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        data_new += chr(ord(d) + 32)
    else:
        data_new += d

print("now your string:", data_new)
```

2. 请通过 python 编程解决[校巴](https://zjusec.com)上 [calculator](https://zjusec.com/challenges/27) 这道编程题（需要内网访问），在实验报告中给出完整代码、成功解决的截图以及正确的 flag

hint: 

- 如果不知道从哪开始可以查看我们提供的[部分代码](https://github.com/team-s2/summer_course_2023/blob/master/src/intro/lab0/client.py)，已经完成了题目的连接以及数据的接收
    - 或者推荐自学使用 [pwntools](https://docs.pwntools.com/en/latest/) 这个 CTF 中非常常用的 python 包进行交互
- `eval` 函数可以用于计算


### Challenge 3（选做）

二进制相关的课题方向（Pwn 以及 Reverse）都需要 x86 汇编的知识，如果对该两方向有兴趣的话，可选完成这个 [asm tour 汇编题目](https://github.com/team-s2/summer_course_2023/blob/master/src/intro/lab0/asm_tour_1.asm)，在实验报告中给出你的解题过程。

> 如果完全没有接触过汇编语言，也无需担心，可以学习 hint 提到的资料。对指令、寄存器、调用规定等知识做个基本了解。

hint:

- 小白老师的[汇编课程资料](http://cc.zju.edu.cn/bhh/)
- [x86的汇编笔记](https://note.tonycrane.cc/cs/pl/asm/)



## Web

参考难度：★★

请访问网址 http://pumpk1n.com/lab0.php 这个神奇的页面藏着一个 flag，请尝试找到它，并在实验报告中记录你的过程。

hint:

- 浏览器中的开发者工具

## Pwn

参考难度：★★

1. 请阅读附件中的 C 代码 [bug_program.c](https://github.com/team-s2/summer_course_2023/raw/master/src/intro/lab0/bug_program.c)，尝试找到代码中所有的***BUG***，并在实验报告中给出描述
2. 附件中的 [bug_program.elf](https://github.com/team-s2/summer_course_2023/raw/master/src/intro/lab0/bug_program.elf) 是 Linux 平台上编译的可执行 ELF 程序，请在 Linux 环境下执行该程序，并在与其交互的过程中触发找到的漏洞，这些漏洞可以使得程序崩溃么？
3. 请修复 bug_program.c 中发现的漏洞，将新的代码命名为 no_program.c 并提交


## Reverse
参考难度：★★★

可恶，为什么这个可执行文件无法运行，其中究竟隐藏着什么秘密！（该秘密为一串有意义的字符串，格式为 `AAA{...}`）：

[题目下载链接](https://raw.githubusercontent.com/team-s2/summer_course_2023/master/src/intro/lab0/rev_challenge)

你需要在实验报告中回答以下几个问题：

1. 可执行文件的入口点地址（Entry Point Address）是多少？
2. 可执行文件无法运行的原因是什么？通过什么方法可以让它正常运行？
3. 可执行文件中隐藏的秘密（即格式为 `AAA{...}` 的字符串）是？你是如何获得它的？

hint:

- 需要简单了解 [ELF 可执行文件的格式、加载、链接执行](https://ctf-wiki.org/executable/elf/structure/basic-info/)
- 如果碰到了 `GLIBC_2.34 not found` 的报错，请下载此版本的题目附件，[链接](https://raw.githubusercontent.com/team-s2/summer_course_2023/master/src/intro/lab0/rev_challenge.old)

## Misc
### Challenge 1
参考难度：★

这里有一串被编码过的神秘的字符串，请找出有意义的原字符串（格式为 `AAA{...}`）：

```text
8Q%uH7oV9C7o!2f7oD*@8Oc$J2Gu:s:JO2T78HTV8PrVj9/]^B:0'e_6SgJh7n,=8;)V$M:Gkm:92eJR8Oc-;;`$6b:Gk[5=]\L#7mT%14Ztqk
```

请在实验报告中给出你具体的解密**过程**。

hint:

- 你可能会需要 [CyberChef](https://cyberchef.org/)（~~而且这里有一个功能可以秒杀这个题目~~）
- 你可能需要了解一些关于 **Base 系列**编码的特征

### Challenge 2
参考难度：★★★

下面这张图是 AAA 的 logo。真的……只是一个 logo 吗？其实这张图片中隐藏了一个 flag（格式 `AAA{...}`），请你找出来。

![](https://raw.githubusercontent.com/team-s2/summer_course_2023/master/src/intro/lab0/misc_challenge2.png)

请在实验报告中给出你的解题过程，包括你最终得到的 flag 内容。

hint：

- flag 被分为了两个部分
- 如果你找不到第一部分，~~仔细观察图片~~，这使用了一种最基础的图片隐写技术 LSB 隐写，请自行搜索学习如何破解
- 如果你找不到第二部分，请仔细查看**文件内容**


## Crypto

### 题目相关背景知识
AES是一种对称加密机制，比RSA这样的非对称加密快许多。由于本题只涉及 `AddRoundKey` 和 `Substitution Bytes` 内容，所以只对实验相关部分进行简要说明，而 AES 的完整细节可以[在这里](https://ctf-wiki.org/crypto/blockcipher/aes/)阅读学习。

#### bytes2matrix
由于 AES 的加密过程中的状态用一个 4x4 的字节矩阵，所以对于字符串形式的明文，首先需要把其表示为一个 4x4 的字节矩阵（对，就是线性代数里那个矩阵），对应题目代码中的 `bytes2matrix`，然后进行后续加密流程。

该部分的代码已经给出，不需要你补全，上述文字只是辅助理解。

#### AddRoundKey
AddRoundKey 步骤很简单：它将当前状态(4x4 的字节矩阵)与当前轮密钥(4x4 的字节矩阵)进行异或运算。

异或需要用到的轮密钥已经给出，对应题目代码中的 `round_key`，你只需要 `add_round_key` 中的补全异或算法即可。（不超过三行❗️）

#### SubBytes
将状态矩阵的每个字节替换为预设 16x16 查找表中的不同字节。查找表称为“Substitution box”或简称“S-box”，或许你可能会对为什么加密过程中需要 substitution 感到疑惑，没关系目前不需要理解相关内容。如果一句话概括原因，是为了使得AES的输入输出之间具有高的“非线性性”。

值得注意的是，substitution 的算法在加密和解密过程中并没有不同，只是使用的 S-box 变成了原 S-box 的逆而已。为了使得题目看起来短一些，我删除了加密过程中使用的 S-box，只给出了加密的 S-box 的逆，对应题目代码中的 `inv_s_box`。你只需要补全 `sub_bytes` 函数即可。（同样不超过三行❗️）

### Challenge
参考难度：★★

[题目下载链接](https://raw.githubusercontent.com/team-s2/summer_course_2023/master/src/intro/lab0/task.py)

上题是对AES的简单抽象，其中需要你补全的 `add_round_key` 和 `sub_bytes` 代码符合AES的 `AddRoundKey` 和 `SubBytes` 的标准实现，请你阅读上述背景或查阅相关文档，实现这两个函数。如果实现正确会输出格式为 `AAA{...}` 的 flag。

请在实验报告中给出你的解题过程，包括你最终得到的 flag 内容。

hint:

- 一共就不超过 10 行代码，大概不需要 hint；如果真的需要，请搜索一下 AES 相关文档和代码实现。
