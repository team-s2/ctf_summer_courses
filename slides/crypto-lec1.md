---
title: Crypto基础 - 2025安全攻防实践
separator: <!-- s -->
verticalSeparator: <!-- v -->
theme: simple
highlightTheme: monokai-sublime
css:
    - custom.css
    - dark.css
revealOptions:
    transition: 'slide'
    transitionSpeed: fast
    center: false
    slideNumber: "c/t"
    width: 1000
---

<style>
@import url('https://cdn.jsdelivr.net/npm/lxgw-wenkai-webfont@1.1.0/style.css');

  html * {
    font-family: 'LXGW WenKai', sans-serif !important;
}
    .button-container {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 20px;
    position: relative;
    width: 100%; 
}


        .button {
            display: flex;
            align-items: center;
            justify-content: center;  
            text-decoration: none;
            border: 1px solid #ddd;
            padding: 0; 
            border-radius: 50%;  
            width: 85px; 
            height: 85px; 
            transition: transform 0.3s ease, border-color 0.3s ease;  
            cursor: pointer;
            overflow: hidden;
        }

        .button img {
            width: 100%;  
            height: 100%;  
            object-fit: cover;  
            border-radius: 50%;  
        }

        .button:hover {
            transform: scale(1.1);
            border-color: rgba(0, 123, 255, 0.2);
            box-shadow: 0 2px 10px rgba(0, 123, 255, 0.2); 
        }

        .button-container .button-text {
            position: absolute; 
            top: 50%;
            left: 100%;  
            transform: translateY(-50%); 
            opacity: 0;  
            visibility: hidden;  
            transition: opacity 0.3s ease, visibility 0.3s ease;
            white-space: nowrap; 
            font-size: 20px;
        }
    </style>

<!-- .slide: data-background="crypto-lec1/background.webp" -->

<br>
<br>
<br>
<center><h5 style="font-size: 55px; text-align: center;">crypto 基础：消息加密</h5></center>
<br>
<br>
<center><h1 style="font-size: 30px; text-align: center;">2026.7.12</h1></center>
<br>
<center><div class="button-container" >
    <button class="button" onclick="toggleContent()" title = "Click to see more about me">
        <img src="crypto-lec1/avator.jpg" alt="Button Image">  
    </button>
    <span>曹语   @WuYan（晤言） · 23级图灵</span>
</div></center>

<!-- s -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->

## 在正式学习 crypto 之前

- 匿名留言板 http://wuy4n.com:9999/
- 你们对 crypto 的印象？

<div class="fragment" style="margin-top: 40px">

我对 crypto 的印象？
- 简洁、纯粹与优雅 (will be introduced later)
- 工具
    - basic: `python` + (`pwntools`)
    - advanced: `sage` + (`sympy` + `gmpy2` + `pycryptodome`)
    - AI?

</div>
<div class="fragment" style="margin-top: 40px">

- 讨厌->热爱 (逐步深入理解的过程)
    - 意义驱动型人格
    - 从根源上明白它(算法) 为什么可以这样存在/存在的意义

</div>

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->

## Why Crypto?
- Crypto is not password
- 起源
    - 战争导致军事机密概念的出现
    - 古希腊 滚筒密码

        <img src="crypto-lec1/introduce.png" alt="Dremig is a big turtle" height=120>

- 一切想要通过数学方法隐藏消息的行为都可以称为 crypto
    - 日常生活
    - 存储/传输数据 容易被篡改/泄露

<!-- s -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->

<div class="middle center">
<div style="width: 100%">

# Part.1 古典密码

</div>
</div>

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->

## Start from a single message

<p style="text-align: center; font-size: 30px; margin-top: 30px;">明文 (m)essage : "Hello, world!"</p>

<div class="fragment" style="margin-top: 30px">

<p style="text-align: center; font-size: 30px; margin-top: 30px;">密文 (c)ipher : "l!e,Hrdoowll "</p>

- 怎么解密？
```python
from random import shuffle
m = "Hello, world!"
t = [i for i in m]
shuffle(t)
c = ''.join(t)
```

- shuffle 的可预测性？（python 随机数预测）

</div>

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->

## 置换密码

- 将明文中的字符按照某种规则重新排列
- 置换表

    <img src="crypto-lec1/transposition.png" alt="Dremig is a big turtle" height=50>
- 长度不同导致的填充问题
    - 填充什么？（空格、固定字符、随机字符）

<div class="fragment" style="margin-top: 30px">

<p style="text-align: center; font-size: 30px; margin-top: 30px;">密文 (c)ipher : "l,Hoelod lwr==!==="</p>

</div>

<div class="fragment" style="margin-top: 30px">

- 算法的弊端？
    - 暴力破解
    - 部分时候中文的顺序并不影响可读性
</div>

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->

## 凯撒密码
- 将明文的每个字母按字母表循环移动固定位数得到密文
- 例如：将字母表向右移动 3 位
    - A -> D, B -> E, C -> F, ..., X -> A, Y -> B, Z -> C
- 密钥 (key) : 3 (ROT13/ROT47)

<div class="fragment" style="margin-top: 0px">

<img src="crypto-lec1/fun.png" alt="Dremig is a big turtle" height=400 class="center">

</div>

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->

## 单表替换
- 将明文中的每个字符替换为另一个字符
- 凯撒加密 enc(x)=(x+key) mod 26
- 仿射密码 enc(x)=(x∗key1+key2) mod 26
- ...

<div class="fragment" style="margin-top: 30px">

<p style="text-align: center; font-size: 30px; margin-top: 30px;">明文 m : "A quick brown fox jumps over the lazy dog."</p>
<p style="text-align: center; font-size: 30px; margin-top: 30px;">密文 c : "D txlfn eurzq ira mxpsv ryhu wkh odcb grj."</p>
</div>

<div class="fragment" style="margin-top: 30px">

- 可攻击性
    - 频率分析 (需要足够长的文本)
    - https://www.quipqiup.com/
</div>

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->

## 跳舞的小人

<img src="crypto-lec1/chal1.png" alt="Dremig is a big turtle" height=400 class="center">

<div class="fragment" style="margin-top: 30px">

- 典型的单表替换 + 图像处理（or 人工标注？）

</div>

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->

## 多表替换-维吉尼亚密码
- 密钥 key 的作用

<div class="fragment" style="margin-top: 30px">

- 第i个字符使用第i个密钥进行偏移
- 密钥任意长，并且以循环使用
- 加密函数 enc(x)=(x+key[i mod len(key)]) mod 26

<p style="text-align: center; font-size: 30px; margin-top: 30px;">明文 m: "HELLO!"</p>
<p style="text-align: center; font-size: 30px; margin-top: 30px;">密钥 key: "KEY"</p>

</div>

<div class="fragment" style="margin-top: 30px">

<p style="text-align: center; font-size: 30px; margin-top: 30px;">密文 c : "RIJVS!"</p>

- 一定程度上抵御了频率分析

</div>

<div class="fragment" style="margin-top: 30px">

- 仅仅只有26个字母？
    - 校巴: vigenere (变种)

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->

## 小总结
- 古典密码的局限性
    - 密钥空间小（暴力破解）
    - 频率分析
    - 仅适用于小规模通信

- 密码学的简单性逐渐显现...
    - 极为简洁的题目以及答案
    - 较为复杂的推理过程

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->
## *onelinecrypto
- 一行代码的密码学
- 京麒 CTF 2025
```python
assert __import__('re').fullmatch(br'flag\{[!-z]{11}\}',flag) and [is_prime(int(flag.hex(),16)^^int(input('🌌 '))) for _ in range(7^7)]
```

<div class="fragment" style="margin-top: 30px">

- 翻译成 python
```python
flag = int(('flag{'+'?'*11+'}').encode().hex(),16)
for _ in range(7**7):
    yourinput = int(input('🌌 '))
    is_prime(flag ^ yourinput)
```
</div>
<div class="fragment" style="margin-top: 30px">

- 测信道获取 is_prime 的判断
</div>

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->
## *onelinecrypto
- 构造足够大的 input 使得 flag ^ input = flag + input
```python
is_prime(flag + yourinput)
```
<div class="fragment" style="margin-top: 30px">

- (flag + yourinput)为质数，说明对于任意某个小质数 p , 可知 (flag + yourinput) mod p != 0 , 即 flag mod p != -yourinput mod p
- 取某个特定小质数 p , 通过多次输入不同的 yourinput , 筛选多个 flag mod p != -yourinput mod p，可以得到 flag mod p 的值
- 取多对质数 p , 可以通过中国剩余定理得到 flag 的值

</div>

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->
## 中国剩余定理（CRT）
- 从两个同余方程组开始
- 设有两个同余方程组：
    - x ≡ a1 (mod m1)
    - x ≡ a2 (mod m2)
- 如果 m1 和 m2 互质，则存在唯一的解 x (mod m1 * m2)
- 解法：
    - 计算 m = m1 * m2
    - 计算 m1 的逆元 inv1 (mod m2)
    - 计算 m2 的逆元 inv2 (mod m1)
    - x = (a1 * inv2 * m2 + a2 * inv1 * m1) mod m

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->
## 冰山一角
- 京麒 CTF 2026 - onelinecrypto （多项式+格密码）
```python
R.<x>=PolynomialRing(GF(3329));h=R.random_element(224);input(flatten([list(choice((-1,1))*h%p) for p,_ in factor(x**256+1)]))==str(h) and print("flag{*}")
```
- ZJUCTF 2025 - Fall in love （三行诗+随机数预测）
```python
[poem := input("$ "), love := __import__("random").Random(int(poem, 16)), hate := __import__("random").Random(__import__("os").urandom(666)), heart := lambda x: x.randint(1, 1314)]
assert poem.startswith(b"I love three things: the sun, the moon and you.".hex()) and poem[len(poem) // 2 :].startswith(b"The sun is for the day, the moon is for the night".hex()) and poem.endswith(b"and you forever.".hex())
print(__import__("i_love_u").flag if all([heart(love) > heart(hate) for _ in range(520)]) else "Hatred blinds us…")
```

<!-- s -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->

<div class="middle center">
<div style="width: 100%">

# Part.2 现代密码

</div>
</div>

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->
## 回到我们的主线
- 现代密码学需要解决古典密码的局限性
- 可能在不认识的人之间安全地传输信息
    - 需要公认的密码学加/解密算法
- 克尔克霍夫定律 ： 安全性应该依赖于密钥的秘密，而不是算法的秘密
- 非对称加密（Asymmetric Encryption）
    - 使用一对密钥（公钥和私钥）进行加密和解密
    - 例如：RSA、ECC
- 对称加密（Symmetric Encryption）
    - 使用相同的密钥进行加密和解密
    - 例如：AES、DES、RC4

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->
## 对称加密
- 使用相同的密钥进行加密和解密
- 分组密码
    - 将明文分成固定大小的块进行加密
    - 例如：AES、DES
    - 明文块 + 密钥 → [加密算法（复杂数学变换）] → 密文块
    - 密文块 + 密钥 → [解密算法（复杂数学变换）] → 明文块
- 流密码
    - 例如：RC4、ChaCha20
    - 密钥 → [密钥流生成器] → 密钥流  
    - 明文 ⊕ 密钥流 → 密文

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->
## 流密码一般的攻击方式
- 密钥 → [密钥流生成器] → 密钥流 
- 密钥重用？
    - 明文1 ⊕ 密钥流 → 密文1
    - 明文2 ⊕ 密钥流 → 密文2
    - 明文1 ⊕ 明文2 = 密文1 ⊕ 密文2
- 基于语义分析的攻击（古典密码的频率分析）
    - TPCTF 2025 Encrypted Chat

<p style="text-align: left; font-size: 30px; margin-top: 30px;">明文 m1 : "A quick brown fox jumps over the lazy dog."</p>
<p style="text-align: left; font-size: 30px; margin-top: 30px;">明文 m2 : "Hello, my friends from Chana. I'm Alan Walker."</p>

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->
## 非对称加密
- 不同的密钥
    - 使用一对密钥（公钥和私钥）进行加密和解密
    - 公钥 (public key) ：用于加密消息，公开给所有人
    - 私钥 (private key) ：用于解密消息，只有接收者知道
- bytes(message) -> int(message) -> int(ciphertext) -> bytes(ciphertext)
    - 通过引入数学方法来创造更多的可能性

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->
## RSA
- 密钥生成：
    - 选择两个大素数 p 和 q
    - 计算 n = p * q
    - 计算 φ(n) = (p-1) * (q-1)
    - 选择公钥 e，使得 1 < e < φ(n) 且 gcd(e, φ(n)) = 1
    - 计算私钥 d，使得 d ≡ e^(-1) (mod φ(n))
- 公钥 (n, e) 和私钥 (n, d)
- 加密：c ≡ m^e (mod n)
- 解密：m ≡ c^d (mod n)
- 正确性：
    - m ≡ (m^e)^d (mod n) ≡ m^(e*d) (mod n) ≡ m^(1 + k*φ(n)) (mod n) ≡ m (mod n)

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->
## Some 数学基础
- 费马小定理 
    - 如果 p 是素数，a 是整数且 a 不被 p 整除，则有 a^(p-1) ≡ 1 (mod p)
    - https://zhuanlan.zhihu.com/p/352730090
- 欧拉定理
    - 如果 a 和 n 互质，则有 a^φ(n) ≡ 1 (mod n)
    - φ(n) 是欧拉函数，表示小于 n 且与 n 互质的正整数的个数
    - https://www.cnblogs.com/1024th/p/11349355.html

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->

## 小总结
- 现代密码学的核心思想
    - 安全性依赖于密钥的秘密，而不是算法的秘密
    - 使用数学方法确保加密和解密的正确性
- 密码学的纯粹性质逐渐显现...
    - 关注的是算法的缺陷

<div class="fragment" style="margin-top: 30px">

- Why Crypto?
    - 一切想要通过数学方法隐藏消息的行为都可以称为 crypto 
    - 数据传输 / 篡改 / 以及拥有者证明
    - 需要有一种办法证明消息是我发的/我知道的

</div>

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->

## 数字签名
- 证明某个消息是由特定的发送者发送的
- 发送者使用自己的私钥对消息进行签名
- 接收者使用发送者的公钥验证签名的真实性
- 著名的数字签名算法
    - RSA 签名
    - DSA（数字签名算法）
    - ECDSA（椭圆曲线数字签名算法）
- RSA 签名验证
    - 发送者签名：s ≡ m^d (mod n)
    - 接收者验证：m' ≡ s^e (mod n)
    - 如果 m' = m，则签名有效

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->
## *SSH 使用 RSA
- SSH 协议使用 RSA 进行密钥交换和身份验证
- 服务器端存储公钥信息
    ```
    <算法类型> <Base64编码数据> [注释]
    ssh-rsa AAAAB3NzaC1yc2E...DAVg== user@host
    ```
- 客户端持有私钥
    ```
    -----BEGIN RSA PRIVATE KEY-----
    base64_decode(DER二进制)
    -----END RSA PRIVATE KEY-----
    ```

<div class="fragment" style="margin-top: 30px">

- http://www.shangyang.me/2017/05/24/encrypt-rsa-keyformat/
- 发送的 m 是什么？
    - https://blog.csdn.net/wang_qiu_hao/article/details/127902007
</div>

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->

## *零知者证明
- 证明某个陈述的真实性，而不泄露任何其他信息
- Schnorr 协议
    - 设有一个大素数 p 和一个生成元 g
    - 证明者 Prover 拥有一个秘密 x，使得 y = g^x (mod p)
    - 证明者想要向验证者 Verifier 证明自己知道 x，而不泄露 x 的值
        1. Prover 选择一个随机数 r，计算 t = g^r (mod p)，并将 t 发送给 Verifier
        2. Verifier 选择一个随机挑战 c，并将 c 发送给 Prover
        3. Prover 计算 s = r + c*x (mod p-1)，并将 s 发送给 Verifier
        4. Verifier 验证 t * y^c ≡ g^s (mod p)
- Hash(m) = H
    - 证明者 Prover 想要证明 m 的哈希值是 H (SJTU CTF 2025 ezHalo2)
- 优雅

<!-- s -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->

## Others
- 随机数预测
- 哈希函数（哈希扩展攻击）
- 讲讲当下 AI 对密码学的冲击
    - 越来越多的密码学（数论知识）被放进预训练数据中
    - （简单/纯粹/优雅）的优点利好 agent 更好更快的解决密码难题
    - aliyun CTF 线下沙龙 （学术/企业）

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->

## Takeaway
- 基础
    - 跳舞的小人 10pt (要有从解析图片到单表替换密文再到明文的链路)
    - 维吉尼亚密码 40 pt 
- 拓展
    - RSA 50 pt
- Bonus 15pt
    - 驾驭 AI 大师： 用 DeepSeek **单prompt** 完成跳舞的小人从解析图片到单表替换密文。
    - 自行设计算法： 要有一定的安全性（分析潜在的攻击可能）
    - 取证大王： 有能力找到去年的文档并完成去年的拓展部分任意一题
    - 课程评价 （0-3pt）


<!-- s -->

<br>
<br>
<br>

<center><h5 style="font-size: 55px; text-align: center;">谢谢大家~ 辛苦啦!</h5></center>

<br>

<strong><center><h5 style="font-size: 40px; text-align: center;">Questions?</h5></center></strong>

<br>

<center>
    <span>曹语 @WuYan / 晤言</span>
</center>

<br>

<strong><center>
    <span style="font-size: 25px;">What to contact with me?</span>
</center></strong>
<center>
    <span style="font-size: 22px;">QQ: 1450567107</span>
</center>