# 导入 Form 类，并导入两个字段类，StringField 和 BooleanField
# DataRequired 验证器只是简单地检查相应域提交的数据是否是空
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
