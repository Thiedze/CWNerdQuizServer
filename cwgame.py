from cwplayer import Player
from cwbuzzer import Buzzer
import json
import sys

class Game():

	def __init__(self):
		self.player = []
		self.websocket = None
		self.buzzer = Buzzer()
		
	def initBuzzer(self):
		self.buzzer.initBuzzer()

	def addPlayer(self, startAddress, name):
		self.player.append(Player(startAddress, name))
		print(self.player)
		
	def sendPlayer(self):
		response = { 
			"action" : "getPlayer",
			"player" : self.player
		}
		print(response)
		#self.websocket.send(json.dumps(response))
		