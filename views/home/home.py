from flask import Flask , render_template , Blueprint , request , redirect,\
                  url_for , flash
from database.database import db
from .. import login_required
from models import BlogPost
from .forms import PostForm
from database.database import db
from flask_login import current_user


home_blueprint = Blueprint(
    'home', __name__,
    template_folder='.templates'
)

@home_blueprint.route("/" , methods = ["GET" , "POST"])
@login_required
def home():
    error = None
    form = PostForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            post = BlogPost(title=form.title.data,description=form.description.data,
                            author_id=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('New entry was successfully posted. Thanks.')
            if form.errors:
                return render_template("home/index.html",posts=posts,error=form.errors,
                           form=form)
            return redirect(url_for("home.home"))
    posts = db.session.query(BlogPost).all()
    return render_template("home/index.html" , posts=posts, error = error,
                           form=form)

@home_blueprint.route("/welcome")
def welcome():
    return render_template("home/welcome.html")
