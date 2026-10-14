# Legal Gate Reference

The Legal Gate prevents the agent from designing an MVP that cannot legally operate. Run it before Elaboration whenever a product touches rights, personal data, regulated industries, payments, public-sector information, minors, health, finance, or content/data monetization.

This is not legal advice. It is a structured risk-discovery stage that prepares questions and constraints for qualified legal review.

## Inputs

- Context artifacts: Vision, Mission, Core Values, Emotional Problem.
- Research artifacts: users, market, competitors, intended geography.
- Product intent: what is monetized, what data/content is processed, who pays, who is affected.
- Known contracts, licenses, privacy notices, terms, consent forms, data sources.

## Outputs

1. **Regulatory map** — laws, regimes, or policy constraints likely to apply.
2. **Rights and data inventory** — what content/data exists, who owns it, who can use it, under what limits.
3. **Use-case matrix** — allowed / restricted / prohibited.
4. **MVP guardrails** — what the MVP may include now.
5. **Required documents** — terms, privacy policy, releases, contracts, DPAs, licenses, audit logs.
6. **Open legal questions** — owner, severity, deadline.

## Procedure

### 1. Identify regulated surfaces

Check whether the product involves personal data, image data, user-generated content, copyrighted works, public-sector records, payments, health, mental health, finance, employment, education, children, automated decisions, scraping/API terms, dataset licenses, or cross-border transfer.

### 2. Build the rights/data inventory

| Asset / data | Source | Owner/controller | Evidence of rights | Allowed use | Restricted use | Unknowns |
|---|---|---|---|---|---|---|

### 3. Build the use-case matrix

| Use case | User segment | Data/content used | Risk | Allowed now? | Required mitigation |
|---|---|---|---|---|---|

Use labels: `allowed`, `restricted`, `blocked`, `unknown`.

### 4. Convert risks into MVP constraints

Translate risk into product design: exclude content from paid pool, require consent, add metadata, disable risky license types, add audit trail, separate internal/free and external/paid contours, add review queue, or require human approval.

### 5. Decide whether to proceed

End with one of: `Proceed`, `Proceed with guardrails`, or `Hold`.

## Quality bar

- Separate verified facts from assumptions.
- Cite source documents or laws where available.
- Never infer ownership from possession.
- Never treat public availability as permission to commercialize.
- Make unresolved risks visible, not buried in prose.
