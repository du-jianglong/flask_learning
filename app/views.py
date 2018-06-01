from app import app, db, lm, oid
from flask import render_template, redirect, url_for, flash, g, session, request
from flask_login import current_user, login_required, login_user
from .forms import LoginForm
from .models import User


# @app.route('/') 是一个装饰器
# @开头，并在函数的上面，说明是装饰器
# 这个装饰器的作用，作 url 与 视图函数 的映射
# index() 叫做视图函数
# 127.0.0.1：5000/ -> 去请求 index() 这个函数，并返回结果给浏览器
@app.route('/')
@app.route('/index')
@login_required
def index():
    title = 'Zylan`s'
    user = g.user
    posts = [  # fake array of posts
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title=title, user=user, posts=posts)


# 运行登录视图函数的时候确定 g 的位置
@app.before_request
def before_request():
    g.user = current_user


# Flask-OpenID 登录回调
@oid.after_login
def after_login(resp):
    print('结果：：：')
    print(resp)
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        username = resp.username
        if username is None or username == "":
            username = resp.email.split('@')[0]
        user = User(username=username, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler   # oid.loginhandle 告诉 Flask-OpenID 这是我们的登录视图函数。
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['username', 'email'])
    return render_template('login.html', form=form, providers=app.config['OPENID_PROVIDERS'])


@lm.user_loader
def load_user():
    # 请注意在 Flask-Login 中的用户 ids 永远是 unicode 字符串，因此把 id 发送给 Flask-SQLAlchemy 之前，把 id 转成整型是必须的，否则会报错！
    return User.query.get(int(id))

