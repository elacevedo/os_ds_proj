import Pyro4

o = Pyro4.Proxy("PYRO:server@ipaddress:55555") #enter ip address of server.

print(o.putWork("test"))
#print(o.getwork())


item = o.getwork()

#worker code
def processdatabase():
	o.putResult(item + "1")
	print(o.getResult())


def main():
	processdatabase() 

if __name__ == "__main__":
    main()
