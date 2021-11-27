import Pyro4
import os
import socket

CLIENTNAME = "Client_%d@%s" % (os.getpid(), socket.gethostname())

def placecalls(o):
        print("Placing database calls....")
        calls = [[CLIENTNAME, "Create", "Water", 1200, 12, 1.00],
                [CLIENTNAME, "Create", "Backpack", 1201, 5, 20.00],
                [CLIENTNAME, "DB"],
                [CLIENTNAME, "Change", "Water", "Name", "Bottled Water"],
                [CLIENTNAME, "Search", "Bottled Water"]]
        for i in range(5):
                o.putWork(calls[i])

def collectresults(o):
        print("Getting back results....")
        counter = 0
        while counter != 5:
                try:
                        result = o.getResult(CLIENTNAME)
                except:
                        pass
		else:
			counter = counter + 1
			print(result)
		
def main():
        o = Pyro4.Proxy("PYRO:server@ipaddress:55555") #enter ip address of server.        print("This program simulates a client making calls and changes to a datab$        placecalls(o)
        collectresults(o)

if __name__ == "__main__":
    main()
