# CREATE Artifact Schema

Use this schema to keep CREATE outputs portable between agents.

## Project metadata

```yaml
product_name:
owner:
date:
stage:
status: draft|reviewed|validated|superseded
jurisdiction:
sources:
```

## Standard artifact block

```markdown
## [Artifact Name]

### Inputs used
- [artifact/source]

### Verified facts
- [fact] — [source]

### Assumptions
- [assumption] — test by [method]

### Output
[main artifact content]

### Decisions implied
- [decision]

### Open questions
- [question] — owner/date

### Handoff to next stage
- [what the next stage must use]
```

## Decision log row

| Date | Stage | Decision | Why | Evidence | Reversible? | Owner |
|---|---|---|---|---|---|---|

## Source index row

| Source | URL/path | Claims supported | Date accessed | Confidence | Notes |
|---|---|---|---|---|---|
