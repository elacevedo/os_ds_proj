import Pyro4

@Pyro4.expose
class hi:
	def hi(self):
		return 'hello'

daemon = Pyro4.Daemon()

uri = daemon.register(hi)
#ns = Pyro4.locateNS()
#ns.register('obj',uri)
print(uri) 

daemon.requestLoop()
