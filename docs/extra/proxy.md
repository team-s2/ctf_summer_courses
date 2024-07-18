# 连接校内网做题指南

!!! abstract
    随着各位同学假期回家，可能会遇到连接内网平台或题目的问题，本文将介绍一些连接内网的方法。

    以下目前只是 TonyCrane 个人的推荐方式，也有可能有描述不准/更好的方式，可以随时在群里补充。

## WebVPN

### 平台

访问校内平台都可以通过 webvpn 完成，通过 [webvpn.zju.edu.cn](https://webvpn.zju.edu.cn) 导航访问即可，例如：

- http://zjusec-com-s.webvpn.zju.edu.cn:8001/
- http://ctf-zjusec-com-s.webvpn.zju.edu.cn:8001/

!!! tip
    大家也可以发现 webvpn 的链接规则：

    - 只有 HTTP 协议，不支持 HTTPS
    - 都通过 `.webvpn.zju.edu.cn:8001` 访问
    - 四级域名的规则为：
        - 原域名的 `.` 替换为 `-`，`-` 替换为 `--`
        - 如果要通过 HTTPS 访问，则在末尾加 `-s`
    - URL 资源路径直接接在链接后面

    也可以自己根据这个规则构造链接访问。

!!! note "本课程网站部署在 GitHub Pages 上，不需要通过校网访问"

### 题目

#### ZJUCTF 容器题目

我们在 ZJUCTF 平台的 `[lec1] container` 题目中介绍了平台的容器题目使用了平台代理，提供的链接是 wss 链接，需要在本地建立 TCP over websocket 后通过本地端口访问。并且介绍了可以使用 WebSocketReflectorX 软件或 websocat 来进行连接。

恰好 webvpn 也支持 websocket，所以这些容器题目都可以通过 webvpn 进行连接，无需其他代理配置。

!!! tip "有了网络知识，大家当然也可以自行探索连接"

使用 webvpn 访问 ZJUCTF 平台后创建容器得到的链接已经是 webvpn 后的 wss 链接了。但是我们知道 webvpn 本身没有 TLS，所以不能直接利用 wss 链接，需要将 wss 改成 ws 才能进行后续的访问。

同时大家也知道 webvpn 如果要记录用户，也要通过 cookie 来记录。通过捕捉连接的包，可以发现在刚认证之后会设置 TWFID 这个 cookie，所以我们在请求的时候也要带上这个 cookie，否则会 302 跳转到 webvpn 页面要求进行登陆。

而 WebSocketReflectorX 并不支持自定义 header 来携带 cookie，所以我们要通过 websocat 来建立映射。可以使用以下命令：

```bash
websocat -H="Cookie: TWFID=................" -b -E tcp-l:127.0.0.1:61234 ws://ctf-zjusec-com-s.webvpn.zju.edu.cn:8001/api/proxy/<uuid>
```

其中：

- `-H="Cookie: TWFID=..."` 来设置 header 里的 cookie
- `tcp-l:127.0.0.1:61234` 表示监听本地的 61234 tcp 端口
    - 61234 可以随意替换
- `ws://ctf-zjusec-com-s.webvpn.zju.edu.cn:8001/api/proxy/<uuid>` 是容器题目的链接
    - 需要从平台复制下来之后将 wss 改为 ws

运行之后通过 `nc 127.0.0.1 61234` 就可以连接题目了（或者如果是 HTTP 服务可以直接在浏览器里访问）。

#### 静态服务题目

即所有人共用一个服务的题目，比如题目中给了 ip 和端口或者域名，校巴上大部分老题目都是这样的。

如果是 web 服务的题目，大部分也可以通过 webvpn 访问，比如校巴 SQL Injection 题目的服务 <http://10.214.160.13:10002/> 可以访问 <http://10-214-160-13-10002-p.webvpn.zju.edu.cn:8001/>（可见 ip 的 `.` 以及 ip 和端口间的 `:` 都替换为了 `-` 并在结尾加了 `-p`）。

如果是 nc 连接的 TCP 服务，那 webvpn 就做不到了，因为它只提供了 HTTP 连接，不能提供裸的 TCP 代理。这时候就需要使用其他方法了。

## 使用代理

不推荐使用 rvpn 自带的 Easy Connect，推荐使用 [ZJU-Connect](https://github.com/Mythologyli/ZJU-Connect) 来搭建反向代理。可以使用 Clash + ZJU Rule 的方式来配置规则代理等，这里不过多描述。

!!! note "Clash 可以使用 TUN 模式来实现全局的系统代理，同学可以自行尝试，以下方式均不依赖于 TUN 模式功能"

### 网页服务代理

对于 web 服务，直接将 Clash 设为系统代理或者使用浏览器插件即可无感进行代理访问，相信不必多说。

### 终端代理

一般来讲，终端不会自动走系统代理，需要设置环境变量来进行代理，Clash 也提供了复制终端代理命令的功能，例如：

```bash
export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890
```

这样一些命令就可以使用代理了，比如 curl、wget、geth 等。但是有一些命令还是不会走代理，比如 nc、python pwntools 进行的连接。

对于 nc，其需要额外传入参数来进行代理：

```bash
❯ man nc
...
     -X proxy_version
             Requests that nc should use the specified protocol when talking to the proxy server.  Supported protocols are “4” (SOCKS v.4), “5” (SOCKS v.5) and “connect” (HTTPS
             proxy).  If the protocol is not specified, SOCKS version 5 is used.

     -x proxy_address[:port]
             Requests that nc should connect to hostname using a proxy at proxy_address and port.  If port is not specified, the well-known port for the proxy protocol is used
             (1080 for SOCKS, 3128 for HTTPS).
```

所以如果 Clash 将 socks5 代理开在了 7890 端口，那么就可以：

```bash
nc -X 5 -x localhost:7890 10.214.160.13 13004
```

这样就能连接到校巴上的题目 safe nft，其中 `-X 5` 也可以省略，因为默认使用的就是 socks5 协议。

对于 pwntools，也提供了代理的功能，详见[文档](https://pwntools-docs-zh.readthedocs.io/zh-cn/dev/context.html#pwnlib.context.ContextType.proxy)，所以在使用的时候可以：

```python
from pwn import *

context.proxy = (socks.SOCKS5, "localhost", 7890)
p = remote("10.214.160.13", 11002)
```

这样就可以使用本地 7890 端口的 socks5 协议进行代理连接了。