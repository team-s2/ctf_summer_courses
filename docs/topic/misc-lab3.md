# Misc Lab 3：取证及区块链基础

本节 Lab 由以下两部分组成：

- 必做部分（各 15 分，共 45 分）：
    - [Challenge 1: SQL Inject Analysis](#challenge-1-15)
    - [Challenge 2: dnscap](#challenge-2-15)
    - [Challenge 3: crack_zju_wlan](#challenge-3-15)
- 选做部分，自由选择，最多计 70 分：
    - [Challenge A<span class="heti-skip">: 内存取证</span>（20 分）](#challenge-a-20)
    - [Challenge B: Ethernaut（15 分）](#challenge-b-ethernaut-15)
    - [Challenge C: Re-entrancy（20 分）](#challenge-c-re-entrancy-20)
    - [Challenge D: hard gambler（35 分）](#challenge-d-hard-gambler-35)
    - [Challenge E: Safe NFT（35 分）](#challenge-e-safe-nft-35)

具体实验报告需要写的内容会在下面具体题目里面描述。对于题目有任何问题都可以在群里/私戳 TonyCrane 提问。

本次 lab 的 ddl 在发布两周以后即 7 月 25 日晚 23:59，请注意安排时间。

## Challenge 1 (15%)

完成课上讲的 HTTP 流量分析例题，即 SQL 注入流量的解析，在[题目平台](https://ctf.zjusec.com/games/3/challenges)的 sqltest。

请完成题目，拿到 flag 并提交验证，在实验报告中写出你的解题思路和具体过程。

## Challenge 2 (15%)

完成课上讲的 UDP (DNS) 流量分析例题，即 dnscat 协议的手动解析，在[题目平台](https://ctf.zjusec.com/games/3/challenges)的 dnscap。

- 参考 dnscat 协议文档：[GitHub:iagox86/dnscat2](https://github.com/iagox86/dnscat2/blob/master/doc/protocol.md)

请完成题目，拿到 flag 并提交验证，在实验报告中写出你的解题思路和具体过程。

## Challenge 3 (15%)

完成校巴上的题目 crac_zju_wlan，链接：[zjusec.com/challenges/105](https://zjusec.com/challenges/105)。

虽然我们课上并没有详细讲解 WiFi 协议密码的破解，但其实只要一个我们课上提到的工具就可以搞定，请尝试完成这道题目。

请完成题目，提交 flag 成功，并在实验报告中写出你的解题思路和具体过程。

## Challenge A: 内存取证 (20%)

我们今年课上并没有讲内存取证，但说白了内存取证就是对 strings、volatility 等工具的使用，你可以自行研究，也可以参考[去年的课件](https://slides.tonycrane.cc/CTF101-2023-misc/lec3/#/2)。

本部分提供了两道比较典型的使用 volatility 来求解的内存取证题目，同学们可以自行搭建 volatility 2.6 环境（也可以使用打包好即开即用的版本，但不要使用 volatility 3.x）。

你需要复现这两道题目中的任意一道：

- N1CTF 2022: just find flag，[附件下载（浙大网盘）](https://pan.zju.edu.cn/share/35e51e4b080bdaf6c017440ee8)
    - 参考 writeup：[Nu1L 官方 wp](https://github.com/Nu1LCTF/n1ctf-2022/blob/main/Misc/just_find_flag/writeup.md)、[TonyCrane 的 wp](https://note.tonycrane.cc/writeups/n1ctf2022/)
- BMZCTF: Administrator's secret，[附件下载（浙大网盘）](https://pan.zju.edu.cn/share/eb1642b8eda74094f42e89041b)
    - 经典老题了，随便一搜就能搜到 writeup

因为是复现的题目，所以需要你给出你完成题目的每一步过程或者**其他更多你自己的尝试**，包括命令、必要的截图以及**你自己的思考**，请不要复制粘贴已有 writeup，否则将视为抄袭。

## Challenge B: Ethernaut (15%)

[Ethernaut](https://ethernaut.openzeppelin.com/) 是一套很好的以太坊智能合约入门题目集，我们在课上也演示过了其中的几道题目，在这部分中，你需要独立完成一些其他题目来学习更多常见漏洞：

- [Coin Flip](https://ethernaut.openzeppelin.com/level/0xA62fE5344FE62AdC1F356447B669E9E6D10abaaF)：基于区块属性的伪随机破解
- [Delegation](https://ethernaut.openzeppelin.com/level/0x73379d8B82Fda494ee59555f333DF7D44483fD58)：delegatecall 带来的潜在风险
- [Vault](https://ethernaut.openzeppelin.com/level/0xB7257D8Ba61BD1b3Fb7249DCd9330a023a5F3670)：获取链上公开的合约 private 状态

每一部分 5 分，你需要在报告中给出你的解题思路、具体执行的过程和最终通过关卡的截图。

## Challenge C: Re-entrancy (20%)

Ethernaut 上 Re-entrancy 题目的私链部署版本，你需要参考课上演示的 Token 题目的交互方法来完成本题。

题目部署在了[题目平台](https://ctf.zjusec.com/games/3/challenges)的 Re-entrancy，具体信息详见平台页面。

请完成题目，拿到 flag 并提交验证，在实验报告中写出你的解题思路和具体过程。

## Challenge D: hard gambler (35%)

完成[校巴](https://zjusec.com)上的题目 [hard gambler](https://zjusec.com/challenges/103)。

请完成题目，拿到 flag 并提交验证，在实验报告中写出你的解题思路和具体过程。

## Challenge E: Safe NFT (35%)

完成 ZJUCTF 2022 的题目 Safe NFT，部署在了[校巴](https://zjusec.com)上，链接：[zjusec.com/challenges/169](https://zjusec.com/challenges/169)。

- hint: 可参考 [ZJUCTF 2022 复盘思路](https://slides.tonycrane.cc/ZJUCTF2022-Review/#/7)

请完成题目，拿到 flag 并提交验证，在实验报告中写出你的解题思路和具体过程。