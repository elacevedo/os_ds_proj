import Pyro4

@Pyro4.expose
class hi:
	def hi(self):
		return 'hello'

# Example of entering and removing from database 
#	def __init__ (self, name):
#		self.name = name
#	def visit(self, database):
#		print (name)
#		self.deposit(database)
#		self.retrieve(database)
#
#	def deposit(self, database)
#		print(database.listitems())
#		item = input("Type your item".strip)
#		if item: 
#			database.store(self.name, item)
#	def retrieve(self, database):
#		print(database.listitems())
#		item = input("Type you item".strip)
#		if item:
#			database.take(self.name, item)


daemon = Pyro4.Daemon()

uri = daemon.register(hi)
#ns = Pyro4.locateNS()
#ns.register('obj',uri)
print(uri) 

daemon.requestLoop()
