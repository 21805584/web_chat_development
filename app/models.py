from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    userinfo = db.relationship('UserInfo', backref='user', lazy='dynamic')
    posts = db.relationship('Posts', backref='user', lazy='dynamic')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    dob = db.Column(db.DateTime, index=True)
    country = db.Column(db.String(64))
    city = db.Column(db.String(64))
    
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_message = db.Column(db.String(300))
    gpt_response = db.Column(db.String(300))
    datetime = db.Column(db.DateTime, index=True, default=datetime.utcnow)