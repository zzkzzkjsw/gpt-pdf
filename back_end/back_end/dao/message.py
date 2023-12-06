from back_end.extensions import db

class Message(db.Model):
    __tablename__ = 'sys_message'
    message_uuid = db.Column(db.String(36), unique=True, nullable=False)
    content = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pdf_url = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(20), unique=True, nullable=False)
    create_time = db.Column(db.DateTime)
    conv_uuid = db.Column(db.String(36))