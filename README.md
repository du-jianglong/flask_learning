Python + Flask Practice Item
====

【 项目使用系统是 windows 10 && python 版本是 3.6 && 编码器用的是 PyCharm 】

_**【 使用时请自行安装 flask 环境】**_

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
