from flask import Flask , render_template , request , redirect,\
     url_for , session , flash , Blueprint
from functools import wraps
from flask_bcrypt import Bcrypt
from .forms import LoginForm
from models import User


bcrypt = Bcrypt()

users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)

def needs_login(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if "logged_in" in session.keys():
            return func(*args,**kwargs)
        else:
            flash("You need to log in")
            return redirect(url_for("users.login"))
    return wrapper

@users_blueprint.route("/login" ,  methods = ["GET" , "POST"])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            user = User.query.filter(User.name==form.username.data).first()
            if user is not None and bcrypt.check_password_hash(user.password,
                                                               form.password.data):
                session["logged_in"] = True
                flash("You were just logged in")
                return redirect(url_for("home.home"))
            else:  
                error = "Invalid Credentials. Please try again!"            
    return render_template("users/login.html" , form=form,  error = error)

@users_blueprint.route("/logout")
@needs_login
def logout():
    session.pop("logged_in" , None)
    flash("You were just logged out")
    return redirect(url_for("home.welcome"))


