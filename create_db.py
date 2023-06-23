from app import app
from database.database import db
from models.blogpost import BlogPost
from models.user import User

# create the database and the db table

with app.app_context():
    db.drop_all()
    db.create_all()

    # insert data
    author = User(name="Omar",email="omar@elkashef.com",password="1234")
    db.session.add(author)
    author_id = User.query.filter_by(name='Omar').first().id
    post = BlogPost(title="Good", description="I\'m good.",author_id=author_id)
    db.session.add(post)
    post = BlogPost(title="Well", description="I\'m well.",author_id=author_id)
    db.session.add(post)
    post = BlogPost(title="Excellent", description="I\'m excellent.",author_id=author_id)
    db.session.add(post)
    author = User(name="Essam",email="essam@elkashef.com",password="1234")
    db.session.add(author)
    author_id = User.query.filter_by(name='Essam').first().id
    post = BlogPost(title="Excellent", description="I\'m excellent.",author_id=author_id)
    db.session.add(post)
    author = User(name="Elkashef",email="elkashef@elkashef.com",password="5678")
    db.session.add(author)
    author_id = User.query.filter_by(name='Elkashef').first().id
    post = BlogPost(title="Postgress", description="Added Postgress.",author_id=author_id)
    db.session.add(post)

    # commit the changes
    db.session.commit()