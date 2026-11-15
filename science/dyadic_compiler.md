# Compiling a whole waiting-time interval

The [first-event stack](first_event.md) has one output row for every possible first event. Treating all those rows with a uniform time distribution would give a normalization proportional to the square root of elapsed time. A dyadic distribution matches the decay of the operator envelope instead. Its squared normalization is only logarithmic in the maximum horizon.

## The normalized filters used by the compiler

Retain the normalized rectangular jump map $`L`$ and $`A=L^\dagger L\le I`$. The [filter construction](filters_and_resources.md) provides projected unitary block encodings, with normalization one, of

```math
E_a=e^{-aA/2},
\qquad
D_a=\sqrt a\,L e^{-aA/2}
\quad(a>0).
```

The first map preserves the input space; the second produces the event label and system in the output space of $`L`$. Both are contractions. For the second,

```math
\|D_a\|\le\max_{0\le z\le1}\sqrt a\,z e^{-az^2/2}\le e^{-1/2}<1.
```

This bound also covers $`a<1`$, when the unconstrained maximum lies outside the interval. Uniformly for a coherently encoded parameter $`0\le a\le T`$, a requested additive block error $`\xi`$ costs $`O((1+\sqrt T)\mathrm{polylog}((2+T)/\xi))`$ calls to the supplied jump block encoding and its inverse. The common coefficient register and time cutoff are fixed by $`T`$ and $`\xi`$; reversible arithmetic computes the dependence on $`a`$. The compiler does not require a different phase table for every possible event time.

One explicit realization uses the Hermitian dilation

```math
H_L=\begin{pmatrix}0&L^\dagger\\L&0\end{pmatrix}.
```

Gaussian and signed derivative-Gaussian Fourier integrals implement $`e^{-aH_L^2/2}`$ and $`\sqrt a H_L e^{-aH_L^2/2}`$ with coefficient one-norm at most one. Their right-to-right and right-to-left blocks are the filters above. Importantly, the even filter does not incur a fixed attenuation at every binary factor. Truncation, finite random registers, coefficient arithmetic, controlled Hamiltonian simulation and their errors are included in the linked primitive's resource account.

## Dyadic bins and the outer stack

Take a dyadic mesh $`\delta=2^{-q}\le1`$. Choose a power of two $`T=2^b\ge\max\{1,\tau\}`$, where $`\tau`$ is the largest normalized horizon to be simulated. The clock represents all grid horizons $`u\le T`$. Partition $`[0,T)`$ into

```math
I_0=[0,1),
\qquad
I_\ell=[2^{\ell-1},2^\ell)
\quad(1\le\ell\le b).
```

Let $`p=b+1`$ be the number of bins and $`c=\sqrt{p+1}`$. There is one further branch for no event. For $`\ell\ge1`$, put $`a_\ell=2^{\ell-1}`$; the length and left endpoint of that bin are both $`a_\ell`$. The first bin has length one and left endpoint zero.

Prepare the no-event branch and the $`p`$ event-bin branches with equal amplitude $`1/c`$. In an event bin of length $`a`$, prepare a uniform superposition over its $`a/\delta`$ grid points. Apply the following projected contraction at the selected point $`s`$:

```math
G_0(s)=L E_s\quad(s\in I_0),
\qquad
G_\ell(s)=D_{a_\ell}E_{s-a_\ell}
=\sqrt{a_\ell}\,L e^{-sA/2}
\quad(s\in I_\ell,\ \ell\ge1).
```

For each event branch, an exact reversible comparison marks $`s\ge u`$ as outside the accepted block. On the no-event branch, apply $`E_u`$. The event-bin and time registers are retained as output records. They are not unprepared or summed coherently after applying the filters.

For a valid time in a bin of length $`a`$, the accepted amplitude is

```math
\frac1c\frac1{\sqrt{a/\delta}}\sqrt a\,L e^{-sA/2}
=\frac{\sqrt\delta}{c}L e^{-sA/2}.
```

The same identity holds for the first bin, where $`a=1`$. Since the bins are disjoint, their retained labels can be relabeled reversibly as the single clock index. In the ideal filter limit, the resulting projected block is exactly

```math
\frac1c M_\delta(u).
```

The normalization $`c`$ is common to every remaining horizon, including $`u=0`$. It does not contain the number $`T/\delta`$ of possible clock values. No probability of a particular physical event is assumed to be bounded below.

## Coherent parameters do not enumerate time points

Compute the residual parameter

```math
v=\begin{cases}
u,&\text{on the no-event branch},\\
s,&\text{in the first event bin},\\
s-a_\ell,&\text{in event bin }\ell\ge1.
\end{cases}
```

All parameters lie in $`[0,T]`$. Apply one coherently parameterized even filter $`E_v`$. Then apply the coherently parameterized odd filter $`D_{a_\ell}`$ on event branches with $`\ell\ge1`$, apply $`L`$ itself on the first event bin, and do nothing further on the no-event branch. The odd filter and $`L`$ act on disjoint outer branches. Temporary arithmetic can be uncomputed because it depends only on the untouched horizon, branch and time registers.

There are $`n=O(1+\log(T/\delta))`$ bits in a time parameter. The interval superpositions use controlled Hadamards and exact reversible integer arithmetic. Equal weights on the finitely many outer branches use ordinary finite-precision rotations. Inside each parameterized filter, uniform Fourier coefficient indices determine signed simulation times by an explicit arithmetic formula; binary controls apply the fixed Hamiltonian evolutions. No circuit iterates over the event-time points. No arbitrary data table, QRAM, supplied spectral decomposition, or input-state preparation oracle is used.

Use separate success work for the even filter and the following odd filter or jump block. This makes the accepted block their product without resetting a failed filter. The construction's unitary and inverse act on the entire work space; they do not apply only to an accepted branch.

If every primitive block has additive error at most $`\xi`$, the accepted block of a product of these two contractions differs by at most $`2\xi`$. The primitive blocks are contractions because they are projections of unitaries. The outer branch amplitudes have squared sum one, so retaining the branch labels introduces no additional factor proportional to the number of time points. Consequently, for any requested $`\zeta>0`$, the actual constructed unitary can have accepted block $`B_u`$ satisfying

```math
\left\|B_u-\frac{M_\delta(u)}c\right\|\le\zeta
```

uniformly in $`u`$, by choosing primitive errors and branch-preparation error $`O(\zeta)`$. Its query count is

```math
Q_B=O\!\left[(1+\sqrt T)
\mathrm{polylog}\!\left(\frac{2T}{\delta\zeta}\right)\right].
```

The horizon register remains fixed during this whole construction. Hence the same statement holds for its controlled direct sum with operator error $`\zeta`$, even if the horizon is superposed and entangled with older records.

## Deterministic amplification, with failures retained

The accepted stack is not postselected. We amplify it into an approximate isometry using the two known projections: the input projection has all fresh work and output-record registers in their initial state; the output projection requires successful work but permits all physical record values. Neither projection reflects about the unknown system input.

The standard projected-unitary singular-value transformation has the following consequence. For any $`0<a\le1`$ and $`0<\nu<1`$, an odd real polynomial of degree $`O(a^{-1}\log(1/\nu))`$, bounded by one on $`[-1,1]`$, can approximate the sign function to error $`\nu`$ on $`[-1,-a]\cup[a,1]`$. Applying that polynomial to a rectangular projected block maps each positive singular value in $`[a,1]`$ to within $`\nu`$ of one. This is the usual oblivious singular-value amplification primitive from Gilyén, Su, Low and Wiebe, [arXiv:1806.01838](https://arxiv.org/abs/1806.01838); its polynomial and short phase list depend only on the chosen threshold and accuracy.

Here the threshold is $`a=1/(2c)`$. To see that this is sufficient for the actual implemented block, let $`z=c\zeta\le1/4`$. Lemma 1 on the [first-event page](first_event.md) and the singular-value perturbation inequality give

```math
1-z\le\sigma(cB_u)\le\sqrt{1+\delta}+z.
```

Thus $`B_u`$ has no singular value below $`1/(2c)`$. Let $`P(B_u)`$ denote its polar isometry. Singular-value calculus and a triangle inequality first give the useful direct bound

```math
\|P(B_u)-M_\delta(u)\|
\le\frac\delta2+2c\zeta.
```

Indeed, $`cB_u`$ is within $`c\zeta`$ of $`M_\delta(u)`$, and changing its singular values to one costs at most $`\delta/2+c\zeta`$.

We also need closeness to the exact polar grid map without charging the mesh error a second time. The following elementary stability estimate suffices:

```math
\|P(B_u)-P_\delta(u)\|\le10c\zeta.
```

To verify it, set $`X=cB_u`$, $`Y=M_\delta(u)`$, $`S=X^\dagger X`$ and $`R=Y^\dagger Y`$. Their smallest eigenvalues are at least $`1/2`$, $`\|S-R\|\le4z`$, $`\|Y\|\le\sqrt2`$, and $`\|S^{-1/2}\|\le4/3`$. The resolvent integral for the inverse square root gives

```math
\|S^{-1/2}-R^{-1/2}\|
\le\frac{\|S-R\|}{\pi}
\int_0^\infty\frac{r^{-1/2}}{(r+1/2)^2}\,dr
=\sqrt2\,\|S-R\|.
```

Expanding $`XS^{-1/2}-YR^{-1/2}`$ then gives a bound $`(4/3+8)z<10z`$. This proves the displayed polar estimate, uniformly over the horizon register.

Let $`W_u`$ be the entire singular-value-transformation unitary on fresh input work. Its accepted block is within $`\nu`$ of $`P(B_u)`$. Its rejected amplitude is at most $`\sqrt{2\nu}`$, because every transformed singular value has squared modulus at least $`(1-\nu)^2`$. Therefore, after embedding its successful output in the finite-clock space,

```math
\|W_u|\mathrm{fresh}\rangle-P(B_u)\|
\le\nu+\sqrt{2\nu}\le3\sqrt\nu.
```

This is an estimate for the complete isometry, not a conditional successful output. All rejected work is retained in an orthogonal numerical-failure branch. A reversible computation can flag that branch and stop its further cascade operations. Its small probability or amplitude is part of the error bound; no run is discarded and no failed register is reset.

Combining the bounds gives both the grid-map implementation error and its comparison with exact waiting:

```math
\|W_u|\mathrm{fresh}\rangle-P_\delta(u)\|
\le10c\zeta+3\sqrt\nu,
```

```math
\|E_\delta W_u|\mathrm{fresh}\rangle-V_u\|
\le\delta+10c\zeta+3\sqrt\nu.
```

In these displays, the embeddings include the algorithm's failure space orthogonally to the target. Choose, for example, $`\zeta\le\eta/(40c)`$ and $`\nu\le\eta^2/36`$. For $`0<\eta\le1/10`$, the two right sides are at most $`\eta`$ and $`\delta+\eta`$, respectively. The construction works simultaneously for every grid horizon with the same phases, success projections and error budget.

## First-event compilation theorem

**Theorem 2.** Given the normalized controlled jump block encoding and inverse, a maximum horizon $`\tau`$, a dyadic mesh $`0<\delta\le1`$, and $`0<\eta\le1/10`$, there is a finite unitary first-event circuit whose complete initialized-workspace isometry differs from $`P_\delta(u)`$ by at most $`\eta`$. Its comparison with exact next-event waiting has error at most $`\delta+\eta`$. The circuit has total output probability one, retains all physical and numerical-failure records, and works coherently over all grid horizons $`u\le\tau`$. Its number of controlled forward or inverse jump-oracle calls is

```math
Q_{\mathrm{first}}
=O\!\left[
\big(1+\sqrt{1+\tau}\big)
\mathrm{polylog}\!\left(\frac{2+\tau}{\delta\eta}\right)
\right].
```

**Proof.** The dyadic stack costs $`Q_B`$ calls. Oblivious amplification uses $`O(c\log(1/\nu))`$ applications of that stack circuit or its inverse. The choice $`T<2\max\{1,\tau\}`$, the logarithmic size of $`c^2`$, and the accuracy choices above yield the stated bound. The previous sections prove the map, error and coherent-control claims. ∎

At mesh and per-call accuracies polynomial in $`\varepsilon/(k+1)`$, composing at most $`k+1`$ slots gives the bound stated in the [cascade theorem](time_discretization.md). The slot and horizon dependence are charged separately; this argument establishes no optimal dependence on $`k`$.

## Circuit resources and what has been implemented

The event clock uses $`O(1+\log(T/\delta))`$ qubits, the event label uses the label width supplied by $`L`$, and the outer branch uses $`O(\log(2+\log T))`$ qubits. Product block encodings retain the success work of the constant number of composed filters. The resources of the parameterized Gaussian filters and their coefficient arithmetic are included in [the resource account](filters_and_resources.md). The sign-amplification polynomial has only polylogarithmic degree, so even polynomial-time phase synthesis for that final amplification is a polylogarithmic setup cost.

If one oracle call is realized by a circuit of cost $`C_U`$, the query-dependent gate cost contains the factor $`Q_{\mathrm{first}}C_U`$, in addition to the stated arithmetic, filter and reflection gates. Gate synthesis of oracle calls must be accurate enough for the complete circuit; an ideal query oracle does not supply free arbitrary classical data loading or free physical control. The system input is supplied to the simulated channel, so the algorithm neither prepares it nor requires its preparation inverse.

These are constructive analytical circuit bounds. The finite checks supplied with the project test the instrument and channel formulas. They do not constitute an implementation of the complete fault-tolerant Gaussian-filter and amplification circuit, a native-gate benchmark, or a demonstrated hardware crossover.
