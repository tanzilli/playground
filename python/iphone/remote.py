import cherrypy
import os

WEB_ROOT = os.getcwd()

class CServer( object ) :
    @cherrypy.expose
    def do_contact(self, **params):
        pass

cherrypy.server.socket_port = 80
cherrypy.server.socket_host = '0.0.0.0'
conf = { '/':
	{ 
		'tools.staticdir.on' : True,
		'tools.staticdir.dir' : WEB_ROOT,
		'tools.staticdir.index' : 'index.html' 
	} 
}
cherrypy.quickstart( CServer(), config = conf )
