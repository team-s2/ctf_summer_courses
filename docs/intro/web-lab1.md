# Web Lab 1：计算机网络基础

## Task 1: DNS (30%)

YYY 在`cubicy.icu`的 DNS 记录中放了一些有趣的东西。

请探索如下问题的答案：

- 使用 `nslookup` 等命令，指定要查询的 DNS 记录类型。那么，`cubicy.icu` 的权威域名服务器是什么？换句话说，在没有缓存的情况下，谁最终负责把这个域名翻译成 IP 地址？**请给出对应的完整命令。**
- 使用 `nslookup` 等命令，`cubicy.icu` 的 IP 地址是什么？**请给出对应的完整命令。**
- 使用 `nslookup` 等命令，多次查询 DNS A 记录，每次的响应都一样吗？如果不一样，出现了哪几种不同的地址？
    - 借助 DNS 服务器，我们可以对同一个域名返回不同的 IP 地址。这对网站有什么好处？
- YYY 使用 Base64 编码在 DNS 记录中藏了一段文本。请找到它。
- 事实上，访问 `cubicy.icu` `www.cubicy.icu` `blog.cubicy.icu` 最终都会抵达同一台服务器上的同一个 web 应用。 通过 DNS 分别查询这几个域名的 IP (IPv4), 观察返回的结果。
    - 尝试直接访问这些 IP 地址，能否访问成功？这些地址是服务器的真实地址吗？
    - 推测 YYY 借助服务提供商的何种服务/何种技术实现了这样的效果？提示：即使 YYY 更换了新的服务器从而改变了源服务器地址，访问者眼中的 IP 地址也无需改变。

## Task 2: HTTP (35%)

请同学们准备 [BurpSuite](https://portswigger.net/burp/communitydownload)（社区版即可）。BurpSuite 能够帮助我们进行抓包分析，或是拦截即将要发送的包并进行修改再发送。

同时，个人在此推荐同学们安装 *HackBar* 浏览器插件。这样只需要按下 `F12` 打开开发者工具即可对 HTTP 请求进行简单的修改后重发。

*Cookie-Editor* 等插件可以帮助你查看网站在浏览器上储存的 Cookie。

任务：

- 使用 BurpSuite 对[学在浙大](https://courses.zju.edu.cn/)的登录过程进行抓包。
    - 大致指出这个 HTTP 报文的各个组成部分。
    - 网站是如何保存用户的登陆状态的？
    - 可供参考：[Intercept HTTP traffic with Burp Proxy](https://portswigger.net/burp/documentation/desktop/getting-started/intercepting-http-traffic)。
- 我们提到过 TCP 是**无边界**的字节流服务。HTTP 工作在 TCP 之上，它为何可以区分不同的包？
    - 提示：对网络协议缺乏了解的开发者经常对 TCP 的拆包/粘包问题感到困惑。
- 事实上，`cubicy.icu` 的源服务器地址是 `101.132.222.48`。尝试直接访问，是否成功？
    - 主机是如何区分直接 IP 访问与通过域名访问的？
    - 在 BurpSuite 中，直接访问该 IP 地址，通过拦截包并修改 HTTP 报文，使得这次请求 IP 地址也能打开主页。**请给出截图或其他证据**。
        - “未备案”页面也视为访问成功。想一想为什么直接通过域名访问不会有这个问题？
            - 提示：梳理一下访问网页的全过程。

## Task 3: 预习 (35%)

- 了解 PHP, JavaScript, SQL 的基础知识，并准备好本地的相关环境。
- 学会使用 Python 中的 `requests` 等库发送请求，通过自定义 Cookie 等方式尝试从学校网站抓取自己的本学期成绩。
    - 如果需要轮询，请注意访问频率控制，不要对服务器造成过大压力。
    - 可以使用生成式 AI 帮助自己学习编码。
    - **你需要提交相关代码**。

## Bonus (+15%)

- 聊一聊你对最新的 HTTP 版本：HTTP/3 的理解。为什么它抛弃了 TCP 协议？
- 了解 DNS Rebinding 攻击；使用现成的 rebinder 完成 SchoolBus（内网）的题目：[SSRF](https://zjusec.com/challenges/47)。
