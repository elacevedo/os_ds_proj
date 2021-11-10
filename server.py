import Pyro4

@Pyro4.expose
class hi:
	def hi(self):
		return 'hello'

daemon = Pyro4.Daemon(host="ipaddress") #enter ipaddress of local machine. 

uri = daemon.register(hi(),"server")
ns = Pyro4.locateNS()
ns.register('obj',uri)
print(uri) 

daemon.requestLoop()
