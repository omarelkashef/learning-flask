from database.database import db
from sqlalchemy import ForeignKey
from .user import User


class BlogPost(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer , primary_key=True)
    title = db.Column(db.String , nullable=False)
    description = db.Column(db.String , nullable=False)
    author_id = db.Column(db.Integer , ForeignKey("users.id"))

 #  def __init__(self , title , description):
  #      self.title = title
   #     self.description = description

