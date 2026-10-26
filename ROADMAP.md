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
| Cross-artefact identifier gate | requirement ↔ model ↔ test ↔ API operation | planned | First new project. Starts from pumllint `trace` and aris2puml `--manifest`; explicit identifiers only, no semantic matching |
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
