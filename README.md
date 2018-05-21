Python + Flask Practice Item
====

【 项目使用系统是 windows 10 && python 版本是 3.6 && 编码器用的是 PyCharm 】

**1、先进入到 flask_learning 目录中接着使用如下的命令创建一个虚拟环境：**

```angular2html
python -m venv flask
```

**2、在 Windows 上安装 virtualenv 最简单地方式就是先安装 pip，安装方式在 这里 <https://pip.pypa.io/en/latest/installing.html>。一旦安装好了 pip 的话，下面的命令可以安装 virtualenv：**

```angular2html
pip install virtualenv
```

**3、为了创建一个虚拟环境，请输入如下的命令行：**

```angular2html
virtualenv flask
```

上面的命令行在 flask 文件夹中创建一个完整的 Python 环境。

**4、安装 flask 以及扩展：**

```angular2html
flask\Scripts\pip install flask
flask\Scripts\pip install flask-login
flask\Scripts\pip install flask-openid
flask\Scripts\pip install flask-mail
flask\Scripts\pip install flask-sqlalchemy
flask\Scripts\pip install sqlalchemy-migrate
flask\Scripts\pip install flask-whooshalchemy
flask\Scripts\pip install flask-wtf
flask\Scripts\pip install flask-babel
flask\Scripts\pip install guess_language
flask\Scripts\pip install flipflop
flask\Scripts\pip install coverage
```
这些命令行将会下载以及安装我们将会在我们的应用程序中使用的所有的包。

**5、在根目录下，开始为应用程序创建基本的文件结构：**
```angular2html
mkdir app
mkdir app/static
mkdir app/templates
mkdir tmp
```
应用程序包是放置于 app 文件夹中。子文件夹 static 是存放静态文件像图片，JS文件以及样式文件。子文件夹 templates 显然是存放模板文件。

**6、为app 包(文件 `app/__init__.py`)创建一个简单的初始化脚本，并导入视图模块:**
```angular2html
from flask import Flask     # 从 flask 这个框架中导入 Flask 这个类

app = Flask(__name__)

# 初始化一个 Flask 对象：
# 1、方便 flask 框架寻找资源
# 2、方便 flask 插件，比如： Flask-Sqlalchemy 出现错误的时候，能够找到问题所在位置

from app import views
```

**7、视图是响应来自网页浏览器的请求的处理器。在 Flask 中，视图是编写成 Python 函数。每一个视图函数是映射到一个或多个请求的 URL。**

编写一个视图函数(文件 app/views.py ):
```angular2html
from app import app
from flask import render_template

# @app.route('/') 是一个装饰器
# @开头，并在函数的上面，说明是装饰器
# 这个装饰器的作用，作 url 与 视图函数 的映射
# index() 叫做视图函数
# 127.0.0.1：5000/ -> 去请求 index() 这个函数，并返回结果给浏览器
@app.route('/')
@app.route('/index')
def index():
    title = 'Zylan`s'
    user = {'nickname': 'Zylan'}
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title=title, user=user, posts=posts)
```

**8、创建配置文件（文件 config.py）并把它置于根目录:**
```angular2html
# 开启调试模式
DEBUG = True

# 表单
CSRF_ENABLED = True     # 激活 跨站点请求伪造 保护
SECRET_KEY = 'god-is-a-girl-biu-biu-biu'    # 当 CSRF 激活的时候才需要，它是用来建立一个加密的令牌，用于验证一个表单。
```


**9、创建一个脚本，启动我们的应用程序的开发 Web 服务器。**

创建一个文件(文件 run.py )并把它置于根目录:
```angular2html
from app import app

import config

app.config.from_object(config)  # 执行 是否 进入 debug 模式

# 如果当前这个文件是作为入口程序执行，那么就执行 app.run()
if __name__ == '__main__':
    app.run()     # 启动一个应用服务器，来接受用户的请求（一直在监听是否有请求，死循环状态）
```

**10、在第7步有这么一句话**
`render_template('index.html', title=title, user=user, posts=posts)`
意思是此刻需要创建一个模板，并向这个模板传递一些参数。

比如，创建两个模板，（文件 app/templates/index.html） && （文件 app/templates/menu.html）：

**`menu.html 如下：`**

```angular2html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>导航栏</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link type="text/css" rel="stylesheet" href="../static/css/reset.css">
    <link type="text/css" rel="stylesheet" href="../static/css/menu.css">
    <script type="text/javascript" src="../static/js/jquery-2.1.1.min.js"></script>
</head>
<body>

<header class="header_box">
    <div class="fixed_width clearfix">
        <div class="logo"><a href="javascript:;">Zylan`s Blog</a></div>
        <div class="menu_box">
            <dl class="menu clearfix">
                <dd><a href="javascript:;" class="active">首页</a></dd>
                <dd><a href="javascript:;">归档</a></dd>
                <dd><a href="javascript:;">作品</a></dd>
                <dd><a href="javascript:;">慢生活</a></dd>
                <dd><a href="javascript:;">关于</a></dd>
                <dd><a href="javascript:;">留言</a></dd>
            </dl>
        </div>
    </div>
</header>

<!--占位符-->
<div class="display_none_div"></div>

{% block content %}{% endblock %}

<!--在这个模板中，我们使用 block 控制语句来定义派生模板可以插入的地方。-->

</body>
</html>
```

**`index.html （实现继承 menu.html 模板）如下：`**

```angular2html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {% if title %}
    <title>{{title}} Blog</title>
    {% else %}
    <title>Welcome To Zylan`s Blog</title>
    {% endif %}
</head>
<body>

{% extends 'menu.html' %}

<!--上面这句话是说：“利用 Jinja2 的模板继承的特点，导入该基础模板。”-->

{% block content %}

<h1>Hello，{{user.nickname}}</h1>

<h3>以下是一个循环：</h3>

{% for post in posts %}
<p>{{post.author.nickname}} ：{{post.body}}</p>
{% endfor %}


<script type="text/javascript" src="../static/js/index.js"></script>

{% endblock %}

</body>
</html>
```

**11、运行**
```angular2html
flask/Scripts/python run.py
```
或

点击 PyCharm 视窗上的运行按钮。

----------------------------------------------------
**未完，待续......**
====
