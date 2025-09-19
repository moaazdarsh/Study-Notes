import matplotlib.pyplot as plt
import math as m

W, graph = plt.subplots()

r = 1300

X = [x/100 for x  in range(-r, r)]
Y0 = [m.sin(x/100) for x in range(-r, r)]
Y1 = [m.sin(x/100 - 1) for x in range(-r, r)]
Y2 = [m.sin(x/100 -2) for x in range(-r, r)]

graph.plot(X, Y0, "b", alpha = 0.33)
graph.plot(X, Y1, "b", alpha = 0.66)
graph.plot(X, Y2, "b")

W.savefig("V&WMedia/Code/Graphs/Wave.png")