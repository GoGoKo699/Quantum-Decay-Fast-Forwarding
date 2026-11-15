# Coherent decay examples and the boundaries of the promise

The compiler addresses full quantum channels. Populations alone do not capture its task: different decay rates leave different waiting-time records, and those records affect surviving coherences. The examples below expose that issue, include a cascade with noncommuting rate matrices, and show why strict triangularity alone is insufficient.

## Two excited levels with unequal lifetimes

Use two ground states $`|g_a\rangle,|g_b\rangle`$ and two excited states $`|e_a\rangle,|e_b\rangle`$. One jump operator is

```math
J=\sqrt{\lambda_a}|g_a\rangle\langle e_a|
+\sqrt{\lambda_b}|g_b\rangle\langle e_b|,
\qquad 0<\lambda_a,\lambda_b\le1.
```

This is a one-event process with homogeneous grade lowering. Its rate matrix is diagonal, with eigenvalues $`0,0,\lambda_a,\lambda_b`$. The input coherence $`|e_a\rangle\langle e_b|`$ contributes the following ground-state coherence at time $`t`$:

```math
c_{ab}(t)=\int_0^t\sqrt{\lambda_a\lambda_b}
e^{-s(\lambda_a+\lambda_b)/2}\,ds
=\frac{2\sqrt{\lambda_a\lambda_b}}{\lambda_a+\lambda_b}
\left(1-e^{-t(\lambda_a+\lambda_b)/2}\right).
```

The missing coherence has entered the event-time record. In particular, the late-time coefficient is less than one when the rates differ. Replacing the jump instrument by one Kraus operator

```math
J\left[\frac{I-e^{-tA}}{A}\right]^{1/2}
```

would instead give $`\sqrt{(1-e^{-t\lambda_a})(1-e^{-t\lambda_b})}`$, approaching one. The quotient is defined continuously on the kernel, but that does not repair the channel error. The two constructions agree on decay probabilities and disagree on off-diagonal matrix elements.

For $`\lambda_a=1/4`$ and $`\lambda_b=1`$, the [reproducible diagnostics](../verification/README.md) obtain:

| Time | Exact ground-coherence coefficient | Incorrect collapsed coefficient |
|---:|---:|---:|
| 1 | 0.371791 | 0.373931 |
| 4 | 0.734332 | 0.787745 |
| 16 | 0.799964 | 0.990800 |
| 64 | 0.800000 | 1.000000 |

These are linear coefficients of the channel on a matrix unit. For a normalized excited superposition, its off-diagonal entry has the additional input factor $`1/2`$. The discrepancy is the reason the [first-event instrument](first_event.md) retains time labels until the channel has been completed.

## A two-event cascade with noncommuting individual rates

Let each grade $`0,1,2`$ have dimension two. In that order, define

```math
J_a=\begin{pmatrix}
0&B_a&0\\
0&0&C_a\\
0&0&0
\end{pmatrix},
\qquad a=1,2,
```

```math
B_1=\frac16\begin{pmatrix}4&1\\0&2\end{pmatrix},
\quad C_1=\frac16\begin{pmatrix}2&1\\-1&3\end{pmatrix},
\quad B_2=\frac16\begin{pmatrix}1&-1\\2&1\end{pmatrix},
\quad C_2=\frac16\begin{pmatrix}1&2\\1&-1\end{pmatrix}.
```

Both jumps lower the grade by one. Their total rate matrix is

```math
A=0_2\oplus\frac1{36}\begin{pmatrix}21&5\\5&7\end{pmatrix}
\oplus\frac1{36}\begin{pmatrix}7&0\\0&15\end{pmatrix},
\qquad \|A\|\simeq0.627842369<1.
```

Thus $`[A,G]=0`$, every trajectory has at most two events, and the normalization is already valid without an instance-dependent rescaling. However,

```math
\|[J_1^\dagger J_1,J_2^\dagger J_2]\|=\frac1{162}>0.
```

Consequently, the individual rate matrices cannot all be diagonalized in one basis. A common scalar relation $`[A,J_a]=\lambda J_a`$ also fails. The example lies within the grading promise while falling outside the special commuting-rate reductions discussed in [related work](../references/related_work.md).

The finite check constructs $`e^{t\mathcal L}`$ by exponentiating the full $`36\times36`$ matrix representation of the Lindblad generator. Independently, it constructs the actual left-grid, polar-normalized first-event recursion, retaining two possible events and continuing at the remaining horizon after each event. For time $`t=4`$:

| Mesh | Unhalved normalized-Choi difference | Resulting diamond-norm upper bound |
|---:|---:|---:|
| 1/4 | 0.025678 | 0.154068 |
| 1/8 | 0.012956 | 0.077734 |
| 1/16 | 0.006507 | 0.039041 |

The upper bound multiplies the normalized-Choi trace norm by the input dimension six. It is a valid, potentially loose estimate rather than an optimized diamond norm. The checks also test complete positivity and trace preservation, compare the recursion with direct Kraus enumeration on a small grid, and cover times $`1,4,16,64`$. This small known-matrix example is a channel diagnostic, not a claim of computational advantage over classical matrix exponentiation.

## Strictly lowering jumps can still have arbitrarily long event records

Consider

```math
J=\frac12\begin{pmatrix}0&1&1\\0&0&1\\0&0&0\end{pmatrix},
\qquad G=\mathrm{diag}(0,1,2),
\qquad
A=\frac14\begin{pmatrix}0&0&0\\0&1&1\\0&1&2\end{pmatrix}.
```

Every matrix element of $`J`$ strictly lowers the grade, and $`J^3=0`$. Nevertheless, $`[A,G]\ne0`$. The no-event evolution can mix grades one and two, replenishing the higher-grade component between jumps.

Set $`K=J e^{-A/2}`$, corresponding to one unit of waiting followed by a jump. Its first column and third row vanish. On the lower-right two-dimensional block of $`e^{-A/2}`$, the off-diagonal entry is nonzero and its diagonal entries are positive. Hence $`K`$ has the form

```math
K=\begin{pmatrix}0&a&b\\0&c&d\\0&0&0\end{pmatrix},
\qquad c\ne0,\quad d>0.
```

For every positive integer $`m`$, the grade-one component of $`K^m|2\rangle`$ is $`c^{m-1}d\ne0`$. Thus the interleaved trajectory is not truncated by $`J^3=0`$. The diagnostics obtain

```math
\|K^3|2\rangle\|^2\simeq6.53094\times10^{-5},
\qquad
\|K^5|2\rangle\|^2\simeq4.76899\times10^{-10}.
```

These are trajectory densities at specified waiting times, not probabilities of a single point in a continuous distribution. Continuity gives nonzero integrated probability on sufficiently small neighborhoods of those times. This example explains the separate assumption $`[A,G]=0`$ in the [model](model.md); homogeneous lowering of each jump is one sufficient way to obtain it.

## Where the time lower bound enters

The noncommuting example demonstrates the scope of the construction. The [matching time-exponent obstruction](lower_bound.md) needs only one unknown two-level decay rate. At time $`t`$, rates zero and $`t^{-1/2}`$ have close normalized oracle unitaries but a constant channel-output separation. This distinction separates a small number of physical decay events from the cost of implementing their unknown state-dependent waiting times.
