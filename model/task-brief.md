# Agent brief: review the Legible systemic impact model

Version: 28 October 2026. Review target: model v0.2.

## Assignment and authority

Independently review the supplied findings, PDF, causal-model JSON and visualization against the user's consolidated requirements below. Decide whether they satisfy the request, identify substantive errors or omissions, and propose precise corrections. Evaluate the model; do not merely summarize or endorse it.

The original task was to **create the model**. The current task is to prepare it for **independent review**. This brief preserves both. Requirements R01–R10 consolidate the user's requests; the review procedure, evidence labels, IDs, measurement suggestions and file organization are assistant-proposed ways to carry them out, and remain open to challenge.

The user-supplied definitions in Appendices A and B are authoritative. They contain the complete definition texts supplied in this conversation, not a reconstructed transcript of unseen turns. The supplied definitions supersede provisional interpretations in model v0.1. Do not substitute another quality taxonomy or equate systemic design with causal-loop mapping alone.

## Original request

> I want you to create a systemic model of the impact of using tools & practices as listed on fdurieux.github.io (section: "artefact by artefact: tools, practices, gaps") on software quality & DORA metrics.
>
> Software quality as defined in the conversation "Software quality elements".
>
> Systemic as defined in the conversation "Systemic design elements".

## Consolidated requirements

| ID | Requirement | What a reviewer should be able to establish |
| --- | --- | --- |
| R01 | Scope the tools, practices and gaps in the named site section. | Every inventory row is represented; tool capabilities, practices, planned work and open gaps are distinguishable. Source revision and date are recorded. |
| R02 | Explain impacts on software quality using Appendix A. | All nine elements retain their meanings. Measurable acceptance criteria and context-dependent priorities are considered. No gate score is treated as proof of software quality. |
| R03 | Explain impacts on DORA delivery performance. | Each claimed path uses a defined metric, relevant event boundary and conditions; quality outcomes remain visible beyond DORA. |
| R04 | Use systemic design as defined in Appendix B. | All nine elements are addressed, including perspectives, power, participation, connected interventions, learning and ownership. Proposed participation is distinguished from work actually conducted. |
| R05 | Preserve four distinct but connected layers. | Artefact quality, product quality, quality in use and delivery performance have clear meanings and explicit links. They are analytical layers, not an assumption of a compulsory sequential lifecycle. |
| R06 | Investigate how artefact defects affect the delivered product. | The model traces inheritance of wrong, missing or stale meaning through dependent artefacts into implementation and tests, with conditions and alternative causes. |
| R07 | Investigate whether downstream effects become worse. | It distinguishes propagation, spread, shared faulty assumptions, delayed discovery, correction scope and operational exposure. It examines amplification and attenuation without assuming inevitable deterioration or an unsupported multiplier. |
| R08 | Make the cascade visible in the systemic visualization. | A reader can follow cross-layer effects, branches, amplifiers, interruption points and feedback. These relationships must appear in the visualization, not only in prose. |
| R09 | Provide a reusable Markdown instruction document containing the supplied definitions. | The original task and both definition texts are included, with a coherent agent assignment. |
| R10 | Compile enough information for an agent to review the findings and document against the instructions. | The review target, source evidence, claim locations, assumptions, limitations and review procedure are available together. |

### The user's cascade clarification

The user noted the four layers in the PDF and asked whether lack of quality in artefacts would cascade into the delivered product and become worse farther downstream. The user then stated:

> If this is the case, I would expect to see this in the visualisation of the systemic model

Treat this as a requirement to investigate and visualize the relationship, not as authorization to presume that every upstream defect inevitably amplifies. The review should assess whether the evidence supports the model's interpretation of this concern.

## Source inputs and boundaries

1. Inventory: [fdurieux.github.io](https://fdurieux.github.io/), section **“Artefact by artefact: tools, practices, gaps.”** Pinned site source: `fdurieux/fdurieux.github.io` commit `9ba9b09cb548a5d496e297cecc57d4f576647292`; inventory snapshot dated 26 October 2026.
2. Supporting evidence: `fdurieux/pumllint` commit `9d728c8c17e15d288022a47abe5d2293ecc0ba0e`, particularly `EVIDENCE.md` and `README.md`.
3. Software quality and systemic design: the user-supplied texts below.
4. Delivery metrics: [DORA's official definitions](https://dora.dev/guides/dora-metrics/), as accessed on 28 October 2026. The model uses deployment frequency, change lead time, change fail rate, failed deployment recovery time and deployment rework rate.
5. Supporting primary guidance: official DORA capability pages and NASA requirements-management guidance. Scope and URLs are in the source register and research notes.

The pinned snapshots define the review baseline. If checking newer material, record the new revision and distinguish subsequent changes from errors in this baseline. The listed third-party tools have not all received an independent current capability audit.

## Model to review

The handoff contains a 17-page PDF, its JSON model, an exported cascade figure and the source used to generate them. Version 0.2 contains 18 inventory rows, nine quality elements, five delivery metrics, 46 graph nodes, 70 signed edges and eight feedback loops. Counts establish coverage and structural consistency only; they do not establish causal validity.

| Location | Content |
| --- | --- |
| PDF pp. 1–2 | Framing, four layers and user-defined quality elements |
| PDF p. 3 / cascade PNG | Cross-layer defect cascade, shared faulty test assumptions and interruption paths |
| PDF p. 4 | DORA definitions, conditions and measurement boundaries |
| PDF pp. 5–8 | All 18 inventory pathways |
| PDF pp. 9–11 | Feedback loops, amplification and outcome-led correction |
| PDF p. 12 | Candidate stocks, delays and bottlenecks |
| PDF pp. 13–14 | Actors, power, interventions and proposed participation |
| PDF pp. 15–16 | Hypotheses, measurement and bounded evidence |
| PDF p. 17 | Sources and maintenance |
| JSON | Node and edge IDs, signs, conditions, delays, sources, inventory mappings and all nine systemic-design elements |

The figures are selected views of the JSON, not a rendering of every edge. Assess whether simplifications remain faithful. The four-layer cascade must coexist with feedback, concurrency and independent downstream sources of defects.

## Independent review procedure

1. Read this brief and both definition appendices before reading the model's conclusions. Establish the user requirements separately from the assistant's choices.
2. Check the pinned inventory against all 18 model rows, including listed practices, coverage limits, planned work and open gaps. Do not interpret “covered” as complete semantic validation.
3. Review the PDF and cascade figure against the JSON. Inspect signs, loop closure and polarity, direction, delay, units, conditions, omitted paths and possible double-counting. Ask whether each relationship is intelligible and falsifiable.
4. Audit the evidence. Follow the major claims in `review/claim-register.json` to their original sources. Separate measured repository results, related research or guidance, inventory descriptions and modelling hypotheses. Check denominators, comparisons, scope and competing explanations.
5. Challenge the cascade specifically: how does an error survive each boundary; when do tests inherit it; what amplifies impact; what stops it; how can one root defect affect many items without being counted as many independent root causes? Examine whether quality in use and delivery performance are adequately connected without being conflated.
6. Check all nine software-quality elements and all nine systemic-design elements. Identify weakly represented dimensions rather than inventing a tool benefit for each cell. Inspect who defines correctness, who can challenge a gate, who bears added work, and who owns learning and correction.
7. Review each DORA path against the official definition. Keep commit-to-production lead time separate from discovery-to-value time, recovery from failed deployments separate from general incident recovery, and deployment rework separate from all development rework. Consider denominators, incident/change mix and the possibility of a metric improving while user outcomes worsen.
8. Assess the proposed learning plan: measurable acceptance criteria, leading and lagging observations, comparison strategy, attribution limits, conditions that would falsify claims, iteration and sustained ownership.
9. Report prioritized findings with precise locations, evidence, consequences and proposed corrections. State what remains unresolved or could not be checked. Avoid treating successful file generation or graph checks as an independent substantive review.

## Suggested review output

Produce `review.md` with an overall verdict (fit for the stated purpose, fit after specified corrections, or substantial revision needed), prioritized findings, coverage against R01–R10, and open questions. A finding should contain:

- Severity and the requirement affected.
- Exact file and page, section, artefact ID, node, edge or loop.
- The issue and supporting source evidence, including uncertainty or contradictory evidence.
- Why it changes the interpretation or usefulness of the model.
- A concrete proposed correction and how to verify it.

Use `review/review-matrix-template.csv` to record coverage if useful. Its verdict cells are intentionally blank. Distinguish documentation errors from causal-model concerns, evidence limitations and unperformed empirical validation. A review may accept a properly labelled hypothesis without treating it as proven.

## Assistant choices and limitations to challenge

- The model is qualitative. It has no calibrated coefficients, simulation, validated universal amplification curve or tool-specific DORA effect estimates.
- Inventory states describe the dated site baseline. Site and programme roadmap disagree on the classification of diagram-to-code drift; both imply unavailable capability in this model.
- Repository experiments concern sequence diagrams and generated code tested against specific suites. They do not validate all artefact classes, all quality elements or production DORA outcomes.
- Related DORA research and NASA engineering guidance do not establish the causal effect of this particular inventory or a universal late-fix cost multiplier.
- Participation, stakeholder priorities, power analysis, interventions and pilot design are proposals. No stakeholder workshops, interviews or organizational intervention study were performed for this document.
- The PDF summarizes evidence selectively. The handoff includes additional source results, notably the with-author repair arm, so the reviewer can assess whether the PDF's evidence discussion needs expansion.
- The review should examine overlap between conceptual variables such as unresolved intent, upstream defects and the stock U; generic edge conditions may require more specificity. A structurally closed loop can still be a weak causal explanation.

The detailed claim register and limitations document expand these points. They are starting points, not a pre-approved review verdict.

---

## Appendix A — “Software quality elements”

*Source: full definition text supplied by the user on 28 October 2026. Reproduced verbatim below.*

**Software quality is how well software meets users’ needs, behaves under real conditions, and can be maintained over time.** It includes several elements:

| Element                                     | What it means                                                                                    |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Functional correctness and completeness** | Performs the required tasks accurately and covers relevant business rules and edge cases.        |
| **Reliability and resilience**              | Works consistently, handles failures gracefully, and recovers without losing or corrupting data. |
| **Usability and accessibility**             | Is understandable, efficient to use, and accessible to people with different abilities.          |
| **Performance and efficiency**              | Responds quickly and uses computing resources appropriately.                                     |
| **Security and privacy**                    | Prevents unauthorized access, protects information, and handles personal data appropriately.     |
| **Maintainability**                         | Is easy to understand, diagnose, fix, and change without introducing defects.                    |
| **Testability**                             | Allows its behaviour to be verified through effective, repeatable tests.                         |
| **Compatibility and adaptability**          | Integrates with other systems and accommodates changes in platforms, requirements, or workload.  |
| **Operability**                             | Is straightforward to deploy, monitor, support, and troubleshoot in production.                  |

These elements need **measurable acceptance criteria**. “Fast,” for example, could mean “95% of requests complete within two seconds under the expected peak load.”

Their relative importance depends on the product: a payment system prioritizes correctness, security, and reliability; an interactive design tool may place greater weight on usability and responsiveness. Clean code, testing, and sound architecture help achieve quality, but the ultimate evidence is how the software performs for users and the people responsible for running and changing it.

## Appendix B — “Systemic design elements”

*Source: full definition text supplied by the user on 28 October 2026. Reproduced verbatim below.*

A **systemic design approach combines systems thinking with participatory design** to understand and change complex situations involving people, organisations, policies, technologies and the environment.

There is no single standard process, but the typical elements are:

| Element                                   | What it involves                                                                                                                                            |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Frame and reframe the challenge**    | Explore what the problem is, whose perspective defines it, and where to draw the boundaries of the system. Revisit assumptions as understanding develops.   |
| **2. Understand people and perspectives** | Investigate lived experiences, needs and behaviours. Include affected communities, decision-makers and voices that are often overlooked.                    |
| **3. Map the system**                     | Identify actors, relationships, resources, incentives and rules. Examine feedback loops, dependencies, power dynamics and delays.                           |
| **4. Explore underlying causes**          | Look at the structures, beliefs and recurring patterns that sustain the situation. Understand why previous efforts have succeeded or failed.                |
| **5. Define desirable futures**           | Build a shared sense of what a better system would achieve, for whom, and how progress would be recognised. Make competing values and trade-offs explicit.  |
| **6. Identify leverage points**           | Find places where intervention could influence wider system behaviour—for example, information flows, incentives, relationships, rules or goals.            |
| **7. Co-design connected interventions**  | Develop a portfolio of complementary changes with relevant actors. These might span services, policy, infrastructure, organisational practices and culture. |
| **8. Experiment and learn**               | Prototype ideas, test assumptions and observe effects—including unintended consequences. Adapt interventions as evidence emerges.                           |
| **9. Enable sustained change**            | Establish ownership, governance, resources and learning mechanisms so that change can continue and evolve.                                                  |

**The process is iterative:** mapping informs experiments, experiments reveal new system dynamics, and those insights can change both the proposed interventions and the original framing.

Participation, attention to power, and continuous learning run through the whole approach.
