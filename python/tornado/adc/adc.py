#!/usr/bin/python
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.gen
import json
from tornado.options import define, options

clients = []
batteryValue=10

 
class WebSocketHandler(tornado.websocket.WebSocketHandler):
	def open(self):
		print "new connection"
		clients.append(self)

	def on_message(self, message):
		print "tornado received from client: %s" % message
		self.write_message(u"OK: " + message)
		#....
	def on_close(self):
		print 'connection closed'
		clients.remove(self)		

def main():
	application = tornado.web.Application([
		(r"/websocket", WebSocketHandler),
		(r"/(.*)", tornado.web.StaticFileHandler, {"path": ".","default_filename": "index.html"}),
	])
	application.listen(8080)
 
	def batteryStatus():
		global batteryValue
		if(batteryValue > 0):
			batteryValue -= 0.1
		else:
			batteryValue=10

		json_string="{'ch0':%.2f,'ch1':2,'ch2':3,'ch3':4}" % batteryValue
		for c in clients:
			c.write_message(json_string)
			print json_string

	mainLoop = tornado.ioloop.IOLoop.instance()
	scheduler = tornado.ioloop.PeriodicCallback(batteryStatus, 100, io_loop = mainLoop)
	scheduler.start()
	mainLoop.start()
	
if __name__ == "__main__":
	main()
