class Question(object):

    def __init__(self, key, question):
        self.question = question["question"]
        self.blue = question["blue"]
        self.orange = question["orange"]
        self.green = question["green"]
        self.yellow = question["yellow"]
        self.answer = question["answer"]