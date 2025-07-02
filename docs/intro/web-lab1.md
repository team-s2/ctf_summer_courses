# Web Lab 1：计算机网络基础

## Task 1: 网络基础 (30%)

请探索如下问题的答案：

- 使用 `nslookup` 命令，用校内DNS服务器查询`www.zju.edu.cn`的IP地址。给出完整的命令和查询结果。
- 使用 `nslookup` 命令，用公网DNS服务器查询`www.zju.edu.cn`的IP地址。给出完整的命令和查询结果。
- 分别直接访问用校内DNS和校外DNS查询到的IP地址，能否访问成功？访问结果有何区别？这些地址是服务器的真实地址吗？试分析造成这种现象的原因。
    - 提示：可以对比用域名和用IP访问的HTTP请求包区别，理解问题出在哪一层

## Task 2: HTTP原理应用 (35%)

请同学们准备 [BurpSuite](https://portswigger.net/burp/communitydownload)（社区版即可）。BurpSuite 能够帮助我们进行抓包分析，或是拦截即将要发送的包并进行修改再发送。

同时，个人在此推荐同学们安装 *HackBar* 浏览器插件。这样只需要按下 `F12` 打开开发者工具即可对 HTTP 请求进行简单的修改后重发。

*Cookie-Editor* 等插件可以帮助你查看网站在浏览器上储存的 Cookie。

任务：

- 使用 BurpSuite和浏览器的开发者工具分析[本科教学信息服务管理平台](https://zdbk.zju.edu.cn/)的成绩查询页面。
    - 大致指出页面加载的流程
    - 找到返回关键信息的接口和参数
    - 可供参考：[Intercept HTTP traffic with Burp Proxy](https://portswigger.net/burp/documentation/desktop/getting-started/intercepting-http-traffic)
- 学会使用 Python 中的 `requests` 等库发送请求，通过自定义 Cookie 等方式尝试从学校网站抓取自己的本学期成绩。
    - 如果需要轮询，请注意访问频率控制，不要对服务器造成过大压力
    - 可以使用生成式 AI 帮助自己学习编码
    - **你需要提交相关代码**

## Task 3: HTTP请求走私实战 (35%)

课上我们学习了前端服务器优先解析Content-Length，后端服务器优先解析Transfer-Encoding造成的HTTP请求走私漏洞。这种走私漏洞通常简称为CL.TE型。

Burpsuite 的开发公司PortSwigger 提供了一个CL.TE型的HTTP请求走私漏洞的[Lab](https://portswigger.net/web-security/request-smuggling/lab-basic-cl-te)。

任务：

- 简述HTTP请求走私漏洞的原理。
- 利用Lab中Blog的Comment功能，展示如何利用HTTP请求走私构造一个恶意数据包，将下一个受害者的HTTP请求内容(部分即可)发送到帖子的评论区。**给出你构造的数据包和成功后的截图**。
    - 你可能需要将HTTP2转换为HTTP1.1，见[Lab页面](https://portswigger.net/web-security/request-smuggling/lab-basic-cl-te)的Tip
    - 提示：[Lab页面](https://portswigger.net/web-security/request-smuggling/lab-basic-cl-te)有官方提供的答案和社区录制的视频，可以参考

## Bonus: 漏洞报告阅读 (+15%)

- 阅读课上提到的Steam支付漏洞的[漏洞报告](https://hackerone.com/reports/1295844)。
    - 用自己的语言简述漏洞的成因
    - 简述绕过服务器校验的原理
