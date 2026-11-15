# Scientific reading route

The question is whether a small number of irreversible quantum decays can be
simulated without stepping through a long waiting time. The answer depends on
preserving the information carried by emission times, rather than replacing
all events by one amplitude-damping operator.

Read [the model](model.md) and [the complete simulation theorem](simulation_theorem.md)
first. The proof then follows these topic pages:

1. [First-event instruments](first_event.md): exact trajectory representation,
   finite clock and polar normalization.
2. [Gaussian filters and resources](filters_and_resources.md): normalized
   Fourier LCUs, finite coefficient registers and charged arithmetic.
3. [Dyadic compiler](dyadic_compiler.md): one whole waiting interval, coherent
   remaining time and unconditional amplification.
4. [Time discretization](time_discretization.md): the full-channel error bound
   and bounded-depth continuation.
5. [Lower bound](lower_bound.md): explicit close oracle completions and the
   unavoidable square-root horizon exponent.
6. [Examples](examples.md): unequal-rate coherence, noncommuting decay and the
   limitation of triangularity alone.

The [interpretation](interpretation.md) connects the algorithmic statement to
the physical loss record. [Related work](../references/related_work.md)
separates the inherited primitives from the global compiler's contribution.
The [verification guide](../verification/README.md) states the finite checks
and their limits.
