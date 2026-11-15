# Full-channel fast-forwarding at bounded decay depth

The result combines a uniform first-event circuit with a bound on the number
of events. Waiting times can be arbitrarily long, and the positive decay
rates can be arbitrarily small. The simulator pays square-root horizon cost
for a waiting-time circuit rather than applying a short-time channel
throughout the horizon.

## Theorem

Adopt the [model and access conventions](model.md). In particular, the
Hamiltonian is zero, every jump strictly lowers a grading with values
$`0,\ldots,k`$, and $`A=\sum_a J_a^\dagger J_a\le I`$ preserves that
grading. Controlled and inverse uses of a normalized projected unitary
encoding of $`L=\sum_a|a\rangle\otimes J_a`$ are supplied.

For every normalized horizon $`\tau\ge0`$ and
$`0<\varepsilon<1/4`$, a finite trace-preserving quantum circuit implements
a system channel satisfying

```math
\|\widetilde{\mathcal E}_\tau-e^{\tau\mathcal L}\|_\diamond
\le\varepsilon
```

in unhalved diamond norm, using

```math
Q=O\!\left[(k+1)\sqrt{1+\tau}\,
\operatorname{polylog}\!\left(
\frac{(2+\tau)(k+1)}{\varepsilon}\right)\right]
```

controlled forward or inverse encoding calls. The estimate includes arbitrary
reference-entangled input states. All internal physical and numerical-failure
records are retained until their final trace-out; no input-dependent
postselection is used. For $`k=0`$ or $`\tau=0`$, the channel is the identity
and no oracle call is needed.

Let $`C_U`$ bound the gates for one controlled forward or inverse encoding
call, including its own implementation accuracy, and let $`n_L,a_L`$ be the
data and success-work widths of the padded encoding. With

```math
b=\left\lceil\log_2\!\left(
\frac{(2+\tau)(k+1)}{\varepsilon}\right)\right\rceil+O(1),
```

a conservative implementation has total elementary gate count

```math
O\!\left[Q\big(C_U+\operatorname{poly}(n_L+a_L+b)\big)
+(k+1)\operatorname{poly}(b)\right]
```

and live-qubit count
$`O((k+1)(n_L+a_L+\operatorname{poly}(b)))`$. The latter is a simple
workspace upper bound, not a memory optimum. The physical clock and event
records themselves use $`O(k(b+\log(m+1)))`$ bits. Classical circuit
compilation and finite-precision scalar preparation are charged in the
[filter resource account](filters_and_resources.md); they require at most
the filter query-length scale times polynomially logarithmic factors, plus
polynomially logarithmic outer-amplification setup. Costs of constructing
the supplied encoding, preparing the caller's input, and reading out an
application's answer are additional.

For physical jumps encoded with known normalization $`\beta`$, use
$`\tau=\beta^2T`$. This normalization and the cost of implementing its
encoding are part of the resource comparison.

## Proof and explicit accuracy allocation

Assume $`k\ge1`$ and $`\tau>0`$. Choose a dyadic mesh $`\delta`$ with

```math
\frac{\varepsilon}{24(k+1)}<\delta
\le\frac{\varepsilon}{12(k+1)}.
```

Round the requested horizon upward to $`u=\delta\lceil\tau/\delta\rceil`$.
Choose the maximum clock horizon $`T`$ as the least power of two at least
$`\max\{1,\tau\}`$. Since $`T`$ is itself a grid value, $`u\le T`$ and
$`T<2\max\{1,\tau\}`$.

The [first-event construction](first_event.md) defines a polar grid isometry
$`P_\delta(v)`$ for every grid horizon $`v\le T`$. It preserves the branch labels and grading and has strictly lowering event
blocks, because its input polar correction is a function of $`A`$. Implement it with complete
initialized-workspace isometry error

```math
\eta=\frac{\varepsilon}{6(k+1)}.
```

The [dyadic compiler](dyadic_compiler.md) supplies this implementation
uniformly over a coherent remaining-horizon register. Its per-slot channel
error is at most $`2\eta`$, and its query count is

```math
O\!\left[\sqrt{1+\tau}\,
\operatorname{polylog}\!\left(
\frac{(2+\tau)(k+1)}{\varepsilon}\right)\right].
```

Use at most $`k`$ event slots. In a no-event branch, stop the trajectory.
In an event branch at grid time $`r\delta`$, retain that time and event
index, subtract $`r\delta`$ reversibly from the remaining horizon, and apply
the next slot. Even the $`r=0`$ branch lowers the grade; it cannot generate
an unbounded discrete sequence. After $`k`$ events the system is in grade
zero, where further dynamics is the identity. Optional unused slots act as
the identity. No-event histories have the same vacuum record, preserving
coherences between their initial grades.

The [channel-level discretization proof](time_discretization.md) gives

```math
\|\mathcal S_{k,u}-\mathcal E_\tau\|_\diamond
\le(4k+2)\delta.
```

It compares uniform-bin wavepackets and the actual physical future
semigroup; it does not compare discrete point masses with a continuous
probability distribution. Keeping previous event-time records makes the
subsequent channel error block diagonal in history after those records are
traced out. Thus there is no factor from the number of histories.

A hybrid replacing one ideal slot at a time by its compiled isometry adds
at most $`2k\eta`$. The actual numerical-failure spaces remain part of the
trace-preserving circuit. An erroneous branch is stopped and retained;
there is no assumption that the finite-precision circuit itself preserves
the grade exactly. The uniform isometry error already bounds that deviation.
Consequently,

```math
\|\widetilde{\mathcal E}_\tau-\mathcal E_\tau\|_\diamond
\le(4k+2)\delta+2k\eta
\le\frac{(4k+2)\varepsilon}{12(k+1)}
+\frac{k\varepsilon}{3(k+1)}<\varepsilon.
```

Multiplying the per-slot query cost by $`k`$ proves the stated, slightly
looser $`k+1`$ bound. The uniform time register has $`O(b)`$ bits. The
[explicit filter circuits](filters_and_resources.md), arithmetic and
ancilla reflections then give the gate and workspace bounds. No loop over
the $`T/\delta`$ possible grid times occurs. ∎

## What is sharp, and what is not

At fixed nonzero accuracy and fixed positive decay depth, the square-root
power of the normalized horizon is optimal: the
[scalar-amplitude lower bound](lower_bound.md) requires
$`\Omega(\sqrt\tau)`$ queries already with one possible event.
Logarithms, dependence on $`k`$, precision, gate counts and workspace are not
claimed optimal. When $`k`$ grows with the horizon, this construction need
not improve on a general linear-time simulator.

The result is a constructive circuit theorem in the stated coherent-access
model. The supplied [finite checks](../verification/README.md) reproduce
instrument identities, coherence kernels and small complete channels.
They are not a compiled fault-tolerant implementation, independent expert
verification, a classical hardness result or a hardware crossover study.
