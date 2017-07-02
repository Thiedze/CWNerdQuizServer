import json
import os

from cwbuzzer import Buzzer
from cwplayer import Player
from cwquiz import Quiz


class Game():

	def __init__(self):
		self.players = []
		self.buzzer = Buzzer()
		
	def setWebSocket(self, webSocket):
		self.webSocket = webSocket
		self.buzzer.setWebSocket(webSocket)
		
	def initBuzzer(self):
		self.buzzer.initBuzzer()

	def addPlayer(self, startAddress, name):
		self.players.append(Player(startAddress, name, len(self.players)))
		print("server: %s" % self.players)
		
	def sendQuizzes(self):
		quizzes = list()
		for file in os.listdir("quizzes"):
			if file.endswith(".json"):
				quizzes.append(file.split(".")[0])
				
		response = { 
			"action" : "getQuizzes",
			"quizzes" : quizzes
		}
		print("server send: %s" % response)
		self.webSocket.write_message(json.dumps(response))
		
	def selectQuiz(self, quiz):
		for root, dirs, files in os.walk("quizzes"):
			for file in files:
				if file.endswith(".json") and file.split(".")[0] == quiz:
					quiz = json.loads(open(os.path.join(root, file)).read(), object_hook=self.as_quiz)
				
					for category in quiz.categories:
						for question in category.question:
							print(question.question)
	
	def sendPlayers(self):
		response = { 
			"action" : "getPlayers",
			"players" : [player.dump() for player in self.players]
		}
		print("server send: %s" % response)
		self.webSocket.write_message(json.dumps(response))
		
