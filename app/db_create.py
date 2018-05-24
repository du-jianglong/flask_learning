from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_ERPO
from app import db
import os.path


# 创建数据库
db.create_all()
if not os.path.exists(SQLALCHEMY_MIGRATE_ERPO):
    api.create(SQLALCHEMY_MIGRATE_ERPO, 'database create')
    api.version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_ERPO)
else:
    api.version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_ERPO, api.version(SQLALCHEMY_MIGRATE_ERPO))

