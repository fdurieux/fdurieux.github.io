# Legible: systemic impact model

A qualitative causal model of how the quality of the artefacts upstream of
code propagates into product quality, quality in use and delivery
performance, and of what interrupts it. Signs and evidence labels, no
magnitudes. Version 0.2 is the model reviewed out of sample against the
pumllint recreation experiment on 2026-10-28
(`recreate_experiment/legible-model-review-2026-10-28/REVIEW.md` in pumllint,
merged as pumllint #205). `CHANGELOG.md` is the record of versions;
`v0.3-change-note.md` is the next revision, drafted and not applied.

## Files

| path | what it is |
|---|---|
| `model-data.py` | **The model.** A Python data module: nodes, edges, loops, stocks, inventory, practices, hypotheses, sources, the cascade. Everything else under `model/` is generated from it or supports it. |
| `model.json` | The model as JSON, generated from `model-data.py`. Never edited by hand. |
| `regen-json.py` | Regenerates `model.json` from `model-data.py` with the standard library only. |
| `build-model.py` | The full renderer: PDF, cascade PNG and JSON, with Matplotlib. Rebuilds are not byte-identical across Matplotlib versions; inspect the layout after a rebuild. |
| `task-brief.md` | The assignment the model answers, with the two supplied definitions (software quality elements, systemic design elements) as appendices. The model's source S9. |
| `legible-defect-cascade-v0.2.png` | The cascade figure as reviewed. |
| `review/claim-register.json`, `review/known-limitations.md`, `review/review-matrix-template.csv` | The author's claims to audit, the author's disclosure of limitations, and the coverage worksheet, as handed to the reviewer. |
| `review/verification-v0.2.json` | The author-side structural and layout checks of the delivered v0.2 files. |
| `evidence/source-register.json`, `evidence/*.md` | The pinned sources and the research notes behind them. |

## Regenerate

```bash
python3 -I model/regen-json.py model/model-data.py model/model.json
```

The full render, with Matplotlib installed:

```bash
python3 model/build-model.py
```

`build-model.py` expects the bundle layout (`work/` and `output/` beside it);
run it from a checkout arranged that way, or adjust its two path constants.

## Versioning

- One file is the model: `model-data.py`. The JSON and the figures are
  generated from it.
- Each version is a git tag. v0.2 is the model as reviewed; the handoff
  bundle it was reviewed in has sha256 `ff499f885792e20e06d3bbca9fc1754381eade56b74312ac9cac5ddee91e45f3`
  and its 20-file manifest is kept in pumllint beside the review.
- Evidence pins run both ways by tag: the model's sources pin pumllint and
  this site at a commit; pumllint's record names the model by tag.
- A review bundle, when one is needed, is built from a tag and is never
  hand-edited.
