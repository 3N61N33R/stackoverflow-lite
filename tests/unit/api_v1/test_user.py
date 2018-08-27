import unittest
import json

from app import app

class TestUser(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def signup_user(self):
        user_info = {
            "name":"Gray Cadeau",
            "email":"graycadeau@gmail.com",
            "password":"pass1234"
        }

        res = self.app.post('/api/v1/auth/signup',
            data = json.dumps(user_info),
            content_type = 'application/json'
        )
        return res

    def test_user_signup(self):
        res = self.signup_user()
        self.assertEqual(res.status_code, 200)

    def login_user(self):
        login_info = {
            "email":"graycadeau@gmail.com",
            "password":"pass1234"
        }

        res = self.app.post('/api/v1/auth/signin',
            data = json.dumps(login_info),
            content_type = 'application/json'
        )
        return res

    def test_login(self):
        res = self.login_user()
        self.assertEqual(res.status_code, 200)

if __name__ == "__main__":
    unittest.main()