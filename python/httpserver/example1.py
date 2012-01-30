#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

port = 8080

class myHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write("Hello World !")
		return

try:
	server = HTTPServer(('', 8080), myHandler)
	print 'Started httpserver on port ' , port
	server.serve_forever()
except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
	
