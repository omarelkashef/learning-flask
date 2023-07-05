from .base import *
from utils.bcrypt import bcrypt
from flask_login import current_user

class TestUser(BaseTestCase):

    # Ensure user can register
    def test_user_registeration(self):
        with self.client:
            response = self.client.post('/register', data=dict(
                username='ad', email='ad@ad.com',
                password='admin', confirm_passowrd='admin'),
                follow_redirects=True)
            self.assertIn(b'Welcome to Flask!', response.data)
            self.assertTrue(current_user.name == "ad")
            self.assertTrue(current_user.email == "ad@ad.com")
            self.assertTrue(current_user.is_active)

    def test_get_by_id(self):
        # Ensure id is correct for the current/logged in user
        with self.client:
            self.client.post('/login', data=dict(
                username="ad", password='ad'
            ), follow_redirects=True)
            self.assertTrue(current_user.get_id() == 1)
            self.assertFalse(current_user.get_id() == 20)

    def test_check_password(self):
        # Ensure given password is correct after unhashing
        user = User.query.filter_by(name='ad').first()
        self.assertTrue(bcrypt.check_password_hash(user.password, 'admin'))
        self.assertFalse(bcrypt.check_password_hash(user.password, 'foobar'))

if __name__ == '__main__':
    unittest.main()