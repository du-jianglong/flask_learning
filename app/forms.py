# 导入 Form 类，并导入两个字段类，StringField 和 BooleanField
# DataRequired 验证器只是简单地检查相应域提交的数据是否是空
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    openid = StringField('openid', validators=[DataRequired('请输入登录账号！')],
                         render_kw={'class': 'form-control oi is-invalid', 'placeholder': '输入账号'})
    password = PasswordField('password',
                             validators=[DataRequired('请输入登录密码！'), Length(min=1, max=20, message='密码最多20个字符！')],
                             render_kw={'class': 'form-control is-invalid', 'placeholder': '输入密码'})
    pic_code = StringField('pic_code', validators=[DataRequired('请输入密码！'), Length(min=1, max=6, message='验证码最多6个字符！')],
                           render_kw={'class': 'form-control pic_code is-invalid', 'placeholder': '验证码'})
    remember_me = BooleanField('remember_me', default=False,
                               render_kw={'class': 'custom-control-input', 'id': 'customControlInline'})
