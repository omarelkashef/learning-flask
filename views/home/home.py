from flask import Flask , render_template , request , redirect,\
     url_for , session , flash , Blueprint
from database.database import db
from .. import needs_login
from models import BlogPost


home_blueprint = Blueprint(
    'home', __name__,
    template_folder='.templates'
)

@home_blueprint.route("/")
@needs_login
def home():
    posts = db.session.query(BlogPost).all()
    return render_template("home/index.html" , posts=posts)

@home_blueprint.route("/welcome")
def welcome():
    return render_template("home/welcome.html")
