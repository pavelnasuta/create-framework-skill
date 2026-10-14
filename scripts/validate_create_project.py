#!/usr/bin/env python3
import argparse, pathlib, sys

REQUIRED = [
    '00_Project_Brief.md','01_Context.md','02_Research.md','04_Elaboration.md',
    '05_Assembly.md','06_Tuning.md','07_Expansion.md','08_Decisions_Log.md','09_Source_Index.md'
]
REQUIRED_PHRASES = {
    '01_Context.md': ['Vision', 'Mission', 'Core Values', 'Emotional'],
    '02_Research.md': ['Market', 'Competitor', 'Pain', 'CJM'],
    '04_Elaboration.md': ['JTBD', 'AARRR', 'MVP'],
    '05_Assembly.md': ['Metrics', 'Assembly'],
    '06_Tuning.md': ['AARRR', 'Feedback', 'A/B'],
    '07_Expansion.md': ['LTV', 'CAC', 'Growth'],
}

def main():
    ap = argparse.ArgumentParser(description='Validate a CREATE project workspace')
    ap.add_argument('project_dir')
    args = ap.parse_args()
    root = pathlib.Path(args.project_dir)
    errors=[]
    warnings=[]
    for f in REQUIRED:
        if not (root/f).exists():
            errors.append('Missing required file: ' + f)
    if not (root/'03_Legal_Gate.md').exists():
        warnings.append('Legal Gate file missing. Acceptable only if legal risk is explicitly not applicable.')
    for f, phrases in REQUIRED_PHRASES.items():
        p=root/f
        if not p.exists():
            continue
        text=p.read_text(encoding='utf-8', errors='ignore')
        if len(text.strip()) < 200:
            warnings.append(f + ' looks too short')
        for phrase in phrases:
            if phrase.lower() not in text.lower():
                warnings.append(f + ' may be missing: ' + phrase)
    source = root/'09_Source_Index.md'
    if source.exists() and source.read_text(encoding='utf-8', errors='ignore').count('|') <= 12:
        warnings.append('Source index appears empty')
    for w in warnings:
        print('WARNING:', w)
    for e in errors:
        print('ERROR:', e)
    if errors:
        sys.exit(1)
    print('CREATE project validation completed')

if __name__ == '__main__':
    main()
