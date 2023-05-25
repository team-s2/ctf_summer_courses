# Lab 0：基础知识及技能

具体内容稍后发布 :)

## Misc
### Challenge 1
参考难度：★

这里有一串被编码过的神秘的字符串，请找出有意义的原字符串（格式为 `AAA{...}`）：

```text
8Q%uH7oV9C7o!2f7oD*@8Oc$J2Gu:s:JO2T78HTV8PrVj9/]^B:0'e_6SgJh7n,=8;)V$M:Gkm:92eJR8Oc-;;`$6b:Gk[5=]\L#7mT%14Ztqk
```

请在实验报告中给出你具体的解密**过程**。

hint:

- 你可能会需要 [CyberChef](https://cyberchef.org/)（~~而且这里有一个功能可以秒杀这个题目~~）
- 你可能需要了解一些关于 **Base 系列**编码的特征

### Challenge 2
参考难度：★★★

下面这张图是 AAA 的 logo。真的……只是一个 logo 吗？其实这张图片中隐藏了一个 flag（格式 `AAA{...}`），请你找出来。

![](https://raw.githubusercontent.com/team-s2/summer_course_2023/master/src/intro/lab0/misc_challenge2.png)

请在实验报告中给出你的解题过程，包括你最终得到的 flag 内容。

hint：

- flag 被分为了两个部分
- 如果你找不到第一部分，~~仔细观察图片~~，这使用了一种最基础的图片隐写技术 LSB 隐写，请自行搜索学习如何破解
- 如果你找不到第二部分，请仔细查看**文件内容**