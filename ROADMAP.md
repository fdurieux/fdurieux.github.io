# Legible — programme roadmap

The record behind <https://fdurieux.github.io/>. The page quotes this file;
a change in a project's state lands here first. Each project keeps its own
roadmap in its own repository; this file only lists them, their artefact
class, their gate state and the trigger that moves them.

States: **shipping** (a repository with releases) · **planned** (named
artefact class, feasibility assessed, no repository yet) · **open** (gap
recorded, no project) · **covered elsewhere** (a third-party tool or a
practice gates the artefact; linked from the page, not built here).

## The gate contract

Every project here implements, and every third-party tool the page calls
"covered" is measured against: exit codes 0/1/2; a severity ladder with a
`--fail-on` threshold; a baseline file and ratchet whose update step stays
out of CI; a JSON report pinned by a schema plus SARIF; zero runtime
dependencies with a pre-commit hook, an editor integration and a CI action;
evidence tagging (measured / mechanism / hypothesis) on every value claim.
pumllint is the reference implementation.

## Projects

| Project | Artefact class | State | Trigger / next step |
|---|---|---|---|
| [pumllint](https://github.com/fdurieux/pumllint) | PlantUML models | shipping | Its own ROADMAP.md |
| [aris2puml](https://github.com/fdurieux/aris2puml) | ARIS EPC exports | shipping | Its own ROADMAP.md; the in-ARIS gate waits on an adopter with Architect |
| Cross-artefact identifier gate | requirement ↔ model ↔ test ↔ API operation | shipping | *[2026-11-15: was planned; now built by [knowgov](https://github.com/fdurieux/knowgov) (statements, provenance, conflicts, the task gate, code-to-knowledge trace; v0.9.1) with [ieam-register](https://github.com/fdurieux/ieam-register) (identities, typed links, approvals; v0.2.13). Their own records: knowgov `backlog/`, ieam-register `decisions/`.]* Was: First new project. Starts from pumllint `trace` and aris2puml `--manifest`; explicit identifiers only, no semantic matching |
| Settlement benchmark ([knowgov-bench](https://github.com/fdurieux/knowgov-bench), private) | a synthetic task corpus with a hidden independent oracle | planned | *[2026-11-15: repository created private by the maintainer; this state vocabulary has no word for a private research record, so planned until a study reports.]* Study MSX-01 recorded there; the first build is its intent and behaviour inventory; the scored run is parked by the maintainer |
| Requirements wording linter | textual requirements (INCOSE GtWR, EARS) | planned | Deterministic lexical rules as the gate; ambiguity detection advisory only (Smella: 59 % precision) |
| EPC toolchain in the open | EPML / EPC conventions | planned | Reader plus ruleset; the only live OSS entry is aris2puml + pumllint |
| BPMN repository-wide checks | BPMN 2.0 | planned | bpmnlint plugin: cross-model references, 7PMG, score. Never a pumllint pack (pumllint never-build) |
| ArchiMate validator with CI output | ArchiMate exchange / Archi | open | Wait for pull; the field is fragmenting into small agent-era tools |
| SysML v2 conventions | SysML v2 text | open | Consume the pilot's validator; add conventions only on pull |
| Diagram-versus-code drift | PlantUML / C4 against code | open | Nearest asset is pumllint's parsed model; a mapping file per language |
| Process design against event logs | process mining conformance | open | Needs an adopter with an event log |
| User-story quality | stories, acceptance criteria | open | No machine check exists; evidence of need recorded (SWE-bench annotation) |

## Log

- *2026-10-26* — Programme named and the site created. The page maps the
  SAFe® Continuous Delivery Pipeline's sixteen activities to artefact,
  gate state and tool, from a tool survey made the same day (sources in
  the pumllint docs series and the session's research reports). Five
  planned or open items come from that survey's ranked gap list; their
  feasibility verdicts are quoted in the table. No new project repository
  exists yet.
- *2026-10-29* — The systemic impact model v0.2 committed under `model/`:
  the source data file, the renderer, the task brief with the supplied
  definitions, the claim register, the known limitations, the author-side
  verification and the cascade figure, as reviewed out of sample in
  pumllint #205 (handoff bundle sha256 `ff499f88…45f3`, 20 files verified
  against the manifest kept there). The JSON is regenerated from the data
  file and is byte-identical to the reviewed copy before the one edit: the
  source S9 link into a personal chat library now points at the task brief
  in this repository. The reviewed PDF stays in the bundle. `model/CHANGELOG.md`
  is the model's record from here on; `model/v0.3-change-note.md` is the
  next revision, drafted and not applied.
- *2026-10-29* — Systemic impact model v0.3: the seven corrections of the
  out-of-sample review (pumllint #205) and the two refinements of the
  degradation test (pumllint #208) applied; one source node added for
  knowledge held only by people, with two edges, four practices (one
  measured, three from the departing-expert plan) and a measured indicator,
  all labelled; two inventory rows added (vocabulary, open; property-based
  invariants, covered by a practice); the page's drift cell aligned to this
  record (open) and its sequence-diagram claim given its condition. 51
  nodes, 79 edges, 8 loops, 20 rows. Evidence pin pumllint `eab25fd`. The
  JSON, the PDF, the cascade figure and a reduced knowledge view are
  generated from the data file. First consumer: the knowledge-preservation
  deck's cascade slide.
- *2026-11-15* — A cross-repository assessment and roadmap (a Codex
  thread of 2026-11-14, pinned at pumllint `fdecc74`, aris2puml `ca22e13`,
  knowgov `538618f`, ieam-register `dd545b7` and this repository
  `099a737`) was read against each repository's record. On the
  maintainer's go of the same day, its benchmark lands as a settlement
  benchmark in a private repository, `knowgov-bench`, with its study
  record (MSX-01) and its decisions there; nothing of its domain, its
  obligations or its cases comes here. Two table rows move: the
  benchmark is added as planned, and the cross-artefact identifier gate,
  planned since 2026-10-26, is marked shipping, because knowgov and
  ieam-register now build it. The roadmap's other packages land where
  each repository keeps its record: knowgov's lighthouse readiness as
  notes on its existing tasks, aris2puml's export identity under its
  item A1, and the one pumllint gap the assessment reproduced (an
  unreachable cycle in a state diagram, unflagged) as a pumllint ROADMAP
  candidate (Arc C).
  - *Opportunity canvas.* Problem: the programme's claim, that governed
    knowledge keeps unsupported behaviour out of accepted code, is shown
    on one proof-of-concept subject and not measured on a task whose
    acceptance is independent of the specification. Users: the
    maintainer, an adopter weighing the stack. Solution: a synthetic
    benchmark whose hidden oracle no generator can read, and a
    pre-registered study comparing full context, a hand-picked package
    and a compiled projection. Cost: the build packages, roughly 31–57
    person-days across the roles the roadmap names; the scored run's
    model spend is parked and unauthorised. Benefit: a measured,
    bounded answer, null or not.
  - *Fit/gap.* Fit: knowgov's task gate, approval bar, execution binding
    and evidence bundle already exist, and the study uses them through
    an instance rather than changing a contract (knowgov 0.9 is frozen).
    Gap: no repository held a hidden oracle, now answered by the private
    home; independent validation cannot be claimed while one maintainer
    and AI sessions fill every role, which the study records as its
    limit; the real source-tool route stays adopter-gated (aris2puml A1).
  - *SWOT.* Strengths: pre-registration, stop rules fixed before any
    run, every repository keeping one record. Weaknesses: one person in
    every role; an optimistic effort estimate. Opportunities: the first
    measurement of a task-specific projection of the knowledge;
    a template for an adopter's own study. Threats: a private record the
    page cannot quote, and a public row that drifts from it; a synthetic
    domain that rewards guessing familiar conventions, which the
    protocol counters with deliberately non-canonical rules.
  - *Advice (the drafter's).* Keep the boundaries; build the benchmark's
    intent and oracle before any compiler; leave the scored run parked
    until the build packages are done and the spend is authorised in
    writing; quote only the study's verdict here, never its content.
    The page (`index.html`) and the README's "Shipping today" line still
    show the pre-2026-11-15 state and follow in a page update.
- *2026-11-15* — The page's cross-artefact consistency row moves from
  planned to covered, on the maintainer's word of the same day ("yes,
  count the coverage row as covered"). The page and the README had
  followed the 2026-11-15 entry above (#4); this row was left planned
  because no entry gave it a state. Measured against the gate contract:
  knowgov's task gate exits 0/1/2 with a `--fail-on` threshold, keeps a
  baseline (`--baseline record|FILE`), writes a JSON report pinned by a
  schema and SARIF through its annotator, and ships a CI action;
  ieam-register's checker exits 1 on any error in the identities and
  typed links; pumllint `trace` still fails on unknown references
  between diagrams and requirements.
  - *Opportunity canvas.* Problem: the page called the artefact class
    planned after the identifier gate had shipped. Users: an adopter
    reading the table. Solution: mark it covered and name the tools.
    Cost: one row. Benefit: the table agrees with the projects list.
  - *Fit/gap.* Fit: exit codes, threshold, baseline, schema-pinned JSON,
    SARIF and a CI action. Gap: identifiers are explicit, never matched
    by meaning; knowledge that is consistently wrong in every document
    passes (knowgov's degradation test, measured); knowgov needs its
    store's libraries, so it is not zero-dependency.
  - *SWOT.* Strengths: the row is backed by gates that fail a build.
    Weaknesses: three repositories behind one row. Opportunities: the
    lighthouse's instance as the first adopter evidence. Threats: an
    adopter reading covered as validated, which the row's missing cell
    answers.
  - *Advice.* Mark it covered with its limit stated in the row.
