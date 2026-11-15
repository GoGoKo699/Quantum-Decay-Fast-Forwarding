# Model and simulation theorem

A decay process may have only a few irreversible events but arbitrarily long
waiting times. Counting its possible jumps does not by itself give a fast
quantum simulation: the waiting time carries information about the input state
and changes the coherence of the output. The construction here compresses that
information while preserving the complete system channel.

## 1. Purely dissipative dynamics

Let the finite-dimensional system have a known grading

```math
\mathcal H=\bigoplus_{g=0}^{k}\mathcal H_g,
\qquad G=\sum_{g=0}^{k}gP_g.
```

The normalized jump operators are $`J_1,\ldots,J_m`$, and

```math
L=\sum_{a=1}^{m}|a\rangle\otimes J_a,
\qquad A=L^\dagger L=\sum_a J_a^\dagger J_a\le I.
```

The generator has **no Hamiltonian term**:

```math
\mathcal L(\rho)=\sum_a J_a\rho J_a^\dagger
-\frac12(A\rho+\rho A),
\qquad \mathcal E_u=e^{u\mathcal L}.
```

We impose two structural promises:

1. Every jump strictly lowers the grading:
   $`P_gJ_aP_h=0`$ unless $`g<h`$.
2. The total loss operator preserves it: $`[A,G]=0`$.

The second promise keeps the no-jump propagator
$`K_0(u)=e^{-uA/2}`$ within each grade. Thus every trajectory has at most
$`k`$ jumps. This statement includes coherent superpositions of initial grades;
the algorithm does not measure the grading.

A sufficient physical subclass is homogeneous excitation loss:
$`[G,J_a]=-r_aJ_a`$ for a positive integer $`r_a`$. Then
$`[G,J_a^\dagger J_a]=0`$ for each $`a`$. The proof only needs the two
promises above, so different jump-rate matrices may fail to commute within a
grade. A triangular or nilpotent jump alone does not imply the second promise;
see the [counterexample](examples.md).

The grading is a promise defining the input family and the supplied bound
$`k`$. No efficient diagonalization of $`A`$ or measurement of its eigenvalues
is supplied. In particular, no positive lower bound on a decay rate or
dissipative gap is assumed. The grade-zero sector is dark because strict
lowering implies $`J_aP_0=0`$.

## 2. Coherent input access

The input primitive is a projected unitary encoding of the rectangular map
$`L`$. Known input and output ancilla projectors $`\Pi,\widetilde\Pi`$ obey

```math
\widetilde\Pi U_L\Pi=L
```

under their specified system-register identifications. Calls to $`U_L`$,
$`U_L^\dagger`$ and their controlled versions are supplied and counted.
Equivalently, a supplied circuit can be controlled and reversed with its
resulting gates charged. The ability to control an arbitrary unknown unitary
is not inferred from forward access.

Known ancilla reflections, ordinary reversible arithmetic and elementary
gates are available. Their costs are included in the
[filter and resource account](filters_and_resources.md). The encoding may
itself require costly loading, calibration or preprocessing; those costs are
additional inputs to the complete gate comparison. Calling an encoding an
oracle does not make its implementation free. No QRAM lookup table is used by
the waiting-time compiler.

The output is a quantum system state. The simulator retains its internal jump
indices, clocks and approximation flags, then discards them. It makes no
claim to reproduce the physical emitted field or to support an arbitrary
controller that resolves continuous jump times. Preparation of the caller's
input state and subsequent measurement or estimation are separate costs.

For unnormalized physical jumps $`F_a`$ with a supplied encoding normalization
$`\beta>0`$, set $`J_a=F_a/\beta`$ and $`\tau=\beta^2T`$. The theorem is
applied at normalized time $`\tau`$. The supplied normalization is a bound,
not a promise that the exact operator norm is revealed classically. If all
jumps are known to vanish, the channel is the identity.

## 3. Accuracy and quantifiers

All channel errors use the **unhalved diamond norm**. For every promised
finite system, encoding, time $`\tau\ge0`$ and target $`0<\varepsilon<1/4`$,
the target is a trace-preserving simulation $`\widetilde{\mathcal E}_\tau`$
with

```math
‖\widetilde{\mathcal E}_\tau-\mathcal E_\tau‖_\diamond
\le\varepsilon.
```

This includes arbitrary reference-entangled inputs. Approximations are
uniform over the input state. Numerical failure branches are retained rather
than postselected away; their contribution is part of this error.

## 4. Proof route

The connected construction has four components:

| Component | Scientific role | Proof |
|---|---|---|
| First-event representation | Keeps the information in emission times | [First event](first_event.md) |
| Finite waiting-time clock | Controls channel error without an elapsed-time factor | [Time discretization](time_discretization.md) |
| Dyadic normalization and amplification | Avoids a normalization proportional to the full waiting horizon | [Compiler](dyadic_compiler.md) |
| Gaussian Fourier filters | Supplies normalization-preserving, no-QRAM circuits | [Filters and resources](filters_and_resources.md) |

The theorem statement and final bounds are assembled in the
[simulation theorem](simulation_theorem.md). The
[lower bound](lower_bound.md) establishes the unavoidable square-root horizon
dependence already for one unknown scalar decay amplitude. It does not claim
optimal dependence on $`k`$, precision, memory or elementary gate count.

## 5. Scope of the consequence

The resource improvement concerns simulation of a restricted but nonunital
class of complete channels. General Hamiltonian dynamics cannot be added for
free: the case with zero jumps would already include arbitrary Hamiltonian
simulation. Unknown slow rates remain in the oracle model, and a small
dissipative gap does not require time stepping in this construction.

An efficient quantum simulation bound is distinct from a demonstrated
classical speedup. The scalar lower bound is against coherent oracle
algorithms under the same access promise. It is not a lower bound for a known
scalar rate supplied as an ordinary number. Read the
[related-work comparison](../references/related_work.md) for the exact inherited
ingredients and the change from prior models.
