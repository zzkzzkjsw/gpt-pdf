from back_end.extensions import db

class Conversation(db.Model):
    __tablename__ = 'sys_conversation'
    conv_uuid = db.Column(db.String(36), primary_key=True, autoincrement=True)
    u_iid = db.Column(db.Integer, unique=True, nullable=False)
    create_time = db.Column(db.DateTime)