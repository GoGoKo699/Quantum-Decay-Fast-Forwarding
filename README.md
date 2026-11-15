# Quantum Decay Fast Forwarding

Can a quantum simulator skip long waits between only a few irreversible
decays? This project gives a full-channel simulation algorithm for purely
dissipative processes with a bounded downward excitation grading. It preserves
the coherence lost into the emission-time record, including unknown and
arbitrarily slow decay rates.

With controlled and inverse access to a normalized encoding of the stacked
jump operators, a process of normalized duration $`\tau`$ and decay depth
$`k`$ can be simulated to unhalved diamond error $`\varepsilon`$ using

```math
Q=O\!\left[(k+1)\sqrt{1+\tau}\,
\operatorname{polylog}\!\left(
\frac{(2+\tau)(k+1)}{\varepsilon}\right)\right]
```

oracle calls. A scalar one-event family requires $`\Omega(\sqrt\tau)`$
queries at fixed accuracy, so the horizon exponent is optimal for fixed
positive decay depth, up to logarithmic factors.

## Results and reading routes

| Result | Meaning | Scientific account |
|---|---|---|
| Complete-channel algorithm | Preserves arbitrary input and reference coherences; no successful-run postselection | [Simulation theorem](science/simulation_theorem.md) |
| Global waiting-time compiler | Dyadic time bands have logarithmic stack normalization | [Compiler](science/dyadic_compiler.md) |
| Uniform discretization | Error accumulates over decay depth rather than elapsed time | [Time-grid proof](science/time_discretization.md) |
| Charged filter circuits | Finite coefficient registers, reversible arithmetic and controlled simulation without QRAM | [Filters and resources](science/filters_and_resources.md) |
| Matching time exponent | Explicit close oracle completions force square-root horizon cost | [Lower bound](science/lower_bound.md) |
| Noncommuting examples | Tests unequal-rate coherence and why triangular jumps alone do not suffice | [Examples](science/examples.md) |

Start with the [scientific guide](science/README.md),
[model](science/model.md) and [physical interpretation](science/interpretation.md).
For attribution and the precise difference from previous simulation methods,
read [related work](references/related_work.md) and the
[bibliography](references/references.bib).

## Reproduce the finite checks

```bash
python -m pip install -r requirements.txt
python verification/verify.py --check
```

The [verification guide](verification/README.md) explains the deterministic
fixtures, independent comparisons, saved results and numerical tolerances.
These checks exercise small complete channels and expose specific failure
modes. They do not implement the full fault-tolerant filter/amplification
circuit or certify asymptotic results independently of the proofs.

## Scope and resources

There is no Hamiltonian term. Every jump strictly lowers a known grading,
and the total loss operator preserves that grading. Homogeneous excitation
loss is a sufficient subclass. Individual rate matrices need not commute;
no decay-rate floor or known rate eigenbasis is assumed.

For physical jumps encoded with normalization $`\beta`$, the normalized
horizon is $`\tau=\beta^2T`$. Construction, control and reversal of that
encoding, classical circuit compilation, finite-precision arithmetic, clocks
and retained workspace are charged separately in the resource theorem.
Input preparation and application-specific readout are additional costs.
The output contract is the reduced-system channel, rather than a continuously
resolved physical emitted field. No generic classical advantage or hardware
crossover is established.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
