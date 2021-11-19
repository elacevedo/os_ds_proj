import Pyro4

o = Pyro4.Proxy("PYRO:server@ipaddress:55555") #enter ip address of server.

print(o.putWork("test"))
print(o.getwork())
