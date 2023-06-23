from database.database import db
from sqlalchemy.orm import relationship
from utils.bcrypt import bcrypt

class User(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String , nullable=False)
    email = db.Column(db.String , nullable=False)
    password_hash = db.Column(db.String , nullable=False)
    posts = relationship("BlogPost" , backref = "author")
  #  test = db.Column(db.Boolean , nullable=True)

    @property
    def password(self):
        raise AttributeError("password is not readable")

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password)


    def __init__(self , **kwargs):
        #password =  bcrypt.generate_password_hash(password)
       # kwargs["password"] = bcrypt.generate_password_hash(kwargs.get("password",None))
        super(User,self).__init__(**kwargs)

   # def __init__(self, name, email, password):
    #    self.name = name
     #   self.email = email
      #  self.password = password
