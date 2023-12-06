from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
from flask_login import LoginManager, UserMixin


db = SQLAlchemy()
login_manager = LoginManager()

# 初始化拓展
def set_extensions(app):
    CORS(app,supports_credentials=True)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'


