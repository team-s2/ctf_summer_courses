---
title: rev专题二 - 2024安全攻防实践
separator: <!--s-->
verticalSeparator: <!--v-->
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

<!-- .slide: data-background="rev-lec3/cover.png" -->
<!--s-->
<!-- .slide: data-background="rev-lec3/background.png" -->

<div class="middle center">
<div style="width: 100%">

# Part.1 Esolang - VM 逆向

Turing Complete

</div>
</div>

<!--v-->
<!-- .slide: data-background="rev-lec3/background.png" -->

## Esolang

An esoteric programming language is a computer programming language designed to experiment with weird ideas, to be hard to program in, or as a joke, rather than for practical use.

<!--v-->
<!-- .slide: data-background="rev-lec3/background.png" -->

## 示例程序

./bf

- hw.bf
- 1.bf
- 2.bf

<br>

通过 gdb 动态调试逆向分析 bf 的逻辑

<!--v-->
<!-- .slide: data-background="rev-lec3/background.png" -->

## brainfxxk

<div class="three-line">

| 指令 | 效果 |
| :--: | :--: |
| > | 指针加一（右移一位）|
| < | 指针减一（左移一位）|
| +   | 指针指向的单元的值加一 |
| - |指针指向的单元的值减一 |
| . | 输出指针指向的单元内容（ASCII码） |
| , | 输入内容到指针指向的单元（ASCII码） |
| [ | 若指针指向的单元值为零，向后跳转到对应的 ] 指令的次一指令处 |
| ] | 若指针指向的单元值非零，向前跳转到对应的 [ 指令的次一指令处 |

</div>

<!--v-->
<!-- .slide: data-background="rev-lec3/background.png" -->

## VM 调试

用 C++ 或者 python 模拟执行 VM 指令，进行调试

- 打印当前步骤的 IP，具体指令，具体修改
- 如果 data 段较小的话也可以每一步打印 data 段的所有内容
- 高级玩法：污点分析，将输入设为污点数据，对污点的读取修改进行断点，若污点对其他数据产生影响则传递污点（对指令更高级的 VM 效果可能更好）

<!--v-->
<!-- .slide: data-background="rev-lec3/background.png" -->

## VM 例题

- NoRegVM（m0lconCTF Teaser 2023）
- ichicken (ZJUCTF 2023)

<!--s-->
<!-- .slide: data-background="rev-lec3/background.png" -->

<div class="middle center">
<div style="width: 100%">

# Part.2 WASM 逆向

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
- wasm rpg（作业）

<!--s-->
<!-- .slide: data-background="rev-lec3/background.png" -->

<div class="middle center">
<div style="width: 100%">

# Part.3 游戏引擎逆向

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

## Mono 例题

- Perfect Match X-treme（Sekai CTF 2022）
- Azusawa’s Gacha World（Sekai CTF 2023）
- ecs!catch（osu!gaming CTF）

<!--v-->
<!-- .slide: data-background="rev-lec3/background.png" -->

## IL2CPP

把 MSIL 转换为 C++ 编码，之后编译成机器码

- 提高运行效率
- 解决 IOS 等平台不支持内置 .NET 虚拟机的问题
- 提高安全性

破解：IL2CPP Dumper

<!--s-->
<!-- .slide: data-background="rev-lec3/background.png" -->

<div class="middle center">
<div style="width: 100%">

# Part.4 游戏机平台逆向

从 FC 到 Switch

</div>
</div>

<!--v-->
<!-- .slide: data-background="rev-lec3/background.png" -->

## 架构

CPU 架构

- NES: 6502
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
    - 星のカービィ 鏡の大迷宮
- NDS
    - HSCTF 2021 hcsDS
- 3DS
    - 0ctf 2023 3ds boy
    - hxpctf 2021 hxp3drm

<!--s-->
<!-- .slide: data-background="rev-lec3/ending.png" -->