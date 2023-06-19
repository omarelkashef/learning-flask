from flask import Flask , render_template , request , redirect , url_for , session , flash
from functools import wraps
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///posts.db'

db = SQLAlchemy(app)


def needs_loggin(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if "logged_in" in session.keys():
            return func(*args,**kwargs)
        else:
            flash("You need to log in")
            return redirect(url_for("login"))
    return wrapper


@app.route("/")
@needs_loggin
def home():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html" , posts=posts)

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/login" ,  methods = ["GET" , "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form["username"] != "admin" or request.form["password"] != "admin":
            error = "Invalid Credentials. Please try again!"
        else:
            session["logged_in"] = True
            flash("You were just logged in")
            return redirect(url_for("home"))
    return render_template("login.html" , error = error)

@app.route("/logout")
@needs_loggin
def logout():
    session.pop("logged_in" , None)
    flash("You were just logged out")
    return redirect(url_for("welcome"))


from models import *


if __name__ == "__main__":
    app.run(debug=True)

