At first we may think of sequences intuitively without the formal definition, it's clear that $0,\;2,\;4,\;6,\;8,...$ and $1,\;2,\;4,\;8,\;16,...$ are sequences. One may say he knows the next number in those sequences, or even say that both of them increase indefinitely to infinity, but is there any logical arguments for these claims?!

A sequence can be characterized in more general and exact ways, either by an explicit formula for each term such as the harmonic series.
$$x_n = \frac{1}n \rightarrow 1,\; \frac{1}2,\; \frac{1}3,\; \frac{1}4,...$$
where we assume $n \in \mathbb{N}$ or by a recursion formula such as the following famous sequence, which can also be characterized with an explicit formula that can be left for the reader to derive.
$$x_1 = 1, \; x_{n+1} = \frac{x_n}{2} \rightarrow 1,\; \frac{1}2,\; \frac{1}4,\; \frac{1}8,...$$
The next example can answer one of the questions presented in the first paragraph, can we logically deduce the next term in a sequence?
$$x_n = 2(n-1) \; mod\:10 \rightarrow 0,\;2,\;4,\;6,\;8,\;0,\;2,...$$
If we look only at the first five terms, we would assume that the next term is $10$, but as we can see the sequence deviates from this pattern afterwards. So it's not possible to predict the next term using the previous ones without making additional assumptions.

```python
import matplotlib.pyplot as plt

W, graph = plt.subplots()

x = range(20)
y = [2**(-n) for n in x]

graph.scatter(x,y, s=5)
plt.show()
```