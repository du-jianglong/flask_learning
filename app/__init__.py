from flask import Flask     # 从 flask 这个框架中导入 Flask 这个类
import config
from flask_sqlalchemy import SQLAlchemy

import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir

app = Flask(__name__)
'''
Flask(__name__) 初始化一个 Flask 对象 ：
1、方便 flask 框架寻找资源
2、方便 flask 插件，比如： Flask-Sqlalchemy 出现错误的时候，能够找到问题所在位置
'''

app.config.from_object(config)  # 执行 是否 进入 debug 模式

db = SQLAlchemy(app)


# 登录配置
# Flask-OpenID 扩展需要一个存储文件的临时文件夹的路径。对此，我们提供了一个 tmp 文件夹的路径。
lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))


from app import views, models  # 导入视图模块
