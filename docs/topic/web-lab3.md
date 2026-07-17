# Web Lab 3：后端漏洞基础

## 前言

本次作业的三道题目全部发布在[ZJUCTF平台](https://ctf.zjusec.net/games/7/challenges)上。每道题目背后的漏洞都可以在PPT上可以找到原理、利用方式和常用的攻击语句。只要做出题目且步骤齐全就会给满分，做不出答案但是能呈现完整的思考过程也给分。**但是禁止抄袭**。

作业中应该包含：

- 从收集信息到利用漏洞全部的思考和操作过程，**至少包含关键步骤，可以截图**
- 有代表性的攻击请求，并推测服务端的处理逻辑
- 用到的脚本代码(如果有的话)
- 得到的Flag

总言之，要能让人相信这是你独立思考的结果。**请把作业整理为一个PDF文档(web_lab3_姓名_学号.pdf)上传**。如果有自己编写的脚本，也放进PDF里，不用额外打包成压缩包上传。

Flag格式均为`flag{XXX}`。如果找到疑似Flag的字符串但提交显示错误，或是发现可能是设计之外的错误，请及时联系我。

## Task 1: Legacy Parser (30%)

- 完成 `Legacy Parser`
  - 平台上可下载源码
  - 你能**直接**访问的只有`public_app.py`上的服务

## Task 2: The Hall of Everlasting Names (35%)

- 完成 `The Hall of Everlasting Names`
  - SVG文件本质是XML
  - Flag在/flag，但可能需要权限
  - 仔细收集信息，寻找隐藏的功能

## Task 3: Passcode++ (35%)

- 完成 `Passcode++`
  - 本题基于MySQL(严格来说是MariaDB，在做题层面和课上讲的MySQL没有任何区别)
  - 服务端有最基础的注入过滤功能
  - passcode存储在当前数据库的唯一表的唯一列中，有多条passcode，每条都可使用
  - Flag**不在**数据库中，输入正确的passcode后自动获得
  - 可能需要自动化脚本


