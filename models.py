from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash 


db = SQLAlchemy()


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(80), nullable=False)
  second_name = db.Column(db.String(80), nullable=False)
  e_mail = db.Column(db.String(80), nullable=False, unique=True)
  password = db.Column(db.String(80), nullable=False)

  def __repr__(self):
      return f'User("{self.first_name}", "{self.second_name}","{self.e_mail}")'
  
  def set_password(self, password):
      self.password = generate_password_hash(password)

  def check_password(self, password):
      return check_password_hash(self.password, password)    

