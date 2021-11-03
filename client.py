import Pyro4

o = Pyro4.Proxy("PYRO:obj_d7ddd2be79b946f9b9fad17cea52373c@localhost:34705")

print(o.hi())
