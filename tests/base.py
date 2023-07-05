from app import app , db
import unittest
from flask_testing import TestCase
from app import app
from models import BlogPost , User

class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        user = User(name="admin", email="ad@min.com", password="admin")
        db.session.add(user)
        db.session.add(BlogPost(title="Test post", description="This is a test. Only a test.",
                                author_id=user.id))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

if __name__ == "__main__":
    unittest.main()