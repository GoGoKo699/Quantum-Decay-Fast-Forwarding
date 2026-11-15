# Why a few decays can still require a quantum clock

An ordinary classical decay with a known rate is easy to sample: draw an
exponential waiting time and update the state. The input here is different.
The rate operator acts on an unknown quantum superposition and is supplied
through a coherent circuit. Learning its eigenvalue would disturb that
superposition. A correct simulation must instead leave the appropriate
information in its internal environmental record.

## One emitted event can carry which-rate information

Consider two excited states decaying into two dark destination states through
one jump,

```math
J=\sigma_1|g_1\rangle\langle e_1|
+\sigma_2|g_2\rangle\langle e_2|.
```

An initial superposition of excited states can transfer coherence into the
destinations. At long times, the multiplier on its off-diagonal element is

```math
\frac{2\sigma_1\sigma_2}{\sigma_1^2+\sigma_2^2}.
```

For rates with amplitudes $`\sigma_1=1`$ and $`\sigma_2=1/2`$, this is
$`4/5`$. The outgoing waiting-time wavepackets have different shapes and
overlap by that amount. A construction that forgets the time record before
forming the channel would incorrectly retain all the coherence. The
[example calculation](examples.md) gives the finite-horizon formula.

The simulator retains a finite approximation to this record. It may discard
the record only after its effect on the system has been preserved. This is
why a population-only simulation or a fast no-jump filter does not establish
the full-channel theorem.

## The dyadic mechanism

The amplitude for a first event at time $`s`$ is
$`L e^{-sA/2}`$. Its operator norm can remain appreciable far out in time
when some rates are very small, so a rate floor cannot simply truncate the
clock at a fixed physical scale.

On a band $`[a,2a)`$, however, the envelope
$`\sqrt a\,L e^{-sA/2}`$ is bounded by a constant. A uniform clock within
each band then contributes exactly the required square-root time-bin weight.
There are only logarithmically many bands up to the requested horizon.
Gaussian Fourier filters implement each band using square-root Hamiltonian
simulation time. Amplifying the complete nearly isometric event stack adds
only logarithmic factors. The
[compiler proof](dyadic_compiler.md) accounts for each of these statements.

The grading makes the recursive use of this clock finite: every genuine
event reduces a bounded resource, while waiting does not replenish it.
The error therefore accumulates over the number of events, rather than
over the number of small physical time steps.

## Meaning of the improvement

The [theorem](simulation_theorem.md) applies to full nonunital channels with
unknown nonuniform rates and noncommuting lowering maps. It requires zero
Hamiltonian and a grade-preserving total loss operator. It is not a generic
fast-forwarding theorem for all open quantum systems.

The square-root lower bound comes from an unknown weak damping amplitude.
It explains why even a single possible event cannot generally be simulated
with only logarithmic horizon dependence under this oracle access. It does
not turn known-rate classical sampling into a hard problem.

Finally, a complete application pays for constructing and controlling the
jump encoding, preparing the input and extracting the desired answer. The
query improvement is an algorithmic capability; it does not by itself
demonstrate an end-to-end classical advantage or a device-level speedup.
