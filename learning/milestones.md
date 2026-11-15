# Thirty milestones from quantum channels to decay fast-forwarding

This common map has **12 background milestones and 18 narrative milestones**. The background moves from an individual quantum alternative to the complete channel, oracle and error contract. The narrative then assembles one coherent waiting period, its finite compiler, bounded-event continuation and the resulting scientific consequence. The allocation reflects the project's connection between open-system dynamics and coherent quantum algorithms.

The map records understanding targets and their dependencies. It does not claim to cover every technical lemma, and it contains no learner assessment or session rules. The [Watrous bridge](watrous_bridge.md) supplies the route into the project; the [scientific account](../science/README.md) owns the statements and proofs.

## The single educational anchor

**John Watrous, *The Theory of Quantum Information* (2018)** is the selected anchor. The section labels below refer to the [author's book materials](https://cs.uwaterloo.ca/~watrous/TQI/), rather than to a second textbook or an additional course.

| Short pointer | Verified section and its role here |
|---|---|
| W1.1.3 | Operator decompositions and norms: adjoints, singular values and operator size |
| W2.1.2 | Quantum states of registers: state representations |
| W2.1.3 | Reductions and purifications of quantum states: joint systems and discarded records |
| W2.2.1 | Definitions and basic notions concerning channels: the physical output map |
| W2.2.2 | Representations and characterizations of channels: Kraus and isometric representations |
| W2.3.1 | Two equivalent definitions of measurements: outcome records and probabilities |
| W2.3.2 | Basic notions concerning measurements: nondestructive measurements and instruments |
| W3.1.1 | Discriminating between pairs of quantum states: operational state distinguishability |
| W3.3.1 | Channel discrimination: reference-assisted tests of a channel |
| W3.3.2 | The completely bounded trace norm: the norm called the diamond norm here |
| W3.3.3 | Distances between channels: comparing physical channel implementations |

These sections supply channel foundations. Lindblad semigroups, projected unitary encodings, Gaussian Fourier filters, coherent arithmetic and amplification are supplied or attributed in the linked project sources. A Watrous pointer does not claim that the book contains the fast-forwarding algorithm or its research-level proof dependencies.

## Background and preliminaries — M01–M12

### M01. Quantum alternatives and a decay amplitude

- **Central question:** What distinguishes a quantum superposition of decay alternatives from a classical list of possible starting states?
- **Understanding target:** Explain a basis state, a superposition, an amplitude and a linear operator; distinguish amplitude from probability without assuming that the alternatives have been measured.
- **Dependencies and story role:** Entry point. Starts with one system before introducing its environment or an algorithm.
- **Conceptual connection:** The unequal-rate example later depends on coherence between two excited levels, rather than only their separate decay probabilities.
- **Source pointers:** W2.1.2; [physical interpretation](../science/interpretation.md#one-emitted-event-can-carry-which-rate-information); [unequal lifetimes](../science/examples.md#two-excited-levels-with-unequal-lifetimes).

### M02. The positive operator that sets the waiting rates

- **Central question:** What does the operator $`A=L^\dagger L`$ say about decay and about states that do not decay?
- **Understanding target:** Interpret an adjoint, a positive operator, a singular value, the operator norm and a kernel; explain how functional calculus defines $`e^{-uA/2}`$, including at a zero eigenvalue.
- **Dependencies and story role:** Uses M01. Connects a local jump amplitude to its positive rate operator.
- **Conceptual connection:** The waiting-time circuit must handle a spectrum of rates, including arbitrarily small rates and dark states, without receiving their eigenbasis.
- **Source pointers:** W1.1.3; [supplied jump map](../science/first_event.md#the-supplied-jump-map); [model](../science/model.md#1-purely-dissipative-dynamics).

### M03. A system together with its unobserved record

- **Central question:** How can discarding an environment change the coherence of a quantum system?
- **Understanding target:** Explain a density operator, a composite state, entanglement, a partial trace and purification; distinguish a classical outcome record from the full joint quantum state.
- **Dependencies and story role:** Uses M01–M02. Expands the picture from one system to system plus environment.
- **Conceptual connection:** Different waiting-time wavepackets can reveal which-rate information even when the final system populations agree.
- **Source pointers:** W2.1.2–W2.1.3; [channel and record bridge](watrous_bridge.md#the-channel-and-its-record); [interpretation](../science/interpretation.md).

### M04. One channel, several representations

- **Central question:** Why can Kraus operators and a larger isometry describe the same physical channel?
- **Understanding target:** Recognize complete positivity and trace preservation, the Kraus completeness identity and an isometric channel dilation; explain why different environmental representations need not change the reduced channel.
- **Dependencies and story role:** Uses M02–M03. Establishes the representation used by the construction.
- **Conceptual connection:** The compiler builds a coherent stack of event operators and discards the record only after obtaining the desired system channel.
- **Source pointers:** W2.2.1–W2.2.2; [first-event normalization](../science/first_event.md#exact-coherent-waiting); [bridge](watrous_bridge.md#the-channel-and-its-record).

### M05. Outcomes, instruments and retained branches

- **Central question:** How does a channel differ from one selected outcome of that channel?
- **Understanding target:** Explain an outcome-indexed completely positive instrument, its probabilities and the trace-preserving sum; distinguish keeping a failure record from conditioning on success.
- **Dependencies and story role:** Uses M03–M04. Adds the operational meaning of no-event, event and numerical-failure labels.
- **Conceptual connection:** The algorithm's finite circuit retains all branches. A successfully accepted block alone is not yet the unconditional simulator.
- **Source pointers:** W2.3.1–W2.3.2 and W2.2.2; [accuracy contract](../science/model.md#3-accuracy-and-quantifiers); [amplification with failures retained](../science/dyadic_compiler.md#deterministic-amplification-with-failures-retained).

### M06. Error that survives an entangled reference

- **Central question:** Why is agreement on a few input states insufficient to establish a full-channel simulation?
- **Understanding target:** Relate trace distance to state discrimination and the diamond norm to channel discrimination; distinguish unhalved diamond error from half trace distance and explain reference-uniform accuracy.
- **Dependencies and story role:** Uses M03–M05. Defines what it means for the entire simulator to be accurate.
- **Conceptual connection:** The output must remain correct for arbitrary inputs entangled with an untouched reference, including coherences between grades.
- **Source pointers:** W3.1.1 and W3.3.1–W3.3.3; [accuracy and quantifiers](../science/model.md#3-accuracy-and-quantifiers); [error-contract bridge](watrous_bridge.md#why-the-error-contract-includes-a-reference).

### M07. A continuous family of physical channels

- **Central question:** How do jump operators and the no-event term combine into continuous-time evolution?
- **Understanding target:** Read the purely dissipative Lindblad generator and its semigroup; interpret the anticommutator's role in preserving trace and explain the channel continuity bound from $`‖\mathcal L‖_\diamond\le2`$.
- **Dependencies and story role:** Uses M02, M04 and M06. Joins local event rules into a complete evolution over time.
- **Conceptual connection:** Rounding a continuation horizon becomes a controlled channel error instead of an unspecified time approximation.
- **Source pointers:** W2.2.1 and W3.3.2–W3.3.3 for channel foundations; [generator and norm](../science/first_event.md#the-supplied-jump-map); [future-time continuity](../science/time_discretization.md#future-time-and-the-full-channel-recurrence).

### M08. A finite event budget with unbounded waiting

- **Central question:** Which structural conditions ensure that waiting cannot replenish the resource consumed by a jump?
- **Understanding target:** Explain the known grading, strict lowering and $`[A,G]=0`$; distinguish the two required promises from the sufficient homogeneous-loss subclass and from nilpotence alone.
- **Dependencies and story role:** Uses M02 and M07. Identifies the physical structure that the algorithm can exploit.
- **Conceptual connection:** The number of events is bounded by $`k`$ while the requested horizon and the longest lifetime may be arbitrarily large.
- **Source pointers:** W1.1.3 for block decompositions; [structural promises](../science/model.md#1-purely-dissipative-dynamics); [strict-lowering counterexample](../science/examples.md#strictly-lowering-jumps-can-still-have-arbitrarily-long-event-records).

### M09. The input is a coherent operation

- **Central question:** What information and operations does a normalized projected unitary encoding supply?
- **Understanding target:** Distinguish the rectangular jump stack from its unitary completion, an accepted block from a deterministic operation, and supplied controlled/inverse access from forward access alone; identify the common normalization as a bound.
- **Dependencies and story role:** Uses M02, M04 and M05. Establishes the algorithmic input without granting a classical matrix description.
- **Conceptual connection:** The compiler operates on unknown jump amplitudes through paid coherent calls and does not obtain exact decay rates or an eigenbasis for free.
- **Source pointers:** W1.1.3 and W2.2.2 for operator and dilation foundations; [coherent input access](../science/model.md#2-coherent-input-access); [oracle convention](../science/filters_and_resources.md#oracle-convention-and-hermitian-dilation).

### M10. Coherent sums and a Hermitian dilation

- **Central question:** How can a non-Hermitian jump map become accessible to Hamiltonian-based filters?
- **Understanding target:** Explain the off-diagonal Hermitian dilation, input/output orientation and a linear combination of unitaries prepared and unprepared coherently; distinguish this accepted operator block from a classical random mixture of channels.
- **Dependencies and story role:** Uses M03–M05 and M09. Connects the channel description to standard quantum-algorithm primitives.
- **Conceptual connection:** Even Gaussian filters act on the input space, while odd filters produce the required input-to-jump-output block.
- **Source pointers:** W1.1.3 and W2.2.2; [Hermitian dilation](../science/filters_and_resources.md#oracle-convention-and-hermitian-dilation); [Fourier identities](../science/filters_and_resources.md#exact-fourier-identities-and-normalization).

### M11. Normalization and composable implementation error

- **Central question:** When can a normalized accepted block be turned into a coherent isometry rather than a postselected output?
- **Understanding target:** Explain the purpose of a common block normalization and near-uniform singular values; distinguish accepted-block error from complete initialized-workspace isometry error and describe why retained leakage matters during controlled composition.
- **Dependencies and story role:** Uses M04–M06 and M09–M10. Completes the implementation foundations before the project-specific construction.
- **Conceptual connection:** The whole first-event stack will be amplified, and its complete error must remain small when controlled by a time register and used in later slots.
- **Source pointers:** W1.1.3 and W3.3.2–W3.3.3 for norms and composition; [deterministic amplification](../science/dyadic_compiler.md#deterministic-amplification-with-failures-retained); [filter lemma and leakage](../science/filters_and_resources.md#filter-lemma-used-by-the-channel-compiler).

### M12. The complete problem and its resources

- **Central question:** What must a successful fast-forwarding theorem provide under the actual input and output contracts?
- **Understanding target:** Assemble the physical promise, supplied oracle, reference-uniform error, quantum output and charged queries/gates/workspace into one task; distinguish that task from population sampling, physical field simulation and a complete application advantage.
- **Dependencies and story role:** Integrates M01–M11. Ends the background with the full framework needed to understand the contribution.
- **Conceptual connection:** A few jumps become useful only if their unknown waiting times can be simulated coherently at a cost below stepping through elapsed time.
- **Source pointers:** W2.2.1–W2.2.2 and W3.3.1–W3.3.3; [model](../science/model.md); [theorem](../science/simulation_theorem.md#theorem); [bridge route](watrous_bridge.md#one-route-through-the-project).

## Narrative and innovation — M13–M30

### M13. Unequal lifetimes leave a visible coherence signature

- **Central question:** Why does replacing the entire jump instrument by one collapsed Kraus operator give the wrong channel?
- **Understanding target:** Explain the unequal-rate coherence integral and its late-time factor; identify the system information carried by the event-time record even when decay probabilities are reproduced.
- **Dependencies and story role:** Uses M02–M05, M07 and M12. Starts the narrative with one concrete obstruction that the compiler must overcome.
- **Conceptual connection:** Retaining the correct waiting-time overlap is necessary for a full quantum channel, rather than an optional refinement of a population algorithm.
- **Source pointers:** W2.1.3 and W2.2.2; [unequal-rate calculation](../science/examples.md#two-excited-levels-with-unequal-lifetimes); [bridge example](watrous_bridge.md#unequal-rates-make-the-record-visible).

### M14. One exact coherent waiting period

- **Central question:** How do no-event survival and all possible first events form one isometry?
- **Understanding target:** Explain the stack with survival $`e^{-uA/2}`$ and event amplitude $`L e^{-sA/2}`$; use its completeness identity without assuming an inverse of $`A`$ or a minimum positive rate.
- **Dependencies and story role:** Uses M02–M05, M07 and M13. Builds the exact local object to be compiled.
- **Conceptual connection:** The continuous event record preserves unequal-rate coherence while normalizing all branches together.
- **Source pointers:** W2.2.2; [exact coherent waiting](../science/first_event.md#exact-coherent-waiting); [finite-clock bridge](watrous_bridge.md#from-a-first-event-isometry-to-a-finite-clock).

### M15. A finite clock whose error does not grow with the horizon

- **Central question:** How can a finite time register approximate a continuous first-event record uniformly over a long waiting interval?
- **Understanding target:** Explain normalized time-bin wavepackets, the left-endpoint stack and the integrated derivative bound; distinguish an operator-norm approximation of dilations from total-variation proximity to point masses.
- **Dependencies and story role:** Uses M02, M06–M07 and M14. Converts the exact waiting object into a finite representation.
- **Conceptual connection:** Integrated decay of the derivative bounds discretization error by the mesh rather than by the number of elapsed-time cells.
- **Source pointers:** W1.1.3, W2.1.3 and W3.3.2; [finite-clock lemma](../science/first_event.md#a-finite-clock-with-a-uniform-error); [wavepacket comparison](../science/time_discretization.md#uniform-wavepacket-comparison).

### M16. Polar correction without a small-rate inverse

- **Central question:** How is the finite waiting-time stack normalized without dividing by a possibly tiny decay eigenvalue?
- **Understanding target:** Explain the Gram interval $`I\le M^\dagger M\le(1+\delta)I`$, its inverse-square-root polar correction and the resulting exact isometry; identify why this inverse is well-conditioned even on dark states.
- **Dependencies and story role:** Uses M02, M04, M11 and M15. Resolves the finite stack's normalization defect before implementation.
- **Conceptual connection:** The correction is a function of $`A`$, so it preserves the grading and leaves every event block strictly lowering.
- **Source pointers:** W1.1.3 and W2.2.2; [normalizing the stack](../science/first_event.md#normalizing-the-stack); [exact norm and polar correction](../science/time_discretization.md#grid-stack-exact-norm-and-polar-correction).

### M17. The remaining horizon is a quantum control register

- **Central question:** Why must the first-event circuit work uniformly for a superposition of remaining times?
- **Understanding target:** Explain the common padded clock and the controlled direct sum over horizons; distinguish a uniform operator bound from a separate bound that accumulates over every possible clock value.
- **Dependencies and story role:** Uses M03, M06, M09 and M14–M16. Connects one local waiting instrument to its future coherent use.
- **Conceptual connection:** Retaining earlier event labels and subtracting their times reversibly enables continuation without measuring the input spectrum or erasing a physical history.
- **Source pointers:** W2.1.3 and W3.3.2–W3.3.3; [coherent remaining horizon](../science/first_event.md#a-coherent-remaining-horizon); [coherent compiler parameters](../science/dyadic_compiler.md#coherent-parameters-do-not-enumerate-time-points).

### M18. A constant envelope on each dyadic time band

- **Central question:** What makes a long late-time interval cheap enough to enter one coherent stack?
- **Understanding target:** Explain why $`\sqrt a\,L e^{-sA/2}`$ is a contraction for $`s\in[a,2a)`$, with a separate initial band; relate its factorization to odd and even filters.
- **Dependencies and story role:** Uses M02, M10 and M14–M17. Introduces the local normalization mechanism behind the time improvement.
- **Conceptual connection:** Small rates can retain amplitude late in time, but their correspondingly small jump amplitudes keep the scaled dyadic envelope bounded.
- **Source pointers:** W1.1.3; [normalized compiler filters](../science/dyadic_compiler.md#the-normalized-filters-used-by-the-compiler); [dyadic interpretation](../science/interpretation.md#the-dyadic-mechanism).

### M19. The whole clock has only logarithmic normalization

- **Central question:** How do band choice, uniform time choice and the dyadic envelope produce the right event amplitudes?
- **Understanding target:** Track the square-root mesh weight, no-event branch and common stack normalization; explain why the number of bands, rather than the largest band length, controls that normalization.
- **Dependencies and story role:** Uses M04–M05, M11 and M17–M18. Assembles the separate bands into one global accepted block.
- **Conceptual connection:** A large number of possible time labels is encoded in a binary register without a linear normalization penalty in the horizon.
- **Source pointers:** W2.2.2; [dyadic bins and outer stack](../science/dyadic_compiler.md#dyadic-bins-and-the-outer-stack); [stack diagnostics](../verification/README.md#additional-discretization-diagnostic).

### M20. Even and odd Gaussian Fourier filters

- **Central question:** Why do the Gaussian and derivative-Gaussian identities preserve useful normalization as their time scale grows?
- **Understanding target:** Explain the coherent Fourier representations of $`e^{-aH^2/2}`$ and $`\sqrt a H e^{-aH^2/2}`$; distinguish probability normalization one from the odd signed measure's constant normalization and from a classical channel mixture.
- **Dependencies and story role:** Uses M02, M10 and M18–M19. Supplies the actual filters required by the dyadic envelope.
- **Conceptual connection:** The Fourier coefficients do not introduce a factor proportional to $`\sqrt a`$, and normalization losses are not multiplied across binary residual filters.
- **Source pointers:** W1.1.3 and W2.2.2 for spectral and dilation foundations; [exact Fourier identities](../science/filters_and_resources.md#exact-fourier-identities-and-normalization); [compiler bridge](watrous_bridge.md#the-dyadic-compiler-and-its-paid-access).

### M21. Finite coefficients without a loaded table

- **Central question:** How are continuous Gaussian coefficients represented by finite quantum registers without a state-preparation oracle?
- **Understanding target:** Explain uniform finite indices, midpoint quantization, Gaussian/Rayleigh sample formulas and a coupling-based operator error; separate the number of possible index values from the register width and circuit work.
- **Dependencies and story role:** Uses M06, M09–M10 and M20. Replaces an ideal continuous coefficient source by a specified finite construction.
- **Conceptual connection:** Coherent arithmetic computes the needed coefficients and signed times from indices, preserving the claimed absence of QRAM in the waiting-time compiler.
- **Source pointers:** W1.1.3 and W2.1.2 for norm and register foundations; [finite coefficient register](../science/filters_and_resources.md#a-finite-uniform-coefficient-register); [reversible arithmetic](../science/filters_and_resources.md#reversible-arithmetic-rather-than-a-state-preparation-oracle).

### M22. Coherent SELECT, returned arithmetic and compiled controls

- **Central question:** What does it cost to apply the different signed evolution times selected by those finite indices?
- **Understanding target:** Explain binary-controlled fixed-time simulation, the geometric sum of time powers, computation and uncomputation of arithmetic, and finite gate/phase compilation; include complete workspace errors rather than only an accepted matrix block.
- **Dependencies and story role:** Uses M09–M11 and M20–M21. Turns formal filters into charged quantum circuits.
- **Conceptual connection:** The square-root filter query scale survives finite coefficient arithmetic and classical compilation, while the encoding's physical implementation cost remains charged.
- **Source pointers:** W1.1.3 and W3.3.2–W3.3.3 for norm composition; [variable-time SELECT](../science/filters_and_resources.md#coherent-variable-time-select); [classical compilation and gates](../science/filters_and_resources.md#classical-compilation-and-other-gates-are-charged).

### M23. Amplify the complete instrument and retain the failures

- **Central question:** Why is amplification applied to the whole near-isometric event stack instead of to its individual outcomes?
- **Understanding target:** Explain the common singular-value interval and polar target; distinguish deterministic isometry amplification with retained leakage from input-dependent postselection and from multiplying per-filter success probabilities.
- **Dependencies and story role:** Uses M05–M06, M11, M16–M17 and M19–M22. Completes one uniformly compiled first-event slot.
- **Conceptual connection:** Uniform amplification preserves a coherent remaining-horizon register and bounds numerical failure in the unconditional channel contract.
- **Source pointers:** W1.1.3, W2.2.2 and W3.3.3; [deterministic amplification](../science/dyadic_compiler.md#deterministic-amplification-with-failures-retained); [first-event compilation theorem](../science/dyadic_compiler.md#first-event-compilation-theorem).

### M24. Continue by event depth rather than elapsed-time steps

- **Central question:** How does the grade promise turn a compiled waiting instrument into a finite complete simulation?
- **Understanding target:** Explain no-event termination, retained event histories, reversible remaining-time updates and the fixed event-depth recursion; show why a zero-index grid event cannot create an infinite loop and why grade zero permits an identity base case.
- **Dependencies and story role:** Uses M07–M08, M14–M17 and M23. Joins local waiting slots into the global decay trajectory.
- **Conceptual connection:** Genuine events lower the grading, while the no-event operator and its polar correction preserve it; coherent superpositions of initial grades are retained.
- **Source pointers:** W2.2.2 and W3.3.3; [full-channel recurrence](../science/time_discretization.md#future-time-and-the-full-channel-recurrence); [theorem assembly](../science/simulation_theorem.md#proof-and-explicit-accuracy-allocation).

### M25. One complete reference-uniform error budget

- **Central question:** Why does the final accuracy budget depend on event depth rather than on the number of time cells or histories?
- **Understanding target:** Combine wavepacket approximation, polar correction, physical continuation-time rounding, horizon rounding and slot implementation errors; distinguish history-sector channel analysis from an unjustified claim about arbitrary controlled environmental dilations.
- **Dependencies and story role:** Uses M06–M07, M15–M17 and M23–M24. Integrates the local approximation bounds into the channel theorem.
- **Conceptual connection:** Previous records are retained and never recombined, so continuation can be analyzed by conditional history sectors without multiplying the bound by their number.
- **Source pointers:** W3.3.2–W3.3.3; [future-time analysis](../science/time_discretization.md#future-time-and-the-full-channel-recurrence); [rounding and implementation](../science/time_discretization.md#horizon-rounding-and-implementation-error); [explicit budget](../science/simulation_theorem.md#proof-and-explicit-accuracy-allocation).

### M26. The complete resource statement

- **Central question:** What exactly improves, and which costs must still be paid, when the event-depth construction fast-forwards the channel?
- **Understanding target:** Interpret the $`\widetilde O((k+1)\sqrt{1+\tau})`$ oracle bound, physical normalization $`\tau=\beta^2T`$, gate and workspace estimates, and classical compilation; identify input preparation, encoding construction/calibration and application readout as additional costs, and recognize that growing event depth can remove the improvement over linear-time simulation.
- **Dependencies and story role:** Uses M09, M12 and M18–M25. Turns the assembled mechanism into its complete algorithmic claim.
- **Conceptual connection:** A long classical time label need not create linear oracle work, but neither query counting nor a compact clock makes the supplied encoding free.
- **Source pointers:** W1.1.3 and W3.3.3 for norm scaling and approximation foundations; [simulation theorem](../science/simulation_theorem.md#theorem); [resource account](../science/filters_and_resources.md#classical-compilation-and-other-gates-are-charged); [paid-access bridge](watrous_bridge.md#the-dyadic-compiler-and-its-paid-access).

### M27. A noncommuting cascade and the reach of finite verification

- **Central question:** What does the six-dimensional example demonstrate that a scalar decay calculation cannot?
- **Understanding target:** Explain its noncommuting individual rate matrices, grade-preserving total rate and two-event cap; interpret CP/TP checks, normalized-Choi differences, direct-recursion agreement and convergence without mistaking them for the asymptotic circuit theorem.
- **Dependencies and story role:** Uses M02, M04, M06, M08 and M24–M26. Connects the general construction back to a small complete channel.
- **Conceptual connection:** The promises allow noncommuting structure within a grade, while the finite calculations expose concrete channel errors that population checks would miss.
- **Source pointers:** W2.2.2 and W3.3.2–W3.3.3; [noncommuting example](../science/examples.md#a-two-event-cascade-with-noncommuting-individual-rates); [verification scope](../verification/README.md#limits-of-verification).

### M28. Why one unknown decay still costs square-root time

- **Central question:** Why can even a single possible event require more than logarithmic query cost at long horizons?
- **Understanding target:** Explain the explicit close block-oracle unitary completions, their controlled/inverse distances and the constant amplitude-damping output gap; apply the hybrid argument while retaining common classical metadata and an unknown exact rate.
- **Dependencies and story role:** Uses M01–M02, M06, M09 and M26. Supplies the converse that identifies the unavoidable horizon exponent.
- **Conceptual connection:** The hard family has rates that shrink with the requested horizon. It is a worst-case coherent-oracle obstruction, not a claim that a classically supplied known scalar rate is hard to simulate.
- **Source pointers:** W3.1.1 and W3.3.1–W3.3.3; [explicit oracle completions](../science/lower_bound.md#explicit-close-unitary-completions); [hybrid and error convention](../science/lower_bound.md#hybrid-argument-and-accuracy-convention).

### M29. The consequential addition after prior work is credited

- **Central question:** Which part of the full result remains new once trajectory methods, coherent stacks, filtering and earlier fast-forwarding results are acknowledged?
- **Understanding target:** Explain the global dyadic waiting-time compiler and bounded-event continuation; distinguish its nonunital channel family and access assumptions from Hermitian/unitary-jump twirls, commuting-rate reductions, field-only output tasks and general linear-time simulators.
- **Dependencies and story role:** Uses M12–M14 and M18–M28. Places the completed construction in its actual scientific neighborhood.
- **Conceptual connection:** A shared ingredient or a finite nilpotent jump is not the contribution by itself; the added capability concerns complete unknown-rate decay channels under the precise promises.
- **Source pointers:** W2.2.1–W2.2.2 for the shared channel language; [related work](../references/related_work.md); [meaning of the improvement](../science/interpretation.md#meaning-of-the-improvement).

### M30. The full story and its limits

- **Central question:** How do a bounded number of irreversible events, a coherent clock and an oracle-rate obstruction fit into one scientific account?
- **Understanding target:** Explain the input-to-output route, the preservation of waiting-time information, the event-depth error/resource accumulation and the matching time exponent at fixed positive depth and fixed nonzero accuracy, up to logarithms; retain zero Hamiltonian, grade-preserving loss, paid controlled/inverse access, reduced-system output and the absence of joint parameter optimality or a demonstrated classical or hardware advantage.
- **Dependencies and story role:** Integrates M13–M29 with the background synthesis M12. Ends the narrative with the complete contribution rather than a new prerequisite or extra result.
- **Conceptual connection:** Few physical decay events do not eliminate quantum waiting-time information. The compiler preserves that information at square-root horizon cost, and the scalar oracle family explains why that exponent cannot generally be removed.
- **Source pointers:** W2.1.3, W2.2.2 and W3.3.1–W3.3.3; [complete theorem](../science/simulation_theorem.md); [matched and unmatched parameters](../science/lower_bound.md#what-is-and-is-not-matched); [interpretation](../science/interpretation.md); [bridge synthesis](watrous_bridge.md#from-one-waiting-period-to-the-complete-theorem).
