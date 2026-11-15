# Discretizing complete decay trajectories

This file proves an error bound for the full output channel, including
arbitrary reference entanglement. A finite time label is embedded as a uniform
wavepacket over its bin. A point-tagged clock and a continuous clock are not
claimed to be close in total variation. The theorem does not grant arbitrary
continuous-time feedback access to the simulator's internal records.

## Model and exact first-event map

Write $\mathcal E_u=e^{u\mathcal L}$, with

$$
\mathcal L(\rho)=\sum_\alpha J_\alpha\rho J_\alpha^\dagger
-\tfrac12\{A,\rho\},\qquad
A=\sum_\alpha J_\alpha^\dagger J_\alpha\le I.
$$

There is no Hamiltonian term. A known grading $G$ has values $0,\ldots,k$;
each $J_\alpha$ strictly lowers grade and $[A,G]=0$. Homogeneity of each
jump in the grading is a sufficient special case of the latter condition.
No-jump evolution therefore preserves grade, and a trajectory from grade at
most $q$ contains at most $q$ jumps. These statements also hold for coherent
superpositions of grades.

Let $L=\sum_\alpha|\alpha\rangle J_\alpha$ and
$F_s=L e^{-sA/2}$. The first-event isometry is

$$
V_u\psi=|{\rm no}\rangle e^{-uA/2}\psi
+\int_0^u |{\rm yes},s\rangle F_s\psi\,ds.
$$

The integral denotes an element of the time-record space
$L^2([0,u])$, not a Riemann integral of orthogonal normalized point vectors.
It is isometric because

$$
V_u^\dagger V_u=e^{-uA}+
\int_0^u A e^{-sA}\,ds=I.
$$

Tracing the retained first-event label and applying the future physical
channel on a jump branch gives the exact Volterra expansion

$$
\mathcal E_u(\rho)=e^{-uA/2}\rho e^{-uA/2}
+\sum_\alpha\int_0^u
\mathcal E_{u-s}
\big(J_\alpha e^{-sA/2}\rho e^{-sA/2}J_\alpha^\dagger\big)\,ds.
$$

It can be verified by differentiation or by the quantum-jump Dyson expansion.
The grading makes its recursive expansion finite at depth $k$.

## Grid stack, exact norm and polar correction

Take $0<\delta\le1$ and a grid horizon $u=m\delta$. Define

$$
M_\delta(u)\psi=|{\rm no}\rangle e^{-uA/2}\psi
+\sqrt\delta\sum_{r=0}^{m-1}|{\rm yes},r\rangle
L e^{-r\delta A/2}\psi.
$$

At a zero eigenvalue the following scalar quotient is defined continuously.
A geometric sum gives the exact identity

$$
M_\delta(u)^\dagger M_\delta(u)
=I+\left[\frac{\delta A}{1-e^{-\delta A}}-I\right]
  (I-e^{-uA}).
$$

For $x\ge0$, $1-e^{-x}\le x$ and
$1-e^{-x}\ge x/(1+x)$. Hence

$$
I\le M_\delta(u)^\dagger M_\delta(u)\le(1+\delta)I.
$$

Let

$$
R_u=[M_\delta(u)^\dagger M_\delta(u)]^{-1/2},\qquad
P_\delta(u)=M_\delta(u)R_u.
$$

Then $P_\delta(u)$ is an isometry and

$$
‖P_\delta(u)-M_\delta(u)‖
\le\sqrt{1+\delta}-1\le\delta/2.
$$

The polar correction is used to specify the exact ideal grid map. The
compiler implements this polar isometry by amplification; it is not asked to
compute an inverse-square-root table. Since $R_u$ is a function of $A$, it
preserves the grading. The jump blocks of $P_\delta(u)$ still strictly lower
grade. At $u=0$ the map is the identity survival branch.

## Uniform wavepacket comparison

Embed $|{\rm yes},r\rangle$ into the normalized indicator wavepacket
$\delta^{-1/2}\mathbf1_{[r\delta,(r+1)\delta)}$ and keep the no-event flag
orthogonal. Denote this embedding by $W$. All horizons may use one common
ambient interval $[0,T]$, with zero padding outside their support.

The load-bearing derivative estimate is

$$
\int_0^u F_s'^\dagger F_s'\,ds
=\frac14A^2(I-e^{-uA})\le\frac14I.
$$

On one bin, Cauchy--Schwarz gives

$$
\int_{r\delta}^{(r+1)\delta}
‖(F_s-F_{r\delta})\psi‖^2\,ds
\le\delta^2\int_{r\delta}^{(r+1)\delta}
‖F_v'\psi‖^2\,dv.
$$

Summing bins therefore yields

$$
‖WM_\delta(u)-V_u‖\le\delta/2,
\qquad
‖WP_\delta(u)-V_u‖\le\delta.
$$

The same operator bounds hold with any untouched reference tensor factor.
Two isometries at operator distance $d$ induce channels at unhalved diamond
distance at most $2d$, even after the same subsequent channel. Thus replacing
$V_u$ by the embedded polar grid isometry costs at most $2\delta$ before
future time is rounded. The bound is independent of the horizon $u$.

## Future time and the full-channel recurrence

The channel norm of the generator satisfies

$$
‖\mathcal L‖_\diamond\le2‖A‖\le2.
$$

Indeed the completely positive jump map has diamond norm $‖A‖$ and the
two left/right multiplication terms together have norm at most $‖A‖$.
Contractivity of channels consequently gives

$$
‖\mathcal E_v-\mathcal E_w‖_\diamond\le2|v-w|.
$$

All complete prior records are retained until final trace. Subsequent maps
read those records and append new ones; they never recombine different prior
histories. It is consequently exact, for the final system channel, to dephase
the prior jump/time labels before analyzing the next event. Each prior
history then has a definite remaining horizon $u$. The same observation lets
us treat the new time label as a CP instrument: read its position POVM and apply the
physical continuation $\mathcal E_{u-s}$ in its sector. Applying this one
channel to $V_u$ and $WP_\delta(u)$ costs at most $2\delta$ by the preceding
isometry bound. For the latter map, the pre-continuation system amplitude is
constant within each time bin. After the time label is discarded, its jump
branch therefore averages $\mathcal E_{u-s}$ uniformly over that bin.
Replacing this average by $\mathcal E_{u-r\delta}$ costs at most
$2\delta$: each $s$ differs from $r\delta$ by at most $\delta$, and the sum
of the jump-branch probabilities is at most one. This probability bound uses
the polar map's exact isometry, not a norm estimate for every separate Kraus
operator. It remains true for every reference-entangled density operator.
The argument uses diamond continuity of physical channels only on these
conditional sectors. It does not infer closeness of arbitrary coherently
controlled Stinespring dilations from closeness of their reduced channels.
The first-event direct-sum operator-norm bounds remain valid coherently;
the separate history-sector argument justifies their use in this recursion.
For a continuous record, this means its spectral-measure instrument followed
by integration, not a trace-class density matrix diagonal in unnormalizable
point vectors.

Now define $\mathcal S_{q,u}$ recursively: apply $P_\delta(u)$; stop on its
no-event flag; on jump label $r$ apply
$\mathcal S_{q-1,u-r\delta}$, and discard all internal labels at the end.
At grade zero it is the identity. Let $d_q$ be the worst unhalved diamond
error on inputs supported on grades at most $q$, allowing arbitrary reference
systems and all grid horizons under consideration. The preceding two
replacements and channel contractivity imply

$$
d_q\le4\delta+d_{q-1},\qquad d_0=0.
$$

The third replacement uses the lower-grade guarantee after every grid jump.
It is valid even for the $r=0$ bin: the remaining time need not decrease at
that discrete branch, because the grade decreases. Therefore

$$
‖\mathcal S_{k,u}-\mathcal E_u‖_\diamond\le4k\delta.
$$

This proof compares complete unconditional channels. It does not compare a
point-tagged grid clock to an ideal continuously measured clock, or allow an
external observer to resolve times inside a bin and condition additional
feedback upon them.

## Horizon rounding and implementation error

For a requested real $t\ge0$, choose the dyadic step and round upward to
$u=\delta\lceil t/\delta\rceil$. Then $0\le u-t<\delta$, and

$$
‖\mathcal S_{k,u}-\mathcal E_t‖_\diamond
\le(4k+2)\delta.
$$

Suppose each compiled, trace-preserving first-event map is within unhalved
diamond error $\zeta$ of its ideal polar grid instrument, uniformly and
coherently in the remaining-time register. A hybrid argument adds at most
$k\zeta$ to the complete-channel error:

$$
‖\widetilde{\mathcal S}_{k,u}-\mathcal E_t‖_\diamond
\le(4k+2)\delta+k\zeta.
$$

For example $\delta\le\varepsilon/[12(k+1)]$ and
$\zeta\le\varepsilon/(3\max\{k,1\})$ leave a strict margin below the
target $\varepsilon$. A sufficient initialized-workspace isometry error per
compiled event is $\zeta/2$. The entire failure space is retained in this
account; no failed filter branch is silently discarded.

The discretization needs $O(\log((t+1)(k+1)/\varepsilon))$ bits per time
record. Its grid may contain many points, but the compiler prepares their
uniform superposition and compares/subtracts binary times; it does not apply
a circuit once per grid point. The separate
[filter-cost proof](filters_and_resources.md) and
[dyadic compiler](dyadic_compiler.md) account for that circuit.
