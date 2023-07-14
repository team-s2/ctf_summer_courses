# Crypto Lab 2: AES, RSA & LWE

这次作业略多，但基本上都是课上讲过的例题的实现，这里的作业分数分配后续可能会改动（捞人），**基础部分做完就能满分，拓展部分可以加分（最多本次课加满）**。

**合理规划基础部分和拓展部分题目的选择，有些拓展题难度不见得比基础题大**，每个人对不同板块的掌握程度也不尽相同，这也是为了模拟真实CTF比赛有限时间内较多题目的情景 **（选题的艺术）**，当然如果真的有能力完成这里的所有题目，你对密码学的理解会提升一个层次。

实验需要提交实验报告。每道做出来的题均需要写在实验报告中，否则无法给分。**实验报告需要写出每道题的思路并贴上攻击脚本（payload）**。对于没法完整做出的题，也可以叙述自己的思路和解题过程，会酌情给分。

今年仍旧有**10分的保底分**（可能也会调整），只要提交作业，成功做出任意一题就能拿到，今年的保底分直接加到最后分数中，因此其实你**只需拿到90分就能满了**。

本次crypto lab对python以及sage的要求会比较高，如果认为自己对python的了解还是不够的话，请务必善用搜索引擎，并积极向助教们提问（对于密码学库的问题尽量咨询密码学方向助教，不过其它python相关问题可以询问所有助教）

本次所有题目都在[ZJU::CTF](https://ctf.zjusec.com/games/4)平台中可以查看，也可以在上面提交flag验证是否正确

**\* 声明：由于去年抄袭现象较为严重，本次作业除了AES基础部分第一题可以在理解基础上完全使用上课演示的代码外，所有题目都会进行查重，查到就不仅仅是这次Lab得0分了😨**

## AES Challenge

### Basic Task

#### Mission 1 (10 points)

完成 CryptoHack 中 Symmetric Ciphers - How AES works - Bringing It All Together 这一题，题目已放在压缩包内，flag 格式为 crypto{xxx}，可以不在 CryptoHack 上提交（上课都讲过一遍了，Copy 一遍都行，主要是理解 AES 的整体结构）。

#### Mission 2 (20 + 20 points)

完成课上例题 ECB Oracle 和 CBC Byte Flip，题目部署在ZJUCTF平台。

#### Mission 3 (30 points)

完成课上例题 Padding Oracle，部署在 ZJUCTF 平台上，这道题目难度也有一些，本题分值为30分。

### Extend Task

#### Mission 1 (10 + 10 points)

完成 Hackergame 2022 题目**不可加密的异世界**的改进版本（原版可关注[Hackergame官方GitHub](https://github.com/USTC-Hackergame)，改进版在压缩包内），体会不同分组模式各自存在的安全性问题，本题难度低于 Beatboxer，但第一小问有 trick（misc回顾），可以先选择游玩此题ヾ(•ω•`)o，本题也部署在了 ZJUCTF 平台。

#### Mission 2 (40 points)

在CryptoHack上完成Symmetric Ciphers - Linear Cryptanalysis - Beatboxer这道题，体会一下完全线性sbox在AES加密中会导致的巨大安全问题，是一道适合入门线性分析的前置问题，没有想象中那么难。

## RSA Challenge

### Basic Task

#### Mission 1 (20 points)

完成[校巴](https://zjusec.com)上的Republican Signature Agency这道题，学习RSA选择明/密文攻击，地址为10.214.160.13:12505。

### Extend Task

#### Mission 1 (35 points)

来道简单的Coppersmith攻击练练手，题目名是Crush On Proust，附件在压缩包内，在校巴上也放了一份，题目不算太难，但对数学要求较高。

## LWE Challenge

### Extend Task

#### Mission 1 (20 points)

来点CryptoHack，CryptoHack - Post Quantum - Learning With Errors - Noise Cheap，本题难度和基础题类似（如果听了LWE相关的），所以也比较推荐来看看。
