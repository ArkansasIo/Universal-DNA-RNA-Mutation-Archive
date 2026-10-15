# Logic Statements, True/False Claims, and Evidence Status

## A. Claim classifications
- **True under assumptions:** follows from stated premises or a defined model.
- **Empirically supported:** observations support the claim within the studied system and uncertainty.
- **False as stated:** contradicted by evidence or invalid due to overgeneralization.
- **Unresolved:** evidence is insufficient, mixed, or not decisive.
- **Not testable as written:** terms or measurements are vague.
- **Model-dependent:** true only under explicit assumptions.

Avoid “proven” for broad empirical claims. Prefer “established mechanism,” “replicated finding,” or “supported in this system.”

## B. Example true/false and unresolved statements

| Claim | Classification | Reason |
|---|---|---|
| DNA mutations can arise from replication errors. | Established | Well-characterized molecular mechanism. |
| DNA repair can reduce persistence of some lesions and errors. | Established | Multiple repair pathways are characterized. |
| Every mutation is harmful. | False | Effects can be deleterious, neutral, or beneficial in context. |
| Every mutation changes a protein. | False | Noncoding and synonymous changes exist; effects vary. |
| Every mutation is inherited by offspring. | False | Somatic changes are generally not inherited through offspring. |
| All RNA viruses mutate faster than all DNA viruses. | False as a universal claim | Replication strategies and rates vary. |
| A variant in a database must cause disease. | False | Record presence and clinical interpretation are distinct. |
| An associated variant is necessarily causal. | False | Linkage, confounding, or indirect mechanisms may explain association. |
| Mutations generally arise because organisms need them. | False as a general mechanism | Mutation generation is not generally directed by organismal need; selection changes frequencies. |
| A variant has identical effects in every background and environment. | False | Effects can depend on genetic background and environment. |
| A computational prediction proves a molecular mechanism. | False | Prediction is not experimental validation. |
| Algebra alone proves an empirical biological hypothesis. | False | Algebra proves consequences of premises, not the premises’ truth in nature. |
| P(at least one event) = 1-(1-μ)^L. | True under assumptions | Requires independent sites with equal probability μ. |
| Mutation and recombination are identical. | False | They are distinct processes. |
| A negative test proves a mutation is absent. | False | Detection limits, coverage, sampling, and sensitivity matter. |

## C. Formal logic
Modus ponens:
\[
(P\rightarrow Q)\land P\Rightarrow Q
\]
The inference form is valid. Biological soundness depends on whether the premise and conditional are supported.

Example:
1. If a variant is validated against a specified reference, it is a validated sequence difference relative to that reference.
2. Variant V is validated against that reference.
3. Therefore V is a validated sequence difference relative to that reference.

This does not imply pathogenicity, benefit, or causality.

## D. Falsifiable hypothesis example
Hypothesis: under condition C, treatment X increases the rate of variant class V relative to control.

Define organism, treatment, exposure, variant class, rate denominator, controls, sample size, analysis plan, and a minimum effect size. A sufficiently powered, well-controlled result whose confidence interval excludes the predeclared increase can reject that quantitative claim for the studied context. It does not disprove every possible effect in all organisms.

## E. Data-labeling rules
Separate observation, interpretation, source, method/version, confidence, contradictory evidence, and status date. Recommended statuses: observed, experimentally_supported, computational_prediction, clinical_interpretation, hypothesis, conflicting, unresolved, illustrative.
