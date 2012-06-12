import cherrypy
import os
import fox

L1 = fox.Daisy11("D2","L1")
L2 = fox.Daisy11("D2","L2")
L3 = fox.Daisy11("D2","L3")
L4 = fox.Daisy11("D2","L4")
L5 = fox.Daisy11("D2","L5")
L6 = fox.Daisy11("D2","L6")
L7 = fox.Daisy11("D2","L7")
L8 = fox.Daisy11("D2","L8")

L1.on()

WEB_ROOT = os.getcwd()

class MyServer(object):
	@cherrypy.expose
	def led(self,id,state):
		print id
		print state
		return

cherrypy.server.socket_port = 8080
cherrypy.server.socket_host = '0.0.0.0'
conf = { '/':
	{ 
		'tools.staticdir.on' : True,
		'tools.staticdir.dir' : WEB_ROOT,
		'tools.staticdir.index' : 'daisy11.html' 
	} 
}
cherrypy.quickstart(MyServer(),config=conf)


