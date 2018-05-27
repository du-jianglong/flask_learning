from flask import Flask     # 从 flask 这个框架中导入 Flask 这个类
import config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
'''
Flask(__name__) 初始化一个 Flask 对象 ：
1、方便 flask 框架寻找资源
2、方便 flask 插件，比如： Flask-Sqlalchemy 出现错误的时候，能够找到问题所在位置
'''

app.config.from_object(config)  # 执行 是否 进入 debug 模式

db = SQLAlchemy(app)


from app import views, models  # 导入视图模块




