# 相关工具的介绍和使用

我们在发布的虚拟机

> 下载[链接](https://pan.baidu.com/s/1lg4JZoYJwKj6ImuKdtv_Nw?pwd=AAAA)（其中用户名为 ctfer，密码为 aaa）

中预装了一些课程中可能会使用到的工具，这里将对其进行展开介绍。同学们也可以根据自身需要，在熟悉的平台中使用这些工具。

## IDA

- 官网：https://hex-rays.com/ida-pro/
- 介绍：无可争议的，最强的逆向工具～二进制程序 F5 一键变回源代码
- 使用：在预装的虚拟机桌面双击 IDA Freeware 7.6 即可，启动效果如下图，随后即可通过 `New` 选择二进制程序进行反编译

![](https://raw.githubusercontent.com/team-s2/summer_course_2023/master/docs/images/tool_pic_ida.png)

> 备注：预装的 IDA 是需要联网使用的免费试用版，如果安装其他渠道下载到的破解版，请注意避免中文路径问题。

### 解决 SSL 版本过高导致的 server not avaliable

由于高版本 ubuntu 使用的是 SSL3+ 的版本，在 IDA 与远端 server 使用时可能会出问题，如果你遇到了 `cloud server not avaliable` 的问题，其关键原因是 SSL3+ 拿掉了 `SSL_get_peer_certificate` 这个方法，[见链接](https://github.com/nodegit/nodegit/issues/1967#issuecomment-1429957927)（又是不向前兼容的设计）

为了修复，我们可以将旧版本 SSL1.1 替换目前环境的 SSL3+，请下载[修复附件](https://github.com/team-s2/summer_course_2023/raw/master/src/intro/lab0/fixf5.zip)，解压缩后在目标目录执行 `fix.sh` 脚本（可能需要 `sudo` 权限），完成后再次测试 IDA 应该就可以正常通过 cloud server 进行 F5 了


## ghidra

- 官网：https://ghidra-sre.org/
- 介绍：开源的一款逆向工具，在处理特定 IDA 不对付的架构时可以使用
- 使用：在预装的虚拟机的命令行中执行 `~/Tools/ghidra_10.3_PUBLIC/ghidraRun` 脚本即可启动，效果如下图，使用的教程可以找网上的相关博客，如[这一篇](https://zhuanlan.zhihu.com/p/59637690)

![](https://raw.githubusercontent.com/team-s2/summer_course_2023/master/docs/images/tool_pic_ghidra.png)


## gef plugin

- 官网：https://github.com/hugsy/gef
- 介绍：Linux 下 gdb 的一款插件，优化调试体验
- 使用：在预装的虚拟机下正常使用 `gdb` 即可以看到插件效果

……

除此外还有一些额外的工具，这些工具会后续补充介绍，或在课程使用时会额外给出讲解。
