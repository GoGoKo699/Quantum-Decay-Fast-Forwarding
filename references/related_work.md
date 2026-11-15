# Related work and the contribution retained here

The result concerns the **full reduced-system channel** of a purely dissipative, finitely graded decay process. Each supplied jump lowers the known grade, the rate operator preserves it, and at most $`k`$ events can occur. The input is a coherent normalized encoding of the stacked jump map, with controlled and inverse access. Under this promise the construction has query cost $`\widetilde O((k+1)\sqrt{1+t})`$; a one-event scalar-rate family requires $`\Omega(\sqrt t)`$ queries at fixed accuracy. The [model](../science/model.md), compiler and error analysis specify the charged normalization, precision and output conventions. The lower bound matches the time exponent for fixed positive $`k`$, rather than establishing optimal joint dependence on every parameter.

The advance is the global waiting-time compiler and its bounded-event continuation. Quantum trajectories, Gaussian Fourier identities, coherent Kraus stacks, Hamiltonian simulation and oblivious isometry amplification are established ingredients. Neither a new quantum-trajectory interpretation nor the first fast-forwardable Lindbladian is claimed.

## Comparison with primary simulation results

| Earlier result | Relevant supplied structure and conclusion | Consequential difference here |
|---|---|---|
| Chen, Gao, Wang and Zhou, [arXiv:2609.18757v2](https://arxiv.org/html/2609.18757v2), Theorem 1.2 | General Hamiltonian block encoding and stacked-jump projected unitary encoding; full-channel diamond simulation with optimal general linear-time query dependence | A known bound on the number of downward events permits square-root time dependence for nonuniform decay rates. This is an additional structural promise, not an improvement to their unrestricted theorem. |
| Borras and Marvian, [Quantum 10, 2063 (2026)](https://doi.org/10.22331/q-2026-04-13-2063), Sections 2–4 | Coherent trajectory algorithm with additive time/precision dependence when the total rate operator is proportional to the identity | The total rate here can have arbitrary spectrum, including zero and arbitrarily small positive eigenvalues. The compiler treats the resulting state-dependent waiting times. |
| Burdine, Bauer, Siopsis and Blair, [Advanced Quantum Technologies 8, 2400606 (2025)](https://doi.org/10.1002/qute.202400606), Sections 2.3–2.4 | Closed Kraus-series reductions for special commutation relations, including finite nilpotent-semigroup cases | Homogeneous lowering does not require their common scalar commutator or mutually commuting individual rate matrices. Unknown operators are used through their charged coherent encoding. |
| Shang et al., [arXiv:2510.06759v2](https://arxiv.org/html/2510.06759v2), Appendix I | Quadratic fast-forwarding for Hermitian jumps with commuting dissipator superoperators | Nonzero strictly lowering jumps are non-Hermitian, and their nonunital decay channel is outside that family. |
| Gao, Ji and Liu, [arXiv:2511.10253v2](https://arxiv.org/html/2511.10253v2), Sections III–IV and Appendix C | Hamiltonian-twirling families with optimal $`t^{1/\alpha}`$ simulation time, including Gaussian $`\sqrt t`$ scaling | Twirling averages unitary channels and is unital. Here the full target channel transfers population into lower grades. Gaussian transforms are used internally as operator filters, not as a twirling representation of the target channel. |
| Shang, An and Shao, [arXiv:2509.09517v2](https://arxiv.org/html/2509.09517v2) | Unitary-jump simulation with additive time/precision query cost; structured block-Pauli cases allow exponential fast-forwarding in circuit depth while retaining linear query work | Strictly lowering jumps are not unitary. The resource improved here is serial oracle queries, with gate and encoding costs stated separately. |

### Why the general transducer theorem does not already give the result

For the normalization $`\alpha_B=1`$ and zero Hamiltonian, the local catalyst in Chen et al., Eq. (44), satisfies

```math
\|\gamma\psi\|^2
=\frac\delta2\left(\|R_\delta\psi\|^2+
\|B R_\delta\psi\|^2\right),
\qquad R_\delta=(I+\delta B^\dagger B/4)^{-1}.
```

On a normalized dark state $`B\psi=0`$, this is $`\delta/2`$. Their global catalyst is the orthogonal sum over time steps, so its squared norm is $`t/2`$ on that state even though no event occurs. Thus their existing catalyst-norm bound does not become a bound in $`k`$ merely by restricting to a finite-event process. A new compiler is required; this observation does not rule out future improvements to their method.

### Why a nilpotent jump is not a new closed-form case by itself

Burdine et al. already analyze finite nilpotent jump structures. Their closed-form reduction assumes, among other conditions, a common scalar relation $`[A,J_a]=\lambda J_a`$, with $`A=\sum_a J_a^\dagger J_a`$, and commuting individual rate matrices. Grading alone does not imply these conditions. For example,

```math
J=a|0\rangle\langle1|+b|1\rangle\langle2|,
\qquad A=\mathrm{diag}(0,|a|^2,|b|^2),
```

has homogeneous lowering, but a common scalar commutator requires $`|b|^2=2|a|^2`$ when $`a,b\ne0`$. The present compiler includes generic unequal rates and multiple noncommuting lowering maps. It does not assume a classically known diagonalizing basis or identify separately postselected Kraus experiments with a reusable deterministic channel.

## No-fast-forwarding remains valid outside the promise

Childs and Li, [Quantum Information and Computation 17, 901–947 (2017)](https://doi.org/10.26421/QIC17.11-12-1), prove a sparse-Lindbladian no-fast-forwarding theorem. Their parity construction, [arXiv:1611.05543v3, Section 7, Eq. (259)](https://arxiv.org/pdf/1611.05543), uses

```math
L_s|n,j\rangle=|n-1,j\mathbin\oplus s_n\rangle,
\qquad L_s|0,j\rangle=0.
```

At time $`t=4N`$, the process can accumulate the parity of $`N`$ unknown bits while descending a chain of length $`N`$. Its event budget therefore grows as $`k=N=\Theta(t)`$. It does not contradict a sublinear-in-time result for fixed or few events. Conversely, the present result does not remove the cost of an arbitrary Hamiltonian: the zero-jump sector would otherwise include unrestricted Hamiltonian simulation. The assumption $`H=0`$ is substantive.

## Shared foundations and related scientific accounts

The [first-event compiler in Quantum Current without Equilibration](https://github.com/GoGoKo699/Quantum-Current-without-Equilibration/blob/98f5365e36a8b0fc9862222b2242f867ba1232ad/science/first_event_compiler.md) already gives the exact first-event normalization identity, a coherent finite Kraus stack, oblivious amplification and a reversible retained event record. Its short-interval implementation is stepped in elapsed time. Its [main task](https://github.com/GoGoKo699/Quantum-Current-without-Equilibration/blob/98f5365e36a8b0fc9862222b2242f867ba1232ad/science/comparison.md) is a source-weighted scalar current, rather than the full channel for arbitrary inputs. These compiler foundations are inherited here. The additional conclusion uses a global dyadic waiting-time stack and an event budget to avoid stepping through a time-length trajectory.

[Quantum Dephasing Threshold](https://github.com/GoGoKo699/Quantum-Dephasing-Threshold/blob/340b97e5e82cabcf79b25030ae2289fca485d039/science/model.md) concerns supplied reflection jumps at constant total rate. Its [pair algorithm](https://github.com/GoGoKo699/Quantum-Dephasing-Threshold/blob/340b97e5e82cabcf79b25030ae2289fca485d039/science/pair-simulation.md) reduces arbitrarily long reflection words to a random-walk endpoint; it gives square-root query cost without bounding the physical event count. The decay compiler instead preserves the action of nonunitary lowering maps and compresses the waiting-time implementation. The two structural promises and proofs do not imply one another.

[Quantum Environment Fast Forwarding](https://github.com/GoGoKo699/Quantum-Environment-Fast-Forwarding/blob/1051ad95048100f32b2bff85084b45a8a6480c3e/science/model.md) specifies a microscopic vacuum dilation, retains the field and discards the final system. Its [single-unitary-jump centering lemma](https://github.com/GoGoKo699/Quantum-Environment-Fast-Forwarding/blob/1051ad95048100f32b2bff85084b45a8a6480c3e/science/centered_environment.md) removes a common unitary acting only on the discarded system. That operation is unavailable for the present system-channel target. Our finite internal time records are retained during the circuit and finally traced out; no physical emitted-field approximation at arbitrary temporal resolution is asserted.

## Algorithmic ingredients and attribution

- The first-event integral and quantum-jump unravelling are standard open-system tools; see Breuer and Petruccione, *The Theory of Open Quantum Systems*, and Borras and Marvian, Section 2.2.
- Coherent implementation of a finite Kraus stack and oblivious amplification of an isometry are established primitives. Borras and Marvian, Section 2.1, Lemmas 1–2, explicitly attribute these tools to Li and Wang; see also [Gilyén et al., STOC 2019](https://doi.org/10.1145/3313276.3316366) for block encodings and robust oblivious singular-value amplification.
- The Gaussian Fourier identities follow from the Gaussian characteristic function and the spectral theorem. Their use with a Hermitian dilation yields the even Gaussian and odd derivative-Gaussian filters. Normalization, finite random bits and coherent coefficient preparation are charged in this project's compiler.
- Controlled Hamiltonian simulation of that dilation uses standard algorithms, such as [Low and Chuang, Quantum 3, 163 (2019)](https://doi.org/10.22331/q-2019-07-12-163). Its simulation time and control precision are included in the query and gate bounds.
- Classical polynomial completion and phase synthesis are also charged. At a fixed margin below one, [Berntson and Sünderhauf, Algorithm 1 and Theorem 3](https://doi.org/10.1007/s00220-025-05302-9), give FFT-based complementary-polynomial construction. [Ni, Sarkar, Ying and Lin, Algorithm 1 and Theorem 5.6](https://arxiv.org/html/2505.12615v1), give near-linear inverse nonlinear FFT synthesis under the stated outer-completion condition. These are inherited classical compilation tools.
- The scalar-rate converse uses the standard query-by-query hybrid argument. Its application here fixes an unknown block-encoded rate and a full-channel output gap; a classically supplied exact rate would be a different input model.

## Scope of the comparison

The comparisons use the linked source versions and selected model, theorem and proof sections inspected on 15 November 2026. They establish the stated model distinctions, not exhaustive priority or independent expert certification. No classical lower bound, hardware crossover or generic optimal joint law in time, event budget and precision follows from this comparison.
