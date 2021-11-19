import Pyro4
import queue
#from productDB import ProductDB

#@Pyro4.expose
#@Pyro4.behavior(instance_mode="single") #register object to be processes concurrently. 
#class hi:
#	def hi(self):
#		return 'hello'


@Pyro4.expose
@Pyro4.behavior(instance_mode="single") #register object to be processes concurrently. 
class Dispatcher(object):
	def __init__(self):
		self.data = queue.Queue()
		self.resultqueue = queue.Queue()
	def putWork(self, item):
		self.data.put(item)
		print("item in queue")
	def getwork(self, timeout = 5):
		try: 
			return self.data.get(block=True, timeout=timeout)
		except queue.Empty:
			raise ValueError("no items in queue")
	def putResult(self, item):
		self.resultqueue.put(item)
		print("item in results queue")
	def getResult(self, timeout=5):
		try: 
			return self.resultqueue.get(block=True, timeout=timeout)
		except queue.Empty:
			raise ValueError("no result available")
	def workqueueSize(self):
		return self.data.qsize()
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


daemon = Pyro4.Daemon(host="ipaddress", port=55555) #insert ip address of server, since it will be static 
													#added static port

uri = daemon.register(Dispatcher(),"server")
ns = Pyro4.locateNS()
ns.register('obj',uri)
print(uri)

daemon.requestLoop()
