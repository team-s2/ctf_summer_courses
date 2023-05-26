# 相关工具的介绍和使用

我们在发布的[虚拟机](http://10.214.160.32:8088/ubuntu101.ova)（其中用户名为 ctfer，密码为 aaa）中预装了一些课程中可能会使用到的工具，这里将对其进行展开介绍。同学们也可以根据自身需要，在熟悉的平台中使用这些工具。

## IDA

- 官网：https://hex-rays.com/ida-pro/
- 介绍：无可争议的，最强的逆向工具～二进制程序 F5 一键变回源代码
- 使用：在预装的虚拟机桌面双击 IDA Freeware 7.6 即可，启动效果如下图，随后即可通过 `New` 选择二进制程序进行反编译

![](https://raw.githubusercontent.com/team-s2/summer_course_2023/master/docs/images/tool_pic_ida.png)

> 备注：预装的 IDA 是需要联网使用的免费试用版，如果安装其他渠道下载到的破解版，请注意避免中文路径问题。

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