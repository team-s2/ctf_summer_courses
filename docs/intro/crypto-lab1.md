# Crypto Lab 1：消息加密和数字签名

本节 Lab 由以下两个部分组成：

- [Task ：维吉尼亚密码破解](#task-40)
- [Challenges](#challenges-bonus-6020)

## Task (40%)
课上介绍了维吉尼亚（Vigenere）密码，其作为多表加密的替换密码，加密强度相对于单表替换已经增强了许多，但是仍然会因语言学特性被轻松破解。

维吉尼亚密码的破解方法在课上有一定介绍，也做了一些展示，密钥的破解基本分为以下两步：

1. 爆破猜测密钥长度
    - 第一种方法是寻找多次重复的密文，然后计算密文间隔的最大公因数，即为最有可能的密钥长度，这个在课上已作展示
    - 此外，也可以爆破密钥长度，计算密文中相隔该长度的字符重合了几次，整体重合次数最多的长度可能就是密钥长度
2. 逐位爆破密钥
    - 确定了密钥长度后，可以通过字母频率或者单词频率猜测密钥的其中几位
    - 随后根据已解密的部分猜测单词，继续进行密钥的破解

本 Task 需要完成 ZJU School-Bus 上的 [vigenere-encrypt](https://zjusec.com/challenges/31) 一题，在实验报告中简单描述这道题的做法。如果没法完整做出，也可以叙述自己的思路和解题过程，会根据完成情况给分。本题分值 40 分。

## Challenges & bonus (75%)
除了古典密码外，现代密码学也有很多有趣的内容。课上的介绍几乎涵盖了如今密码学的大部分内容，比如对称加密的流密码攻击、非对称加密的 RSA 及应用、DSA 数字签名的构建和验证、哈希函数的扩展攻击、随机数的预测等，大家可以根据自身情况选择感兴趣的内容进行深入学习。

本模块主要考察同学们通过网络资源学习密码学的能力（当然课上也已经讲解了大致的攻击方向），根据题目的难度设置对应的分值，大家可以任选一道或多道题目完成，但是该模块分数不溢出 75 分。

### 古典密码的拓展 (60%)

希尔密码是古典密码学与线性代数的结合，通过希尔密码的破解，也可以初步感受现代密码学的特点：以数学为基础的算法构建和破解。

本 Challenge 需要完成 ZJU School-Bus 上的 [HSC](https://zjusec.com/challenges/168) 一题，在实验报告中简单描述这道题的做法。

这里首先先让同学们学习一下 sagemath 的使用方法，对完成本题或者之后专题的学习有较大的帮助。

- 对题目中的 MT 矩阵进行随机赋值，使其可逆，使用 sage 求出它的逆矩阵，分值 10 分
- 随机设置 flag 生成 FT，计算 RT，再通过 RT 和 MT 求出 FT 的值，与原 FT 进行比对，分值 10 分

如果后续没有选择密码学专题的打算，上述复现可以使用[在线环境](https://sagecell.sagemath.org/)。

HSC 题目分值 40 分，加上 sage 复现部分本 Challenge 共 60 分，同样，如果没法完整做出，也可以叙述自己的思路和解题过程，会根据完成情况给分。

### RSA 的密钥格式解析 (40%+35%)

RSA 密钥的格式有很多种，常见的有 PEM、DER 等格式。PEM 格式的密钥是 Base64 编码的 DER 格式密钥，DER 格式的密钥是 ASN.1 编码的二进制格式。

你可能需要参考包括但不限于 [此博客](http://www.shangyang.me/2017/05/24/encrypt-rsa-keyformat/) 来了解 RSA 密钥的具体格式和结构。

本 Challenge 需要完成比赛平台上的 Leaked RSA Key 一题，在实验报告中描述这道题的做法。

- 解析 DER 格式的 RSA 密钥，解释各个字段的含义，分值 30 分
- 使用 [factordb](https://factordb.com/) 或者 yafu 等其他工具分解 RSA 模数解出明文，分值 10 分
- (慎选) 解析不出意外的话，你会发现私钥只有前半部分。你可以尝试使用 RSA 已知私钥高位攻击来恢复后半部分，仅使用网络上的脚本只能获得 15 分，如果能够在报告中详细解释攻击过程和原理，可以获得 35 分。

如果没法完整做出，也可以叙述自己的思路和解题过程，会根据完成情况给分。

### DSA 数字签名的构建和验证 (60%+15%)

DSA 数字签名算法是现代密码学中重要的数字签名算法之一，广泛应用于各种安全协议中。在课上我们介绍了 DSA 的基本原理和签名验证过程，也简要介绍了相关的攻击方式。

你可能需要参考 DSA签名的线性随机数 k 攻击 来完成本题。

本 Challenge 需要完成 ZJU School-Bus 上的 [Democratic Signature Agency
](https://zjusec.com/challenges/85) 一题，在实验报告中简单描述这道题的做法。完成本题可以获得 60 分。

- （慎选）如果你完成了 ZJU School-Bus 上的 [D.S.A Revenge](https://zjusec.com/challenges/118)，你会获得额外的 15 分奖励。

如果没法完整做出，也可以叙述自己的思路和解题过程，会根据完成情况给分。

### 随机数的预测 (50%+15%)

随机数在密码学中起着重要的作用，尤其是在密钥生成和加密算法中。

在课上我们主要介绍了随机数的生成和预测方法，以及相关的攻击方式，你可以尝试实现一些简单的随机数预测攻击。

本 Challenge 需要完成 ZJU School-Bus 上的 [PRNG Study1](https://zjusec.com/challenges/94) 一题，在实验报告中简单描述这道题的做法。完成本题可以获得 50 分。

- 如果想要获得额外的 15 分奖励，你可以再选择任意一种语言的随机数生成器进行分析并阐述攻击的思路。

如果没法完整做出，也可以叙述自己的思路和解题过程，会根据完成情况给分。

### （慎选）哈希函数的扩展攻击 (60%)

哈希函数是现代密码学中重要的组成部分，广泛应用于数字签名、消息认证等场景。在课上我们介绍了哈希函数的基本原理和常见的攻击方式。

本 Challenge 需要完成 ZJU School-Bus 上的 [treasurebank](https://zjusec.com/challenges/32) 一题，在实验报告中简单描述这道题的做法。

- 你可能需要注意 mdx 并非 md5，以及本题目需要 python2 环境。

如果没法完整做出，也可以叙述自己的思路和解题过程，会根据完成情况给分。

### 其他

当然，密码学的内容远不止于此，你可以根据自己的兴趣和能力选择其他的密码学内容进行学习和挑战。欢迎自行选择一种现代密码学的内容进行深入学习和挑战，并与密码学助教联系评估分值（可能会比较严格），如果你对上述题目的分值评估有异议，或者需要针对某题释放更多的hint，也可以与密码学助教沟通。

如果有对本节基础课程有什么建议或者感想，视情况给予额外的奖励，但是不会超过 10 分。

如果你有能力完成了以上全部的题目，队长一定会请你喝茶的😀