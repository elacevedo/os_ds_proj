import Pyro4
import queue

@Pyro4.expose
@Pyro4.behavior(instance_mode="single") #register object to be processes concurrently.
class Dispatcher(object):
        def __init__(self):
                self.data = queue.Queue()
                self.resultqueue = queue.Queue()
                self.clients = []
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
        def getResult(self, client, timeout=5):
                try:
                        return self.resultqueue.get(block=True, timeout=timeout)
                except queue.Empty:
                        raise ValueError("no result available")
        def workqueueSize(self):
                return self.data.qsize()
        def resultQueueSize(self):
                return self.resultqueue.qsize()
        def getpid(self, pid, counter):
                self.clients.append(pid)
                newPid = self.clients.index(pid)
                return newPid

daemon = Pyro4.Daemon(host="127.0.0.1", port=55555) #insert ip address of server, since it will be static
                                                                                                        #added static port

uri = daemon.register(Dispatcher(),"server")
ns = Pyro4.locateNS()
ns.register('obj',uri)
print(uri)

daemon.requestLoop()
