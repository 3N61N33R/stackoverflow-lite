import unittest
import json

from app import app

class TestUser(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def post_question(self):
        query_info = {
            "question":"How do I refactor tests with database?"
        }

        res = self.app.post('/api/v1/questions',
            data = json.dumps(query_info),
            content_type = 'application/json'
        )
    
        return res
        

    def test_post_questions(self):
        res = self.post_question()
        self.assertEqual(res.status_code, 201)

    def test_get_all_questions(self):
        res = self.app.get('/api/v1/questions')
        self.assertEqual(res.status_code, 200)

    def test_get_specific_question(self):
        res = self.app.get('/api/v1/questions/6')
        self.assertEqual(res.status_code, 200)

    def test_delete_specific_question(self):
        res = self.app.get('/api/v1/questions/8')
        self.assertEqual(res.status_code, 200)

if __name__ == "__main__":
    unittest.main()