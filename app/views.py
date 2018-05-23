from app import app
from flask import render_template, redirect, url_for

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


@app.route('/login')
def login():
    return render_template('formLogin.html')
