from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
app = Flask(__name__)

HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "bishe"

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"

db = SQLAlchemy(app)
with app.app_context():
    with db.engine.connect() as conn:
        # rs = conn.execute("select 1")
        query_str=text("select 1;")
        rs = conn.execute(query_str)
        print(rs.fetchone())


class User(db.Model):
    __tablename__ = 'sys_user'
    u_iid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login_id = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    nickname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    create_time = db.Column(db.DateTime)


# with app.app_context():
#     user1 = User(login_id='admin', password='admin')
#     user2 = User(login_id='test', password='test')
#     db.session.add(user1)
#     db.session.add(user2)
#     db.session.commit()

# sql: insert sys_user(login_id,password) values ('admin','admin')

with app.app_context():
    # user = User.query.get(2)
    # print(f'{user.u_iid}: {user.login_id}-{user.password}')
    users = User.query.filter_by(login_id='admin')
    for user in users:
        print(user.password)

with app.app_context():
    user = User.query.filter_by(login_id='admin').first()
    user.password='123'
    db.session.commit()

with app.app_context():
    user = User.query.filterby(login_id='admin').first()
    db.session.delete(user)
    db.session.commit()

