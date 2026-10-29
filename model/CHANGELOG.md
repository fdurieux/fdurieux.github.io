# Systemic impact model — changelog

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
carries the chat-library link in its sources page and stays in the bundle;
the repository's PDF will be the v0.3 render. The bundle's repository
snapshots are not committed: their pinned commits are the record. The
bundle's `work/rendered/` previews were not in the bundle.

## v0.1 — 2026-10-28, provisional

Superseded the same day by v0.2 (the supplied definitions, Q1–Q9 in the
user's order, the four layers connected, branching into tests, validation
and correction paths). Not committed; `model-data.py` carries v0.1 as its
base and applies v0.2 on top.

## Next: v0.3

Drafted in `v0.3-change-note.md`, not applied: the review's seven
corrections, the degradation test's two refinements (pumllint #208), and one
extension for knowledge held only by people.
