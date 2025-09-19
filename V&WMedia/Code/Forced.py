import matplotlib.pyplot as plt
import math as m

W, graph = plt.subplots()

r = 125

X = [x/10 for x  in range(r)]
Y = [ 10/m.sqrt( (25-(x/10)**2)**2 + (2* 0.7 *x/10)**2) for x in range(r)]

graph.plot(X, Y, "b")

W.savefig("V&WMedia/Code/Graphs/Forced.png")