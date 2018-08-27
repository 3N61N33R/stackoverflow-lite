from datetime import datetime
import pdb

users = []
questions = []
answers = []


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def add(self):
        users.append(self)

    def serialize(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password
        }

    def get_by_email(self,email):
        for user in users:
            if user == email:  
                return user
        return None


class Question:
    question_id = 1

    def __init__(self, question=None):
        self.question = question
        self.id = Question.question_id
        self.timestamp = "{}".format(
            datetime.utcnow().strftime("%d-%m-%Y %H:%M"))

        Question.question_id += 1

    def add(self):
        questions.append(self)
        for question in questions:
            print(question.serialize())

    def get_all(self):
        queries = []
        for question in questions:
            queries.append(question.serialize())
        return queries

    def serialize(self):
        return {
            "question": self.question,
            "id": self.id,
            "time": self.timestamp
        }

    def get_specific(self, que_id):
        for question in questions:
            if question.id == que_id:
                return question

        return None

    def delete_specific(self, que_id):
        for question in questions:
            if question.id == que_id:
                questions.remove(question)
                return question
        return False


class Answer:
    answer_id = 1

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.id = Answer.answer_id
        self.timestamp = "{}".format(
            datetime.utcnow().strftime("%d-%m-%Y %H:%M"))

        Answer.answer_id += 1

    def add(self):
        answers.append(self)

    def get_all_ans(self,que_id):
        responses = []
        for answer in answers:
            if answer.question.id == que_id:
                responses.append(answer.serialize())
        return responses

    def serialize(self):
        return {
            "answer": self.answer,
            "id": self.id,
            "time": self.timestamp,
            'question': self.question.serialize()

        }

    def get_one(self, que_id, ans_id):
        for answer in answers:
            if answer.id == ans_id and answer.question.id == que_id:
                return answer
        return None

    
