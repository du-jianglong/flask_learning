# 开启调试模式
DEBUG = True

# 表单
CSRF_ENABLED = True  # 激活 跨站点请求伪造 保护
SECRET_KEY = 'god-is-a-girl-biu-biu-biu'  # 当 CSRF 激活的时候才需要，它是用来建立一个加密的令牌，用于验证一个表单。

# 定义 OpenID 提供者列表
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'G'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
]
