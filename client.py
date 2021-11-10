import Pyro4

o = Pyro4.Proxy("PYRO:server@ipaddress:port") #enter ip address of server along with port. 

print(o.hi())
