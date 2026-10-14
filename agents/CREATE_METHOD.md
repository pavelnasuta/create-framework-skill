# CREATE Method — Universal Agent Playbook

Use this file with any agent system, even if it does not support formal skill folders.

## Mission

Guide a user from a raw idea to a validated product strategy without losing context. Preserve a chain of artifacts. Do not jump ahead to solutions before context, research, and constraints are clear.

## Operating modes

### Accumulation mode

Use when the user is still giving raw notes, interview snippets, files, or context. Collect and label facts; do not synthesize a final strategy yet.

### Build mode

Use when the user says to assemble, form, or produce the document. Run the CREATE stages, fill missing artifacts, and produce a structured dossier.

### Iteration mode

Use after the first dossier exists. Update only affected artifacts, preserve decision history, mark superseded assumptions, and rerun validation.

## Stage protocol

For every stage, follow this loop:

1. **Inputs** — list artifacts used.
2. **Reasoning frame** — explain what the stage decides.
3. **Artifact** — produce the named output.
4. **Decision impact** — state what changed for the product.
5. **Open questions** — record missing evidence.
6. **Handoff** — write what the next stage receives.

## CREATE stages

### C — Context

Artifacts: Vision, Mission, Core Values, Emotional Problem.

Anti-pattern: writing features before the emotional problem is clear.

### R — Research

Artifacts: Market and trend analysis, competitor matrix, user research plan/synthesis, CJM, archetypes, source index.

Anti-pattern: using generic market claims without sources.

### Legal Gate

Artifacts: legal/regulatory surface map, rights/data inventory, allowed/restricted/blocked use-case matrix, MVP guardrails.

Anti-pattern: treating legal risk as a note instead of a product constraint.

### E — Elaboration

Artifacts: JTBD, solution hypotheses, prototype scenarios, AARRR model, MVP concept.

Anti-pattern: designing all features instead of testing one core JTBD.

### A — Assembly

Artifacts: data/content generation plan, API/system map, UI/component plan, business metrics, build roadmap.

Anti-pattern: implementation plan not tied to metrics.

### T — Tuning

Artifacts: funnel diagnosis, feedback synthesis, bottleneck hypotheses, A/B test plan, iteration backlog.

Anti-pattern: optimizing based on opinions without observed behavior.

### E — Expansion

Artifacts: LTV/CAC strategy, monetization model, growth loops, automated iteration system, scale guardrails.

Anti-pattern: scaling before retention/activation evidence exists.

## Final dossier structure

```markdown
# [Product] — CREATE Dossier
## Executive Summary
## C — Context
## R — Research
## Legal Gate
## E — Elaboration
## A — Assembly
## T — Tuning
## E — Expansion
## Decision Log
## Source Index
## Open Questions
```

## Verification checklist

- [ ] Every stage has explicit inputs and outputs.
- [ ] Every factual claim is sourced or marked as a hypothesis.
- [ ] MVP traces to a JTBD, emotional problem, and value hypothesis.
- [ ] Legal/risk guardrails are reflected in product scope.
- [ ] Metrics exist before tuning.
- [ ] Expansion uses Tuning evidence.
- [ ] Decision log records major tradeoffs.
