import tornado.ioloop
import tornado.web
import ablib

class ledon(tornado.web.RequestHandler):
	def get(self):
		print "Led ON"
		led.on() 

class ledoff(tornado.web.RequestHandler):
	def get(self):
		print "Led OFF"
		led.off() 

application = tornado.web.Application([
	(r"/ledon", ledon),
	(r"/ledoff", ledoff),
	(r"/(.*)", tornado.web.StaticFileHandler, {"path": ".","default_filename": "index.html"}),
])

if __name__ == "__main__":
	led = ablib.Daisy11('D11','L1')

	application.listen(8080,"0.0.0.0")
	tornado.ioloop.IOLoop.instance().start()


