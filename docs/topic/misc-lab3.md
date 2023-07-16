# Misc Lab 3：流量、内存取证及更多探索

本节 Lab 由以下两部分组成：

- 基础部分，必做（每题 20 分，共 80 分）
    - [Challenge 1: SQL Inject Analysis](#challenge-1)
    - [Challenge 2: dnscap](#challenge-2)
    - [Challenge 3: crack_zju_wlan](#challenge-3)
    - [Challenge 4: volatility 安装与使用](#challenge-4)
- 选做部分，每个 20 分，整体多出 100 分的为 bonus
    - [Challenge 5: pysandbox](#challenge-5)
    - [Bonus Task: misc 课程总结](#bonus-task)

具体实验报告需要写的内容会在下面具体题目里面描述。对于题目有任何问题都可以在群里/私戳 TonyCrane 提问。

本次 lab 的 ddl 在发布两周以后即 7 月 28 日晚 23:59，请注意安排时间。

## Challenge 1

完成课上讲的 HTTP 流量分析例题，即 SQL 注入流量的解析。

- 题目附件：[sqltest.pcapng](https://raw.githubusercontent.com/team-s2/summer_course_2023/master/src/topic/misc-lab3/sqltest.pcapng)

请完成题目，拿到 flag，并在实验报告中写出你的解题思路和具体过程。

## Challenge 2

完成课上讲的 UDP (DNS) 流量分析例题，即 dnscat 协议的手动解析。

- 题目附件：[dnscap.pcap](https://raw.githubusercontent.com/team-s2/summer_course_2023/master/src/topic/misc-lab3/dnscap.pcap)
- 参考 dnscat 协议文档：[GitHub:iagox86/dnscat2](https://github.com/iagox86/dnscat2/blob/master/doc/protocol.md)

请完成题目，拿到 flag，并在实验报告中写出你的解题思路和具体过程。

## Challenge 3

完成校巴上的题目 crac_zju_wlan，链接：[zjusec.com/challenges/105](https://zjusec.com/challenges/105)。

虽然我们课上并没有详细讲解 WIFI 协议密码的破解，但其实只要一个我们课上提到的工具就可以搞定，请尝试完成这道题目。

请完成题目，提交 flag 成功，并在实验报告中写出你的解题思路和具体过程。

## Challenge 4

作为 misc 手，配环境也是需要掌握的一个技能之一，而 volatility 这个内存取证工具的环境也是“出了名的”折磨，所以请你来配置好相关 python 环境，成功运行 volatility 2.6 版本，并复现我们上课讲的例题。具体要求：

- 从官方 GitHub 下载 volatility2 的源码（不要 volatility3）
- 直接在本机/虚拟机/ wsl 上配置环境，成功运行
- 复现课上两道例题之一（多做不加分）
    - N1CTF 2022: just find flag，[附件下载（浙大网盘）](https://pan.zju.edu.cn/share/ba58dc4939adaab1a5614f5725)
    - BMZCTF: Administrator's secret，[附件下载（浙大网盘）](https://pan.zju.edu.cn/share/2184f98536c7967867e1e2fa62)
- **注意/提示**：
    - 不要使用下载即用、打包好的版本，请自己配置环境从 python 运行
    - 不要使用 volatility 3.x 版本
    - python 的环境管理推荐使用 conda（miniconda 或 anaconda 都可以）
    - 可以参考网上的安装教程等等

请在报告中写出你配置 volatility 的过程（包括命令、必要的截图等），以及在配置环境时遇到的问题以及解决方法（如果有的话）。同时在报告中也请给出你复现题目的具体步骤，包括命令、必要的截图等。

## Challenge 5

尝试完成校巴上的 pysandbox 系列题目（一共有四道，但实际上一共 16 个版本）：

- pysandbox6: [zjusec.com/challenges/69](https://zjusec.com/challenges/69)（10 分）
- pysandbox10: [zjusec.com/challenges/70](https://zjusec.com/challenges/70)（10 分）
- pysandbox13: [zjusec.com/challenges/71](https://zjusec.com/challenges/71)（不加分，但鼓励尝试）
- pysandbox16: [zjusec.com/challenges/72](https://zjusec.com/challenges/72)（不加分，但鼓励尝试）

可以参考课上给的 python 沙箱逃逸笔记学习：[note.tonycrane.cc/ctf/misc/escapes/pysandbox](https://note.tonycrane.cc/ctf/misc/escapes/pysandbox/)。

请完成对应题目，提交 flag 成功，并在实验报告中写出你的解题思路和具体过程。

## Bonus Task

misc 系列三节课已经结束了，希望你已经对 misc 类题目有了基本的了解，并且学会了一些基础 misc 题目的做法，养成了一点做 misc 的基本思维。

这 20 分我希望你能够自己回顾一下我们的这三节课，回顾一下：

1. 自己都学到了些什么，学会了什么，或者没学会什么
2. 有什么心得体会，有什么感悟，对于 misc 题有什么认识
3. 对于 misc 这三节课怎么评价，有没有什么想说的，或者想吐槽的
4. 有没有什么你想学但没学到的东西，或者希望我们改进的地方
5. 以后还想不想继续学习 CTF，继续学习 misc 之类的
6. 任何任何你想要说的话……

请思考一下这些问题，在报告里留下你想说的话。我们不会根据你总结的立场或者字数来进行打分，我们打分的标准是你总结的态度，换句话说，只要你认真思考了这些问题（不需要全部），表达出了你的想法，我们就会给你这 20 分。

---

misc 部分的 lab 到这里也就结束了，希望这三次课、三个 lab 给你带来了良好的体验，也希望你能够真正的有所收获。喜欢的话也希望你能在这条路上坚持下去。以后在学习 CTF、学习 misc 时有什么问题也可以来找我（TonyCrane）一起探讨，期待我们能 play misc together！