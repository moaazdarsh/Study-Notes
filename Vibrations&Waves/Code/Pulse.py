import matplotlib.pyplot as plt
import math as m

W, graph = plt.subplots()
r = 100
X = [x/10 for x  in range(-r, r)]
Y0 = [1/((x/10)**2 +1) for x in range(-r, r)]
Y1 = [1/((x/10 - 1.5)**2 +1) for x in range(-r, r)]
Y2 = [1/((x/10 - 3)**2 +1) for x in range(-r, r)]

graph.plot(X, Y0, "b", alpha = 0.33)
graph.plot(X, Y1, "b", alpha = 0.66)
graph.plot(X, Y2, "b")

W.savefig("Vibrations&Waves/Code/Graphs/Pulse.png")