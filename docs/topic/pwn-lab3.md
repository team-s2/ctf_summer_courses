# Pwn Lab 3：More ROP plz

本节 Lab 由以下内容组成：

1. 按照课上的演示，爆破 32 程序的栈随机化并通过 shellcode 进行攻击 (20 points)
2. 按照课上的演示，选用 one_gadget 或者 ret2csu 的方法再次完成 lab2 中的 ropbaby (20 points)
3. 完成 ropbasic 题目 (25 points)
4. 完成 ropbasic-harden 题目 (35 points)
5. Bonus: 完成校巴的新题目 off-by-null (30 points)

相信完成这些题目后，相信你已经可以自信地 claim 自己是 master of ROP 了

## Challenge 1

相比于课堂下发的 `bruteforce_example`，这里的 `bruteforce_homework` 稍微修改了一下栈缓冲区的大小，详见[附件](https://github.com/team-s2/summer_course_2023/tree/master/src/topic/pwn-lab3/bruteforce)

请通过编写正确的 exploit 生成带有 shellcode 的 `badfile`，类似课堂上的演示去本地循环的爆破 32 位下的栈随机，请在报告中给出最后爆破成功拿到 shell 的截图

## Challenge 2

上次 lab2 中的 ropbaby 我们要求通过 ROP 去执行 `system` 或者 `execve`，这节课结束后，请通过 `one_gadget` 的方式或者 `ret2csu` 的方式进行 ROP 攻击，请在报告中给出成功利用的截图以及将相关代码的打包上传

## Challenge 3

在 `ropbaby` 的基础上，增加了栈保护 stack canary，就成了 `ropbasic`。请完成对其的漏洞分析以及利用

- [题目附件](https://github.com/team-s2/summer_course_2023/tree/master/src/topic/pwn-lab3/ropbasic)
- 题目部署在校网 IP: `10.214.160.13`, Port: `11022`

请在报告中附上漏洞分析以及做法，给出成功拿到 flag 的截图，并将攻击代码以附件形式上传

## Challenge 4

在 `ropbasic` 的基础上，增加了 SECCOMP 保护，就成了 `ropbasic-harden`。请完成对其的漏洞分析以及利用

- [题目附件](https://github.com/team-s2/summer_course_2023/tree/master/src/topic/pwn-lab3/ropbasic-harden)
- 题目部署在校网 IP: `10.214.160.22`, Port: `50003`

> hint: 注意做 orw 的时候，不是去调用 libc 函数里的 open/read/write 哦，而是要想办法 ROP 做具体系统调用哦

## Bonus

记得课上提到的一句，对于栈迁移，即使是 1 个字节，甚至是空字节，也足够强大么？那么，就让校巴的一道新题目来实证这一点吧

- [题目信息](https://zjusec.com/challenges/139)

注意：
1. 请本地成功测试后再攻击远程
2. 请在报告中详细给出攻击的思路，以及攻击代码的分析，附上最后的成功的截图