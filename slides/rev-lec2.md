---
title: rev专题一 - 2025安全攻防实践
separator: <!--s-->
verticalSeparator: <!--v-->
theme: simple
highlightTheme: github
css:
    - custom.css
revealOptions:
    transition: 'slide'
    transitionSpeed: fast
    center: false
    slideNumber: "c/t"
    width: 1000

---


<style>
@import url('https://cdn.jsdelivr.net/npm/lxgw-wenkai-webfont@1.1.0/style.css');

  /* html * {
    font-family: 'LXGW WenKai', sans-serif !important;
} */
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

<!-- .slide: data-background="rev-lec2/background.png" -->

<br>
<br>
<br>
<center><h5 style="font-size: 55px; text-align: center;">Reverse专题一: 游戏/异架构逆向</h5></center>
<br>
<br>
<center><h1 style="font-size: 30px; text-align: center;">2025.7.9</h1></center>
<br>
<center><div class="button-container" >
    <button class="button" onclick="toggleContent()" title = "Click to see more about me">
        <img src="rev-lec2/avator.jpg" alt="Button Image">  
    </button>
    <span>黄一航 @huayi</span>
</div></center>



<!--s-->
<!-- .slide: data-background="rev-lec2/background.png" -->


<div class="middle center">
<div style="width: 100%">


# Part.0 准备工作

</div>
</div>

<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->

## 准备工作

一些需要安装的工具

- windows环境
- CE
- x64dbg/ollydbg

<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->

## 逆向专题一内容

- 异架构以及不同语言的逆向——本质 各种架构介绍
- 游戏逆向——目的  示例游戏的编写语言 游戏引擎
- 6502汇编 NES （BeginCTF红白机）

- Windows下的游戏逆向（pvz CE）

- Python逆向（反编译pyc）

- 古早Java游戏（诺基亚贪吃蛇）

- Javascript逆向（网页小游戏+代码混淆）

- Unity游戏逆向（C# dnspy）


<!--s-->
<!-- .slide: data-background="rev-lec2/background.png" -->

<div class="middle center">
<div style="width: 100%">


# Part.1 红白机和GBA

</div>
</div>

<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->

## 红白机（NES）和6502


<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->

## GBA


<!--s-->
<!-- .slide: data-background="rev-lec2/background.png" -->

<div class="middle center">
<div style="width: 100%">


# Part.2 JAVA和诺基亚

</div>
</div>


<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->

## Java

- 编译型语言，编译得到 Java 字节码
  - 通过解释字节码实现跨平台
- 反编译工具
  - JD-GUI / Jadx / Fernflower
- Android 逆向
  - 采用的是 Dalvik 字节码 / Smali
  - apktool / frida / Android Studio
- 综合性较强的题目
  - 涉及到 Java 反射 / 字节码操作 / 本地方法

<!--s-->
<!-- .slide: data-background="rev-lec2/background.png" -->

<div class="middle center">
<div style="width: 100%">


# Part.3 Windows游戏逆向示例-PvZ

</div>
</div>


<!--s-->
<!-- .slide: data-background="rev-lec2/background.png" -->

<div class="middle center">
<div style="width: 100%">


# Part.4 其他语言的逆向

</div>
</div>

<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->


## Python
- Python 在 import 时会生成 .pyc 文件
  - 可以通过 uncompyle6 反编译


<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->

## Javascript

<!--s-->
<!-- .slide: data-background="rev-lec2/background.png" -->


<div class="middle center">
<div style="width: 100%">


# 谢谢大家
---
# questions?

</div>
</div>