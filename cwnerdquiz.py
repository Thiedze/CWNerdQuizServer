import json
import asyncio
import websockets
import sys

from cwgame import Game

global game

async def reciever(websocket, path):
	while True:
		message = await websocket.recv()
		message = json.loads(message)
		print("Input:" + str(message))
		if(message["action"] == "initBuzzer"):
			game.initBuzzer()
		elif(message["action"] == "savePlayer"):
			game.addPlayer(message["startAddress"], message["name"])
		elif(message["action"] == "getPlayer"):
			game.sendPlayer()		

async def sender(websocket, path):
	while True:
		message = game.buzzer.getInput()
		if message != None:
			print(message)
			await websocket.send(message)
		
if __name__ == '__main__':
	game = Game()
	loop = asyncio.get_event_loop()
	reciever_server = websockets.serve(reciever, 'localhost', 9000)
	sender_server = websockets.serve(sender, 'localhost', 4711)

	try:
		loop.run_until_complete(reciever_server)
		loop.run_until_complete(sender_server)
		loop.run_forever()
	except KeyboardInterrupt:
		pass
	finally:
		reciever_server.close()
		#sender_server.close()
		loop.close()
	