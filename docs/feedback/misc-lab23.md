# Misc Lab 2/3 批改反馈

这里集中反馈一下 misc lab 2/3 批改过程中遇到的一些共性问题，以及一些成题的来源和题解。

## Lab 2
### Challenge 1/2/3

三道基础的图片隐写，大家完成的也都很好，相信 Background 部分的图片隐写简单一把梭就可以轻松解决这三道题。

前两题都是校巴上的题，所以这里就不放出相关解法之类的了。

第三题的 LSB 按照 BGR 三个通道的顺序来提取最低位即可，得到的是一张 png 图片的二进制。这个顺序什么的可以通过 stegsolve/CyberChef 尝试来得到，或者 zsteg 自动枚举也可以。同时注意这里的隐写内容是一张图片，而不是直接的 flag，所以在这种过程中要注意任何可疑的文件类型，而不要仅仅关注 flag 格式或者纯文本。

### Challenge 4: Palette Stego

出这道题的思路是 2022 TQLCTF 的一道隐写题目 Cat&Soup 里面一部分利用了 EZStego 这个调色盘隐写算法，所以就改了这么一道题目。当时的 writeup：

- [官方 writeup](https://datacon.qianxin.com/blog/archives/386)，这道题目在 pdf 第 25 页
- [一个复现 writeup by @c10udlnk](https://www.cnblogs.com/c10udlnk/p/15926071.html)

直接搜一搜 EZStego 的相关原理，然后照着原理写代码就可以了，具体代码可以去看第二个 writeup，里面也给了两篇 EZStego 相关的文章链接：

- ["Waiter! There's a Message in My Soup!"](https://supercomputingchallenge.org/02-03/finalReports/022.pdf)
- [《EzStego的嵌入、提取与检测的C++实现》](http://www.cqvip.com/qk/95033x/200622/23338153.html)

这道题我 flag 是直接一个字符=一个字节=八个比特来的，所以它甚至可以直接通过 zsteg -a 来解出来，这样做的我没有任何扣分，毕竟也拿到 flag 了：

```text
❯ zsteg -a chal.png | grep AAA
b1,g,lsb,xy         .. text: "...AAA{gOoD_joB_P4lEtTE_M0D3_c@N_al$0_57E9o!}......AAA{gOoD_joB_P4lEtTE_M0D3_c@N_al$0_57E9o!}......AAA{gOoD_joB_P4lEtTE_M0D3_c@N_al$0_57E9o!}......AAA{gOoD_joB_P4lEtTE_M0D3_c@N_al$0_57E9o!}......AAA{gOoD_joB_P4lEtTE_M0D3_c@N_al$0_57E9o!}......AAA{gOoD_joB_"
b1,g,msb,XY         .. text: "$la_N@c_3D0M_ETtEl4P_Boj_DoOg{AAA......}!o9E75_0$la_N@c_3D0M_ETtEl4P_Boj_DoOg{AAA......}!o9E75_0$la_N@c_3D0M_ETtEl4P_Boj_DoOg{AAA......}!o9E75_0$la_N@c_3D0M_ETtEl4P_Boj_DoOg{AAA......}!o9E75_0$la_N@c_3D0M_ETtEl4P_Boj_DoOg{AAA......}!o9E75_0$la_N@c_3D0M_ETt"
b1,g,msb,Xy         .. text: "A......}!o9E75_0$la_N@c_3D0M_ETtEl4P_Boj_DoOg{AAA......}!o9E75_0$la_N@c_3D0M_ETtEl4P_Boj_DoOg{AAA...g{AAA......}!o9E75_0$la_N@c_3D0M_ETtEl4P_Boj_DoOg{AAA......}!o9E75_0$la_N@c_3D0M_ETtEl4P_Boj_DoOg{AA_DoOg{AAA......}!o9E75_0$la_N@c_3D0M_ETtEl4P_Boj_DoOg{AA"
b1,g,lsb,xY         .. text: "_al$0_57E9o!}......AAA{gOoD_joB_P4lEtTE_M0D3_c@N_al$0_57E9o!}......AAA{gOoD_joB_P4lEtTE_M0D3_c@N_al$_c@N_al$0_57E9o!}......AAA{gOoD_joB_P4lEtTE_M0D3_c@N_al$0_57E9o!}......AAA{gOoD_joB_P4lEtTE_M0D3_c@NM0D3_c@N_al$0_57E9o!}......AAA{gOoD_joB_P4lEtTE_M0D3_c@N"
```

我承认阁下的 zsteg 确实厉害，但倘若我和 Cat&Soup 一样一个字符只有 7 bit，阁下又该如何应对呢？（x

### Challenge 5: Spectrogram

这题是从 Hackergame 2021 的 p😭q 改编的（其实就是换了个源音频），做法直接根据代码逆过来就可以了。原题的 writeup：

- [官方 writeup](https://github.com/USTC-Hackergame/hackergame2021-writeups/blob/master/official/p%F0%9F%98%ADq/README.md)
- [我当时的 writeup](https://note.tonycrane.cc/writeups/hackergame2021/#pq)

这里我用的源音频是辨识度极高的 Never Gonna Give You Up 的开头，听过的应该都能一下子认出来（

### Challenge 6: Huffman Stego

这题的原题是 MRCTF 2022 的 jpeg and the tree。我的更改也就是换了个 flag 而已。原题的 writeup：

- [官方 writeup](https://github.com/BuptMerak/mrctf-2022-writeups/blob/main/offical/MISC.md#jpeg-and-the-tree)
    - writeup 里面也提供了很多链接，以及完整的解法

原题比赛时的 hint 是灵感来自 Google CTF 2021，是 zip 文件中的冗余哈夫曼编码的问题，要比这个简单一点，也可以看一下，writeup：[Google CTF: David and the Tree](https://room2042.gitlab.io/writeup/2021-07-24-google_ctf-david_and_the_tree/)。

时间原因没有做这题的还是建议有空来复现一下，个人认为是对 JPEG 文件格式的很好的复习。以及有兴趣的也可以考虑/实现一下把解答过程反过来，即这道题是怎么出的。

## Lab 3
### Challenge 1: SQL Inject Analysis
这题是 BUUCTF 上的一道成题 [sqltest](https://buuoj.cn/challenges#sqltest)。直接分析请求内容，解析 SQL 盲注即可。这题的 writeup 也很多，直接搜 "BUUCTF sqltest" 就能搜到很多 writeup。

### Challenge 2: dnscap
这题是 BSides San Francisco CTF 2017 的原题 dnscap.pcap。同样也能搜到很多现有的 writeup，甚至 CTF Wiki 上 DNS 协议部分的例题解析就是这道：

- [CTF Wiki > Misc > 流量包分析 > 协议分析 > DNS#例题](https://ctf-wiki.org/misc/traffic/protocols/dns/#_2)

有些同学还止步于对着 DNS 请求的内容从十六进制转为 ASCII 字符，然后删减重复的部分试图拿到 png。我都写了要去看一下 dnscat 协议的，根据那个舍弃多余数据再提取就能直接拿到完整 png 了。而且有同学甚至写了 pcap 包解析的完整代码来提取内容，感觉有些太没必要了，wireshark 的 tshark 已经很方便了，而且我上课也演示过用法，为什么不用呢。

### Challenge 3: crack_zju_wlan
校巴上的题目，做法不多解释。

主要问题是解压得到了 .img 文件之后有些同学不知道怎么处理。直接手动从里面摘 pcap 文件肯定是不太好的，binwalk/foremost 什么的其实也可以。这个 img 的意思是镜像文件（甚至有同学还以为是图片可还行），所以正经做法是直接挂载它或者用 7z 之类的软件来解压。解压之后观察解压后的全部内容，套用工具求解即可。

### Challenge 4: volatility 安装与使用
其实 volatility 安装说简单也不算简单，说复杂也不是那么复杂。要做的其实就是先搞出一个干干净净的 python 2.x 的环境（所以推荐使用 conda），然后执行 setup.py 安装，再补充一下部分插件需要的 pycrypto 和 distrom3 两个包就可以了。

复现也不必多说，我上课都演示过了。

剩下的 Challenge 5 就留给大家有兴趣的话自行研究吧。