---
name: create-framework
description: Run CREATE from raw idea to validated growth.
version: 2.0.0
author: Pavel Nasuta, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [product, strategy, ai, methodology, mvp, growth]
    related_skills: []
---

# CREATE Framework Skill

CREATE is a context-preserving product methodology for taking any product, service, internal tool, content business, AI agent, or public-sector digital service from raw idea to validated growth. It is built for agent workflows: every stage produces artifacts that become explicit inputs for the next stage, so the agent never has to rely on memory or vibes.

## When to Use

Use this skill when the user wants to:

- develop a product or service from a raw idea;
- turn scattered product notes into a coherent strategy;
- build MVP documentation, GTM, pricing, metrics, or growth loops;
- evaluate monetization, market, legal feasibility, and user demand;
- coordinate multiple agents around one product-development method;
- generate a reusable product dossier that survives long sessions and handoffs.

Don't use this skill for one-off copywriting, quick UI tweaks, or pure technical debugging unless the task is part of a larger product-development cycle.

## Core Rule: Preserve the Context Thread

Never treat a CREATE stage as a standalone prompt. Each stage must consume the artifacts from previous stages and produce named artifacts for future stages.

The correct chain is:

```text
C Context → R Research → Legal Gate when needed → E Elaboration → A Assembly → T Tuning → E Expansion
```

If an upstream artifact is missing, either ask for it or generate it first. Do not skip directly to MVP, pricing, GTM, or growth without the context that grounds them.

## Required Project Folder

Create a project folder with this structure unless the user gives another format:

```text
CREATE_<product>/
├── 00_Project_Brief.md
├── 01_Context.md
├── 02_Research.md
├── 03_Legal_Gate.md
├── 04_Elaboration.md
├── 05_Assembly.md
├── 06_Tuning.md
├── 07_Expansion.md
├── 08_Decisions_Log.md
├── 09_Source_Index.md
└── artifacts/
```

Every file should be readable as a standalone artifact. The final document is the concatenation of these files plus an executive summary.

## Procedure

### 0. Intake

Collect enough context to start, without over-interviewing the user:

- raw idea;
- target user/customer;
- business model or monetization intent if known;
- geography/jurisdiction if relevant;
- constraints: budget, team, timeline, data, legal, tech stack;
- what exists already: research, notes, product, metrics, interviews.

Completion criterion: `00_Project_Brief.md` contains the idea, assumptions, known facts, open questions, and success definition.

### 1. C — Context

Read `references/c-context.md`. Produce Vision, Mission, Core Values with operational rules, and Emotional Problem.

Completion criterion: every later stage can quote the emotional core and values when making tradeoffs.

### 2. R — Research

Read `references/r-research.md`. Produce market/trend analysis, SWOT/PESTEL/Porter where useful, competitor analysis, user research plan/synthesis, pain points, CJM, archetypes, and source index.

Completion criterion: factual claims are sourced or explicitly marked `(hypothesis, not yet verified)`.

### 3. Legal Gate — Conditional but Mandatory for Risky Products

Read `references/legal-gate.md` whenever the product touches content/data monetization, personal data, health, finance, children, public-sector data, user-generated content, IP, employment, regulated industries, payments, or licenses.

Completion criterion: MVP scope includes only legally acceptable flows, and unresolved legal risks are visible as blockers or assumptions.

### 4. E — Elaboration

Read `references/e-elaboration.md`. Produce JTBD, solution hypotheses, prototype options, AARRR model, MVP concept, and validation metrics.

Completion criterion: MVP tests one core value hypothesis for one primary JTBD.

### 5. A — Assembly

Read `references/a-assembly.md`. Produce content/data generation plan, API/system scenario, UI components, build plan, business goals, metrics, and instrumentation plan.

Completion criterion: a builder or no-code implementer can start without asking what the MVP is supposed to do.

### 6. T — Tuning

Read `references/t-tuning.md`. Produce funnel analysis, feedback analysis, bottlenecks, A/B testing plan, and prioritized iteration backlog after real or simulated MVP data.

Completion criterion: every improvement hypothesis references a metric, feedback quote, or observed behavior.

### 7. E — Expansion

Read `references/e-expansion.md`. Produce LTV/CAC plan, monetization strategy, growth loops, automated iteration system, and scale risks.

Completion criterion: growth recommendations do not contradict Core Values, legal constraints, or Tuning evidence.

## Output Standards

For every artifact, include:

- **What we know** — verified facts and sources;
- **What we assume** — assumptions to test;
- **What this implies** — decisions or constraints;
- **What to do next** — concrete next actions;
- **Open risks** — unresolved blockers.

Prefer tables for comparisons, matrices, pricing tiers, and risk registers. Prefer short paragraphs for narrative sections.

## Evidence Rules

- Use web/search tools, documents, data exports, interviews, or user-provided facts for factual claims.
- Mark unsourced market statements as hypotheses.
- Keep a `09_Source_Index.md` with source, claim supported, date accessed, and confidence.
- Do not invent legal certainty; use `(requires legal review)` where needed.

## Agent Coordination

For multi-agent workflows:

- one agent owns the master dossier;
- research agents write source-backed notes only;
- synthesis agents must cite which artifact they used;
- builder agents must not change strategic assumptions silently;
- all handoffs append to `08_Decisions_Log.md`.

## Verification

Before final delivery, run the project validator if available:

```bash
python scripts/validate_create_project.py CREATE_<product>/
```

Then verify manually:

- all seven stages exist;
- legal gate is present or explicitly marked not applicable;
- no factual claim lacks source/hypothesis status;
- MVP traces back to a JTBD and emotional problem;
- metrics trace back to AARRR and business goals;
- expansion uses tuning evidence, not generic growth advice.
