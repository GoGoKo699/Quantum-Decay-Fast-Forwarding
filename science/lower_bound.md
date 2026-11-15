# A square-root time lower bound from one unknown decay rate

The square-root dependence on the requested time is necessary in the supplied coherent-oracle model, already for a two-level system with at most one event. This is a worst-case oracle statement. It does not assert that every known decay process remains difficult at long times.

## One-event channels with identical classical metadata

Let the known grading be $`G=\mathrm{diag}(0,1)`$, with zero internal Hamiltonian and one jump

```math
J_\sigma=\sigma|0\rangle\langle1|,
\qquad A_\sigma=\sigma^2|1\rangle\langle1|,
\qquad 0\le\sigma\le1.
```

The classically supplied normalization is the common bound $`1`$. The exact norm $`\|J_\sigma\|=\sigma`$ is **not** supplied as classical input. The system dimension, grading, number of jump labels, normalization, requested horizon and allowed query types are the same for every member of the family. The unknown parameter occurs only in the oracle.

The generator and its action on the excited state are

```math
\mathcal L_\sigma(\rho)
=\sigma^2\left(|0\rangle\langle1|\rho|1\rangle\langle0|
-\frac12\{|1\rangle\langle1|,\rho\}\right),
```

```math
e^{t\mathcal L_\sigma}(|1\rangle\langle1|)
=(1-e^{-t\sigma^2})|0\rangle\langle0|
+e^{-t\sigma^2}|1\rangle\langle1|.
```

For every requested $`t\ge1`$, compare $`\sigma_0=0`$ and $`\sigma_1=t^{-1/2}`$. Their ideal outputs on this known input have half trace distance

```math
\alpha=1-e^{-1}.
```

Both channels satisfy the grading promise with $`k=1`$. Small nonzero rates are essential to this worst-case family; a known positive lower bound on the decay rate would change the long-time problem.

## Explicit close unitary completions

Write $`c_\sigma=\sqrt{1-\sigma^2}`$. In the basis $`|0,0\rangle,|0,1\rangle,|1,0\rangle,|1,1\rangle`$, where the first register is the block ancilla, supply

```math
U_\sigma=
\begin{pmatrix}
0&\sigma&c_\sigma&0\\
0&0&0&1\\
1&0&0&0\\
0&c_\sigma&-\sigma&0
\end{pmatrix}.
```

The columns are orthonormal and

```math
(\langle0|\otimes I)U_\sigma(|0\rangle\otimes I)=J_\sigma.
```

Thus this is an exact block encoding with common normalization one. Its distance from $`U_0`$ is

```math
d_\sigma:=\|U_\sigma-U_0\|
=\sqrt{2-2\sqrt{1-\sigma^2}}
=2\sin\left(\frac{\arcsin\sigma}{2}\right)
\le\sqrt2\,\sigma.
```

Inverse and controlled calls do not evade this proximity:

```math
\|U_\sigma^\dagger-U_0^\dagger\|=d_\sigma,
\qquad
\|\mathrm{ctrl}(U_\sigma)-\mathrm{ctrl}(U_0)\|=d_\sigma.
```

The same holds for controlled inverses and direct-sum selection of these query types. Each use is one charged oracle call. No arbitrary-time power of the unknown oracle is supplied for unit cost.

## Hybrid argument and accuracy convention

Suppose a simulator uses at most $`q`$ oracle calls and produces channels $`\widetilde\Phi_\sigma`$ with **unhalved** diamond error at most $`\epsilon`$:

```math
\|\widetilde\Phi_\sigma-e^{t\mathcal L_\sigma}\|_\diamond\le\epsilon.
```

All known gates, initial ancillas and control choices are independent of the unknown $`\sigma`$. Arbitrary input-independent computation, retained quantum memory, intermediate measurements and resets are allowed. Purifying the known operations, a query-by-query hybrid gives Euclidean distance at most $`q d_{\sigma_1}`$ between the two final pure states. Their reduced outputs consequently have half trace distance at most $`q d_{\sigma_1}`$.

On the other hand, the triangle inequality and the two simulator error bounds give output half trace distance at least $`\alpha-\epsilon`$ on the excited-state input. Hence

```math
q\ge\frac{\alpha-\epsilon}{d_{\sigma_1}}
\ge(\alpha-\epsilon)\sqrt{\frac t2},
\qquad 0\le\epsilon<\alpha,
\qquad t\ge1.
```

In particular, at any fixed $`0\le\epsilon\le(1-e^{-1})/2`$,

```math
q\ge\frac{1-e^{-1}}{2\sqrt2}\sqrt t=\Omega(\sqrt t).
```

This is the standard hybrid lower-bound method applied to an explicit dissipative channel family. The [finite checks](../verification/README.md) verify the unitary completion, controlled/inverse distances and constant channel-output separation at selected horizons. The analytical argument establishes the bound for all $`t\ge1`$.

The zero-rate member is convenient, rather than necessary. If a positive rank-one jump is required, compare $`\sigma_0=t^{-1/2}`$ and $`\sigma_1=2t^{-1/2}`$ for $`t\ge8`$. Both jumps have rank one and the same kernel, their oracle distance is at most $`\sqrt{2/t}`$, and their output half trace distance is $`e^{-1}-e^{-4}`$. The same proof gives a square-root lower bound at fixed sufficiently small error.

## What is and is not matched

The [upper bound](model.md) and this converse match the time exponent for fixed positive event budget, up to logarithmic factors. They do not establish optimal joint dependence on $`k`$ and $`\epsilon`$, a classical computational lower bound, or a hardware advantage. Providing the exact scalar rate classically makes this particular two-level channel easy to synthesize directly; the theorem concerns the common-normalization quantum-oracle input specified above.
