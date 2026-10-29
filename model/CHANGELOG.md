# Systemic impact model — changelog

## v0.3 — 2026-10-29

51 nodes, 79 signed edges, 8 loops, 20 inventory rows, 6 stocks, 12
practices, 15 sources. Evidence pin: pumllint `eab25fd` (#208, the
degradation results), this site `bb78dff`; the review is pumllint #205
(`fd4a1f0`). Specified in `v0.3-change-note.md`; this entry records what
landed.

**Corrections from the out-of-sample review** (pumllint #205, F1–F7):

- E73 `codedef → deriveddef` (+, M-bounded) and node `depchange` with E74
  `depchange → codedef` (+, M-bounded): the reverse path, from the
  timestamp unit and the export crash.
- Claim C06 upgraded to M, bounded (one instance; premise originating in
  code); node `diverse` with E78 `diverse → detection` (+, M-bounded).
- `deriveddef` narrowed to behaviour-carrying artefacts; node `explderived`
  with E75 `updef → explderived` (+, H) and E76 `explderived → codedef`
  (+, M-bounded, attenuated); E51 gains a moderator, the precedence rank of
  the layer that states the behaviour; E03's condition names the sole-input
  case.
- E77 `drift → confidence` (+, M-bounded); A01's limit and loop B2 cite the
  25-claim instance.
- Stock N, assumption-register entries per artefact set, as the indicator
  for `unknown`; `fidelity` says which reference it is measured against;
  E32's condition rewritten; node `completeness` with E79
  `completeness → detection` (+, M-bounded).
- A08 and A09 limits cite their measurements; H3 and H4 carry one
  measurement each.
- P9, calibrate the oracle by mutation; E58 cited as M-bounded for the
  early-correction loop.

**Refinements from the degradation test** (pumllint #208): the E51
moderator is precedence, not failing runs (D1); E32's measured default is
to record an assumption, not to invent (D2); A09 carries the
pre-registration's one error about the trace gate.

**Extension**: node `tacit`, knowledge held only by people, with E71
`tacit → updef` (+, H) and E72 `tacit → unknown` (+, H); stock P, the
capture inventory with its residual, no percentage; practices P10 elicit,
P11 externalise, P12 validate with the owner; the boundary names the stock
as inside and the network and succession as outside. No edge from capture
to any delivery metric.

**Inventory and page**: A19 vocabulary (glossary), open; A20 property-based
invariants, covered by a practice. `index.html`: the PlantUML row's drift
cell reads open, as the ROADMAP records, with its measurement; the
sequence-diagram sentence carries its condition and the ablation result;
the two rows added to the table.

**Figures and renderer**: `build-model.py` now runs from `model/`, reads
the counts from the data, paginates the inventory, practices, stocks and
sources over 22 pages, and draws the people source, the dependency source,
the role split, the reverse arrow and drift under a green gate on the
cascade page. `knowledge-view.py` generates the reduced view
(`knowledge-view.svg`) from `model.json`. The v0.2 cascade figure is kept
as `legible-defect-cascade-v0.2.png`; `legible-defect-cascade.png` and the
PDF are the v0.3 renders. `review/verification.json` is the v0.3 run; the
v0.2 one is kept beside it.

**Departures from the change note**: practice numbering (P9 calibration,
P10–P12 people-side); edge ids as generated; the claim register gains C13
rather than a separate row per edge.

## v0.2 — 2026-10-28, committed 2026-10-29

The model as reviewed out of sample against the pumllint recreation
experiment (pumllint #205, `recreate_experiment/legible-model-review-2026-10-28/REVIEW.md`;
verdict: fit for its stated purpose after specified corrections, for the
cascade). 46 nodes, 70 signed edges, 8 loops, 18 inventory rows, 9 quality
elements, 5 delivery metrics. Evidence pin: pumllint `9d728c8` (S3), this
site `9ba9b09` (S1, S2).

Provenance. Committed from the handoff bundle
`legible-agent-review-handoff.zip`, sha256
`ff499f885792e20e06d3bbca9fc1754381eade56b74312ac9cac5ddee91e45f3`, whose
20 files verify against the manifest kept in pumllint at
`recreate_experiment/legible-model-review-2026-10-28/target/SHA256SUMS`.
`model.json` regenerated from `model-data.py` with `regen-json.py` is
byte-identical to the bundle's `output/legible-systemic-impact-model.json`
(sha256 `7a54ca85…`) before the one edit below.

One edit against the bundle. Source S9, the supplied definitions, pointed
into a personal chat library. In `model-data.py` and
`evidence/source-register.json` the URL now points at `model/task-brief.md`
in this repository, which preserves the definitions verbatim (the author's
`verification-v0.2.json` records `supplied_definitions_preserved_verbatim`).
`model.json` was regenerated after the edit and differs from the bundle's
copy in that one field only.

Not committed. The reviewed PDF (`output/legible-systemic-impact-model.pdf`)
carries the chat-library link in its sources page and stays in the bundle.
The bundle's repository snapshots are not committed: their pinned commits
are the record.

## v0.1 — 2026-10-28, provisional

Superseded the same day by v0.2 (the supplied definitions, Q1–Q9 in the
user's order, the four layers connected, branching into tests, validation
and correction paths). Not committed; `model-data.py` carries v0.1 as its
base and applies v0.2 on top.
