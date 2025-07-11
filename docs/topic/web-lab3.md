# Web Lab 3：后端漏洞基础

## 前言

本次作业的三道题目全部发布在[ZJUCTF平台](https://ctf.zjusec.com/games/5/challenges)上。只要做出题目且步骤齐全就会给满分，做不出答案但是能呈现完整的思考过程也会给分。**但是禁止抄袭**。

作业中应该包含：

- 从收集信息到利用漏洞全部的思考和操作过程，**至少包含关键步骤，可以截图**
- 有代表性的攻击请求，并推测服务端的处理逻辑
- 用到的脚本代码(如果有的话)
- 得到的Flag

总言之，要能让人相信这是你独立思考的结果。**请把作业整理为一个PDF文档(学号-姓名-web-lab3.pdf)上传**。如果有自己编写的脚本，独立打包成(学号-姓名-web-lab3-attachment.zip)和PDF一起上传。

Flag格式均为`AAA{XXX}`。如果找到疑似Flag的字符串但提交显示错误，或是发现可能是“设计之外”的错误，请及时联系OverJerry。

## Task 1: Being and Code (30%)

- 完成 `Being and Code`。
  - 平台上可下载源码
  - 本题用到的是轻量级数据库SQLite，语法和MySQL非常像
  - 本题不会涉及到在MySQL和SQLite下有明显差异的攻击技术
  - Flag在根目录某文件里，文件名未知
  - 你可能需要实现有回显的RCE

## Task 2: Yes Author (35%)

- 完成 `Yes Author`。
  - 题目只解析你上传的.docx文件
  - 有内容的.docx文件本质是一个.zip压缩包
  - Flag在/flag文件内
  - 本题不需要RCE

## Task 3: Passcode+ (35%)

- 完成 `Passcode+`。
  - 本题基于MySQL
  - 服务端有最基础的注入过滤功能
  - `passcodes`表的`passcode`列下存储了全部的passcode，有多行数据
  - Flag**不在**数据库中，输入正确的passcode后自动获得


