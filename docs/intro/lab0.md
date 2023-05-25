# Lab 0：基础知识及技能

具体内容稍后发布 :)


## Reverse
参考难度：★★★☆

可恶，为什么这个可执行文件无法运行，其中究竟隐藏着什么秘密！（该秘密为一串有意义的字符串，格式为 `AAA{...}`）：

![题目附件](https://raw.githubusercontent.com/team-s2/summer_course_2023/master/src/intro/lab0/rev_challenge)

你需要在实验报告中回答以下几个问题：

1. 可执行文件的入口点地址（Entry Point Address）是多少？
2. 可执行文件无法运行的原因是什么？通过什么方法可以让它正常运行？
3. 可执行文件中隐藏的秘密（即格式为 `AAA{...}` 的字符串）是？你是如何获得它的？

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
#### AES Overview
AES是一种对称加密机制，比RSA这样的非对称加密快许多。

对于字符串形式的明文，首先需要把其表示为一个 4x4 的字节矩阵，对应题目代码中的 `bytes2matrix` 和 `bytes2matrix`。然后进行如下所示的加密流程：

1. 密钥扩展
    从128位的密钥中，派生出11个单独的128位“轮密钥”：每个轮密钥用于一个 AddRoundKey 步骤。

2. 初始密钥加
    AddRoundKey - 第一个轮密钥的字节与状态的字节进行异或运算。

3. 加密轮次 - 这个阶段被循环执行10次，包括9个主轮次和一个“最终轮次”
   a) SubBytes - 根据查找表（“S-box”）替换状态的每个字节为不同的字节。
   b) ShiftRows - 状态矩阵的最后三行进行转置——向左或向右移动一列或两列或三列。
   c) MixColumns - 对状态的列进行矩阵乘法运算，将每列的四个字节组合在一起。这在最终轮次中被跳过。
   d) AddRoundKey - 当前轮密钥的字节与状态的字节进行异或运算。

![](https://raw.githubusercontent.com/team-s2/summer_course_2023/master/src/intro/lab0/AES.png)

#### AddRoundKey
AddRoundKey 步骤很简单：它将当前状态(4x4 的字节矩阵)与当前轮密钥(4x4 的字节矩阵)进行异或运算。

在后面的题目中需要你补全相关函数。

#### SubBytes
将状态矩阵的每个字节替换为预设 16x16 查找表中的不同字节。查找表称为“Substitution box”或简称“S-box”，可能一开始看起来令人困惑。让我们来分解一下。

在1945年，美国数学家克劳德·香农发表了一篇开创性的信息论论文。它确定了“混淆”作为一个安全密码必不可少的属性。 “混淆”意味着密文与密钥之间的关系应尽可能复杂。仅凭密文，不应有任何方法可以了解密钥。

如果密码混淆性差，就有可能表达密文、密钥和明文之间的关系为线性函数。例如，在凯撒密码中，密文与明文之间的关系可以表示为 y = x + k，这是一种明显的关系，容易从密文逆推铭文。更复杂的线性变换可以使用高斯消元等技术解决。甚至低次多项式，例如像 y = x^2 + x 这样的方程，也可以使用代数方法有效地求解。然而，通常来说，多项式的次数越高，解决问题就越难，只能通过越来越多的线性函数来逼近它。

S-box 的主要目的是以抵抗线性函数逼近的方式转换输入。S-box 旨在实现高非线性性，虽然 AES 的 S-box 并不完美，但它非常接近。

后面的题目已经给出了 S-box 的逆，需要你补全相关函数实现 AES 中的 Substitution 的逆函数。

### Challenge 1
参考难度：★

[题目下载链接](https://raw.githubusercontent.com/team-s2/summer_course_2023/master/src/intro/lab0/task.py)

上题是对AES的简单抽象，其中需要你补全的 `add_round_key` 和 `sub_bytes` 代码符合AES的 `AddRoundKey` 和 `SubBytes` 的标准实现，请你阅读上述背景或查阅相关文档，实现这两个函数。如果实现正确会输出格式为 `AAA{...}` 的 flag。

请在实验报告中给出你的解题过程，包括你最终得到的 flag 内容。

hint:

- 一共就不超过10行代码，大概不需要hint；如果真的需要，就搜索一下相关文档和代码实现。