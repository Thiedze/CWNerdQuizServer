import json

import tornado.websocket

from cwgame import Game


game = None 

class WebSocketHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        global game
        if(game == None):
            game = Game()
        game.setWebSocket(self)
      
    def on_message(self, message):
        message = json.loads(message)
        print ('server received: %s' % message)
        if(message["action"] == "initBuzzer"):
            game.initBuzzer()
        elif(message["action"] == "savePlayer"):
            game.addPlayer(message["startAddress"], message["name"])
        elif(message["action"] == "getPlayers"):
            game.sendPlayers()
        elif(message["action"] == "getQuizzes"):
            game.sendQuizzes()
        elif(message["action"] == "selectQuiz"):
            game.selectQuiz(message["quiz"])
        
    def check_origin(self, origin):
        if(origin == 'http://localhost:8000'):
            return True
        else:
            return False
