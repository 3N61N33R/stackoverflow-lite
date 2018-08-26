from datetime import datetime

users =[]
questions =[]
answers = []

class User:
    def __init__(self, name,email,password):
        self.name = name
        self.email = email
        self.password = password

    def add(self):
        users.append(self)

    def serialize(self):
        return {
            "name":self.name,
            "email":self.email,
            "password":self.password
        }

class Question:
    question_id = 1
    def __init__(self, question = None):
        self.question = question
        self.id = Question.question_id
        self.timestamp ="{}".format(datetime.utcnow().strftime("%d-%m-%Y %H:%M"))


        Question.question_id +=1

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

    def get_specific(self, id):
        for question in questions:
            if question.id == id:
                return question

        return None

    def delete_specific(self, question_id):
        for question in questions:
            if question.id == question_id:
                questions.remove(question)
                return question
        return False

class Answer:
    answer_id = 1
    def __init__(self, answer, question = None):
            self.question = question
            self.answer = answer
            self.id = Answer.answer_id

            Answer.answer_id +=1

    def add(self):
        answers.append(self)

    def serialize(self):
        return {
            'question': self.question.serialize(),
            "answer": self.answer,
            "id" :self.id

        }

    