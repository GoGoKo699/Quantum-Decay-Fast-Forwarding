# Reproduce the finite channel checks

From the repository root, run:

```bash
python -m pip install -r requirements.txt
python verification/verify.py --check
```

The recorded run used NumPy 2.3.5 and SciPy 1.17.0. The script checks mathematical invariants before comparing its numeric output with [expected_results.json](expected_results.json). It reports version information but permits small floating-point differences across installations: absolute tolerance $`5\times10^{-11}`$ and relative tolerance $`2\times10^{-7}`$ for the saved numeric results.

To inspect current numeric results without changing the saved reference:

```bash
python verification/verify.py --output /tmp/decay-check-results.json
```

## What the checks address

| Check | Independently constructed comparison | Failure it can expose |
|---|---|---|
| Scalar oracle | Explicit four-dimensional unitary completion, its controlled and inverse versions, analytic amplitude-damping output | An oracle-distance or normalization error in the square-root lower bound |
| Unequal-rate coherence | Full Lindblad matrix exponential against the analytic first-event integral | Incorrectly replacing the event-time instrument by one collapsed Kraus operator |
| Noncommuting grade-two cascade | Full generator exponential against the actual left-grid polar recursion | Wrong event ordering, loss of coherence, incorrect continuation horizon or lack of grid convergence |
| Small-grid recursion reconstruction | Direct corrected-Kraus enumeration against an eigenbasis convolution | An error in the efficient classical diagnostic itself |
| Event-stack normalization | Explicit finite Kraus sums against the isometry and near-isometry identities | Missing time-bin weights, a singular kernel treatment or incorrect polar normalization |
| Strict-lowering counterexample | Nilpotent triangular jump against interleaved waiting/jump products | Mistaking jump nilpotence alone for a finite physical event budget |

The cascade fixture is specified by rational matrices in the [examples](../science/examples.md). There is no random seed or external dataset. Its two individual rate matrices do not commute, its total rate commutes with the known grading, and every three-jump word vanishes. These are material properties of the claimed scope.

## The actual polar-grid diagnostic

For a grid horizon $`u=n\delta`$, the script builds the unnormalized first-event stack

```math
M_n=|\mathrm{no}\rangle e^{-n\delta A/2}
+\sqrt\delta\sum_{r=0}^{n-1}|\mathrm{yes},r\rangle L e^{-r\delta A/2},
\qquad R_n=(M_n^\dagger M_n)^{-1/2}.
```

Its Kraus operators are $`e^{-n\delta A/2}R_n`$ and $`\sqrt\delta J_a e^{-r\delta A/2}R_n`$. After an event at index $`r`$, it applies the remaining-depth channel for $`(n-r)\delta`$. In particular, a left-endpoint event with $`r=0`$ consumes event depth while retaining the same horizon. The recursion ends at depth two; its identity base case is physically needed only on grade zero after two events.

The code evaluates this finite channel directly as a matrix. Diagonalizing the six-dimensional $`A`$ accelerates **this classical diagnostic**; it is not a free operation assumed by the quantum algorithm. An exponential-kernel recurrence reduces the classical finite-grid computation to a linear number of small matrix products per event depth. A separately implemented direct enumeration agrees on the small test grid.

For every listed approximate channel, the script checks trace preservation and nonnegative normalized-Choi eigenvalues within floating-point tolerance. It records the unhalved trace norm of the normalized-Choi difference. For input dimension $`d=6`$, multiplying that quantity by six bounds the unhalved diamond distance. The code does not solve a diamond-norm semidefinite program.

## Additional discretization diagnostic

The separate `noncommuting_graded_cascade` result section tests the exactly trace-preserving microchannel

```math
K_0=e^{-\delta A/2},
\qquad
K_a=J_a\left[\frac{I-e^{-\delta A}}{A}\right]^{1/2}.
```

The quotient has value $`\delta`$ on the kernel. Powers of this microchannel allow at most one event per grid cell and round the continuation to the cell's right endpoint. This is a related discretization, rather than the polar-grid algorithm used in the proof. The result section `actual_polar_grid_cascade` is the diagnostic for that algorithm. Both are compared with the same independently exponentiated exact generator.

The event-stack checks likewise distinguish the exact microchannel correction from the algorithm's raw left-grid stack and polar correction. They verify $`I\le M_n^\dagger M_n\le(1+\delta)I`$, the polar isometry identity and the norm bounds of the dyadic envelope. The dyadic branch normalization includes both the time bins and the no-event branch.

## Limits of verification

These finite floating-point computations catch specific channel and implementation mistakes. They do not establish a universal or asymptotic theorem, interval-certified numerical bounds, a physical noise model, a compiled quantum circuit, or the gate complexity of Gaussian filters and oblivious amplification. The analytical proofs establish those statements at their stated scope. The code's dense matrix operations are deliberately confined to small fixtures and are not the proposed quantum simulation algorithm.
