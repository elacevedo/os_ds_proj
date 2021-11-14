import Pyro4
import queue
from productDB import ProductDB

@Pyro4.expose
@Pyro4.behavior(instance_mode="single") #register object to be processes concurrently. 
class hi:
	def hi(self):
		return 'hello'

class Dispatcher_Fetch(object):
	def __init__(self):
		self.fetch_all = queue.Queue()
		self.resultqueue = queue.Queue()
	def putWork(self, item):
		self.fetch_all.put(item)
	def getwork(self, timeout = 5):
		try: 
			return self.fetch_all.get(block=True, timeout=timeout)
		except queue.Empty:
			raise ValueError("no items in queue")
	def putResult(self, item):
		self.resultqueue.put(item)
	def getResult(self, timeout=5):
		try: 
			return self.resultqueue.get(block=True, timeout=timeout)
		except queue.Empty:
			raise ValueError("no result available")
	def workqueueSize(self):
		return self.fetch_all.qsize()
	def resultQueueSize(self):
		return self.resultqueue.qsize()

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
