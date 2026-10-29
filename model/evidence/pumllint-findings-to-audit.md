# Bounded repository findings to audit

Source: S3, `repository-snapshots/pumllint/EVIDENCE.md`, pinned in the source register. These are reported repository results, not an independent rerun. Inspect the complete protocols, sample construction, pre-registered expectations, failures and limitations in that file before drawing conclusions.

## Repair arms: executed scenario pass rates

| Original group / intervention | Reported rate | Scenario runs |
| --- | ---: | ---: |
| Pristine L5 reference | 0.949 | 156 |
| Degraded L2 baseline | 0.741 | 201 |
| L2 repaired without author | 0.841 | 88 |
| L2 repaired with author | 0.957 | 93 |
| Degraded L1 baseline | 0.642 | 162 |
| L1 repaired without author | 0.583 | 84 |
| L1 repaired with author | 0.857 | 84 |

These rates are suite-relative and shown for within-protocol comparison, not as general correctness percentages. Scenario runs are not independent teams, products, diagrams or deployments. Repeated generation and multiple scenarios per artefact must not be mistaken for the same number of independent experimental units.

In the author-less arm, structural repair helped the L2 group, but repaired L1 was 5.9 percentage points below its degraded baseline. All 16 repaired diagrams passed the minimum-level-2 gate; 15 reached at least L4. This separates checkable method conventions from recovery of intended meaning. The experiment does not show that a gate always harms quality.

The with-author arm is relevant counterevidence to any claim that repair is intrinsically ineffective. It improved the reported rates, especially for L1. Its “author” was an LLM stand-in, with a disclosed leakage audit; residual failures and invention remained. It is not evidence that actual domain stakeholders participated in developing this systemic model or that similar effects will occur in production.

The PDF's quantitative discussion concentrates on the author-less arm. A reviewer should decide whether the with-author results need more prominence in the document, and how cautiously to interpret the source's causal wording.

## Other evidence distinctions

The execution-oracle work reports a relationship between diagram maturity and executed behaviour within its experimental families. Judged structural fidelity and executed correctness disagree enough that the pre-registered agreement threshold failed. Do not merge these instruments or present judged fidelity as correctness.

The source also records a later third-party defect-ledger observation. It explicitly says that ledger was read, not re-derived. Neither the full foreign-corpus ledger nor an independent verification of it is included here; do not promote it to independently reproduced evidence.

The bundle includes documentary evidence, not the entire experimental dataset or executable harness. Paths such as `execution_results/analysis.json`, `experiment_results/analysis.json` and analysis scripts are named in the source. Retrieve any required files at the pinned commit for a separate replication exercise and report what is unavailable. No experiment was rerun to produce this handoff.
