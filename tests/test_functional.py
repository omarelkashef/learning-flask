from .base import *
from flask_login import current_user


class FlaskTestCase(BaseTestCase):
    
    # Ensure that Flask was set up correctly
    def test_index(self):
        response = self.client.get("/login" , content_type = 'html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that main page requires user login
    def test_main_route_requires_login(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertIn(b'You need to log in', response.data)

    # Ensure that posts show up on the main page
    def test_posts_show_up_on_main_page(self):
        response = self.client.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True
        )
        self.assertIn(b'This is a test. Only a test.', response.data)


class UsersViewsTests(BaseTestCase):
      # Ensure that the login page loads correctly
    def test_login_page_loads(self):
        response = self.client.get('/login')
        self.assertIn(b'Please login', response.data)

    # Ensure login behaves correctly with correct credentials
    def test_correct_login(self):
        response = self.client.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True
        )
        self.assertIn(b'You were just logged in', response.data)
        self.assertTrue(current_user.name == "admin")
        self.assertTrue(current_user.is_active)

    # Ensure login behaves correctly with incorrect credentials
    def test_incorrect_login(self):
        response = self.client.post(
            '/login',
            data=dict(username="wrong", password="wrong"),
            follow_redirects=True
        )
        self.assertIn(b'Invalid Credentials. Please try again!', response.data)
    
    # Ensure logout behaves correctly
    def test_logout(self):
        self.client.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True
        )
        response = self.client.get('/logout', follow_redirects=True)
        self.assertIn(b'You were just logged out', response.data)
        self.assertFalse(current_user.is_active)

    #Ensure that logout page requires user login
    def test_logout_route_requires_login(self):
        response = self.client.get('/logout', follow_redirects=True)
        self.assertIn(b'You need to log in', response.data)
    
if __name__ == "__main__":
    unittest.main()