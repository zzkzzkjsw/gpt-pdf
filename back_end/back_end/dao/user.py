from back_end.extensions import db
from flask_login import UserMixin
import hashlib

class User(db.Model,UserMixin):
    __tablename__ = 'sys_user'
    u_iid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login_id = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    nickname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    create_time = db.Column(db.DateTime)

    def get_id(self):
        return self.u_iid
    
    def set_password(self, password):  # 用来设置密码的方法，接受密码作为参数  
        self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()  # 将生成的密码保持到对应字段  

    def validate_password(self, password):  # 用于验证密码的方法，接受密码作为参数  
        if hashlib.sha256(password.encode('utf-8')).hexdigest() == self.password:
            return True
        return False