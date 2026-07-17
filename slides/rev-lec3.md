---
title: rev专题二 - 2025安全攻防实践
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

<!-- .slide: data-background="rev-lec3/background.png" -->

<br>
<br>
<br>
<center><h5 style="font-size: 55px; text-align: center;">Reverse专题二：异架构/游戏逆向</h5></center>
<br>
<br>
<center><h1 style="font-size: 30px; text-align: center;">2025.7.17</h1></center>
<br>
<center><div class="button-container" >
    <button class="button" onclick="toggleContent()" title = "Click to see more about me">
        <img src="rev-lec3/avatar.jpg" alt="Button Image">  
    </button>
    <span>张曹琛 @Das Schloss</span>
</div></center>



<!--s-->
<!-- .slide: data-background="rev-lec3/background.png" -->

<div class="middle center">
<div style="width: 100%">

# Part.1 WASM 逆向

前端 + 汇编 = ?

</div>
</div>

<!--v-->
<!-- .slide: data-background="rev-lec3/background.png" -->

## 普通前端代码

例题：osu!gaming ctf - wysi baby

<br>

- JavaScript：完全明文
- 可以混淆，但是难看且慢

<!--v-->
<!-- .slide: data-background="rev-lec3/background.png" -->

## wasm

例题：osu!gaming ctf - wysi revenge

<br>

- wasm 类似 LLVM BC 或者可执行文件
- 浏览器会自动转换成 WAT，类似 LLVM IR

<!--v-->
<!-- .slide: data-background="rev-lec3/background.png" -->

## 逆向方法

- ghidra wasm 插件
- JEB

<!--v-->
<!-- .slide: data-background="rev-lec3/background.png" -->

## 更多例题

- assembly online
- wasm rpg

<!--s-->
<!-- .slide: data-background="rev-lec3/background.png" -->

<div class="middle center">
<div style="width: 100%">

# Part.2 游戏引擎逆向

Unity

</div>
</div>

<!--v-->
<!-- .slide: data-background="rev-lec3/background.png" -->

## Mono

Unity 使用 Mono 架构，实现 .Net Framework 跨平台执行

<br>

C# 编译生成 MSIL，进而被执行

<!--v-->
<!-- .slide: data-background="rev-lec3/background.png" -->

## C# 逆向

类似 python，MSIL 非常容易被逆向回 C#

<br>

dnSpy：能将 MSIL 反汇编回 C#，并且支持 MSIL 甚至 C# 的修改

<!--v-->
<!-- .slide: data-background="rev-lec3/background.png" -->

## IL2CPP

把 MSIL 转换为 C++ 编码，之后编译成机器码

- 提高运行效率
- 解决 IOS 等平台不支持内置 .NET 虚拟机的问题
- 提高安全性

破解：IL2CPP Dumper

<!--v-->
<!-- .slide: data-background="rev-lec3/background.png" -->

## Unity 例题

- Perfect Match X-treme（Sekai CTF 2022）
- baby unity（XYCTF 2024）

<!--s-->
<!-- .slide: data-background="rev-lec3/background.png" -->

<div class="middle center">
<div style="width: 100%">

# Part.3 游戏机平台逆向

Nintendo - 从 FC 到 Switch

</div>
</div>

<!--v-->
<!-- .slide: data-background="rev-lec3/background.png" -->

## 架构

CPU 架构

- NES: 6502
- GB: Z80
- GBA: ARM v7
- NDS: ARM v9
- 3DS & switch: ARM v11

<br>

其中 6502 架构较为少见，ARM 虽使用较多，但由于 RISC 以及调试不方便，相比 Intel 汇编也更困难一点

<br>

不同主机/掌机平台的 ROM 格式也有区别

<!--v-->
<!-- .slide: data-background="rev-lec3/background.png" -->

## 逆向方法

静态调试：IDA 或者 ghidra 的 loader plugin

<br>

动态调试：各种模拟器

<!--v-->
<!-- .slide: data-background="rev-lec3/background.png" -->

## 例子

- NES
    - Rockman
- GBA
    - Hackergame 2021 GPA
    - 星之卡比 镜之大迷宫
- NDS
    - HSCTF 2021 hcsDS
- 3DS
    - 0ctf 2023 3ds boy
    - hxpctf 2021 hxp3drm

<!--s-->
<!-- .slide: data-background="rev-lec3/background.png" -->

<div class="middle center">
<div style="width: 100%">

# Part.4 windows平台游戏逆向

PlantsVsZombies

</div>
</div>

<!--v-->
<!-- .slide: data-background="rev-lec3/background.png" -->

## 重要工具

Cheat Engine

- 最主要的功能：内存搜索
- 支持多种扫描方式
- 可对内存进行修改或锁定
- 内置反汇编器等工具


<!--v-->
<!-- .slide: data-background="rev-lec3/background.png" -->

## 例子

植物大战僵尸

<br>

Cheat Engine 分析游戏 + CPP 编写游戏修改工具

<br>

- OpenProcess
- ReadProcessMemory
- WriteProcessMemory
- VirtualProtectEx

<!--v-->
<!-- .slide: data-background="rev-lec3/background.png" -->

## 其他游戏修改技术路线

- DLL 注入 + 卸载（CreateRemoteThread + LoadLibrary）
- Hook 技术 （IAT Hook，Inline Hook；SSDT Hook；DMA Attack）

<br>

如何反作弊？

<!--s-->
<!-- .slide: data-background="rev-lec3/background.png" -->

<div class="middle center">
<div style="width: 100%">


# 谢谢大家

---

# questions?

</div>
</div>
