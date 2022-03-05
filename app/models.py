from . import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    email=db.Column(db.String(100),unique = True)
    password =db.Column(db.String(100))
    username = db.Column(db.String(1000))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

     
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        
        self.pass_secure = generate_password_hash(password)

    
    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)
    
    def __repr__(self):
        return f'User {self.username}'