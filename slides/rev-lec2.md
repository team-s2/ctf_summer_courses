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
<center><h5 style="font-size: 55px; text-align: center;">Reverse专题一:游戏/异架构逆向</h5></center>
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
- Windows环境
- IDA keypatch插件
- 010Editor
- Cheat Engine(CE)
- x32/x64dbg
- ollydbg
- 对应架构的模拟器或调试工具


<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->

## 逆向专题一内容

- 异架构以及不同语言的逆向——本质 各种架构介绍
- 游戏逆向——目的  示例游戏的编写语言 游戏引擎

- NES 6502汇编 / GBA arm
- Windows 下的游戏逆向
- Unity 游戏逆向
- Javascript 逆向
- Python 逆向
- ...


<!--s-->
<!-- .slide: data-background="rev-lec2/background.png" -->

<div class="middle center">
<div style="width: 100%">


# Part.1 从FC/NES到Switch

</div>
</div>

<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->

## 架构及逆向方法介绍
- NES: 6502
- GBA: ARM v7
- NDS: ARM v9
- 3DS & switch: ARM v11
- 逆向方法
    - 静态分析：IDA或者ghidra
    - 动态调试：各种模拟器

<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->

## 红白机和6502汇编
- 6502有3个寄存器、栈指针、标志位(P)和程序计数器：寄存器是累加器(A)，X变址寄存器，和Y变址寄存器，每一个都是8位的，大多数指令把结果留在累加器里；
- [6502在线执行](https://codediy.github.io/nes-zh/easy6502/index.html) 

<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->

## 例1 Beginctf2024 红白机
- 6502汇编
- 试试上面的网站？

<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->

## GBA
- IDA Pro对ARM架构的支持
- mGBA模拟器调试
- 可以偷偷玩一下Pokemon，里面藏了个flag


<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->
## 例2 Hackergame2021 GPA
- IDA分析找到关键函数
- keypatch改变程序控制流
- .elf -> .gba 用010Editor对比修改关键字节


<!--s-->
<!-- .slide: data-background="rev-lec2/background.png" -->

<div class="middle center">
<div style="width: 100%">


# Part.2 Windows游戏PvZ逆向

<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->

## 工具
- IDA
- CE
- x32/x64dbg
- ollydbg
  
<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->
## Cheat Engine
- 有官方的CE教学12关
- 支持内存扫描
- 支持代码注入

<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->
## 例3 修改PvZ游戏内容
- 修改阳光
- 修改冷却时间
- 阳光自动收集
- 多种修改功能->整合->修改器或用于改版制作


<!--s-->
<!-- .slide: data-background="rev-lec2/background.png" -->

<div class="middle center">
<div style="width: 100%">


# Part.3 C#和Unity


</div>
</div>

<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->

## C#逆向工具
- Unity 使用Mono架构，实现 .Net Framework 跨平台执行
- C# 编译生成MSIL，进而被执行
- ILSpy
- dnSpy

<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->

## 例4 Perfect Match X-treme
- Assembly-CSharp.dll 是 Unity 游戏引擎编译后的核心脚本程序集，包含游戏开发者编写的 C# 代码逻辑
- 记忆力不行怎么办...行也没用
- 晕3d怎么办...不晕也没用
- dnSpy分析关键函数
- CE扫描内存偷flag
- 修改重力(MoveBehaviour.MovementManagement)和高度判断(HeightCheck)
- 或许其他方法？


<!--s-->
<!-- .slide: data-background="rev-lec2/background.png" -->

<div class="middle center">
<div style="width: 100%">


# Part.4 其他逆向


</div>
</div>

<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->

## Javascript
- 涉及混淆->反混淆
- 动态调试

<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->

## 例5 BeginCTF stickgame
- 反混淆 https://obf-io.deobfuscate.io/
- 动态调试
- 修改分数

<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->

## Python
- .pyc文件是 Python将.py源代码编译后生成的字节码文件
- 可以通过uncompyle6反编译
<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->

## 安卓-Java
- jadx
- 安卓模拟器

<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->

## Golang
- IDAGolangHelper

<!--s-->
<!-- .slide: data-background="rev-lec2/background.png" -->

<div class="middle center">
<div style="width: 100%">


# Part.5 其他

</div>
</div>

<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->

## 总结
- 游戏逆向为了什么？
    - 修改作弊？ 怀旧？ 了解原理？ 
    - 打比赛？ 上课？
- 架构千千万，学也学不完—>查阅资料和快速学习的能力十分重要


<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->

## 作业
- 基础：
    - 复现课上的题目例2 GPA

    - 复现课上的题目例4 Perfect Match X-treme

    - 复现课上的题目例5 stick game

    - 完成题目：微观世界，题目材料在学在浙大上给出，请于提交的报告中呈现逆向过程与结果

    - 完成题目：迷宫，题目材料在学在浙大上给出，请于提交的报告中呈现逆向过程与结果

- 挑战：
    - 尝试自己喜欢的游戏逆向/工具开发，可以描述逆向的原因，技术流程和结果等等（也可以查阅网上资料）。
    - 例子: Minecraft mod制作/Terraria失谐门等等


<!--v-->
<!-- .slide: data-background="rev-lec2/background.png" -->


## 预告
- 逆向专题2 "自动"逆向技巧 @f0rm2l1n 
    - 引言：人工密集型的逆向过程
    - 基础：符号执行器基础 - 以 angr 为例
    - 实战：符号执行用于自动化逆向
    - 反思：符号执行存在的不足
    - 拓展：其他"自动"化技巧探讨
- Maybe他自己的一些逆向经验见解分享

<!--s-->
<!-- .slide: data-background="rev-lec2/background.png" -->


<div class="middle center">
<div style="width: 100%">


# 谢谢大家~希望大家能够喜欢上逆向！
---
# Questions?
Contact me? QQ 917581079

</div>
</div>