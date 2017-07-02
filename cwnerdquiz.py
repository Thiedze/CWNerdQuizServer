import socket

import tornado.ioloop
import tornado.web

from cwwebsockethandler import WebSocketHandler

def make_app():
	return tornado.web.Application([
		(r"/ws", WebSocketHandler),
	])

if __name__ == "__main__":
	http_server = tornado.httpserver.HTTPServer(make_app())
	http_server.listen(9000)
	print ('*** Websocket Server Started at %s***' % socket.gethostbyname(socket.gethostname()))
	tornado.ioloop.IOLoop.instance().start()