# Web Lab 2：用户侧攻击

yelan

## 要求

1. Lab2 最多计 115 分

2. 对于Task 1,5,6,报告不需要太详细,只要求关键分析步骤以及正确截图,做出来就是满分,即使做不出来也会根据做题进度和思考过程给分.

3. 对于不需要提交 flag 的题目,不要求你的解答很深入,能运用课上讲过的知识即可

4. 如果有代码是 AI 生成的,请注明并贴上你与 AI 的对话记录

5. 题目难度并非单调递增的

6. **务必杜绝抄袭,这点非常重要,本课程对抄袭 0 容忍**.

### Task 1: HTML Parser (15 分)

这里有一个含有大量节点的 HTML 文档,请把它解析为一个树状结构并按照**层序遍历**的方式输出每个节点的类型及 `id` ,得到一行很长的字符串`s`.其中每个节点的类型和 `id` 之间用`:`连接(如果没有 `id` 则以 `:` 作为这个节点的结尾),不同节点之间用`,`分隔

样例输入:

```html
<html>
<head>
    <title>Test</title>
</head>
<body>
    <div id="main">
        <h1 name="welcome">Welcome</h1>
        <p>This is a test.</p>
        <ul>
            <li id="item1">Item 1</li>
            <li id="item2">Item 2</li>
        </ul>
    </div>
</html>
```

预期输出(`s`):

```
html:,head:,body:,title:,div:main,h1:,p:,ul:,li:item1,li:item2
```

然后计算`s`的 `MD5` 值,在外面加上`AAA{}` 的格式提交,题目平台的`flag`按照以下代码生成:

```python
import hashlib
s = "......"
md5_hash = hashlib.md5(s.encode()).hexdigest()
print("AAA{" + md5_hash + "}")
```

### Task 2: Show me the secret (20 分)

回顾课程第 16 页 slides 的情景,自行搭建一个服务,编写完整脚本泄露受害者页面的 flag

如果你不知道从哪里开始,你可以解释下面这个情景并在此基础上编写获取 flag 的脚本

```python
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

SECRET_VALUE = "AAA{Well_done!Here_is_20_points_for_you!D81B3EB8-ABA4}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/victim')
def victim():
    if request.remote_addr != "127.0.0.1":
        return "You are not victim, only the victim can access this page.", 403
    return render_template('victim.html', secret=SECRET_VALUE)

@app.route('/inject', methods=['GET', 'POST'])
def inject_css():
    if request.method == 'POST':
        css_content = request.form.get('css', '')
        with open('static/custom.css', 'w') as f:
            f.write(css_content)
        return redirect(url_for('inject_css'))

    css_content = ""
    if os.path.exists('static/custom.css'):
        with open('static/custom.css', 'r') as f:
            css_content = f.read()

    return render_template('inject.html', css=css_content)

if __name__ == '__main__':
    if not os.path.exists('static'):
        os.makedirs('static')
    if not os.path.exists('static/custom.css'):
        with open('static/custom.css', 'w') as f:
            f.write('/* css injection */')
    
    app.run(host='0.0.0.0', port=5000)
```

```html
<!-- victim.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Victim</title>
    <link rel="stylesheet" href="/static/custom.css">
</head>
<body>
    <div>
        <p>Welcome, Victim!</p>
        <p>Your page is safe, no one will see the secret info.</p>
    </div>
    
    <div>
        <input type="hidden" name="secret" value="{{ secret }}">
    </div>
</body>
</html>
```

```html
<!-- inject.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div>
        The current css of the victim's page is:
        <pre>{{ css }}</pre>
    </div>
    <div>
        <form action="/inject" method="post">
            <label for="css">Inject CSS:</label>
            <br>
            <textarea id="css" name="css" rows="10" cols="30"></textarea>
            <br>
            <button type="submit">Inject</button>
        </form>
    </div>
</body>
</html>
```

### Task 3: node._sanitized (30 分)

结合课上讲的 DOM Clobbering  知识,搜索并简要解释 CVE-2017-0928 的原理

### Task 4: Gradient (30 分)

在 Task2 的基础上,你仍然可以控制受害者页面的 CSS,但如果受害者页面的 flag 不以

```html
<input type="hidden" name="secret" value="AAA{secret}">
```

的简单形式出现,而是以以下形式出现:

```html
<div id="secret">
    <span>A</span>
    <span>A</span>
    <span>A</span>
    <span>{</span>
    <span>W</span>
    <span>e</span>
    <span>l</span>
    <span>l</span>
    <span>_</span>
    <span>d</span>
    <span>o</span>
    <span>n</span>
    <span>e</span>
    ......
    <span>!</span>
    <span>}</span>
</div>
```

你该如何编写脚本获取 flag?

### Task 5: XSS 1 (30 分)

通过[xss-labs](http://test.ctf8.com)前五关,每关六分.源码可在 https://github.com/do0dl3/xss-labs 找到

### Task 6: XSS 2 (30 分)

通过[xss-labs](http://test.ctf8.com)前十关,每关六分.源码同上

### Task 7: 拓展 (20 分)

简要回答下面两个问题,言之有理即可:

- 自行搜索并学习**中间人攻击**,解释为什么我们要避免连接公共Wifi (如饭馆,咖啡厅)

- 自行搜索并学习课上提到的**CSP 策略**,解释为什么 CSP 可以防止 XSS 攻击,并构造一个配置不当的 CSP 被绕过的例子(不需要给出代码实现,只需要描述)