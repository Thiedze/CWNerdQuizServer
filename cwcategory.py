from cwquestion import Question


class Category(object):

    def __init__(self, name, questions):
        self.questions = dict()
        for key, value in questions.items():
            question = Question(key, value)
            self.questions[key] = question
        