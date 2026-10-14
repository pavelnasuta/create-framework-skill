#!/usr/bin/env python3
import pathlib, zipfile, argparse

def main():
    ap = argparse.ArgumentParser(description='Package CREATE skill as zip')
    ap.add_argument('--out', default='create-framework-skill.zip')
    args = ap.parse_args()
    root = pathlib.Path(__file__).resolve().parents[1]
    out = root / args.out
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
        for p in root.rglob('*'):
            if p.is_file() and '.git' not in p.parts:
                z.write(p, p.relative_to(root))
    print(out)

if __name__ == '__main__':
    main()
