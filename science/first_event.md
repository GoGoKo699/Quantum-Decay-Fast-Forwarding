# A first-event instrument that does not step through elapsed time

The quantum-trajectory representation separates waiting for the next event from applying the event. This separation is useful here because the no-event evolution has a positive generator. We first identify the exact instrument, then construct a finite clock whose error is uniform in the remaining waiting time. The [dyadic compiler](dyadic_compiler.md) implements that entire clock with logarithmic normalization. The [time discretization account](time_discretization.md) uses it repeatedly in a cascade.

## The supplied jump map

Let $`\mathcal H`$ be the system space. Include all rates in the jump operators and write

```math
L=\sum_{j=1}^{m}|j\rangle\otimes J_j,
\qquad A=L^\dagger L=\sum_jJ_j^\dagger J_j,
\qquad 0\le A\le I.
```

The rectangular map $`L:\mathcal H\to\mathbb C^m\otimes\mathcal H`$ includes the event label. Its normalized controlled block encoding and inverse are the supplied quantum primitives. The generator has no internal Hamiltonian:

```math
\mathcal L(\rho)=\sum_jJ_j\rho J_j^\dagger-\frac12\{A,\rho\}.
```

The positivity of $`A`$ is essential to the construction. No positive lower bound on its nonzero eigenvalues is assumed. In particular, dark states are allowed. The grading assumptions used to limit the number of events enter the cascade argument; the one-event statements on this page hold for any contraction $`L`$.

For the generator above, the jump completely positive map has diamond norm $`‖A‖\le1`$, and the anticommutator part has diamond norm at most $`‖A‖`$. Consequently,

```math
‖\mathcal L‖_\diamond\le2,
\qquad
‖e^{u\mathcal L}-e^{v\mathcal L}‖_\diamond\le2|u-v|
\quad(u,v\ge0).
```

The second inequality follows by integrating the generator between the two horizons and using diamond norm one of a quantum channel.

## Exact coherent waiting

For a remaining horizon $`u\ge0`$, put

```math
K_0(u)=e^{-uA/2},
\qquad F_s=L e^{-sA/2}.
```

Use an environment with a no-event vector and an orthogonal event space $`L^2([0,u])\otimes\mathbb C^m`$. The next-event isometry is

```math
V_u|\psi\rangle
=|\mathrm{no}\rangle K_0(u)|\psi\rangle
+\int_0^u|\mathrm{yes},s\rangle F_s|\psi\rangle\,ds.
```

The integral is a vector in $`L^2`$: its squared norm is the integral of the squared norm of the integrand. Indeed,

```math
V_u^\dagger V_u
=e^{-uA}+\int_0^u e^{-sA/2}A e^{-sA/2}\,ds
=e^{-uA}+\int_0^u A e^{-sA}\,ds=I.
```

This identity also holds on $`\ker A`$, where the integral vanishes. It uses no inverse of $`A`$ and no minimum decay rate. The map has the usual interpretation: either no event occurs before the horizon, or the first event occurs at time $`s`$ with its label retained. After an event, the system has to evolve for the remaining time $`u-s`$.

Keeping the time record matters. In general, the jump contribution is

```math
\int_0^u L e^{-sA/2}\rho e^{-sA/2}L^\dagger\,ds.
```

It is not the channel of a single Kraus operator obtained by taking a square root of $`I-e^{-uA}`$. Different singular values of $`L`$ leave different waiting-time states. Erasing that information would change their coherences.

## A finite clock with a uniform error

Choose a dyadic mesh $`0<\delta\le1`$ and a grid horizon $`u=M\delta`$. Define the finite rectangular stack

```math
M_\delta(u)
=|\mathrm{no}\rangle e^{-uA/2}
+\sqrt\delta\sum_{r=0}^{M-1}|\mathrm{yes},r\rangle F_{r\delta}.
```

The clock index is a binary integer. There may be many possible values of that integer; their number does not imply that they must be loaded from a table or visited one at a time.

**Lemma 1 (norm and continuum comparison).** Uniformly for every grid horizon $`u\ge0`$,

```math
I\le M_\delta(u)^\dagger M_\delta(u)\le(1+\delta)I.
```

Let $`E_\delta`$ embed the discrete event vector $`|r\rangle`$ as the uniform unit vector on its interval $`[r\delta,(r+1)\delta)`$, and leave the no-event vector fixed. Then

```math
‖E_\delta M_\delta(u)-V_u‖\le\frac\delta2.
```

**Proof.** Functional calculus for $`A`$ gives

```math
M_\delta(u)^\dagger M_\delta(u)
=e^{-uA}+\delta\sum_{r=0}^{M-1}A e^{-r\delta A}
=I+\left(\frac{\delta A}{I-e^{-\delta A}}-I\right)(I-e^{-uA}).
```

The quotient has its continuous value $`I`$ at eigenvalue zero. For $`0\le x\le1`$,

```math
1\le\frac{x}{1-e^{-x}}\le1+x.
```

The upper bound follows from $`e^{-x}\le(1+x)^{-1}`$. These scalar inequalities prove the norm statement, including zero eigenvalues.

For the approximation statement, differentiate the jump amplitude:

```math
F'_s=-\frac12 L A e^{-sA/2},
\qquad
\int_0^u(F'_s)^\dagger F'_s\,ds
=\frac14 A^2(I-e^{-uA})\le\frac14 I.
```

For any input vector $`\psi`$ and a mesh interval with left endpoint $`a`$, Cauchy–Schwarz gives

```math
\int_a^{a+\delta}‖(F_s-F_a)\psi‖^2\,ds
\le\delta^2\int_a^{a+\delta}‖F'_s\psi‖^2\,ds.
```

Summing the intervals proves a squared error at most $`\delta^2‖\psi‖^2/4`$. The no-event component is unchanged. This proves the operator-norm bound. ∎

The comparison uses uniform wave packets, not a claim that a continuous distribution is close in total variation to point masses. The embedding is a proof device for the system-channel approximation. The algorithm's output contract does not include an arbitrary continuous-time environmental field.

## Normalizing the stack

The left-endpoint stack is close to, but not exactly, an isometry. Define its polar isometry

```math
P_\delta(u)
=M_\delta(u)\big(M_\delta(u)^\dagger M_\delta(u)\big)^{-1/2}.
```

This inverse is harmless: the matrix inside it is at least $`I`$. It is unrelated to an inverse of the decay matrix $`A`$. Lemma 1 places every singular value of $`M_\delta(u)`$ in $`[1,\sqrt{1+\delta}]`$, so

```math
‖P_\delta(u)-M_\delta(u)‖
\le\sqrt{1+\delta}-1\le\frac\delta2,
\qquad
‖E_\delta P_\delta(u)-V_u‖\le\delta.
```

For channels obtained by tracing the environmental records, an operator-norm difference $`r`$ between two isometries implies an unhalved diamond-norm difference at most $`2r`$. The statement is reference stable: tensoring either isometry with an identity changes none of these operator-norm estimates.

The compiler does not compute this inverse by diagonalizing $`A`$, postselect successful runs, or prepare an input-dependent state. It implements the polar isometry by oblivious singular-value amplification of one uniformly normalized stack, as proved on the [next page](dyadic_compiler.md).

## A coherent remaining horizon

Fix one maximum grid horizon $`T`$ and use the same mesh and interval labels for every $`u\in\{0,\delta,\ldots,T\}`$. Preserve the binary horizon register while implementing a controlled direct sum,

```math
\mathbb M_\delta
=\sum_u|u\rangle\langle u|\otimes M_\delta(u).
```

The corresponding $`\mathbb P_\delta`$ and continuum comparison are direct sums with the same control register. All bounds above therefore hold in operator norm with no factor for the number of horizons. This permits superposed remaining times. Only after the complete amplified first-event circuit has finished does reversible arithmetic subtract an accepted event time from the horizon.

The finite clock and the polar correction are parts of the algorithm. Quantum-trajectory unravelling, Kraus-stack block encodings and oblivious isometry amplification are inherited tools. In particular, Borràs and Marvian, [arXiv:2509.10425v2](https://arxiv.org/abs/2509.10425), Section 2.1, reviews the stack and isometry-amplification primitives. The new compiler here uses a global dyadic envelope to keep the stack normalization logarithmic in the maximum horizon, instead of applying short-interval instruments throughout elapsed time.
