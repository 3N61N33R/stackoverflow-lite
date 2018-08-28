import unittest
import json

from app import app

class TestAnswer(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def post_answer(self):
        question = {
            "question":"How do I refactor tests with database?"
        }

        res = self.app.post('/api/v1/questions/',
            data = json.dumps(question),
            content_type = 'application/json'
        )

        answer = {
            "response":"You could first of all seperate your tests?"
        }

        res = self.app.post('/api/v1/questions/2/answers',
            data = json.dumps(answer),
            content_type = 'application/json'
        )
        return res

    def test_post_answer(self):
        res = self.post_answer()
        self.assertEqual(res.status_code,201)

    def test_get_answers(self):
        res = self.app.get('/api/v1/questions/1/answers')
        self.assertEqual(res.status_code, 200)

if __name__ == "__main__":
    unittest.main()