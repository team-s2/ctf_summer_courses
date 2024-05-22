# Lab 0：基础知识及技能

!!! warning "本实验尚未完成修改"

本课程的 Lab 0 由两部分组成:

- [Prerequisite](#prerequisite) 部分以及
- [Misc](#misc), [Reverse](#reverse), [Pwn](#pwn), [Web](#web), [Crypto](#crypto) 部分**五选一**

> 鼓励多选，探索自己感兴趣的方向！

完成的报告请命名为 `lab0_姓名_学号.pdf`，以邮件附件的形式提交到 <team-aaa@zju.edu.cn>；并于邮件中提供个人的联系方式～

!!! warning "前排提示"
    本课程与其他大家一直在上的学校课程有很大不同。CTF 是一个非常灵活多变又非常注重实践的比赛，所以我们会更偏向于引导大家独立探索、自主学习，而非将所有需要的知识统统灌输给大家。

    因此本 Lab 0 乃至后续的所有实验中都会有很多需要同学们自己去上网查资料，自己学习一些新知识的地方。而且在做 Lab 遇到问题时也需要大家先自行排查问题原因，搜索解决方案。如果你真的解决不了想在群里提问或者私戳助教，也请先阅读[提问的智慧](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/main/README-zh_CN.md)和[别像弱智一样提问](https://github.com/tangx/Stop-Ask-Questions-The-Stupid-Ways/blob/master/README.md)两篇文章。

    如果你实在受不了自学这种方式，只想要通过接受我们的输出来学习 CTF，或者你只想以最低成本拿下短学期学分，那么这门课或许并不适合你，你应当考虑放弃选修本课程。

Lab 过程中遇到的无法解决的问题或者其他任何与课程相关的问题都欢迎加入课程交流群进行讨论，QQ 群号 704994583。

## Prerequisite

### Challange 1

**Linux 环境的搭建与简单使用**

参考难度：★★

后续课程的许多内容都需要 Linux 环境支持，本 challenge 需要大家提前准备好一个自己习惯的 Linux 环境，并熟悉基本的 shell 命令。

???+ note "环境推荐"
    === "Windows"
        推荐使用 WSL，相关安装教程请自行上网搜索。

        也可以使用 VMWare Workstation 或者 VirtualBox 等虚拟机软件安装 Linux 系统。

    === "macOS"
        如果你非常熟悉 macOS 环境且你的 mac 是 intel 处理器的话，大部分情况下你也可以直接使用你的 macOS 环境。（当然完成 reverse / pwn 的题目大概率还是需要 Linux 环境）

        也可以使用 Parallels Desktop / VMWare Fusion 等虚拟机软件安装 Linux 系统。

        如果你的 mac 是 M 系列 Apple Silicon 处理器的话，也就是说你的电脑是 arm 架构，那么你就需要一个 x86 Linux 的环境了。最方便的方法是使用 docker（关于 docker 安装见[官网](https://docs.docker.com/desktop/install/mac-install/)）。macOS 下的 docker 可以通过 qemu 来模拟运行不同架构的容器，比如运行一个 x86_64 架构的 ubuntu:latest 容器你可以运行：

        ```bash
        docker run -it -d --platform linux/amd64 --name ubuntu_amd64 ubuntu:latest
        # -d 后台运行，--platform 指定目标架构，--name 指定容器名 ubuntu:latest 指定镜像
        docker exec -it ubuntu_amd64 /bin/bash
        # 进入容器的 bash 终端
        ```

        更多关于 docker 的使用方法，比如目录挂载、网络配置等可以自行上网学习。

    === "Linux"
        显然，你已经有了（

    关于 Linux 发行版，我们推荐 Ubuntu 22.04 LTS / Ubuntu 24.04 LTS / Kali Linux 2024.1 等。

> 当然，如果你已经拥有了熟悉的 Linux 环境，请放心大胆使用。

具备 Linux 环境后，请观看并学习[「实用技能拾遗」朋辈辅学课程](https://slides.tonycrane.cc/PracticalSkillsTutorial/)中的 lec1 即「Shell 基础及 CLI 工具推荐」课程学习 Linux 基础知识，并完成以下任务：

- 在本机中通过 ssh 远程连接到你的 Linux 环境（使用 Linux 宿主机可跳过本任务）；
- 在实验报告中给出**任意 4 个** shell 命令的用法介绍以及在 Linux 环境下的实操截图；
- 完成 [SadServers](https://sadservers.com/) 上的题目 ["Saint John": what is writing to this log file?](https://sadservers.com/scenario/saint-john) 给出解答以及通过截图。

!!! tip "Hint"
    - Linux 环境的准备可以参考[前年的课程作业](https://github.com/team-s2/ctf_summer_courses/blob/2022/homework/trivial/01_linux_hw.pdf)


### Challenge 2

**基础的 python 编程**

参考难度：★

后续的课程中不乏通过编程来节省人力成本解决特定问题。掌握脚本语言 python 会让这些事半功倍。

> 当然，即使你没有学习过 python 也无需慌张；你可以通过如[菜鸟教程](https://www.runoob.com/python3/python3-tutorial.html)和各类慕课进行简单的学习。你无需成为一个 python master，基本的代码阅读能力以及编程能力足以使你通过此课。

???+ note "关于 python 环境安装的建议"
    建议使用 python 3.12.x 版本。
    
    如果你确定你的 Linux 环境只用来完成本次课程，你可以直接通过 apt 来安装 python。

    否则推荐直接安装 [miniconda](https://docs.anaconda.com/free/miniconda/) / [mamba](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html) / [anaconda](https://www.anaconda.com/download/success) 等工具进行 python 环境的安装、管理和切换。

请完成如下任务，并在实验报告中给出你的代码：

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
2. 请通过 python 编程解决[校巴](https://zjusec.com)上 [calculator](https://zjusec.com/challenges/27) 这道编程题（需要内网访问），在实验报告中给出完整代码、成功解决的截图以及正确的 flag。

!!! tip "Hint"
    - 如果不知道从哪开始可以查看我们提供的[部分代码](https://github.com/team-s2/ctf_summer_courses/blob/master/src/intro/lab0/client.py)，已经完成了题目的连接以及数据的接收（直接使用 socket 进行连接）
        - 或者推荐自学使用 [pwntools](https://docs.pwntools.com/en/latest/) 这个 CTF 中非常常用的 python 包进行更方便的交互
    - `eval` 函数可以用于计算


### Challenge 3（选做）

二进制相关的课题方向（Pwn 以及 Reverse）都需要 x86 汇编的知识，如果对该两方向有兴趣的话，可选完成这个 [asm tour 汇编题目](https://github.com/team-s2/ctf_summer_courses/blob/master/src/intro/lab0/asm_tour_1.asm)，在实验报告中给出你的解题过程。

> 如果完全没有接触过汇编语言，也无需担心，可以学习 hint 提到的资料。对指令、寄存器、调用规定等知识做个基本了解。

!!! tip "Hint"
    - 小白老师的[汇编课程资料](http://cc.zju.edu.cn/bhh/)
    - [TonyCrane 的 8086 的汇编笔记](https://note.tonycrane.cc/cs/pl/asm/)

## 【TODO】Web

参考难度：★★

请访问网址 http://pumpk1n.com/lab0.php 这个神奇的页面藏着一个 flag，请尝试找到它，并在实验报告中记录你的过程。

hint:

- 浏览器中的开发者工具

## Pwn

参考难度：★★

1. 请阅读附件中的 C 代码 [program.c](https://github.com/team-s2/ctf_summer_courses/raw/master/src/intro/lab0/program.c)，尝试找到代码中所有的***BUG***，并在实验报告中给出描述
2. 附件中的 [program.elf](https://github.com/team-s2/ctf_summer_courses/raw/master/src/intro/lab0/program.elf) 是上述源代码 Linux 平台上编译的可执行 ELF 程序，请在 Linux 环境下执行该程序，并在与其交互的过程中触发找到的漏洞，这些漏洞可以使得程序崩溃么？
3. 请修复 `program.c` 中发现的漏洞，将新的代码命名为 `nobug_program.c` 并提交
4. (可选) 参考网上[资料](https://www.cnblogs.com/zhuyp1015/p/3901191.html)，学习 valgrind 使用，并使用其去验证 2 过程中的漏洞触发，提交过程截图


## Reverse

参考难度：★★

[题目下载链接](https://github.com/team-s2/ctf_summer_courses/raw/master/src/intro/lab0/crackme)

1. 尝试通过反汇编/反编译工具逆向该可执行 ELF 程序，并成果获得 `Access Granted` 的提示。请在报告中给出逆向步骤，
2. (可选) 思考逆向该 crackme 的过程中，有无什么可能的取巧、自动的方式
3. (注意) 对逆向方向感兴趣的同学请了解如下基础知识
    - [ELF 可执行文件的格式、加载、链接执行](https://ctf-wiki.org/executable/elf/structure/basic-info/)

## Misc
### Challenge 1

参考难度：★

这里有一串被编码过的神秘的字符串，请找出有意义的原字符串（格式为 `AAA{...}`）：

```text
8Q%uH7oV9C7o!2f7oD*B9M/>U2Gu:s:JP%n6W>j@8PrYk9/]^B:0'e_6SgJh7n-*Q5rM>=:Gkm:7oN)U:I/,P;`$6b:Gk[5=]%gm7mT%14Ztqk
```

请在实验报告中给出你具体的解密**过程**。

!!! tip "Hint"
    - 你可能会需要 [CyberChef](https://lab.tonycrane.cc/CyberChef/)（~~而且这里有一个功能可以秒杀这个题目~~）
    - 你可能需要了解一些关于 **Base 系列**编码的特征

### Challenge 2

参考难度：★★★

下面这张图是 AAA 的 logo。真的……只是一个 logo 吗？其实这张图片中隐藏了一个 flag（格式 `AAA{...}`），请你找出来。

![](https://github.com/team-s2/ctf_summer_courses/raw/master/src/intro/lab0/misc_challenge2.png)

请在实验报告中给出你的解题过程，包括你最终得到的 flag 内容。

!!! tip "Hint"
    - flag 被分为了两个部分
    - 如果你找不到第一部分，~~仔细观察图片~~，这使用了一种最基础的图片隐写技术 LSB 隐写，请自行搜索学习如何破解
    - 如果你找不到第二部分，请仔细查看**文件内容**

## 【TODO】Crypto

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
