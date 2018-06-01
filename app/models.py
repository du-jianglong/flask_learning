from app import db  # db是在app/__init__.py生成的关联后的SQLAlchemy实例

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(32), nullable=False)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    @property
    def is_authenticated(self):
        # is_authenticated 方法有一个具有迷惑性的名称。一般而言，这个方法应该只返回 True，除非表示用户的对象因为某些原因不允许被认证。
        return True

    @property
    def is_active(self):
        # is_active 方法应该返回 True，除非是用户是无效的，比如因为他们的账号是被禁止。
        return True

    @property
    def is_anonymous(self):
        # is_anonymous 方法应该返回 True，如果是匿名的用户不允许登录系统。
        return False

    def get_id(self):
        # get_id 方法应该返回一个用户唯一的标识符，以 unicode 格式。
        return str(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.String(10000))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Post %r>' % (self.title)
