#!/usr/bin/env python3
import argparse
import datetime
import pathlib
import re

STAGES = [
    ('00_Project_Brief.md', 'Project Brief'),
    ('01_Context.md', 'C — Context'),
    ('02_Research.md', 'R — Research'),
    ('03_Legal_Gate.md', 'Legal Gate'),
    ('04_Elaboration.md', 'E — Elaboration'),
    ('05_Assembly.md', 'A — Assembly'),
    ('06_Tuning.md', 'T — Tuning'),
    ('07_Expansion.md', 'E — Expansion'),
    ('08_Decisions_Log.md', 'Decision Log'),
    ('09_Source_Index.md', 'Source Index'),
]

def slugify(value: str) -> str:
    value = re.sub(r'[^\w\-а-яА-ЯёЁ]+', '_', value.strip())
    value = re.sub(r'_+', '_', value).strip('_')
    return value or 'product'

def write_lines(path: pathlib.Path, lines: list[str]) -> None:
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')

def main() -> None:
    parser = argparse.ArgumentParser(description='Initialize a CREATE project workspace')
    parser.add_argument('--name', required=True, help='Product/project name')
    parser.add_argument('--idea', required=True, help='Raw idea')
    parser.add_argument('--out', default='.', help='Output directory')
    args = parser.parse_args()

    root = pathlib.Path(args.out) / ('CREATE_' + slugify(args.name))
    root.mkdir(parents=True, exist_ok=True)
    (root / 'artifacts').mkdir(exist_ok=True)

    for fname, title in STAGES:
        path = root / fname
        if path.exists():
            continue
        if fname == '00_Project_Brief.md':
            write_lines(path, [
                f'# {args.name} — CREATE Project Brief', '',
                'Created: ' + datetime.date.today().isoformat(), '',
                '## Raw idea', '', args.idea, '',
                '## Target user/customer', '', 'TBD', '',
                '## Context and constraints', '',
                '- Geography/jurisdiction: TBD',
                '- Team/budget/timeline: TBD',
                '- Existing assets/data: TBD',
                '- Monetization intent: TBD', '',
                '## Known facts', '',
                '| Fact | Source | Confidence |', '|---|---|---|', '',
                '## Assumptions to test', '',
                '| Assumption | Why it matters | Test method |', '|---|---|---|', '',
                '## Success definition', '', 'TBD', '',
                '## Open questions', '', '- TBD', ''
            ])
        elif fname == '08_Decisions_Log.md':
            write_lines(path, [
                '# Decision Log', '',
                '| Date | Stage | Decision | Why | Evidence | Reversible? | Owner |',
                '|---|---|---|---|---|---|---|'
            ])
        elif fname == '09_Source_Index.md':
            write_lines(path, [
                '# Source Index', '',
                '| Source | URL/path | Claims supported | Date accessed | Confidence | Notes |',
                '|---|---|---|---|---|---|'
            ])
        else:
            write_lines(path, [
                '# ' + title, '',
                '## Inputs used', '', '- TBD', '',
                '## Artifact outputs', '', 'TBD', '',
                '## Verified facts', '',
                '| Fact | Source | Confidence |', '|---|---|---|', '',
                '## Assumptions', '',
                '| Assumption | Test |', '|---|---|', '',
                '## Decisions implied', '', '- TBD', '',
                '## Open questions', '', '- TBD', '',
                '## Handoff to next stage', '', '- TBD', ''
            ])
    print(root)

if __name__ == '__main__':
    main()
