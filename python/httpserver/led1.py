#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
import cgi
import thread
import threading
import ablib
import time

PORT_NUMBER = 8080
blink = True

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		# Define the default page
		if self.path=="/":
			self.path="/index_led1.html"

		try:
			#Check the file extension required and
			#set the right mime type

			sendReply = False
			if self.path.endswith(".html"):
				mimetype='text/html'
				sendReply = True
			if self.path.endswith(".jpg"):
				mimetype='image/jpg'
				sendReply = True
			if self.path.endswith(".gif"):
				mimetype='image/gif'
				sendReply = True
			if self.path.endswith(".js"):
				mimetype='application/javascript'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True

			if sendReply == True:
				#Open the static file requested and send it
				f = open(curdir + sep + self.path) 
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
			return

		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)

	#Handler for the POST requests
	def do_POST(self):
		global blink

		if self.path=="/blink":
			form = cgi.FieldStorage(
				fp=self.rfile, 
				headers=self.headers,
				environ={'REQUEST_METHOD':'POST',
		                 'CONTENT_TYPE':self.headers['Content-Type'],
			})

			if (form["cmd"].value=="stop blinking"):
				print "Stop blinking"
				blink=False
			else:
				blink=True
				print "Start blinking"

			#Redirect the browser on the main page 
			self.send_response(302)
			self.send_header('Location','/')
			self.end_headers()
			return			
			
#This is a thread that runs the web server 
def WebServerThread():			
	try:
		#Create a web server and define the handler to manage the
		#incoming request
		server = HTTPServer(('', PORT_NUMBER), myHandler)
		print 'Started httpserver on port ' , PORT_NUMBER
		
		#Wait forever for incoming htto requests
		server.serve_forever()

	except KeyboardInterrupt:
		print '^C received, shutting down the web server'
		server.socket.close()


# Runs the web server thread
thread.start_new_thread(WebServerThread,())		

# Use the L1 led on Daisy11 module
ledL1=ablib.Daisy11("D2","L1")

#Forever loop
while True:
	# Check the blink flag
	if blink==True:	
		ledL1.on()
		time.sleep(0.2)
		ledL1.off()
		time.sleep(0.2)
	else: 
		ledL1.off()

