import unittest
import json

from app import app

class TestUser(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def post_question(self):
        query_info = {
            "How do I refactor tests with database?"
        }

        res = self.app.post('/app/v1/questions',
            data = json.dumps(query_info),
            content_type = 'application/json'
        )
        return res

    def post_answer(self):
        res_info = {
            "response":"You could first of all seperate your tests?"
        }

        res = self.app.post('/app/v1/questions/4/ans',
            data = json.dumps(res_info),
            content_type = 'application/json'
        )
        return res

    def test_post_answer(self):
        res = self.post_answer()
        self.assertEqual(res.status_code,201)

    def update_answer(self):
        update_info = {
            "response":"You could first of all seperate your tests e.g test_base,test_auth etc"
        }

        res = self.app.put('/api/v1/questions/4/ans/6',
            data = json.dumps(update_info),
            content_type = 'application/json'
        )
        return res

    def test_update_answer(self):
        res = self.update_answer()
        self.assertEqual(res.status_code,201)

if __name__ == "__main__":
    unittest.main()