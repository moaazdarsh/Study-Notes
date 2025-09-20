At first we may think of sequences intuitively without the formal definition, it's clear that $0,\;2,\;4,\;6,\;8,...$ and $1,\;2,\;4,\;8,\;16,...$ are sequences. One may say he knows the next number in those sequences, or even say that both of them increase indefinitely to infinity, but is there any logical arguments for these claims?!

A sequence can be characterized in more general and exact ways, either by an explicit formula for each term such as the harmonic sequence.
$$x_n = \frac{1}n \rightarrow 1,\; \frac{1}2,\; \frac{1}3,\; \frac{1}4,...$$
Or by a recursion formula such as the following famous sequence, which can also be characterized with an explicit formula that can be left for the reader to derive.
$$x_1 = 1, \; x_{n+1} = \frac{x_n}{2} \rightarrow 1,\; \frac{1}2,\; \frac{1}4,\; \frac{1}8,...$$
The next example can answer one of the questions presented in the first paragraph, can we logically deduce the next term in a sequence?
$$x_n = 2(n-1) \; mod\:10 \rightarrow 0,\;2,\;4,\;6,\;8,\;0,\;2,...$$
If we look only at the first five terms, we would assume that the next term is $10$, but as we can see the sequence deviates from this pattern afterwards. So it's not possible to predict the next term using the previous ones without making additional assumptions.

Now let's introduce a more formal definition of sequences:

> A function $f(n): \mathbb{N} \rightarrow \mathbb{R}$ is called a *sequence* and is denoted by $\{x_n\}_{n=1}^\infty$ or $\{x_n\}_{1}^\infty$.

---
## Limits

You may notice an interesting property in some sequences such as $\left\{ \frac{n-1}n \right\}_1^\infty$ which is that they seem to approach a specific value as $n$ gets bigger.
$$\left\{ \frac{n-1}n \right\}_1^\infty \rightarrow 0,\; \frac{1}2,\; \frac{2}3,\; \frac{3}4,\; \frac{4}5,...$$
For this specific sequence we can explain that clearly.
$$\left\{ \frac{n-1}n \right\}_1^\infty = \left\{ 1-\frac{1}n \right\}_1^\infty$$
As $n$ increases the value $\frac{1}n$ gets smaller, that enables us to make $x_n$ as close as we would like to $1$, the sequences which have this property are *convergent* and the number they approach is their *limit*, we define both as follows.

>A sequence *converges* to its *limit* $L$ if $\forall \epsilon > 0 \; \; \exists N$ such that $|x_n - L| < \epsilon \; \; \forall n>N$ and we denote that as
>$$\lim_{n \rightarrow \infty}{x_n} = L$$

This definition may seem much more complex than the intuition we had, or even detached from it, but it's in fact the same thing. We can make $x_n$ as close to $L$ as we would like, which means that we can make $|x_n -L|$ smaller than any number $\epsilon$ given that $n$ is large enough, so we choose to make it larger than some number $N$.