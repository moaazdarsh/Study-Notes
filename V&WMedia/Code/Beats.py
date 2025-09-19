import matplotlib.pyplot as plt
import math as m

W, graph = plt.subplots()

r = 600

X = [x/100 for x  in range(-r, r)]
Y = [2 * m.cos(1*x/100) * m.cos(20.5*x/100) for x in range(-r, r)]
E1 = [2 * m.cos(1*x/100) for x in range(-r, r)]
E2 = [-2 * m.cos(1*x/100) for x in range(-r, r)]

graph.plot(X, Y, "b")
#graph.plot(X, E1, "r", alpha = 0.65)
#graph.plot(X, E2, "r", alpha = 0.65)

W.savefig('V&WMedia/Code/Graphs/Beats.png')