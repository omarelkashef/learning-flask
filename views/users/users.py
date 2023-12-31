from flask import render_template , request , redirect,\
     url_for , flash , Blueprint
from functools import wraps
from flask_bcrypt import Bcrypt
from .forms import LoginForm , RegisterForm
from models import User
from flask_login import login_required , login_user , logout_user
from database.database import db

bcrypt = Bcrypt()

users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)
@users_blueprint.route("/login" ,  methods = ["GET" , "POST"])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            user = User.query.filter(User.name==form.username.data).first()
            if user is not None and bcrypt.check_password_hash(user.password,
                                                               form.password.data):
                login_user(user)
                flash("You were just logged in")
                return redirect(url_for("home.home"))
            else:  
                error = "Invalid Credentials. Please try again!"            
    return render_template("users/login.html" , form=form,  error = error)

@users_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You were just logged out")
    return redirect(url_for("home.welcome"))

@users_blueprint.route("/register" , methods = ["GET" , "POST"])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(name=form.username.data,password=form.password.data,
                    email=form.email.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        if form.errors:
            return render_template("user/register.html" , form=RegisterForm(request.form),error=form.errors)
        return redirect(url_for("home.home"))
    return render_template("users/register.html" , form=form)

