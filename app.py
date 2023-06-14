from flask import Flask , render_template , request , redirect , url_for , session , flash , g
from functools import wraps
import sqlite3

app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'
app.database = "sample.db"

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
    g.db = db_connect()
    cur = g.db.execute('select * from posts')
    #posts = {row[0]: row[1] for row in cur.fetchall()} 
    posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
    g.db.close()
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

def db_connect():
    return sqlite3.connect(app.database)

if __name__ == "__main__":
    app.run(debug=True)

