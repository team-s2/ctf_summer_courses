# crypto lab 2: AES, RSA & LWE

实验需要提交实验报告。每道做出来的题均需要写在实验报告中，否则无法给分。**实验报告需要写出每道题的思路并贴上攻击脚本（payload）**。对于没法完整做出的题，也可以叙述自己的思路和解题过程，会酌情给分。

今年仍旧有**15分的保底分**（可能也会调整），只要提交作业，成功做出任意一题就能拿到，今年的保底分直接加到最后分数中，因此其实你**只需拿到85分就能满了**。本次虽然所有作业总分为155分，不过最多只能获得15分的bonus，加满为止，所以可以合理选取作业题目。

本次crypto lab对python以及sage的要求会比较高，如果认为自己对python的了解还是不够的话，请务必善用搜索引擎，并积极向助教们提问（对于密码学库的问题尽量咨询密码学方向助教，不过其它python相关问题可以询问所有助教）

本次有两道题目部署在[ZJU::CTF](https://ctf.zjusec.com/games/3)平台，有两道为校巴上的题目，另外还有一道CryptoHack上的题目，可以在上面提交flag验证是否正确。

**\* 声明：由于前两年抄袭现象较为严重，本次作业所有题目都会进行查重，查到就不仅仅是这次Lab得0分了😨**

## AES部分

- 完成课上例题CBC Byte Flip，题目部署在ZJUCTF平台，本题分值为20分
- 完成课上例题Padding Oracle，部署在ZJUCTF平台上，本题分值为30分

## RSA部分

- 完成[校巴](https://zjusec.com)上的Republican Signature Agency这道题，学习RSA选择明/密文攻击，地址为10.214.160.13:12505，分值25分
- 来道简单的Coppersmith攻击练练手，题目名是Crush On Proust，在校巴上可以看到，题目不算太难，但对数学要求较高，本题分值35分

## 格密码

- 来点CryptoHack，CryptoHack - Post Quantum - Learning With Errors - Noise Cheap，本题分值30分