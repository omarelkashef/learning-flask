from database.database import db
from sqlalchemy.orm import relationship


class User(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String , nullable=False)
    email = db.Column(db.String , nullable=False)
    password = db.Column(db.String , nullable=False)
    posts = relationship("BlogPost" , backref = "author")

#    def __init__(self, name, email, password):
 #       self.name = name
  #      self.email = email
   #     self.password = password
