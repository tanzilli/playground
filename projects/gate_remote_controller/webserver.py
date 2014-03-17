import tornado.ioloop
import tornado.web
import tornado.websocket
import ablib
from time import sleep
import json

gate = ablib.Daisy8('D11','first','RL0')
clients = []

#Handler for incoming websocket messages
class WebSocketHandler(tornado.websocket.WebSocketHandler):

	#When a client opens a new websocket session
	#add it to the client list
	def open(self):
		clients.append(self)

	def on_message(self, message):
		rxmsg=json.loads(message)

		#Check for opengate command from 
		#clients
		if rxmsg["cmd"]=="opengate":
			gate.on() 
			
			#Change the button color to red on every client
			message='{"cmd":"button_on"}'
			for c in clients:
				c.write_message(message)
			sleep(1)
			gate.off() 

			#Change the button color to green on every client
			message='{"cmd":"button_off"}'
			for c in clients:
				c.write_message(message)
			
			return 

	#When a client closes a websocket session
	#renove it from the client list
	def on_close(self):
		clients.remove(self)		

application = tornado.web.Application([

	#Serve the incoming websocket messages
	(r"/websocket", WebSocketHandler),

	#Serve the static files
	(r"/(.*)", tornado.web.StaticFileHandler, {"path": ".","default_filename": "index.html"}),
])

if __name__ == "__main__":
	application.listen(8080,"0.0.0.0")
	tornado.ioloop.IOLoop.instance().start()
