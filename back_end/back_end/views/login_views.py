from flask import Blueprint, request, redirect
from back_end.dao.user import User
import json
from back_end.extensions import db, login_manager
from flask_login import login_required, login_user, logout_user
login_views = Blueprint('login_views',__name__)

@login_manager.user_loader
def load_user(user_id):  # 创建用户加载回调函数，接受用户 ID 作为参数  
    user = User.query.get(int(user_id))  # 用 ID 作为 User 模型的主键查询对应的用户
    return user  # 返回用户对象


@login_views.route("/login",methods=['POST'])
def login():
    request_data = request.get_json()
    user = User.query.filter_by(login_id=request_data.get('username')).first()
    if (user and user.password == request_data.get('password')):
        login_user(user)
        data = {
            'status': 'Success',
            'message':'登录成功',
            'data': {
                'nickname':user.nickname
            }
        }
        response = json.dumps(data)  # 将python的字典转换为json字符串
        return response,200,{"Content-Type":"application/json"}
    else:
        data = {
            'status': 'Success',
            'message':'用户名或密码错误',
            'data': ''
        }
        response = json.dumps(data)  # 将python的字典转换为json字符串
        return response,200,{"Content-Type":"application/json"}

@login_views.route("/session",methods=['POST'])
def session_verification():
    data = {
        'status': 'Success',
        'message':'',
        'data': ''
    }
    response = json.dumps(data)  # 将python的字典转换为json字符串
    return response,200,{"Content-Type":"application/json"}

@login_views.route("/register",methods=['POST'])
def register():
    request_data = request.get_json()
    user = User.query.filter_by(login_id=request_data.get('username')).first()
    if (user is None):
        user = User(login_id=request_data.get('username'), password=request_data.get('password'),nickname=request_data.get('nickname'))
        db.session.add(user)
        db.session.commit()
        data = {
            'status': 'Success',
            'message':'注册成功',
            'data': ''
        }
        response = json.dumps(data)  # 将python的字典转换为json字符串
        return response,200,{"Content-Type":"application/json"}
    else:
        data = {
            'status': 'Success',
            'message':'用户已注册',
            'data': ''
        }
        response = json.dumps(data)  # 将python的字典转换为json字符串
        return response,200,{"Content-Type":"application/json"}
#   try {
#     const AUTH_SECRET_KEY = process.env.AUTH_SECRET_KEY
#     const hasAuth = isNotEmptyString(AUTH_SECRET_KEY)
#     res.send({ status: 'Success', message: '', data: { auth: hasAuth, model: currentModel() } })
#   }
#   catch (error) {
#     res.send({ status: 'Fail', message: error.message, data: null })
#   }


