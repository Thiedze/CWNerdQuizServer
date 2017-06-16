from cwplayer import Player
from cwbuzzer import Buzzer
import json

class Game():

	def __init__(self):
		self.player = []
		self.websocket = None
		self.buzzer = Buzzer()
		
	def setWebsocket(self, websocket):
		self.websocket = websocket
		self.buzzer.setWebsocket = self.websocket
		
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
		self.websocket.sendMessage(json.dumps(response).encode("UTF-8"), False)
		