# CREATE Framework Skill

**CREATE** is a reusable product-development methodology for agents and human teams. It turns a raw product idea into a context-preserving chain of artifacts: strategy, research, legal checks, JTBD, MVP, assembly plan, validation, and growth.

The framework is designed for AI agents that lose context across long tasks. CREATE solves this by making every stage produce explicit artifacts that become the input for the next stage.

## What CREATE means

| Letter | Stage | Main question | Core output |
|---|---|---|---|
| C | Context | Why should this product exist emotionally and strategically? | Vision, Mission, Core Values, Emotional Problem |
| R | Research | What is true about market, users, competitors and constraints? | Market analysis, competitors, user pains, CJM, archetypes |
| E | Elaboration | What should we build first, and why? | JTBD, solution hypotheses, prototypes, AARRR, MVP concept |
| A | Assembly | How do we assemble a working product/system? | Content/code/API/UI plan, metrics, build plan |
| T | Tuning | What do real data and feedback tell us? | Funnel analysis, feedback insights, A/B tests |
| E | Expansion | How do we scale responsibly? | LTV/CAC, monetization, growth loops, auto-iteration |

## Repository structure

```text
skill/create-framework/SKILL.md          # Main skill file for agent systems that support skills
skill/create-framework/references/       # Stage prompts and operating rules
agents/CREATE_METHOD.md                  # Universal agent playbook, not tied to Hermes
agents/system-prompt.md                  # Compact system/developer prompt for other agents
scripts/init_create_project.py           # Generates a project workspace from a raw idea
scripts/validate_create_project.py       # Checks that required artifacts exist
scripts/package_skill.py                 # Produces a portable .zip skill package
templates/                               # Reusable markdown templates
evals/evals.json                         # Test prompts for validating the skill
```

## Quick start for agents

1. Read `agents/CREATE_METHOD.md`.
2. Ask the user for the raw idea and constraints.
3. Create a workspace:

```bash
python scripts/init_create_project.py --name "My Product" --idea "raw idea"
```

4. Run CREATE stages in order. Do not skip upstream artifacts.
5. Validate before delivery:

```bash
python scripts/validate_create_project.py path/to/workspace
```

## Quick start for humans

If your agent supports skill folders, install/copy `skill/create-framework/` into its skills directory. If it does not, paste `agents/system-prompt.md` into the agent's instruction layer and keep `agents/CREATE_METHOD.md` available as a reference.

## Design principles

- **Context thread over isolated prompts.** Every answer must cite the prior artifacts it depends on.
- **Evidence over confident guessing.** Market, competitor, legal, and pricing claims must be sourced or marked as hypotheses.
- **Emotion before features.** CREATE starts with the emotional problem because features without emotional context become generic.
- **Legal gate before build.** If the product monetizes content/data, personal data, regulated activity, rights, payments, health, finance, children, or public-sector data, run the Legal Gate before MVP design.
- **Real validation before scaling.** Expansion is not brainstorming; it uses Tuning outputs.

## License

MIT. Authored by Pavel Nasuta with Hermes Agent support.
