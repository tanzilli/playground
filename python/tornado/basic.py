import tornado.ioloop
import tornado.web

application = tornado.web.Application([
	(r"/(.*)", tornado.web.StaticFileHandler, {"path": ".","default_filename": "index.html"})
])

if __name__ == "__main__":
	application.listen(8080,"0.0.0.0")
	tornado.ioloop.IOLoop.instance().start()


