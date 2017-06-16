import json

from autobahn.asyncio.websocket import WebSocketServerProtocol, WebSocketServerFactory
import asyncio

from cwgame import Game

class CWNerdQuizProtocol(WebSocketServerProtocol):

	def __init__(self):
		super(WebSocketServerProtocol, self).__init__()
		
	def setGame(self, game):
		print("setGame")
		self.game = game
		game.setWebsocket(self)

	def onConnect(self, request):
		print("Client connecting: {0}".format(request.peer))

	def onOpen(self):
		print("WebSocket connection open.")

	def onMessage(self, payload, isBinary):	
		print(payload.decode('utf8'))
		message = json.loads(payload.decode('utf8'))
		if(message["action"] == "initBuzzer"):
			self.game.initBuzzer()
		elif(message["action"] == "savePlayer"):
			self.game.addPlayer(message["startAddress"], message["name"])
		elif(message["action"] == "getPlayer"):
			self.game.sendPlayer()

	def onClose(self, wasClean, code, reason):
		print("WebSocket connection closed: {0}".format(reason))
		
	def connectionLost(self, reason):
		WebSocketServerProtocol.connectionLost(self, reason)
		log("Connection closed: Reason is {}".format(reason))
		
class CWNerdQuizFactory(WebSocketServerFactory):

	

if __name__ == '__main__':
	factory = WebSocketServerFactory("ws://127.0.0.1:9000")
	factory.protocol = CWNerdQuizProtocol

	loop = asyncio.get_event_loop()
	coro = loop.create_server(factory, '0.0.0.0', 9000)
	server = loop.run_until_complete(coro)

	try:
		loop.run_forever()
	except KeyboardInterrupt:
		pass
	finally:
		server.close()
		loop.close()
	