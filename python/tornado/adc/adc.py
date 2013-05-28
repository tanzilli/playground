#!/usr/bin/python
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.gen
import ablib
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

	def on_close(self):
		print 'connection closed'
		clients.remove(self)		

def main():
	adc=ablib.Daisy20()

	application = tornado.web.Application([
		(r"/websocket", WebSocketHandler),
		(r"/(.*)", tornado.web.StaticFileHandler, {"path": ".","default_filename": "index.html"}),
	])
	application.listen(8080)
 
	def adcReader():
		global batteryValue
		
		if(batteryValue > 0):
			batteryValue -= 0.1
		else:
			batteryValue=10

		json_string="{'ad0':%.2f,'ad1':%.2f,'ad2':%.2f,'ad3':%.2f}" % (adc.get(0),adc.get(1),adc.get(2),adc.get(3))
		for c in clients:
			c.write_message(json_string)

	mainLoop = tornado.ioloop.IOLoop.instance()
	scheduler = tornado.ioloop.PeriodicCallback(adcReader, 100, io_loop = mainLoop)
	scheduler.start()
	mainLoop.start()
	
if __name__ == "__main__":
	main()
