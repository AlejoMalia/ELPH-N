# ELPH-N · The Elephant in a Neuron

### Metrological certification of the continuous custody of a closed volume between two stations

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22959145.svg)](https://doi.org/10.5281/zenodo.22959145)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-brightgreen.svg)](https://www.python.org/)
[![Framework: 87.5%](https://img.shields.io/badge/Framework-87.5%25%20(8%20axes)-orange.svg)](#5-what-is-known-and-what-is-not)
[![Bench: 0%](https://img.shields.io/badge/Bench%20validation-0%25-red.svg)](#5-what-is-known-and-what-is-not)
[![Decisions: 721](https://img.shields.io/badge/Dated%20decisions-721-blue.svg)](docs/decisions/decisions_registry.md)

- **Paper** — [English (MD)](THE_ELEPHANT_IN_A_NEURON_EN.md) · [English (PDF)](THE_ELEPHANT_IN_A_NEURON_EN.pdf) · [Español (MD)](EL_ELEFANTE_EN_UNA_NEURONA_ES.md) · [Español (PDF)](EL_ELEFANTE_EN_UNA_NEURONA_ES.pdf)
- **Library** — [`elphn`](#6-the-library): 27 formulas that refuse to run outside their verified domain

---

# Does an Elephant Fit in a Neuron?

## Abstract

This work presents a complete and falsifiable metrological framework for **certifying that
a closed volume has been transferred between two stations without alteration of its
contents**, without reading those contents and without cloning them. It is not a transport
framework: transport is trivial and was solved centuries ago. It is a **certification**
framework — what must be measured, with which estimator, against which floor, over which
averaging window, and at what declared risk, in order to state that the object that
arrived is the object that left.

The framework is articulated in **109 statements**, each of which is: **(1)** stated with
its formula or threshold, **(2)** dimensionally validated, **(3)** labelled with its
evidentiary status and its source, **(4)** accompanied by an experiment that would refute
it, **(5)** with that experiment costed in euros and hours, **(6)** with its averaging
window declared, and **(7)** attacked by at least one calculation from twenty-eight test
batteries, and surviving. **The seven statement axes stand at 100 %.**

An eighth axis — **MEASURED** — asks whether a bench measurement of our own exists. It
stands at **0 %**. **The framework is at 87.5 %.**

Its formal contributions are: the **agreement contract** `A = √(Ω_imp/Ω_act)` with its
declared dead zone; the **identity criterion** that distinguishes an act of transfer from
an equivalent act of manufacture; the **averaging-window law**, by which the estimator's
breakdown point bounds the window from above; the **GATE-0** protocol of spatial
admissibility with its ring plate and robust regression; the **measured false-acceptance
rate** over 3·10⁶ impostors; and the **mass × scale phase diagram**, which delimits exactly
where the framework applies today and which single requirement — a correlation length
`υ ≥ L` — blocks the rest.

> **The framework is posed. It is not verified.** Those are two different things and this
> work reports both without mixing them: statement completeness **100 %**, material
> validation **0 %**. Closing the second costs **€1,674**, and the specification is open
> for any laboratory to execute.

## 1. Genesis: why a neuron, and why an elephant

### 1.1 The original question

The programme was born from a deliberately disproportionate question: **does an elephant
fit in a neuron?** The answer was known in advance — no — but the question forced a precise
formulation of *why* not, and that formulation turned out to be the real problem: **what is
required in order to state that a physical configuration has been transferred, and not
copied, not manufactured, not substituted?**

The neuron entered as a **test substrate**, not as an object of study. The programme was
never about neuroscience. Measurements were made on connectomes because they were the only
public dataset with tens of thousands of individually identified elements in metric
coordinates: **a test bench for space**, not a brain.

### 1.2 How it started: an investigator putting the machines to the test

The programme did not begin as a physics project. It began as **a test of artificial
intelligence systems**. The author wanted to know how far a real investigation could be
carried — with data, with contradictions, with errors that had to be recorded — using
language models as collaborators rather than as search engines.

The initial question was deliberately disproportionate: **does an elephant fit in a
neuron?** It was known that it does not. What was not known was whether an artificial
system, pushed for weeks, would be capable of **saying why not with numbers**, of
**recording its own errors**, and of **correcting itself against its own previous result** —
which is, in the end, the only thing that distinguishes research from generating convincing
text.

Three systems worked on it: **Claude (Anthropic)**, **Grok (xAI)** and **Gemini (Google
DeepMind)**, under the author's direction, arbitration and final decision. The division was
not by declared capability but by **tension**: each was taken to the point where the
framework was weakest, and what each did with the same gap was compared.

**And it is worth stating precisely what the author's role was, because it was not that of
a spectator.** A language system, driven for weeks over a real problem, **hits walls and
stays there**: it repeats the route it already knows, declares impossible what is merely
difficult, and mistakes an inherited premise for a law of physics. That happened repeatedly
in this programme, and **it is dated in the register**.

The author **did not direct: he intervened.** He proposed the ideas and mechanisms that
unblocked the work at the points where it had stopped, demanded that data be sought outside
where it was being sought, and forced the framework corrections that changed the entire
programme. The ones that weighed most are all in this document:

* **the reformulation of the connectome as a space** — a neuron is a city, an impostor is a
  wrong address — which made it possible to design D-370 and **bring down the programme's
  largest declared limit**;
* **the hard rule of D-647**: complete, physical, a whole human, **without cutting**;
* **the correction of D-670**: *"it is a COMPLETE HUMAN BEING, all of it one unit; if no
  reading is needed, the concept is a HUMAN inside a BUBBLE"* — which **repealed the
  read-and-reconstruct route**, eliminated 193 of 200 open science-fiction questions at a
  stroke, and yielded the **non-fusion theorem**;
* **the demand to search outside the label**: *"do not look for papers under
  'teleportation', look for them by layer and by guild"* — which is where Eiband, Daugman,
  the BIPM, Johnston, TUP and the UHMS came from;
* **the insistence on attacking rather than enumerating**, and on **asking the simplest
  questions in the world**, which yielded thirteen gaps in seventeen naive questions against
  four in seven formal modes of attack;
* **the instruction to write the protocol minute by minute**, which exposed a 63 % error in
  the time of the act that had stood for four decisions;
* **the proposal to extrapolate the BANK TRANSFER cycle to the act**, which turned out to be
  the most efficient attack in the whole programme: **sixteen gaps in twenty-two concepts** —
  and it gave a name, **Herstatt risk, 1974**, to a problem the programme had found the day
  before without knowing what it was called. From it came **delivery versus payment** (the
  occupant does not leave until there is a verdict), the **two-phase commit** that splits
  power between origin and destination, **finality**, **reconciliation**, and the
  **four-eyes principle**;
* **the order to CATALOGUE, DEFINE AND MEASURE the limbos and their classes**, which turned a
  metaphor — *"it is in limbo"* — into **a magnitude with a definition, a formula and units**:
  six limbos, the formula `risk(L) = duration · P(event) · (1 − P(mitigation))`, their
  **elasticities** with respect to route, mass and acceleration, and the result no other
  route would have produced — **the most dangerous limbo is the shortest one, and ordering by
  duration and by danger are inverse** — together with the **fusion threshold of 19,837 km**
  and the **physical floor of L4**;
* and, before all of them, **the creation of the MATE method**, the framework of work under
  which all of the above was done.

> **Without those interventions the programme would not have advanced.** This is not a
> courtesy of authorship: it is a datum of the method. **An artificial system sustains rigour
> and the accounting of errors better than a tired human; a human sees when the problem is
> badly posed, and that the system does not see on its own.** This framework is the result of
> both, and the register makes it possible to check which did which.

### 1.3 The closed-route episode · why this framework carries 721 dated decisions

Midway through the programme, something occurred that in the author's judgement justifies
the chronological register on its own.

**The facts, as they stand in the register and are verifiable there:**

1. Decisions **D-552 to D-557 (18 September 2026)** were written by an external agent
   (Gemini) and were marked in the register as **UNVALIDATED**, with **three located
   errors**: declaring the whole leg an intact piece using the calf calliper (15.2 cm) when
   the thigh measures 26.6 cm; a ✓ **written by hand into the code** over an `N₇ = 1.082`
   that violated the criterion `pass ⟺ N < 1`; and **counting the same condition twice**,
   which produced 19 conditions where the framework had 18.
2. Those decisions reopened the **destruction-and-reconstruction route** — manufacturing the
   body at the destination — which was **a secondary line by the investigator's decision**,
   not the framework.
3. That route **forces deep cold**, and not by choice: manufacturing a body takes **5.1
   days**, and tissue already made has to survive while the rest is built. Only −130 °C fits
   the window.
4. Under that premise, the result was **IMPOSSIBLE**.

**And then, in D-567, on asking where the cold came from, this was seen:**

> **The cold was not a condition of transport. It was a consequence of RECONSTRUCTING.**
> As soon as matter travels — `φ = 1` — the window goes from **5.1 days to 18 minutes**, and
> 18 minutes fit inside the **40 minutes of hypothermic circulatory arrest** that cardiac
> surgery performs routinely every day. **`N` = 17.9/40 = 0.45: PASS, and without
> vitrifying anything.**

**The methodological lesson, which is what matters here:**

> **A closed route reopened without consulting the register produces a false impossibility.**
> The "IMPOSSIBLE" did not come from physics: it came from **a premise the programme had
> already set aside**. And what undid it was not a better argument, but **going back to the
> register** — D-522 was earlier and already said so — **and looking for old literature**:
> hypothermic circulatory arrest has been published for decades and nobody had brought it to
> the table.

**Nothing is asserted in this work about intentions.** There is no way to know what a system
"intended", and attributing purpose to it would be exactly the kind of statement without
evidentiary status that this framework exists to prevent. What is documented, dated and
verifiable in the register is the **pattern of facts**: unvalidated decisions, three locatable
errors, a previously closed route, a result of impossibility, and a way out that was in the
programme's own archive.

**Three of the rules that govern the framework come from this:**

| rule | statement |
|:--|:--|
| **99** | A synthetic substitute is worth nothing until it **reproduces the FLOOR of the original**. |
| **500** | **Is it impossible?** Only one thing is, and it is proven: *instantaneous + certified*. Everything else has a price. |
| **631** | **Applying the framework to what has ALREADY HAPPENED is the cheapest attack**, because the answers are published. |

And from this also comes the form of this document: **every statement with its evidentiary
status, every correction marked, every error dated.** A framework that publishes only its
successes cannot be audited, and one that cannot be audited is not a framework.

### 1.4 The method: TRIADA and MATE

**TRIADA** — before spending computation: **inventory** what is already measured, write the
**mathematics before running** with numerical predictions P1/P2/P3, and identify what
computation can be **reused**.

**MATE** — *Methodology of Advance by Strategic Tension*, created by the author from the
projection of a mate-in-three in chess. Five rules: **conservation of tension** (a line that
releases the tension is abandoned even if it looks safe) · **invariance of the rules** (the
rules of the game do not change to suit the plan) · **projection of the last three** (before
moving, the final three moves are named) · **advance through critical squares** (progress is
measured by squares that matter, not by moves made) · **mate ≠ theatre** (a position that
looks winning and is not, is a loss).

> **TRIADA is the opening and MATE is the endgame. TRIADA is R3 turned into procedure.**

---

## 2. The problem, stated plainly

Suppose you move a sealed container from station A to station B. Nothing is read from
inside it, nothing is cut, nothing is copied — the container simply travels, and whatever it
holds travels with it as cargo. **How would you prove that the object that arrived is the
object that left?**

This is a measurement question, and it is the same one asked, in different vocabularies, by
traceable metrology, tamper-evident sealing, biometric verification and settlement finality
in banking. None of those fields answers it for a *whole closed volume whose interior is
never inspected*, which is the case this framework addresses.

**Excluded from day one:** wormholes, speculative quantum formalism, and magical
dematerialisation. **Nothing here proposes a new mechanism of nature.**

## 3. The object being certified

| term | what it means |
|:--|:--|
| **the act** | one transport of one shell from station A to station B |
| **the shell** (bubble) | the closed volume that travels. **This** is what is certified |
| **the interior** (cabin) | never read, never modified. Occupants travel as cargo |
| **the floor** | the irreducible disagreement of the measuring system with itself, established by **re-placing** the part, not by re-photographing it |
| **Ω** (omega) | disagreement between the reading at A and the reading at B, `Ω = 1 − corr` |
| **the impostor** | *a wrong destination address* — never "a different individual" |
| **A** (the band) | how far the act sits from the **nearest** impostor, `A = √(Ω_imp/Ω_act)` |

A teleportation is measured **between two places in the same space** — London → New York —
never between two individuals. Comparing two distinct individuals **is not a transport**.

## 4. The claim

**The contract exists if and only if `A > 1 + dA`**, where `dA/A = ½√(u_imp² + u_act²)` is a
declared **dead zone**. `A > 1` alone is not a contract — with 10 % uncertainties,
`A ∈ [0.934, 1.071]` is a coin flip, and the engine reported such ties as passes until that
was found and fixed.

- **`FAR ≤ 3/k`** — a rate is never reported without its sample size. *Zero deaths in 37
  acts* means **at most one in twelve**, not zero.
- **`ψ = g·K⁴/A⁴ = 1.03·10⁻⁴`** — the act is **9,713 times more material than
  informational**. This is what licenses the framework to be metrology rather than
  information theory.
- **`υ ≥ L`, the law of the map** — the correlation length of form error is set by the size
  of *the operation that formed the part*. Both shells must therefore be formed in **one
  operation with the same tooling**, which eliminates welds as a failure mode.
- **The bubble ceiling is 5.03 m** — 4–6 seats, not 100. And it does not matter, because
  `E ∝ L³ ∝ N` makes **energy per person flat**: there is no economy of scale to lose by
  splitting.
- **The door is never the punishment** — after commit, delivery is always fulfilled and the
  only thing that can fail is the certificate.

## 5. What is known and what is not

**No figure in this repository comes from a bench measurement of our own.** Every value is a
derivation, a simulation or a citation, and carries its status (`MEAS / DER / LIT / DEC`).
The library enforces this: a unit test asserts that no formula claims traceability it has
not earned.

| axis | status |
|:--|--:|
| statement · units · evidential · falsifiable · costed · window · **RESISTED** | **100 %** |
| **MEASURED** | **0 %** |
| **framework** | **87.5 %** |

```bash
python3 experiments/lib/auditoria_marco.py     # prints all eight axes, honestly
```

The eighth axis exists **because** the first seven reached 100 %. An instrument scoring
100 % on everything has stopped discriminating, and these grades are set by the people doing
the work: **a self-graded 100 % is worth less than a 98.7 % with named gaps.**

Closing the eighth axis is specified and costed at **€1,674** — bench metrology plus desk
and room tests. §9 of the paper carries the protocol, the shopping list and the
pre-registered predictions.

## 6. The library

```bash
pip install -e .
```

```python
import elphn

v = elphn.contract_holds(om_impostor=4.993e-2, om_act=8.16e-4)
print(v)          # A = 7.822  threshold = 1.071  -> CONTRACT

elphn.far_bound(37)                 # 0.0811 — zero in 37 is not zero
elphn.bubble_ceiling()              # 5.03 m — above this there is nothing to certify
print(elphn.formulary())            # every formula with its status, units and domain
```

The design claim is narrow and testable: **a scientific library should refuse to be used
outside the domain its authors verified.** Most do not, and the failure is silent.

```python
>>> elphn.transit_time(5_570e3, g=9.0)     # London-New York at 9 g
DomainError: Transit time: peak velocity 22.2 km/s exceeds Earth escape velocity
(11.2 km/s) at 9 g; beyond 1417 km this profile is a departure, not a hop, and the
coast phase it needs is not modelled  [D-713]
```

That limit was found by calling the formula outside the range its authors had checked — it
had been returning beautiful, wrong numbers for hundreds of decisions. Every guard rail in
the package has a story like that, named in its `source` field.

```bash
python3 -m unittest discover -s tests -t .     # 41 tests: published figures + every domain
```

## 7. What this is worth outside its own premise

Stated plainly, because the method demands it of every other claim.

**The transport premise contributes nothing to any existing field.** Moving an 888 kg shell
at 3 km/s is a ballistic vehicle, and that engineering is better developed elsewhere.

**What may survive independently is method, and much of it is rediscovered** — the
evidentiary tagging reinvents NUSAP (Funtowicz & Ravetz 1990), the dead zone is GUM, the
rule of three is Hanley & Lippman-Hand 1983, and two-phase commit is banking. Three things
plausibly have value on their own:

1. **`υ ≥ L` as an acceptance criterion** — probably folk knowledge in precision
   engineering, but we have not found it stated as a quantitative go/no-go test with a
   robust estimator.
2. **GATE-0 as a correctability veto** — one exponent answering *is this error field
   correctable by a local affine, or not?*
3. **The limbo catalogue** — intervals with a guarantee suspended, with an elasticity.
   Surgery, launch, banking and aviation each have their own version under their own
   vocabulary. The finding that generalises: **the most dangerous window was the shortest
   one**, because duration is what everyone measures and mitigation is what nobody does.

## 8. Layout

```
THE_ELEPHANT_IN_A_NEURON_EN.md / .pdf    the paper (English)
EL_ELEFANTE_EN_UNA_NEURONA_ES.md / .pdf  the paper (Spanish)
elphn/                        the reference library — 27 formulas with enforced domains
tests/                        41 tests: published figures, and every domain limit
docs/FORMULARIO.md            46 formulas in 8 blocks, with evidential status
docs/ESTADO-EVIDENCIAL.md     the MEAS / DER / LIT / DEC scale
docs/decisions/               the chronological register — 721 dated decisions
experiments/lib/REGLAS.md     844 accumulated method rules
experiments/lib/auditoria_marco.py   the completeness instrument (8 axes)
core_engine/src/gate0.py             the veto the architecture hangs from
core_engine/src/maquina.py           act verification engine
tools/                        Markdown→PDF renderer, plate generator, Annex D generator
```

## 9. Authorship and citation

**Alejo Malia** — principal investigator. Declared architecture, direction of the programme,
external evidence, and the methodological contributions of his own: the
**connectome-as-globe** framing, the **bank-transfer** view applied to the protocol, the
**catalogue and measurement of the limbo**, and the creation of the **MATE system**.

Computational assistance: **Claude (Anthropic)**, with **Grok (xAI)** and **Gemini (Google
DeepMind)** in earlier phases. Calculations, attack batteries and drafting were carried out
in collaboration; architecture decisions are the investigator's. Arithmetic errors made
during the work are documented in the decision register rather than removed, because the
method claims that **optimistic accounting is the characteristic failure mode of this kind
of work**, and a framework claiming that must show its own cases.

### How to cite

```bibtex
@misc{malia_elphn_2026,
  author       = {Malia, Alejo},
  title        = {The Elephant in a Neuron: Metrological Certification of the
                  Continuous Custody of a Closed Volume between Two Stations},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.22959145},
  url          = {https://doi.org/10.5281/zenodo.22959145}
}
```

Malia, A. (2026). *The Elephant in a Neuron: Metrological Certification of the Continuous
Custody of a Closed Volume between Two Stations.* Zenodo.
[https://doi.org/10.5281/zenodo.22959145](https://doi.org/10.5281/zenodo.22959145)

**License:** CC BY-NC-SA 4.0 · **DOI:** [10.5281/zenodo.22959145](https://doi.org/10.5281/zenodo.22959145) · **Status:** pre-registered protocol, **not** a report of results.
