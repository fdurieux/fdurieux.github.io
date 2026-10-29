# Legible: systemic impact model

A qualitative causal model of how the quality of the artefacts upstream of
code propagates into product quality, quality in use and delivery
performance, and of what interrupts it. Signs and evidence labels, no
magnitudes. `CHANGELOG.md` is the record of versions. v0.2 is the model
reviewed out of sample against the pumllint recreation experiment
(pumllint #205); v0.3 applies that review, the degradation test (pumllint
#208) and one extension for knowledge held only by people.

## Files

| path | what it is |
|---|---|
| `model-data.py` | **The model.** A Python data module: nodes, edges, loops, stocks, inventory, practices, hypotheses, sources, the cascade. Everything else under `model/` is generated from it or supports it. |
| `model.json` | The model as JSON, generated from `model-data.py`. Never edited by hand. |
| `regen-json.py` | Regenerates `model.json` from `model-data.py` with the standard library only. |
| `build-model.py` | The full renderer: the PDF, the cascade figure and `model.json`, with Matplotlib. Writes page previews to `rendered/` (ignored by git) and the structural checks to `review/verification.json`. Rebuilds are not byte-identical across Matplotlib versions; inspect the layout after a rebuild. |
| `knowledge-view.py` | Generates `knowledge-view.svg`, the reduced view of the cascade with the four capture levers, from `model.json`; standard library only. |
| `legible-systemic-impact-model.pdf`, `legible-defect-cascade.png`, `knowledge-view.svg` | The current renders. `legible-defect-cascade-v0.2.png` is the figure as reviewed. |
| `task-brief.md` | The assignment the model answers, with the two supplied definitions (software quality elements, systemic design elements) as appendices. The model's source S9. |
| `review/claim-register.json`, `review/known-limitations.md`, `review/review-matrix-template.csv` | The author's claims to audit, the author's disclosure of limitations, and the coverage worksheet, as handed to the reviewer and updated for v0.3. |
| `review/verification.json`, `review/verification-v0.2.json` | The structural and layout checks of the current render, and of the delivered v0.2 files. |
| `evidence/source-register.json`, `evidence/*.md` | The pinned sources and the research notes behind them. |
| `v0.3-change-note.md` | The specification of v0.3, kept as applied. |

## Regenerate

```bash
python3 -I model/regen-json.py model/model-data.py model/model.json
```

```bash
python3 -I model/knowledge-view.py model/model.json model/knowledge-view.svg
```

The full render, with Matplotlib installed, from the repository root:

```bash
python3 model/build-model.py
```

It prints `Layout bounds OK` or the overflowing text runs by page; a render
with overflow is not committed.

## Versioning

- One file is the model: `model-data.py`. The JSON and the figures are
  generated from it.
- Each version is a git tag. v0.2 is the model as reviewed; the handoff
  bundle it was reviewed in has sha256 `ff499f885792e20e06d3bbca9fc1754381eade56b74312ac9cac5ddee91e45f3`
  and its 20-file manifest is kept in pumllint beside the review.
- Evidence pins run both ways by tag: `model.json` carries `evidence_pin`
  with the pumllint and site commits; pumllint's record names the model
  by tag.
- A review bundle, when one is needed, is built from a tag and is never
  hand-edited.
