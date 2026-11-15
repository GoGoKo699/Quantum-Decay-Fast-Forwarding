# Normalized Gaussian filters and their complete costs

The dyadic compiler uses two functions of a supplied jump stack. This file
constructs them with finite registers, uniform coefficient preparation and
explicit controlled simulation. Neither a Gaussian state oracle nor QRAM is
assumed. The Fourier identities are standard spectral filtering; the new
channel construction uses these filters inside the complete first-event stack.

## Oracle convention and Hermitian dilation

Let

```math
L=\sum_\alpha |\alpha\rangle J_\alpha,\qquad A=L^\dagger L\le I.
```

Zero-pad the rectangular operator $`L`$ to a square operator on a register of
$`n_L`$ qubits. The padding is a representation convention, not a supply of
unknown pure states. A supplied unitary $`U_L`$, with $`a_L`$ success ancillas,
has accepted block $`L`$. Its inverse and controlled versions are available;
alternatively a supplied circuit makes these controls constructible at their
ordinary gate cost. Controlled access to an arbitrary unknown unitary is not
silently inferred.

On an orientation qubit, define the Hermitian unitary

```math
U_H=\begin{pmatrix}0&U_L^\dagger\\U_L&0\end{pmatrix}.
```

Compression of the same success ancillas gives a normalization-one block
encoding of

```math
H_L=\begin{pmatrix}0&L^\dagger\\L&0\end{pmatrix},\qquad
‖H_L‖\le1.
```

Implementing $`U_H`$ uses a constant number of controlled $`U_L,U_L^\dagger`$
calls and an orientation flip. Its square has input block $`A`$ and output
block $`LL^\dagger`$. Consequently, the input block of an even function of
$`H_L`$ is the corresponding function of $`\sqrt A`$, while an odd function
has the required input-to-output block. This is the usual Hermitianization
and block-encoding construction [GSLW19, §4].

## Exact Fourier identities and normalization

For $`a\ge0`$ and $`Z\sim N(0,1)`$, spectral calculus gives

```math
E_a(H)=e^{-aH^2/2}
       =\mathbb E_Z e^{-i\sqrt a ZH}.
```

The coefficient measure is a probability measure: its $`L^1`$ normalization is
exactly one. For the odd envelope, differentiation of the Gaussian
characteristic function gives

```math
O_a(H)=\sqrt a\,H e^{-aH^2/2}
       =\mathbb E_Z iZ e^{-i\sqrt a ZH}.
```

Write $`C=\mathbb E|Z|=\sqrt{2/\pi}<1`$. If $`R`$ has Rayleigh density
$`r e^{-r^2/2}`$ on $`r>0`$, and $`\xi\in\{-1,1\}`$ is independent and uniform,
then the same identity is

```math
O_a(H)=C\,\mathbb E_{R,\xi}
        [i\xi e^{-i\xi\sqrt a RH}].
```

Thus the odd Fourier $`L^1`$ normalization is $`C`$, not $`\sqrt a`$. A single
known flag rotation with accepted amplitude $`C`$ turns the normalized average
into the desired block. In particular, the accepted input-to-output block is

```math
\sqrt a\,L e^{-aA/2}.
```

The maximum scalar magnitude of this odd function is $`e^{-1/2}`$ when
$`a\ge1`$. These identities do not replace a filter by a channel mixture:
the average is prepared coherently and unprepared as an LCU block. Failed
blocks remain in orthogonal workspace until the complete stack is amplified.

## A finite, uniform coefficient register

Here is an explicit discretization valid uniformly for $`0\le a\le a_{\max}`$.
Let $`0<\eta\le1/4`$, and choose a power of two $`M\ge8`$ satisfying

```math
M\ge4096(a_{\max}+1)/\eta^2.
```

Uniform indices $`j,\ell\in\{0,\ldots,M-1\}`$ are prepared by Hadamards.
Set

```math
u_j=(j+1/2)/M,\quad v_\ell=(\ell+1/2)/M,\quad
r(u)=\sqrt{-2\log u}.
```

For the even filter, compute

```math
\tau_{j\ell}(a)=\sqrt a\,r(u_j)\cos(2\pi v_\ell).
```

For the odd filter, use one uniform index and one sign qubit and compute
$`\tau_j(a,\xi)=\xi\sqrt a\,r(u_j)`$, together with the exact phase $`i\xi`$.
The continuous versions are respectively Box--Muller normal sampling and
inverse-CDF Rayleigh sampling. Only their explicit formulas are used here.

To bound the discretization, couple $`U,V`$ uniform on $`(0,1)`$ to their
midpoint quantizers $`Q_M(U),Q_M(V)`$. The monotonicity of $`r`$ gives

```math
\int_0^1|r(u)-r(Q_M(u))|\,du
\le \frac{4\sqrt{2\log(2M)}}{M}.
```

For completeness, the bins above $`1/M`$ telescope and contribute at most
$`r(1/M)/M`$. In the first bin, integration of the Gaussian tail gives

```math
\int_0^{1/M}r(u)\,du
\le M^{-1}[r(1/M)+1/r(1/M)],
```

and adding the midpoint term gives the displayed bound. The cosine is
$`2\pi`$-Lipschitz, and $`r(Q_M(U))\le R_M:=\sqrt{2\log(2M)}`$. Therefore
the coupling errors obey

```math
\mathbb E|\sqrt a Z-\tau_{Q_M(U),Q_M(V)}(a)|
\le(4+\pi)\sqrt a R_M/M,
```

and the signed Rayleigh construction has error at most $`4\sqrt a R_M/M`$.
For $`M\ge8`$, $`R_M\le\sqrt M`$. Our choice of $`M`$ makes both errors at most
$`\eta/8`$. The elementary inequality

```math
‖e^{-isH}-e^{-itH}‖\le|s-t|\quad(‖H‖\le1)
```

turns these coupling bounds into operator-norm bounds on both finite LCUs.
All sample times have magnitude at most

```math
T=\sqrt{2a_{\max}\log(2M)}.
```

This is also an explicit finite cutoff. The number of samples may be
polynomial in $`a_{\max}/\eta`$, but no circuit iterates over them or loads a
table of sample values. The even register has $`2\log_2M`$ qubits, and the odd
register has $`\log_2M+1`$ qubits.

## Reversible arithmetic, rather than a state-preparation oracle

Compute each $`\tau`$ to absolute error at most $`\eta/16`$, coherently in its
uniform index and, when needed, a binary parameter $`a`$. A sufficient word
size, including guards, is

```math
B=O\!\left(\log\frac{a_{\max}+1}{\eta}\right).
```

There is a direct polynomial-size reversible implementation:

1. Find the leading nonzero bit of $`u`$ and write $`u=2^{-e}v`$, $`1\le v<2`$.
   Evaluate $`\log v`$ from
   $`2\sum_{h\ge0}z^{2h+1}/(2h+1)`$, $`z=(v-1)/(v+1)\le1/3`$.
   $`O(B)`$ terms give exponentially small truncation error; add $`-e\log2`$.
2. Compute the square root by binary digit extraction on the fixed-point
   integer. Because $`|\sqrt x-\sqrt y|\le\sqrt{|x-y|}`$, twice the desired
   fractional precision before the square root controls its absolute error
   even near zero.
3. Evaluate $`\cos(2\pi v)`$ on its bounded interval by an $`O(B)`$-term Taylor
   polynomial, with fixed-point guard bits, then multiply and round.

Schoolbook reversible multiplication, long division and the above finite
polynomial evaluations give a conservative $`O(B^4)`$ Toffoli bound and
$`O(B^3)`$ temporary bits. Compute--use--uncompute returns these arithmetic
bits exactly; the finite rounded function is computed reversibly, and its
approximation error is already charged. Rational coefficients and the
constants $`\pi,\log2,C`$ require polynomially many classical bits and
polynomial-in-$`B`$ classical preparation. No assumption about a fast inverse
error function is needed.

## Coherent variable-time SELECT

Represent the rounded signed time on $`B`$ bits, with fractional spacing at
most $`\eta/16`$. Apply the product of fixed evolutions
$`e^{-i2^{h-p}H}`$ controlled on its magnitude bits, and reverse their signs
with the sign bit. The sum of all positive binary time powers is at most
$`2(T+1)`$. Every fixed-time simulator is compiled in advance; it is not
synthesized from an exponentially large table indexed by $`j,\ell`$.

Use an initialized-workspace operator error at most $`\eta/(16B)`$ per
controlled simulator. The error in the complete SELECT is then at most
$`\eta/16`$, including on coherent superpositions of all indices. Standard
block-encoded Hamiltonian simulation gives, conservatively,

```math
Q_{\rm filt}
=O\!\left[(\sqrt{a_{\max}}+1)
     \mathrm{polylog}\frac{a_{\max}+1}{\eta}\right]
```

queries to controlled $`U_L,U_L^\dagger`$ [LC19; GSLW19]. Arithmetic rounding
adds at most $`\eta/16`$ operator error. Preparing the uniform indices,
computing the times, performing SELECT, uncomputing the times and undoing the
Hadamards gives the finite LCU accepted block. For the odd case include the
one amplitude-$`C`$ flag rotation, synthesized to error at most $`\eta/16`$.
The sum of discretization, rounding, simulation and rotation errors is less
than $`\eta`$.

This construction works as a direct sum over a coherent, finitely encoded
parameter $`a`$: use a common $`M,T,B`$ determined by $`a_{\max}`$ and compute
$`\sqrt a`$ in the arithmetic. All error estimates are uniform in $`a`$.
The exact $`a=0`$ cases can also be handled directly. A later comparator can
select a residual time or discard times beyond a coherent horizon without
changing the filter normalization.

## Classical compilation and other gates are charged

The query bound does not regard arbitrary phase synthesis as free. One
implementation of each fixed-time Hamiltonian simulator uses the ordinary
even/odd Chebyshev approximations to $`\cos(sx)/4`$ and $`\sin(sx)/4`$, followed
by their constant-normalization combination and robust oblivious amplification.
This normalization is a fixed known constant, so phase-matched
constant-round amplification suffices; its finitely many constant angles
are computed and synthesized to the required precision. Their degree is
$`d=O(|s|+\log(1/\zeta))`$ for target error $`\zeta`$. Chebyshev interpolation
can compute their coefficient lists using $`O(d\mathrm{polylog}(d/\zeta))`$
bit operations. The fixed scaling gives a constant margin from the unit
circle. The complementary polynomial is also constructed and charged: map a
real parity polynomial $`p`$ to the Laurent polynomial
$`b(z)=ip((z+z^{-1})/2)`$ and shift by a monomial when an analytic polynomial
is required. Apply [BS25, Algorithm1, Theorem3]. It evaluates
$`\log(1-|b|^2)`$ by FFT, retains its analytic Fourier part, exponentiates and
uses another FFT to obtain the canonical complementary coefficients.
This logarithmic Fourier spectral-factor construction is the outer-factor
step, also called the Weiss step. The complement has no roots in the closed unit disk; hence it supplies the
required outer completion. In the convention of [NSYL25], assign this
zero-free analytic factor to $`a^*`$; conjugate and reverse the coefficients
when converting from the opposite spectral-factor convention. This is a
linear-time coefficient relabelling. At constant margin, coefficient error
$`\epsilon_c`$ needs $`N=O(d\log(d/\epsilon_c))`$ samples and
$`O(N\log N)`$ arithmetic operations. The logarithm is evaluated a fixed
distance from its singularity. Choose its arithmetic and coefficient
precision with $`O(\log^2d+\log(1/\zeta))`$ guard bits, or a larger fixed
polylogarithmic number; this also covers the error growth in the subsequent
stable inverse factorization. Thus neither the completion nor its numerical
precision hides a power of $`1/\zeta`$ or $`d`$.

Use this canonical completion in the numerically stable inverse nonlinear
FFT of [NSYL25, Algorithm1, Theorem5.6]; its phase synthesis
uses $`O(d\log^2d)`$ arithmetic operations with
$`O(\log^2d+\log(1/\zeta))`$ bits. This bounds the classical compilation by
$`d\mathrm{polylog}(d/\zeta)`$ bit operations. The fixed normalization
is paid only inside each Hamiltonian-simulation primitive, where robust
amplification restores the simulated unitary; it is not multiplied across
the residual Gaussian filters.

Summing the compiled binary time powers retains
$`Q_{\rm filt}\mathrm{polylog}((a_{\max}+1)/\eta)`$ classical bit
operations and circuit-description size. This setup depends on the requested
time and accuracy and the supplied oracle interface, not on a list of matrix
entries. An oracle gate cost $`g_L`$ yields total gate cost

```math
Q_{\rm filt}\,[g_L+\mathrm{poly}(n_L+a_L+B)]
+\mathrm{poly}(B),
```

with $`O(n_L+a_L+\mathrm{poly}(B))`$ live qubits for one filter call,
including its data, success and arithmetic registers. Standard finite-gate
rotation synthesis contributes polylogarithmic factors in the accuracy.
Physical implementation costs inside $`g_L`$ are not removed by this theorem.

## Filter lemma used by the channel compiler

For $`A=L^\dagger L\le I`$, $`0\le a\le a_{\max}`$ and $`0<\eta\le1/4`$,
the preceding construction supplies normalization-one block encodings,
with operator error at most $`\eta`$, of

```math
e^{-aA/2}
\quad\hbox{and}\quad
\sqrt a\,L e^{-aA/2}.
```

Their query and complete implementation costs are the bounds above. A
normalization-one block encoding is not a deterministic nonunitary filter.
Fresh block-success bits retain every failure in coherent composition;
only the full near-isometric first-event stack is amplified in
[the dyadic compiler](dyadic_compiler.md). In particular, no factor $`1/2`$
is inserted into every binary residual Gaussian, which would reintroduce a
polynomial normalization loss.

When a Hamiltonian-simulation implementation is specified first through an
accepted block, its accepted-block error is chosen quadratic in the desired
initialized-workspace isometry error. Near-unitarity then bounds the retained
failure amplitude by the desired error, rather than its square root. The
constant-normalization amplification is analyzed with that smaller error.
This replaces $`\log(1/\zeta)`$ by at most a constant multiple and leaves the
query, gate and classical-preprocessing bounds unchanged. No leakage is
discarded when such a simulator is controlled by a clock bit.

## References for inherited ingredients

- **[GSLW19]** A.Gilyén, Y.Su, G.H.Low and N.Wiebe,
  *Quantum singular value transformation and beyond*, STOC2019,
  [arXiv:1806.01838](https://arxiv.org/abs/1806.01838): block encodings,
  polynomial transformations, linear combinations and robust amplification.
- **[LC19]** G.H.Low and I.L.Chuang, *Hamiltonian Simulation by Qubitization*,
  Quantum3,163(2019),
  [arXiv:1610.06546v3](https://arxiv.org/abs/1610.06546v3): simulation from a
  projected unitary oracle. The present bounds allow extra logarithms.
- **[NSYL25]** H.Ni, R.Sarkar, L.Ying and L.Lin,
  *Inverse nonlinear fast Fourier transform on SU(2) with applications to
  quantum signal processing*,
  [arXiv:2505.12615v1](https://arxiv.org/html/2505.12615v1): Algorithm1 and
  Theorem5.6, with the outer-completion and nonzero-margin conditions retained.
- **[BS25]** B.K.Berntson and C.Sünderhauf,
  *Complementary Polynomials in Quantum Signal Processing*,
  Commun.Math.Phys.406,161(2025),
  [DOI:10.1007/s00220-025-05302-9](https://doi.org/10.1007/s00220-025-05302-9):
  canonical outer completion, Algorithm1 and Theorem3. An authored full-text
  copy is available [here](https://pmc.ncbi.nlm.nih.gov/articles/PMC12137491/).
