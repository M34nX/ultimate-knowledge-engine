# 50-Agent Work and Verification Architecture

**Status: proposed design only. No agent runtime is implemented by this document.**

This design specifies 50 specialist roles for UKE: 40 delivery agents and 10 independent verification agents. It is a role and governance specification, not evidence that 50 agents currently run, operate in parallel, or have repository access.

## Goals

- Increase throughput across research, content production, engineering, and maintenance without weakening quality.
- Keep factual claims traceable to reliable sources and distinguish Draft, Reviewed, Verified, and Outdated content.
- Separate creation from verification so an author cannot approve their own work.
- Make decisions auditable, reproducible, and safe to rerun.

## Topology

A future orchestrator decomposes a task into bounded work packages, assigns them to delivery roles, gathers artifacts, and submits each relevant change to the verification roles. Parallel execution is allowed only for independent tasks and only when the eventual runtime supports it. Each work package has one designated owner per file to avoid conflicting edits.

## 40 delivery agents

| ID | Role | Primary responsibility |
|---|---|---|
| W01 | Project planner | Break goals into scoped tasks, dependencies, and acceptance criteria. |
| W02 | Requirements analyst | Turn learner and maintainer needs into testable requirements. |
| W03 | Domain researcher | Research technical subjects using primary sources first. |
| W04 | Source curator | Select sources and record provenance and reuse constraints. |
| W05 | Knowledge architect | Design concept boundaries, stable IDs, and relationships. |
| W06 | Taxonomy designer | Maintain domain, topic, and prerequisite classifications. |
| W07 | Terminology editor | Maintain consistent technical terminology and definitions. |
| W08 | Curriculum designer | Design learning paths, outcomes, and prerequisite sequences. |
| W09 | Lesson author | Draft structured lessons with examples and learning objectives. |
| W10 | Concept author | Draft reusable encyclopedia and dictionary concepts. |
| W11 | Exercise designer | Create practice tasks with clear expected outcomes. |
| W12 | Assessment designer | Create quizzes and rubrics aligned to learning objectives. |
| W13 | Capstone designer | Design applied projects with milestones and acceptance criteria. |
| W14 | Code-example author | Produce minimal, reproducible examples for supported toolchains. |
| W15 | Persian translator | Translate approved source material into Persian without changing meaning. |
| W16 | English editor | Improve clarity and consistency of English content. |
| W17 | Localization specialist | Handle locale conventions, RTL presentation, and localized navigation. |
| W18 | Visual learning designer | Specify diagrams and accessible text alternatives. |
| W19 | Metadata maintainer | Maintain frontmatter, IDs, tags, and lifecycle metadata. |
| W20 | Citation curator | Attach claim-level citations and verify bibliographic details. |
| W21 | Schema engineer | Evolve JSON Schema contracts with compatibility notes. |
| W22 | Validator engineer | Implement deterministic structural and metadata checks. |
| W23 | Markdown/link engineer | Maintain Markdown linting, relative links, and anchor checks. |
| W24 | Knowledge-graph engineer | Maintain graph nodes, edge types, and referential integrity. |
| W25 | Search/index engineer | Design reproducible indexing and retrieval metadata. |
| W26 | Frontend engineer | Build learner-facing interface components when the app exists. |
| W27 | Backend/API engineer | Design and implement service APIs and application logic. |
| W28 | Documentation-site engineer | Maintain the generated documentation site and navigation. |
| W29 | Accessibility engineer | Implement accessible semantics, keyboard support, and RTL usability. |
| W30 | UX researcher | Evaluate learner journeys and identify usability problems. |
| W31 | Test engineer | Design unit, integration, regression, and content tests. |
| W32 | CI/build engineer | Maintain deterministic CI, build steps, and quality gates. |
| W33 | Release engineer | Prepare release notes, versioning, and release checklists. |
| W34 | Dependency maintainer | Track dependency updates, compatibility, and lockfile hygiene. |
| W35 | Defensive security engineer | Threat-model the system and implement defensive controls. |
| W36 | Privacy engineer | Minimize personal data and document retention and consent boundaries. |
| W37 | Performance engineer | Measure and improve build, search, and application performance. |
| W38 | Observability maintainer | Define useful logs, metrics, and failure reporting without secrets. |
| W39 | Content maintenance analyst | Detect stale, duplicated, incomplete, or version-sensitive material. |
| W40 | Integration engineer | Coordinate interfaces and integration across work packages. |

## 10 independent verification agents

These roles review evidence and artifacts produced by delivery agents. They must not simply repeat the author's conclusions.

| ID | Verification focus | Required checks |
|---|---|---|
| V01 | Source and factual accuracy | Verify important claims against authoritative, current sources; flag unsupported claims. |
| V02 | Independent fact-check | Re-check claims independently and identify contradictions or fabricated references. |
| V03 | Logic and consistency | Check reasoning, definitions, prerequisites, examples, and conclusions for contradictions. |
| V04 | Data and calculation integrity | Recalculate numerical examples and validate tables, units, and transformations. |
| V05 | Code and test correctness | Run relevant tests where available; inspect reproducibility, edge cases, and failure handling. |
| V06 | Structure and build integrity | Check schemas, metadata, IDs, graph references, Markdown links, and build output. |
| V07 | Translation and terminology | Compare meaning across locales, terminology, code identifiers, and RTL-sensitive content. |
| V08 | Security and privacy | Check secrets exposure, unsafe execution, permissions, dependency risks, and data minimization. |
| V09 | Accessibility and freshness | Review accessibility, version scope, source freshness, and compatibility claims. |
| V10 | Final adjudicator | Resolve reviewer disagreements from evidence; assign the final status and explain blockers. |

## Required work-package contract

Every assigned task must produce:

1. **Scope:** objective, paths in scope, paths out of scope, and dependencies.
2. **Claims:** factual or technical claims introduced or changed.
3. **Evidence:** source URLs or repository paths, version/date where relevant, and the exact claim supported.
4. **Artifacts:** changed paths, generated outputs, and reproducible commands.
5. **Tests:** checks run, results, environment, and checks not run.
6. **Risks:** known limitations, security/privacy concerns, and unresolved questions.
7. **Status proposal:** Draft, Reviewed, Verified, or Outdated, with reasons.

A reviewer must report PASS, FAIL, or NEEDS_HUMAN_REVIEW, cite concrete evidence, and distinguish a confirmed defect from uncertainty. A missing test is not a passing test. A source link alone does not prove that a claim is supported.

## Approval and release gates

- Authors cannot approve their own work. Verification assignments must be separate from delivery assignments.
- Any FAIL from V01–V09 blocks Verified status until the issue is fixed and rechecked.
- A factual claim with unresolved evidence remains Draft or Needs review; reviewer vote counts cannot turn it into truth.
- Critical security or privacy findings block merge and release.
- V10 may resolve disagreements only by recording evidence and rationale. It cannot waive a critical security issue or invent missing evidence.
- Automated CI checks and human review are separate gates. A green structural validator does not establish factual correctness.
- Changes to main, release publication, destructive actions, or external side effects require the repository's normal maintainer approval.
- Final reports record role IDs, inputs, changed paths, test evidence, reviewer decisions, and unresolved risks. Secrets and personal data must never appear in logs.

## Suggested execution sequence

1. The orchestrator scopes the task and assigns one owner per file or work package.
2. Delivery agents work on isolated branches or non-overlapping paths.
3. The integration agent assembles the proposed change.
4. CI runs deterministic repository checks.
5. V01–V09 review the relevant evidence independently.
6. Delivery agents address findings and rerun affected checks.
7. V10 records the final decision.
8. A maintainer reviews and merges the pull request; release status changes only after release gates pass.

## Current implementation boundary

The repository currently contains structural validation tooling and GitHub Actions for that tooling. This document does not add an agent runtime, model gateway, tool permissions, parallel worker execution, or automated reviewer agents. Those require a separately designed and tested implementation, provider configuration, secure credential handling, budget limits, observability, and explicit maintainer approval.
