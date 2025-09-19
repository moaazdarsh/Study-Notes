import matplotlib.pyplot as plt
import math as m

W, graph = plt.subplots()

r = 800
sc = 0.1

X = [sc * x for x  in range(r)]
Y = [ m.e**(-0.07*x * sc) * m.cos(x * sc) for x in range(r)]
E1 = [m.e**(-0.07*x * sc) for x in range(r)]
E2 = [-m.e**(-0.07*x * sc) for x in range(r)]

graph.plot(X, Y, "b")
graph.plot(X, E1, "r", alpha = 0.5)
graph.plot(X, E2, "r", alpha = 0.5)

W.savefig("V&WMedia/Code/Graphs/Underdamped.png")