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
<center><h5 style="font-size: 55px; text-align: center;">crypto 基础：消息加密 / 数字签名</h5></center>
<br>
<br>
<center><h1 style="font-size: 30px; text-align: center;">2025.7.6</h1></center>
<br>
<center><div class="button-container" >
    <button class="button" onclick="toggleContent()" title = "Click to see more about me">
        <img src="crypto-lec1/avator.jpg" alt="Button Image">  
    </button>
    <span>曹语 @WuYan / 晤言</span>
</div></center>

<!-- s -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->

## 在正式学习 crypto 之前
我对 crypto 的印象？
<div class="fragment" style="margin-top: 40px">

- 简洁、纯粹与优雅 (will be introduced later)
- 工具
    - basic: `python` + (`pwntools`)
    - advanced: `sage` + (`sympy` + `gmpy2` + `pycryptodome`)

</div>
<div class="fragment" style="margin-top: 40px">

- 讨厌->热爱 
    - 逐步深入理解的过程
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

# Part.1 消息加密

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

- shuffle 的可预测性？（插个眼）

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
    - Lab0 Challenge 1
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
    - 校巴: vigenere

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
for _ in range(7^7):
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

- 对某个小质数 p , 可知 (flag + yourinput) mod p != 0 , 即 flag mod p != -yourinput mod p
- 通过多次输入不同的 yourinput , 可以得到 flag mod p 的值
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
## 回到我们的主线
- 现代密码学需要解决古典密码的局限性
- 可能在不认识的人之间安全地传输信息
    - 需要公认的密码学加/解密算法
- 克尔克霍夫定律 ： 安全性应该依赖于密钥的秘密，而不是算法的秘密
- 对称加密（Symmetric Encryption）
    - 使用相同的密钥进行加密和解密
    - 例如：AES、DES、RC4
- 非对称加密（Asymmetric Encryption）
    - 使用一对密钥（公钥和私钥）进行加密和解密
    - 例如：RSA、ECC
- 哈希函数（Hash Function）
    - 将任意长度的输入转换为固定长度的输出，且不可逆
    - 例如：SHA-256、MD5

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
## 对称加密
- 使用相同的密钥进行加密和解密
- 分组密码
    - 将明文分成固定大小的块进行加密
    - 例如：AES、DES
    - 明文块 + 密钥 → [加密算法（复杂数学变换）] → 密文块
- 流密码
    - 例如：RC4、ChaCha20
    - 密钥 → [密钥流生成器] → 密钥流  
    - 明文 ⊕ 密钥流 → 密文
- 一些可能的加密要求

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->
## 流密码一般的攻击方式
- 密钥 → [密钥流生成器] → 密钥流 
- 密钥重用？
    - 明文1 ⊕ 密钥流 → 密文1
    - 明文2 ⊕ 密钥流 → 密文2
    - 明文1 ⊕ 明文2 = 密文1 ⊕ 密文2
- 基于语义分析的攻击
    - TPCTF 2025 Encrypted Chat

<p style="text-align: left; font-size: 30px; margin-top: 30px;">明文 m1 : "A quick brown fox jumps over the lazy dog."</p>
<p style="text-align: left; font-size: 30px; margin-top: 30px;">明文 m2 : "Hello, my friends from Chana. I'm Alan Walker."</p>


<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->
## 哈希函数
- 将任意长度的输入转换为固定长度的输出，且不可逆
- 明文块 + 哈希值 → [哈希函数（复杂数学变换）] → 新哈希值
- 常见的哈希函数
    - SHA-256：输出 256 位（32 字节）
    - SHA-1：输出 160 位（20 字节）
    - MD5：输出 128 位（16 字节）
- 安全性要求
    - 抗碰撞性：难以找到两个不同的输入产生相同的哈希值
    - 抗预映射性：难以从哈希值反推出原始输入
- 哈希碰撞攻击
- 哈希扩展攻击

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->

## 小总结
- 现代密码学的核心思想
    - 安全性依赖于密钥的秘密，而不是算法的秘密
    - 使用数学方法确保加密和解密的正确性
- 密码学的纯粹性质逐渐显现...
    - 关注的是算法的缺陷

<!-- s -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->

<div class="middle center">
<div style="width: 100%">

# Part.2 数字签名

</div>
</div>

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->

## *零知者证明
- 证明某个陈述的真实性，而不泄露任何其他信息
- Hash(m) = H
    - 证明者 Prover 想要证明 m 的哈希值是 H
- SJTU CTF 2025 ezHalo2

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

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->

## DSA 签名
- DSA 签名过程
    - https://www.cnblogs.com/Decisive/p/14607738.html

<div class="fragment" style="margin-top: 30px">

- 校巴 Democratic Signature Agency
    - 需要了解随机数重用/关联的攻击方式
- 优雅

</div>

<!-- s -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->

<div class="middle center">
<div style="width: 100%">

# Others

</div>
</div>

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->

## *随机数预测
- 让"偶然"变得均匀可靠
- 猜数字小游戏

    ```python
    import random
    while True:
        secret_number = random.getrandbits(7) + 1  # 生成1到128之间的随机数
        attempts = 0
        while attempts < 10:
            guess = int(input("猜一个1到128之间的数字: "))
            attempts += 1
            if guess < secret_number: ...
            elif guess > secret_number: ...
            else: ...
    ```
    - D3CTF 2025 d3guess
- shuffle 的可预测性?

<!-- v -->
<!-- .slide: data-background="crypto-lec1/background.webp" -->
## 线性同余生成器 (LCG)
- C语言随机数生成 rand
- 公式
    - X_{n+1} = (a * X_n + c) mod m
    - a, c, m 是常数，X_n 是当前的随机数
- 破解
    - https://zer0yu.github.io/2018/11/02/Cracking-LCG/

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