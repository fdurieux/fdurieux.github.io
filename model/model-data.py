"""Content for the Legible systemic impact model. Draft definitions are explicit."""
MODEL = {
  "title": "Legible: a systemic model of quality and delivery",
  "version": "0.1-provisional",
  "date": "2026-10-28",
  "status": "Qualitative causal model; not calibrated or validated as a whole",
  "definition_status": {
    "software_quality": "The exact conversation 'Software quality elements' could not be retrieved. Q1-Q9 below are explicit working categories, not a reconstruction of the user's definition.",
    "systemic": "The exact conversation 'Systemic design elements' could not be retrieved. Related context describes framing, perspectives, system mapping, underlying causes, desirable futures, leverage, co-design, experimentation and sustained change. This model operationalizes that related material provisionally.",
    "reconciliation": "Replace or map the working quality categories and systemic elements when the original excerpts are supplied; revisit every affected mapping and causal claim."
  },
  "boundary": {
    "unit": "One application or service and its contributing value stream; suppliers and shared platforms are explicit dependencies.",
    "start": "Business hypothesis or technical-change need",
    "end": "Production use, operation and learning that revises intent and implementation",
    "inside": ["people and decision rights", "upstream artefacts", "checks and authoring practices", "implementation and testing", "release decisions", "operational learning", "capacity allocation"],
    "moderators": ["change risk and complexity", "existing architecture and debt", "team skill and staffing", "release policy", "platform reliability", "demand", "regulatory constraints", "AI use", "test and observability coverage"],
    "purpose": "Improve useful and safe outcomes for users while sustaining the ability to change software; a green gate or higher deployment count is not the purpose.",
    "inventory_scope": "All 18 rows in the site's artefact-by-artefact table, using its 2026-10-26 survey as the inventory snapshot. States are site classifications, not an independent fresh audit of every tool."
  },
  "sources": [
    {"id":"S1","title":"Legible site and artefact inventory","url":"https://github.com/fdurieux/fdurieux.github.io/blob/9ba9b09cb548a5d496e297cecc57d4f576647292/index.html","scope":"18-row inventory, six gate properties, boundaries; snapshot dated 2026-10-26"},
    {"id":"S2","title":"Legible programme roadmap","url":"https://github.com/fdurieux/fdurieux.github.io/blob/9ba9b09cb548a5d496e297cecc57d4f576647292/ROADMAP.md","scope":"Shipping, planned and open work; programme gate contract"},
    {"id":"S3","title":"pumllint EVIDENCE.md","url":"https://github.com/fdurieux/pumllint/blob/9d728c8c17e15d288022a47abe5d2293ecc0ba0e/EVIDENCE.md","scope":"Sequence-diagram code-generation experiments and author-less repair limitations; no production DORA effect measured"},
    {"id":"S4","title":"DORA software delivery performance metrics","url":"https://dora.dev/guides/dora-metrics/","scope":"Current five metrics and application/service measurement boundary; accessed 2026-10-28"},
    {"id":"S5","title":"DORA: documentation quality","url":"https://dora.dev/capabilities/documentation-quality/","scope":"Documentation and technical-capability research, not tool-specific intervention proof"},
    {"id":"S6","title":"DORA: continuous integration","url":"https://dora.dev/capabilities/continuous-integration/","scope":"Fast feedback, frequent integration and automated tests"},
    {"id":"S7","title":"DORA: working in small batches","url":"https://dora.dev/capabilities/working-in-small-batches/","scope":"Batch size and feedback; capability research"},
    {"id":"S8","title":"DORA: streamlining change approval","url":"https://dora.dev/capabilities/streamlining-change-approval/","scope":"Heavy approval processes, delays, batching and risk"},
    {"id":"S9","title":"ISO/IEC 25010:2023 overview","url":"https://www.iso.org/standard/78176.html","scope":"Reference for a multidimensional product-quality lens; not the missing conversation"},
    {"id":"S10","title":"DORA: test automation","url":"https://dora.dev/capabilities/test-automation/","scope":"Maintainable tests of actual user journeys; checks alone do not replace test execution"}
  ],
  "evidence_legend": {
    "M": "Measured in a bounded local experiment; its scope and limits travel with the claim.",
    "R": "External primary research supports a related capability or relationship; no claimed tool-specific effect size.",
    "H": "Proposed mechanism or hypothesis in this model; needs local validation.",
    "I": "Inventory/capability description from the site; not an outcome-effect claim."
  },
  "quality": [
    ["Q1","Functional suitability","The required behaviour is correct, sufficiently complete and useful.","Independent acceptance outcomes; escaped functional defects; task completion."],
    ["Q2","Reliability and recoverability","The service behaves dependably and can restore useful service after failure.","SLO attainment, incident impact, restore/rollback drills."],
    ["Q3","Security","Threats and unauthorized actions are prevented, detected and contained.","Verified security properties, exploitable findings, incident exposure."],
    ["Q4","Performance efficiency","Response and resource use meet the workload's needs.","p95/p99 latency and resource cost under a specified workload."],
    ["Q5","Compatibility and interoperability","Components and consumers exchange information and coexist correctly.","Consumer contract tests, migration compatibility and integration failures."],
    ["Q6","Interaction capability","People can understand and operate the product, including accessibility needs.","Observed task success, errors, accessibility checks and user research."],
    ["Q7","Maintainability and testability","People can understand, diagnose, change and verify the implementation.","Change effort, testability, change coupling and diagnosis time."],
    ["Q8","Flexibility and adaptability","The product can adapt to changed environments, scale and requirements.","Demonstrated migration, scaling and replacement scenarios."],
    ["Q9","Safety","Hazards to people, assets or the environment are controlled.","Hazard analysis and independently verified safety constraints." ]
  ],
  "quality_notes": [
    "These working categories are ISO-inspired, not a verbatim taxonomy or the missing conversation. Subcharacteristics are grouped for this model.",
    "Technical debt is a stock of deferred work and future change burden, especially affecting Q7 and Q8; it is not a synonym for every quality defect.",
    "Privacy, compliance and business fitness cut across categories and need explicit requirements and evidence. DORA cannot stand in for them.",
    "Artefact quality, implemented product quality, quality experienced in use, and delivery performance are distinct layers. Agreement between two artefacts is not independent evidence of correctness."
  ],
  "metrics": [
    ["DF","Deployment frequency","Production deployments per period; higher capability to deploy is desirable.","Less rework and smaller viable changes can permit more deployments.","Only if demand, deployment automation and release policy allow it; do not manufacture deploys."],
    ["CLT","Change lead time","Elapsed time from a code commit to production deployment; lower is desirable.","Fewer downstream corrections and less coordination can shorten the path.","An upstream gate can move work before the commit, or add waiting after it; track both."],
    ["CFR","Change fail rate","Fraction of deployments requiring immediate remedial intervention; lower is desirable.","Fewer escaped defects in covered failure classes can reduce failures.","Many defects do not cause immediate deployment failure; denominators and change mix matter."],
    ["FDRT","Failed deployment recovery time","Time to recover from a failed deployment needing intervention; lower is desirable.","Current models and trace links can shorten diagnosis and change impact analysis.","Depends on actual responder use, telemetry and recovery controls; fewer failures alone do not shorten this duration."],
    ["DRR","Deployment rework rate","Fraction of deployments unplanned because of production incidents; lower is desirable.","Fewer escaped defects can reduce corrective deployments.","Not all rework, debt work or planned improvement qualifies; keep classification consistent."]
  ],
  "inventory": [
    {"id":"A01","artefact":"PlantUML models","state":"covered","tools":"pumllint: semantic rules, score, ratchet, trace, editor and CI","mechanism":"Earlier detection of supported modelling defects; author resolves missing decisions before implementation.","quality":["Q1","Q2","Q7"],"route":"CFR/DRR may fall via fewer escaped defects; CLT may fall via less rework; FDRT only if current models aid response.","limit":"A maturity score is not product correctness. Diagram-code drift is not checked by the listed gate. Author-less semantic invention can harm.","evidence":"M for a bounded sequence-to-code experiment; H for production effects","source":["S1","S3"]},
    {"id":"A02","artefact":"ARIS process models (EPC)","state":"covered","tools":"aris2puml converts; pumllint checks the resulting activity diagrams","mechanism":"Expose supported process defects to executable checks without silently repairing their source meaning.","quality":["Q1","Q2","Q7"],"route":"Less process misunderstanding may reduce rework and failure; CLT, CFR and DRR are indirect outcomes.","limit":"Conversion fidelity, supported constructs and author review matter. In-ARIS validation still needs an adopter; no automatic transfer of sequence-codegen effect sizes.","evidence":"I + H","source":["S1"]},
    {"id":"A03","artefact":"Textual requirements","state":"planned","tools":"StrictDoc, Doorstop, Sphinx-Needs, OpenFastTrace for structure and links","mechanism":"Find missing or broken references; make requirement ownership and change impact easier to resolve.","quality":["Q1","Q7"],"route":"Less clarification and omitted impact may improve CLT, CFR and DRR.","limit":"Current structural checks do not establish truth or semantic completeness. The wording linter is planned; ambiguity detection is advisory.","evidence":"I + H","source":["S1"]},
    {"id":"A04","artefact":"User stories","state":"open","tools":"No maintained checker listed; proposed complement: examples and joint refinement","mechanism":"People expose missing cases and conflicting expectations before code is written.","quality":["Q1","Q6"],"route":"Avoided misunderstanding may reduce total change time and corrective deployments.","limit":"This is a human-validation intervention, not a shipped machine gate. A story template can be complete while the problem is misunderstood.","evidence":"I + H","source":["S1"]},
    {"id":"A05","artefact":"Specification prose","state":"covered","tools":"Vale and markdownlint","mechanism":"Consistent terminology and presentation reduce avoidable reading and maintenance friction.","quality":["Q7"],"route":"A weak, indirect CLT pathway through comprehension; no direct claim about runtime defect prevention.","limit":"Well-written prose may still contain vague guards or wrong business rules; style cleanup can crowd out substantive review.","evidence":"I + H; R for documentation generally","source":["S1","S5"]},
    {"id":"A06","artefact":"Acceptance scenarios (Gherkin)","state":"covered","tools":"gplint; proposed complement: execute independently reviewed examples","mechanism":"Check scenario conventions, then connect useful examples to executable acceptance evidence.","quality":["Q1","Q7"],"route":"CFR and DRR can improve only through defects actually detected and fixed; CLT through faster diagnosis.","limit":"Linting Gherkin is not running tests. Tests generated from the same mistaken specification can agree with wrong code.","evidence":"I + H; R for test automation generally","source":["S1","S10"]},
    {"id":"A07","artefact":"BPMN process models","state":"planned","tools":"bpmnlint and Camunda plugins; repository-wide extension planned","mechanism":"Detect supported local process-modelling violations before implementation or process execution.","quality":["Q1","Q2","Q7"],"route":"Potentially fewer process defects and less rework: CFR/DRR down and CLT down.","limit":"Do not credit the planned cross-model rules or score today. Local structural validity does not prove business behaviour.","evidence":"I + H","source":["S1"]},
    {"id":"A08","artefact":"Decision tables (DMN)","state":"covered","tools":"dmnlint, with the site's stated small rule set","mechanism":"Remove the specific decision-table defects the configured rules detect.","quality":["Q1","Q7"],"route":"Fewer decision errors may reduce CFR/DRR, if those defects otherwise reach production.","limit":"Do not infer complete overlap, gap, legal or business-rule verification from a lint pass; use independent boundary examples.","evidence":"I + H","source":["S1"]},
    {"id":"A09","artefact":"Cross-artefact consistency","state":"planned","tools":"pumllint trace today; requirement-model-test-API identifier graph planned","mechanism":"Explicit identifiers expose orphan references and missed change impact across connected artefacts.","quality":["Q1","Q5","Q7"],"route":"Less omitted change scope may improve CLT/CFR/DRR; trace-informed diagnosis may improve FDRT.","limit":"A valid link is not semantic agreement or test adequacy. The full graph and diagram-code drift detection are not shipped by this inventory.","evidence":"I + H","source":["S1","S2"]},
    {"id":"A10","artefact":"Architecture decisions (ADR)","state":"open","tools":"adr-guard and adrpy-ai, both described as pre-1.0","mechanism":"Preserved rationale, ownership and decision status may reduce repeated debate and contradictory changes.","quality":["Q7","Q8"],"route":"Potential CLT and FDRT improvement through comprehension and diagnosis.","limit":"File validation does not validate a trade-off; stale rationale can entrench a poor design. Keep the site's open classification.","evidence":"I + H","source":["S1"]},
    {"id":"A11","artefact":"C4 architecture models","state":"covered","tools":"Structurizr CLI validation and inspections","mechanism":"Make architecture structure easier to inspect and identify supported inconsistencies.","quality":["Q5","Q7"],"route":"Fewer coordination mistakes may improve CLT; current maps may aid FDRT.","limit":"A valid architecture model does not prove that deployed dependencies match it or that the system meets reliability or performance goals.","evidence":"I + H","source":["S1"]},
    {"id":"A12","artefact":"ArchiMate enterprise models","state":"open","tools":"Archi GUI validator and custom scripts, as listed","mechanism":"Human interpretation of validated relationships may improve cross-team change impact decisions.","quality":["Q5","Q7","Q8"],"route":"Potential coordination and CLT benefit, mediated by governance decisions.","limit":"No shared gate-capable catalogue is claimed by the snapshot. Central approval can add more delay than modelling removes.","evidence":"I + H","source":["S1"]},
    {"id":"A13","artefact":"SysML v2 and Capella","state":"open","tools":"Pilot implementation and Capella validation rules","mechanism":"Check supported systems-model constraints and clarify interfaces or stated requirements.","quality":["Q1","Q5","Q9"],"route":"Potential integration-failure reduction; delivery effects depend on system-software interfaces and validation.","limit":"No general standalone gate is credited by the snapshot. Formal model validity is not a safety case; safety requires hazard-specific evidence.","evidence":"I + H","source":["S1"]},
    {"id":"A14","artefact":"API contracts (OpenAPI, AsyncAPI)","state":"covered","tools":"Spectral, vacuum, Redocly; vacuum score and minimum","mechanism":"Enforce configured contract conventions and make interface expectations explicit before consumer implementation.","quality":["Q5","Q7","Q3"],"route":"Interface defects and rework may fall, improving CFR/DRR/CLT.","limit":"A conforming document is not a verified implementation. Security benefits require relevant rules and tests; backward compatibility is not automatic.","evidence":"I + H","source":["S1"]},
    {"id":"A15","artefact":"Schemas (Protobuf, GraphQL, JSON Schema)","state":"covered","tools":"buf, graphql-eslint, sourcemeta jsonschema; buf breaking checks","mechanism":"Catch supported schema defects and incompatible changes before dependent consumers fail.","quality":["Q5","Q1","Q7"],"route":"A relatively short causal path to fewer integration failures and corrective deployments: CFR/DRR down.","limit":"Schema compatibility does not establish semantic compatibility or safe data migration. Runtime and consumer coverage still matter.","evidence":"I + H","source":["S1"]},
    {"id":"A16","artefact":"Data models","state":"covered","tools":"SQLFluff, dbt-checkpoint, dbt_project_evaluator","mechanism":"Improve supported SQL/project conventions and surface maintainability or structural issues.","quality":["Q7","Q1"],"route":"Less data-pipeline rework may improve CLT and DRR; some detected defects may affect CFR.","limit":"The site leaves conceptual and logical models uncovered. Lint passes do not prove data correctness, efficient queries or safe migrations.","evidence":"I + H","source":["S1"]},
    {"id":"A17","artefact":"Threat models","state":"open","tools":"pytm and Threagile, with custom risk gating","mechanism":"Make trust boundaries and attack paths discussable; link threats to implemented and verified controls.","quality":["Q3","Q2","Q9"],"route":"Security risk may decrease without any immediate DORA change; CFR/DRR only for affected deployment incidents.","limit":"Generating a threat report is not mitigation. Custom thresholds, control ownership and security testing are required.","evidence":"I + H","source":["S1"]},
    {"id":"A18","artefact":"Process design against reality","state":"planned","tools":"Process-mining conformance, for example PM4Py; custom gate","mechanism":"Compare observed event traces with the model, then investigate deviations and revise design or execution.","quality":["Q1","Q2","Q7"],"route":"Reduced recurrent process defects and bottlenecks may improve end-to-end time, CFR and DRR.","limit":"Requires suitable logs and case identities. Deviations can be beneficial adaptations; conformance to a bad process is not quality.","evidence":"I + H","source":["S1"]}
  ],
  "actors": [
    ["Users and domain owners","Validate intent, edge cases and acceptable outcomes","Can reject a semantically wrong 'green' artefact; supply independent examples."],
    ["Product owners and sponsors","Choose scope, priorities and improvement capacity","Do not convert freed capacity automatically into more unfinished work."],
    ["Analysts and architects","Own models, interfaces, rationale and dependencies","Maintain source truth; distinguish unsupported constructs and missing decisions."],
    ["Developers and AI agents","Consume artefacts and implement changes","Resolve uncertainty with an owner; agents cannot authorize invented business meaning."],
    ["QA, security and safety specialists","Choose independent acceptance and risk evidence","Challenge shared assumptions; gate on justified risk, not document appearance."],
    ["Platform and gate maintainers","Own check precision, latency, versions and integration","Tune rules, make failures actionable, audit suppressions and baseline changes."],
    ["Operations and responders","Use current context and report production behaviour","Feed incident causes and observed drift back to authors; verify recovery paths."],
    ["Governance and risk owners","Set proportional controls and exceptions","Time-bound waivers with accountable ownership; change incentives when scores are gamed."]
  ],
  "practices": [
    ["P1","Run at the author and in CI","Shorter feedback delay and less avoidable handoff work","Measure time-to-action and usefulness, not tool-install count; S1/S6."],
    ["P2","Separate clean / findings / unable-to-run","Makes the check result actionable and its failure visible","An unexecuted check must not silently become a pass; S1."],
    ["P3","Use severity and a justified threshold","Focus scarce review effort on consequential defects","Do not hard-block low-precision ambiguity judgements; validate rule precision locally; S1."],
    ["P4","Baseline and ratchet","Allows brownfield adoption while exposing regression","Baseline update outside the gate; new/untracked work needs an explicit policy. A ratchet alone does not repay old debt; S1/S3."],
    ["P5","Use stable IDs and machine-readable reports","Makes change-impact links and review evidence retrievable","Record what inputs, versions and scope were checked; a link or report is not a semantic proof; S1."],
    ["P6","Tag evidence and publish failures","Limits false confidence and supports revision of rules","Keep local experiment results separate from external research and untested mechanisms; S1/S3."],
    ["P7","Validate intent with people and independent tests","Prevents common-mode errors across requirements, models, tests and code","Site-level complement to the inventory: stakeholders, walking skeleton and shipped-product feedback; S1/S10."],
    ["P8","Review incidents and observed deviations","Closes the loop from actual outcomes to upstream intent","Proposed implementation practice; distinguish useful exceptions from defects and update artefacts deliberately; H."]
  ],
  "nodes": [], "edges": [], "loops": [],
  "stocks": [
    ["U","Unresolved upstream defects","Count within an explicit artefact scope","introduced by new or changed intent; removed by validated correction","A warning count is an observation, not the stock itself."],
    ["T","Technical and information debt","Estimated remediation effort, hours","deferred work and drift add effort; verified remediation removes it","Estimates require re-estimation; not interchangeable with defect count."],
    ["K","Validated, current shared knowledge","Count of owned, validated knowledge items","validation adds; invalidation and stale context remove","Coverage, relevance and use matter more than volume."],
    ["W","Work in progress and waiting","Changes in a consistently defined workflow","admitted changes add; completed or abandoned changes remove","A larger W stock can increase waiting even if coding is faster."]
  ],
  "hypotheses": [
    ["H1","Precise early checks prevent relevant escaped defects","Run an applicable high-precision rule subset; record confirmed findings, corrections and targeted escape classes.","Confirmed early catches rise initially; targeted escapes and unplanned correction work fall later.","If escapes do not change despite genuine coverage and consumption, inspect rule relevance, propagation and test blind spots."],
    ["H2","Gate burden can outweigh prevention","Track wait and triage time by stage; introduce advisory-first checks and compare similar change cohorts.","False positives or centralized sign-off increase waiting and bypass before any delayed quality gain.","If burden is material without prevented defect evidence, tune, relocate or remove the gate instead of escalating strictness."],
    ["H3","Traceability reduces omitted change impact","For changes with known dependent consumers, compare identified impacts with independently reviewed actual impacts.","Fewer missed consumers and shorter diagnosis after the trace is used.","If links exist but are stale or unused, graph coverage is not a leading indicator of the claimed benefit."],
    ["H4","Intent validation prevents 'green but wrong' repairs","Flag guessed or unresolved decisions; require domain-owner resolution and independent outcome examples.","Incorrect repairs decline even if gate scores change little.","If no independent oracle exists, do not infer correctness from matching specifications and tests."]
  ]
}

NODES = [
 ("check","Effective check use","variable","Rate of relevant, supported checks whose findings are acted on"),
 ("early","Validated early correction","flow","Relevant upstream defects actually resolved per period"),
 ("knowledge","Current, validated shared knowledge","stock","K"),
 ("fidelity","Implementation correctness","variable","Verified agreement with valid intended behaviour"),
 ("escape","Escaped defect burden","variable","Relevant production defects weighted by impact per period"),
 ("reactive","Reactive workload","variable","Capacity consumed by incident handling and correction"),
 ("capacity","Improvement capacity","variable","Time available for preventive work and learning"),
 ("pressure","Delivery pressure","variable","Pressure to complete work against available capacity"),
 ("bypass","Bypassing or deferring checks","variable","Share of applicable controls avoided or superficial"),
 ("gateburden","Gate burden","variable","Execution, review, triage and waiting effort per change"),
 ("waiting","Waiting time","variable","Elapsed time awaiting checks, decisions and approval"),
 ("batch","Change batch size","variable","Scope coupled into one deployment"),
 ("severity","Control strictness","decision","How much evidence or approval a change must pass"),
 ("green","Apparent gate success","variable","Observed passing score or check result"),
 ("confidence","Unwarranted confidence","variable","Confidence unsupported by independent outcome evidence"),
 ("validation","Independent intent validation","variable","Domain challenge and acceptance evidence independent of the artefact being checked"),
 ("unknown","Unresolved or invented decisions","stock","Missing intent left unresolved or replaced by unsupported assumptions"),
 ("repair","Score-driven semantic repair","decision","Repair effort aimed at passing while intent remains unresolved"),
 ("debt","Technical and information debt","stock","T"),
 ("drift","Artefact-to-reality drift","stock","Mismatch between current design records and observed implementation or process"),
 ("discrepancy","Confirmed discrepancies","variable","Gaps established using actual behaviour and relevant independent evidence"),
 ("learning","Validated learning and updates","flow","Corrections to design, assumptions, rules and practices per period"),
 ("diagnosis","Diagnosis duration","variable","Elapsed time to identify an actionable cause after a failed deployment"),
 ("trace","Useful explicit traceability","variable","Coverage of current, correct, consumed references relevant to a change"),
 ("missed","Missed change impact","variable","Dependent behaviour or consumers omitted from a change"),
 ("wip","Work in progress","stock","W"),
 ("inflow","Change admission rate","flow","Changes admitted into the measured workflow per period"),
 ("completion","Change completion rate","flow","Changes exiting the measured workflow per period"),
 ("demand","Additional accepted demand","decision","Extra scope accepted when freed capacity is seen"),
 ("df","Deployment frequency","metric","DF"),
 ("clt","Change lead time","metric","CLT"),
 ("cfr","Change fail rate","metric","CFR"),
 ("fdrt","Failed deployment recovery time","metric","FDRT"),
 ("drr","Deployment rework rate","metric","DRR"),
 ("total","Hypothesis-to-validated-value time","metric","Elapsed end-to-end time including upstream work and post-release learning")
]
MODEL["nodes"] = [dict(id=n,label=l,kind=k,definition=d) for n,l,k,d in NODES]

def edge(a,b,s,delay,mechanism,evidence="H",sources=(),condition="Other relevant factors held comparable"):
    MODEL["edges"].append(dict(id=f"E{len(MODEL['edges'])+1:02d}",source=a,target=b,polarity=s,delay=delay,mechanism=mechanism,evidence=evidence,sources=list(sources),condition=condition))

edge("check","early","+","same change","Acted-on valid findings permit earlier correction.",sources=["S1"])
edge("early","knowledge","+","days to weeks","Validated correction improves retained, current shared knowledge.")
edge("knowledge","fidelity","+","next implementation","Relevant knowledge helps people or agents implement valid intent.","M-bounded / R-related / H-transfer",["S3","S5"],"Knowledge is correct, current and actually consumed; the measured result covers sequence-codegen only")
edge("fidelity","escape","-","after release","Fewer relevant implementation errors escape, given comparable validation.")
edge("escape","reactive","+","hours to weeks","Escaped defects generate diagnosis and corrective work.")
edge("reactive","capacity","-","same period","Finite capacity is diverted from prevention.")
edge("capacity","check","+","weeks","Capacity can sustain rule maintenance, adoption and timely correction.",condition="Management allocates freed time to improvement")
edge("reactive","pressure","+","same period","Unplanned demand raises pressure against commitments.")
edge("pressure","bypass","+","days","Pressure may incentivize deferring or bypassing checks.")
edge("bypass","check","-","same change","Avoided or superficial controls reduce effective use.")
edge("severity","gateburden","+","immediate","Stricter demands can add review or triage burden.",condition="Added requirements consume nontrivial time; not every stricter rule does")
edge("gateburden","waiting","+","immediate","Burden creates queues when service capacity is constrained.")
edge("waiting","batch","+","days to weeks","Teams may bundle changes to amortize waits.","R-related / H-local",["S8"])
edge("batch","cfr","+","next deployments","Larger coupled changes may increase deployment failure risk.","R-related / H-local",["S7","S8"])
edge("cfr","severity","+","after incidents","A reactive governance response may add controls.","R-related / H-local",["S8"],"Organization responds to incidents by increasing approval burden")
edge("severity","check","+","days to weeks","Relevant enforced controls can increase effective detection.",condition="Precision, coverage and compliance remain adequate")
edge("escape","cfr","+","deployments","Deployment-associated defects can cause immediate intervention.",condition="Deployment volume and mix comparable; includes only defects relevant to immediate failure")
edge("escape","drr","+","later deployments","Incident corrections can produce unplanned deployments.",condition="Consistent incident classification and comparable total deployment denominator")
edge("reactive","clt","+","days","Contention and rework after commit can delay production.",condition="Reactive work lies on or competes for the measured post-commit path")
edge("waiting","clt","+","same change","Post-commit waiting contributes to elapsed lead time.",condition="Waiting occurs after the measurement's code-commit start")
edge("capacity","df","+","weeks","Available capacity can enable additional small production changes.",condition="Useful demand, deployability and release policy permit deployment")
edge("trace","missed","-","same change","Used, correct links reveal affected consumers and artefacts.")
edge("missed","escape","+","after release","Omitted impact can leave incompatible or incorrect behaviour.")
edge("trace","diagnosis","-","during incident","Relevant current links can narrow impact and causes.",condition="Responders consult the links and can relate them to actual runtime evidence")
edge("knowledge","diagnosis","-","during incident","Correct context reduces search and interpretation time.","R-related / H-local",["S5"])
edge("diagnosis","fdrt","+","during incident","Diagnosis time contributes to failed-deployment recovery.",condition="On the critical recovery path; rollback, detection and validation may dominate")
edge("repair","green","+","immediate","Filling formal gaps can raise a convention score.","M-bounded",["S3"],"Observed in the author-less repair experiment; no general guarantee")
edge("green","confidence","+","immediate","A passing score may be misread as proof of semantic correctness.")
edge("confidence","validation","-","next review","False assurance can displace independent challenge.")
edge("validation","unknown","-","days","Domain confirmation resolves uncertainty and rejects invented decisions.")
edge("unknown","repair","+","next generation","Unresolved intent can prompt more guessed repairs to pass.",condition="A score-seeking workflow permits semantic invention")
edge("unknown","fidelity","-","next implementation","Unknown or invented rules can lead to incorrect behaviour.","M-bounded / H-transfer",["S3"])
edge("drift","discrepancy","+","weeks","Comparison with actual behaviour reveals mismatches.",condition="Independent observation, suitable logs or other relevant evidence exists")
edge("discrepancy","learning","+","weeks","Owned discrepancies motivate validation and corrective updates.",condition="Owners have capacity and incentives to act")
edge("learning","drift","-","weeks to months","Updating design or behaviour reduces confirmed mismatch.")
edge("learning","knowledge","+","weeks","Retained validated lessons improve current shared knowledge.")
edge("drift","knowledge","-","weeks to months","Stale material reduces the amount of current reliable knowledge.")
edge("debt","reactive","+","months","Deferred work can increase change effort and avoidable failure work.")
edge("pressure","debt","+","weeks to months","Under pressure, work may be deferred rather than completed sustainably.")
edge("capacity","debt","-","months","Funded remediation retires deferred work.",condition="Capacity is actually used for validated remediation")
edge("capacity","demand","+","planning cycle","Visible capacity can cause leaders to accept more scope.",condition="Rebound demand is accepted rather than limiting work in progress")
edge("demand","inflow","+","same planning cycle","Accepted scope increases admissions.")
edge("inflow","wip","+","immediate","Admissions add to WIP when completion does not keep pace.")
edge("wip","waiting","+","days to weeks","More queued work increases waiting under constrained service capacity.")
edge("waiting","pressure","+","days to weeks","Longer waits increase delivery pressure.")
edge("completion","wip","-","immediate","Completion removes work from the defined workflow.")
edge("waiting","total","+","same change","Waiting anywhere inside the end-to-end boundary adds elapsed time.")
edge("early","total","-","across delivery","Early correction can avoid larger downstream corrective work.",condition="Avoided later work exceeds added early effort and remains on the critical path")
edge("gateburden","total","+","same change","Additional inspection or triage consumes end-to-end time.",condition="Burden is on the critical path and not offset by avoided work")

def loop(id,title,nodes,kind,reading,leverage,evidence):
    es=[];sign=1
    for a,b in zip(nodes,nodes[1:]+nodes[:1]):
        e=next(e for e in MODEL["edges"] if e["source"]==a and e["target"]==b)
        es.append(e["id"]);sign *= 1 if e["polarity"]=="+" else -1
    assert (sign==1)==(kind=="R")
    MODEL["loops"].append(dict(id=id,title=title,type=kind,nodes=nodes,edges=es,reading=reading,leverage=leverage,evidence=evidence))

loop("R1","Prevention and reinvestment",["check","early","knowledge","fidelity","escape","reactive","capacity"],"R","Better effective checking can reduce reactive work and release capacity for more prevention. It can also run in reverse.","Protect some freed capacity for authorship, rule tuning and debt reduction.","H as a whole; E03 has bounded experiment and related research support")
loop("R2","Firefighting and bypass",["escape","reactive","pressure","bypass","check","early","knowledge","fidelity"],"R","Escapes consume time, pressure rises, checks are bypassed and the defect-prevention system deteriorates.","Limit WIP and protect time to resolve findings; reward surfaced uncertainty.","H")
loop("R3","Approval and batching trap",["severity","gateburden","waiting","batch","cfr"],"R","Responding to failure with more burdensome approval can create larger batches and further failure.","Use fast, risk-sensitive checks and peer decisions close to the work; monitor queues.","R-related capability evidence; H for a particular local implementation")
loop("R4","Green but wrong",["repair","green","confidence","validation","unknown"],"R","Score-oriented semantic invention can produce apparent success, reduce independent challenge and perpetuate unresolved intent.","Escalate missing intent to its owner; require independent outcome examples, not just a higher score.","M for E27 and bounded repair failure; H for the organizational feedback loop")
loop("B1","Corrective risk control",["escape","cfr","severity","check","early","knowledge","fidelity"],"B","Relevant controls can counter deployment failures, provided they improve effective checking instead of merely adding burden.","Compare B1 against competing R3; calibrate precision and response, not strictness alone.","H")
loop("B2","Reality-based learning",["drift","discrepancy","learning"],"B","Observation exposes mismatch, and owned learning reduces it by changing the model or the implementation.","Maintain useful runtime evidence and independent review; conformance is not automatically the right objective.","H")

MODEL["assumptions"] = [
 "Edge polarity means same-direction (+) or opposite-direction (-) change, holding stated conditions comparable; it does not mean good/bad or a numerical coefficient.",
 "Delay categories are modelling assumptions, not estimated effect timings.",
 "A directed path to DORA is a testable causal hypothesis, not proof that buying or installing a named tool changes that metric.",
 "Checks influence only represented properties within their supported scope; unknown and unrepresented requirements remain outside the gate.",
 "Automation and human practice are complements; reported findings must be interpreted and resolved with valid intent.",
 "Local linter, score and documentation improvements cannot by themselves establish deployed runtime quality."
]

# v0.2: user-supplied definitions and explicit cross-layer defect propagation.
MODEL['version']='0.2'
MODEL['definition_status']={
 'software_quality':'The nine elements and meanings supplied by the user on 2026-10-28 are authoritative. Their supplied order defines Q1-Q9 in this revision.',
 'systemic':'The user supplied the full nine-element systemic-design definition on 2026-10-28: systems thinking plus participatory design, iterative learning and attention to power.',
 'validation':'Definition alignment is complete. Causal effects remain conditional and not calibrated; stakeholder participation is proposed, not claimed to have occurred.'
}
MODEL['quality']=[
 ['Q1','Functional correctness and completeness','Performs the required tasks accurately and covers relevant business rules and edge cases.','Independent acceptance outcomes; escaped functional defects; task completion.'],
 ['Q2','Reliability and resilience','Works consistently, handles failures gracefully, and recovers without losing or corrupting data.','SLO attainment, failure injection and verified data recovery.'],
 ['Q3','Usability and accessibility','Is understandable, efficient to use, and accessible to people with different abilities.','Observed task success, user errors and accessibility checks.'],
 ['Q4','Performance and efficiency','Responds quickly and uses computing resources appropriately.','Latency and resource use under a stated workload.'],
 ['Q5','Security and privacy','Prevents unauthorized access, protects information, and handles personal data appropriately.','Verified controls, access tests, privacy requirements and exposure.'],
 ['Q6','Maintainability','Is easy to understand, diagnose, fix, and change without introducing defects.','Diagnosis and change effort; change coupling; regression burden.'],
 ['Q7','Testability','Allows its behaviour to be verified through effective, repeatable tests.','Repeatable independent tests, controllability and observability.'],
 ['Q8','Compatibility and adaptability','Integrates with other systems and accommodates changes in platforms, requirements, or workload.','Consumer tests, migration and adaptation scenarios.'],
 ['Q9','Operability','Is straightforward to deploy, monitor, support, and troubleshoot in production.','Deployment, monitoring, support and recovery evidence.']
]
MODEL['quality_notes']=[
 'The user-supplied nine elements are authoritative; indicators are proposed operationalizations, not extra definitions.',
 'Quality requires measurable, context-dependent acceptance criteria and evidence from users, operators and maintainers.',
 'Artefact quality, product quality, quality in use and delivery performance are distinct but causally connected lenses, not independent silos or four lifecycle stages.',
 'Technical debt is deferred work and future change burden. Safety and compliance remain explicit domain constraints where applicable, without replacing the nine supplied elements.'
]
qmaps=[['Q1','Q2','Q6','Q7'],['Q1','Q2','Q6'],['Q1','Q6','Q7'],['Q1','Q3'],['Q6'],['Q1','Q7'],['Q1','Q2','Q6'],['Q1','Q7'],['Q1','Q6','Q7','Q8','Q9'],['Q6','Q8','Q9'],['Q6','Q8','Q9'],['Q6','Q8'],['Q1','Q7','Q8'],['Q5','Q6','Q8'],['Q1','Q6','Q8'],['Q1','Q6'],['Q2','Q5'],['Q1','Q6','Q9']]
for a,qs in zip(MODEL['inventory'],qmaps):a['quality']=qs
MODEL['systemic_elements']=[
 ['Frame and reframe the challenge','Treat upstream-to-downstream defect propagation as a candidate explanation; revisit boundary and assumptions.'],
 ['Understand people and perspectives','Involve authors, domain owners, users, implementers, testers and responders; their costs and priorities differ.'],
 ['Map the system','Show dependency branches, shared assumptions, feedback, power, incentives and delays across the four quality lenses.'],
 ['Explore underlying causes','Investigate why invalid assumptions survive, why tests share them and why pressure displaces correction.'],
 ['Define desirable futures','Agree useful, dependable outcomes and acceptable trade-offs, beyond green gates and deployment counts.'],
 ['Identify leverage points','Resolve intent early, diversify validation evidence, reveal change impact and protect correction capacity.'],
 ['Co-design connected interventions','Combine relevant checks with domain clarification, independent acceptance, traceability and runtime feedback.'],
 ['Experiment and learn','Observe propagation, escapes, exposure and rework; revise the model when evidence contradicts it.'],
 ['Enable sustained change','Assign owners, fund maintenance and learning, and govern exceptions and obsolete assumptions.']
]
for s in MODEL['sources']:
 if s['id']=='S9':
  s.update(title='User-supplied software quality and systemic-design definitions',url='https://github.com/fdurieux/fdurieux.github.io/blob/main/model/task-brief.md',scope='Full texts supplied on 2026-10-28 and preserved in the task brief; authoritative definitions')
MODEL['sources'].append({'id':'S11','title':'NASA: requirements management','url':'https://www.nasa.gov/reference/6-2-requirements-management/','scope':'Requirements dependencies, impact analysis and later change cost; engineering guidance, not a measured universal amplification factor'})

for n,l,k,d in [
 ('updef','Unresolved upstream artefact defects','stock','Invalid, ambiguous, missing or stale intent relevant to a product decision; not every style finding'),
 ('deriveddef','Defects in derived artefacts','variable','Wrong assumptions embodied in models, contracts, data definitions or decisions'),
 ('codedef','Implementation defects','stock','Incorrect or missing behaviour, data treatment or operational controls in the built product'),
 ('testdef','Inherited test-oracle errors','variable','Tests or reviewers using the same wrong assumption as the implementation'),
 ('detection','Effective independent detection','variable','Detection based on relevant evidence that does not merely repeat the disputed assumption'),
 ('reach','Dependent artefact reach','variable','Number of relevant downstream consumers and dependencies for an upstream decision'),
 ('affected','Affected downstream items','variable','Distinct artefacts, components or services carrying consequences of an upstream defect'),
 ('latency','Defect detection latency','variable','Time between introduction and reliable detection of a defect'),
 ('scope','Correction scope','variable','Artefacts, components, data and stakeholders requiring coordinated correction'),
 ('exposure','Operational exposure','variable','Relevant users, transactions or operations exposed to faulty behaviour over time'),
 ('harm','Adverse outcomes in use','outcome','Observed errors, disruption, loss or other user/operational consequences')
]:MODEL['nodes'].append(dict(id=n,label=l,kind=k,definition=d))

edge('updef','deriveddef','+','during derivation','Unresolved intent can be copied, elaborated or guessed into downstream models and contracts.','H',['S11'],'The disputed intent is consumed and not corrected; not a claim that every artefact defect propagates')
edge('deriveddef','codedef','+','implementation','Wrong represented intent can be implemented faithfully.','M-bounded / H-transfer',['S3'],'Bounded sequence-codegen evidence; other artefacts, human workflows and product dimensions require validation')
edge('updef','testdef','+','test design','Tests derived from the same wrong source can inherit its omissions or expected outcomes.','H',condition='Test derivation repeats the faulty premise without an independent oracle')
edge('testdef','detection','-','verification','Shared faulty expectations can hide implementation errors despite passing tests.','H',condition='The affected requirement is not independently challenged elsewhere')
edge('detection','escape','-','before release','Detection followed by containment or valid correction prevents relevant faults escaping.','H',condition='Findings are acted on and regression checks cover the correction')
edge('codedef','escape','+','after release','Implementation defects can escape into production when relevant checks miss them.','H',condition='Comparable detection and deployment scope')
edge('validation','updef','-','before implementation','Domain-author validation resolves wrong or missing intent before it is reused.','H',condition='Validation has sufficient domain knowledge and independent evidence')
edge('validation','detection','+','verification','Independent examples and reality checks can expose a common wrong premise.','H')
edge('early','updef','-','same change','Validated correction removes defects from the relevant upstream scope.','H')
edge('updef','affected','+','across derivations','Additional relevant upstream defects may affect more dependent items.','H',condition='Comparable dependency structure; count unique impacts without treating every copy as a new root cause')
edge('reach','affected','+','across derivations','One wrong decision can affect several dependent artefacts or components.','H',['S11'],'The dependency actually carries that decision; simple link count is insufficient')
edge('affected','scope','+','when corrected','More affected items can require a wider coordinated repair.','H',['S11'])
edge('latency','scope','+','days to months','Late detection can leave more dependencies, persisted data and commitments to unwind.','H',['S11'],'Consequences accumulate; delay does not inevitably increase scope')
edge('scope','reactive','+','during correction','Wider coordinated correction can consume more unplanned effort.','H',condition='Comparable repair automation, reversibility and component isolation')
edge('escape','harm','+','when exposed','Escaped defects can impair outcomes experienced by users or operators.','H',condition='The faulty behaviour is exercised and relevant consequences are not contained')
edge('exposure','harm','+','during use','More use of faulty behaviour can spread its consequences.','H',condition='Comparable defect severity, containment and user context')
edge('harm','learning','+','feedback cycles','Observed adverse outcomes can prompt investigation and validated learning.','H',condition='Outcomes are observable, attributed and acted upon; learning is not automatic')
edge('learning','updef','-','subsequent changes','Correcting source intent and dependent artefacts can remove the originating defect.','H',condition='Root cause is addressed; a local workaround alone does not resolve upstream intent')
edge('pressure','updef','+','subsequent authoring','Pressure can encourage unresolved assumptions and rushed source changes.','H',condition='Ownership, time and incentives permit incomplete or guessed intent to be handed on')
edge('testdef','latency','+','until independent evidence','Passing checks based on the wrong premise can postpone reliable detection.','H')
edge('validation','testdef','-','test design and review','Independent domain examples can correct faulty expected outcomes or omitted cases in tests.','H',condition='The independent evidence is valid and the test oracle is actually updated')
loop('R5','Cascade and rushed repair',['updef','deriveddef','codedef','escape','reactive','pressure'],'R','Unresolved intent propagates into implementation; escaped defects generate reactive work and pressure, which can encourage further unresolved intent.','Resolve the root assumption and all affected dependants; protect time for validation rather than just patching symptoms.','H as a loop; the model-to-code leg has bounded M support')
loop('B3','Outcome-led source correction',['updef','deriveddef','codedef','escape','harm','learning'],'B','Observed harm can drive validated learning that corrects the originating intent and interrupts recurrence.','Use independent user and operational evidence, accountable source owners and impact-aware correction.','H; depends on observation, attribution and action')
MODEL['cascade']={
 'interpretation':'The four layers are distinct analytical lenses with causal links; they do not form a mandatory linear or waterfall process.',
 'mechanisms':[
  ['Propagation','Wrong or missing meaning is inherited by a downstream decision or implementation.'],
  ['Spread','One root defect reaches several artefacts, components or teams through relevant dependencies.'],
  ['Concealment','Tests, code and models share a faulty premise, so agreement and green checks can delay discovery.'],
  ['Entrenchment','Further decisions, integration, persisted data and commitments expand the correction scope.'],
  ['Exposure','Use turns latent faults into consequences for users, operations and the business.']
 ],
 'limits':[
  'Propagation is conditional, not inevitable. Independent validation, domain expertise, containment and supported checks can stop or attenuate it.',
  'A defect need not become semantically more wrong at every stage. Its spread, exposure, correction scope or consequences can grow while the root error remains the same.',
  'Some downstream faults are introduced independently and cannot be attributed to upstream artefacts.',
  'No universal late-fix cost multiplier or monotonic quality decline is asserted.',
  'The full cascade and its DORA effects are hypotheses, not a measured production outcome of the tool inventory.'
 ],
 'measurements':[
  'Root defect ID, originating artefact/version and independent basis for calling it wrong.',
  'Downstream items actually affected, confirmed by impact analysis rather than link count alone.',
  'Where inherited errors were detected, corrected, contained or escaped; detection delay.',
  'Shared assumptions between code, tests and reviews; independently verified missed cases.',
  'Correction scope, rework effort, exposure and observed user/operational impact, separately from root-defect count.'
 ]
}
MODEL['revision_notes']=['v0.2 makes cross-layer propagation, branching into tests, amplification mechanisms and containment explicit in the visualization.','The nine quality elements now follow the user-supplied definition; Q-code meanings differ from v0.1, and inventory mappings were reconciled.']

# v0.3 (2026-10-29): the out-of-sample review (pumllint #205), the pre-registered degradation test
# (pumllint #208), and one source node for knowledge held only by people. Every new element carries
# its evidence label; the people-side edges are H until the departing-expert pilot runs.
MODEL['version']='0.3'
MODEL['date']='2026-10-29'
MODEL['evidence_pin']={'pumllint':'eab25fd','site':'bb78dff','review':'pumllint #205 (fd4a1f0)','degradation':'pumllint #208 (eab25fd)','previous':{'pumllint':'9d728c8','site':'9ba9b09'}}
MODEL['sources']+=[
 {'id':'S12','title':'pumllint: the systemic model reviewed against the recreation experiment','url':'https://github.com/fdurieux/pumllint/blob/eab25fd/recreate_experiment/legible-model-review-2026-10-28/REVIEW.md','scope':'Out-of-sample test of v0.2, artefact-to-product leg only; findings F1-F9; verdict fit for its stated purpose after specified corrections, for the cascade'},
 {'id':'S13','title':'pumllint: degrading the kit, pre-registered and graded','url':'https://github.com/fdurieux/pumllint/blob/eab25fd/recreate_experiment/degradation-2026-10-28/PREREGISTRATION.md','scope':'Fifteen defects planted in a specification kit, one layer at a time; six arms; six of fifteen reached the code, all six concealed by the arm\'s own suite; every outcome follows the kit\'s declared precedence'},
 {'id':'S14','title':'pumllint: knowledge transfer for a departing expert','url':'https://github.com/fdurieux/pumllint/blob/eab25fd/recreate_experiment/knowledge-transfer/DOMINIQUE-CASE.md','scope':'A plan, not a run: inventory from traces, elicitation, externalisation, a grading test with a denominator, a residual by name; the source of practices P10-P12'},
 {'id':'S15','title':'pumllint: what the kit does not reach','url':'https://github.com/fdurieux/pumllint/blob/eab25fd/recreate_experiment/results/coverage/UNREALISED.md','scope':'89 % of one real program\'s statements exercised by the kit\'s suite; 141 never reached; 61 with no caller, the measured size of the tacit remainder for that program'}
]

# Nodes: one source stock outside the artefact boundary, one exogenous source, one role split, two detection inputs.
for n,l,k,d in [
 ('tacit','Knowledge held only by people','stock','Intent, rules, exceptions and history that no artefact in the inventory states; held by people, in the strong sense (cannot be fully told) or the weak sense (sayable, unwritten). The network and succession are outside the model.'),
 ('depchange','Platform and dependency change','variable','A change in a platform, library or runtime that alters behaviour the code assumed, downstream of any intent'),
 ('explderived','Defects in explanatory artefacts','variable','Wrong assumptions embodied in models and prose that explain structure or intent without carrying executable behaviour'),
 ('diverse','Diverse independent derivation','variable','Independent re-derivations of the same artefact from the same inputs, whose divergences are triaged rather than scored away'),
 ('completeness','Completeness against an inventory','variable','Coverage of a requirement inventory by a derived artefact, measured separately from the precision of what it states')
]:MODEL['nodes'].append(dict(id=n,label=l,kind=k,definition=d))
for n in MODEL['nodes']:
 if n['id']=='deriveddef':
  n.update(label='Defects in behaviour-carrying derived artefacts',definition='Wrong assumptions embodied in contracts, decision tables, data definitions and executable examples: the artefacts a builder takes behaviour from')
 if n['id']=='fidelity':
  n['definition']+='; state whether it is measured against validated intent or against a reference implementation, which can disagree'

# Edges amended on evidence (review F1-F7, degradation D1-D2).
_E={e['id']:e for e in MODEL['edges']}
_E['E03']['condition']+='; the measured result covers sequence-codegen where the model was the consumer\'s only behavioural input'
_E['E32']['condition']='Sign holds against valid intent, not against a reference implementation: an invented clean refusal was better than the original\'s crash (M, one instance, S12 F5). The measured default when intent is missing is to record an assumption, not to invent (S13 D5)'
_E['E51'].update(moderator='Precedence rank of the layer that states the behaviour: the code takes each behaviour from the highest-ranked layer that states it (M, bounded: all fifteen degradation outcomes follow the kit\'s declared precedence, S13)',condition='Bounded evidence: sequence-codegen (S3) and a 3 500-line data program rebuilt cell for cell from a code-derived kit (S12); the artefact is consumed through its precedence rank')
_E['E51']['sources']=['S3','S12','S13']
_E['E58'].update(evidence='M-bounded',sources=['S12'],condition='One code-only revision of the kit took spec defects from 2 to 0 and non-identical artefacts from 22 to 11, all 11 by construction (S12 F7)')
del _E

# New edges E71-E79.
edge('tacit','updef','+','at authoring','What only a person knows is omitted from the written intent: the author did not know, or knew and did not write.','H',['S14'],'The person is not in the authoring loop, or the item is tacit in the strong sense')
edge('tacit','unknown','+','at derivation','What was never written arrives at the builder as an assumption; a kit stands in for a person it cannot ask.','H',['S14','S15'],'Assumption-register entries per artefact set are the measured shadow of this stock: 65, 50 and 30 from a code-derived kit, 117 and 94 from a generated wiki (S12 F5)')
edge('codedef','deriveddef','+','during derivation','Derivation treats implemented behaviour, defects included, as intent.','M-bounded',['S12'],'The derived artefact is calibrated to the implementation, not to independent intent: the timestamp unit and the export crash both reached code-derived artefacts (S12 F1)')
edge('depchange','codedef','+','on upgrade','A changed platform or dependency alters behaviour the code assumed.','M-bounded',['S12'],'No test pins the assumed behaviour: pandas 3.0.5 turned a millisecond stamp into seconds (S12 F1)')
edge('updef','explderived','+','during derivation','Unresolved intent is copied into models and prose as readily as into contracts.','H',['S11'],'The disputed intent is consumed and not corrected')
edge('explderived','codedef','+','implementation','An explanatory artefact carries behaviour only when it is the builder\'s sole behavioural input; otherwise its defects are attenuated by the behaviour-carrying layer.','M-bounded',['S12','S13'],'Attenuation measured: 12 diagram defects reached no rebuild, and defects planted only in diagrams reached nothing, because a higher-ranked layer stated the behaviour (S12 F3, S13 D1)')
edge('drift','confidence','+','immediate','A passing structural gate over a drifted artefact reads as assurance.','M-bounded',['S12'],'The gate scores the set against itself, never against the code: a Level 5, 100/100 set carried 25 claims the code contradicts (S12 F4)')
edge('diverse','detection','+','verification','Independent derivations disagree where a shared premise is wrong; the disagreement is the detection.','M-bounded',['S12'],'Divergences are triaged, not scored away: two rebuilders refused cleanly where the original crashes, and both recorded it (S12 F2)')
edge('completeness','detection','+','verification','Coverage of an inventory finds the omissions that precision cannot see.','M-bounded',['S12'],'Accurate but incomplete is the measured shape: claim precision 0.992 against strict coverage 0.245 (S12 F5)')

# Loops, hypotheses, stocks, practices, boundary, inventory, cascade.
for L in MODEL['loops']:
 if L['id']=='B2':L['evidence']='H; one instance M-bounded: a model set read against its code, adjudicated, spot-checked by execution (S12 F4)'
 if L['id']=='R4':L['evidence']='M for E27 and bounded repair; M-bounded for drift feeding confidence (E77); H for the organizational loop'
for h in MODEL['hypotheses']:
 if h[0]=='H3':h[4]+=' Measured once: trace reported 158/158 requirements verified while 33 specified statements were never executed (S12 F6).'
 if h[0]=='H4':h[4]+=' Measured once: a kit derived from code wrote the original\'s crash into the spec as a requirement, the rebuild reproduced it, and the suite scored it as correct (S12 F2).'
MODEL['stocks']+=[
 ['N','Unresolved or invented decisions','Assumption-register entries per artefact set','unstated intent adds; validation and externalisation remove','Measured on five rebuilds: 65, 50, 30 from a code-derived kit; 117, 94 from a generated wiki. A count of assumptions, not of defects.'],
 ['P','Knowledge held only by people','Items in a capture inventory: found, validated, externalised with a check, residual by name','elicitation and externalisation remove; departures and unrecorded decisions add','No percentage of knowledge captured: the population has no denominator. Its downstream shadow is N.']
]
MODEL['practices']+=[
 ['P9','Calibrate the oracle by mutation','Tests the tests before any rebuild, so detection is independent rather than shared-premise','Planted mutants must fail the suite; m1 failed 2 scenarios and m2 failed 11 before any recreation ran (M-bounded, S12 F7).'],
 ['P10','Elicit what only people know','Fills upstream omissions at their source and shrinks the assumption stock','Inventory from traces before any session; worked cases, counterexamples, exception walks, incident replay, quirk and orphan adjudication, with the successor present (H, S14).'],
 ['P11','Externalise into the normative home, with a check','Turns an elicited item into shared, current knowledge that drift can be measured against','Rules to decision tables, terms to the glossary, flows to models, reasons to decision records, procedures to runbooks; the register links provenance and is never a second source of truth (H, S14).'],
 ['P12','Validate every extracted claim with its owner','The independent channel that breaks the reverse path from code into derived artefacts (E73)','Observed, inferred and intended kept apart; a defect preserved for compatibility is a recorded decision with scope and an example; feeds E57 (H as a practice; the channel is M-bounded, S12 F2).']
]
MODEL['boundary']['inside'].append('knowledge held only by people, as a source stock; the network and succession stay outside')
MODEL['boundary']['moderators'].append('precedence rank among derived artefacts')
for a in MODEL['inventory']:
 if a['id']=='A01':
  a['limit']+=' Drift under a green gate is measured: one maintained set at Level 5, 100/100, with 25 claims the code contradicts (S12 F4).'
  a['evidence']+='; M-bounded for drift under a green gate'
  a['source']+=['S12']
 if a['id']=='A08':
  a['limit']+=' Measured: 13 tables with 0 gaps, 0 overlaps and 1 untyped output, which was the defect; output typing caught what gap analysis passed (S12 F6).'
  a['source']+=['S12']
 if a['id']=='A09':
  a['limit']+=' Measured: trace reported 158/158 verified while 33 specified statements were never executed; clause-level coverage is the gap. Deleting a requirement\'s only scenario trips the trace gate; deleting the rule from a requirement that keeps a scenario does not (S12 F6, S13).'
  a['source']+=['S12','S13']
MODEL['inventory']+=[
 {'id':'A19','artefact':'Vocabulary (glossary)','state':'open','tools':'No gate in the inventory; the experiment\'s glossary check (terms used repeatedly and defined nowhere) is a candidate','mechanism':'A defined term is one identity across artefacts; an undefined recurring term is a decision nobody wrote.','quality':['Q1','Q6'],'route':'Fewer silent disagreements between artefacts may reduce rework and omitted change scope: CLT and CFR, indirect.','limit':'Measured once: 42 of 60 recurring kit terms had no definition before wave 2 (S12 F8). A definition is not agreement on meaning.','evidence':'I + H; M-bounded for the gap','source':['S12']},
 {'id':'A20','artefact':'Property-based invariants','state':'covered','tools':'Covered by a practice: hypothesis-style property tests on the specified invariants, run against the original and each rebuild','mechanism':'Properties exercise behaviour no example scenario reaches, independently of the examples the kit states.','quality':['Q1','Q2','Q7'],'route':'Detection of behaviour the scenario suite misses: CFR and DRR, indirect.','limit':'Measured once: six intrinsic properties at 100 examples each and one differential property, 7/7, on one program (S12). A property holds for the cases generated, not for all.','evidence':'M-bounded on one program; H elsewhere','source':['S12']}
]
MODEL['cascade']['mechanisms']+=[
 ['Reverse derivation','Implemented behaviour, defects included, is read back into artefacts derived from the code; an oracle calibrated on the same code passes the inheritance as correct.'],
 ['Precedence','What propagates is decided by the highest-ranked layer that states the behaviour; a defect in a lower layer loses to a correct higher one, and a wrong value in the highest wins.']
]
MODEL['cascade']['limits'].append('Attenuation holds only while a higher-ranked layer still states the behaviour correctly; a defect planted consistently in every layer propagates and is concealed by the derived suite.')
MODEL['cascade']['measurements']+=[
 'Assumption-register entries per artefact set, as the count of what the inputs did not state.',
 'Per planted or found defect: propagated, attenuated, or recorded as an assumption; and which gate, if any, saw it.'
]
MODEL['revision_notes'].append('v0.3 applies the out-of-sample review (S12, F1-F7) and the degradation test (S13, D1-D2): a reverse edge from code into derived artefacts, a dependency-change source, derived artefacts split by role with precedence as the moderator, drift feeding confidence, an indicator for the unknown stock, diverse derivation and completeness as detection inputs, oracle calibration as a practice; and one extension, a source stock for knowledge held only by people with two edges and three practices, all H until the departing-expert pilot runs. Two inventory rows added (A19, A20). No magnitudes; no edge from capture to delivery metrics.')
