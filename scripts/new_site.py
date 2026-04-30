#!/usr/bin/env python3
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / 'templates' / 'brochure-site'
ACTIVE = ROOT / 'sites' / 'active'

def slugify(text: str) -> str:
    out = []
    prev_dash = False
    for ch in text.lower().strip():
        if ch.isalnum():
            out.append(ch)
            prev_dash = False
        else:
            if not prev_dash:
                out.append('-')
                prev_dash = True
    return ''.join(out).strip('-') or 'new-site'

def replace_tokens(path: Path, replacements: dict[str, str]) -> None:
    if path.suffix.lower() not in {'.astro', '.css', '.json', '.md', '.txt', '.mjs', '.svg'} and path.name != 'package.json':
        return
    text = path.read_text(encoding='utf-8')
    for key, value in replacements.items():
        text = text.replace(key, value)
    path.write_text(text, encoding='utf-8')

def main() -> int:
    if len(sys.argv) < 3:
        print('Usage: python3 scripts/new_site.py <slug> <business name>')
        return 1

    slug = slugify(sys.argv[1])
    business_name = sys.argv[2].strip()
    target = ACTIVE / slug

    if target.exists():
        print(f'Error: {target} already exists')
        return 2

    shutil.copytree(TEMPLATE, target)
    replacements = {
        '__SITE_SLUG__': slug,
        '__BUSINESS_NAME__': business_name,
        '__TAGLINE__': f'{business_name} done right',
        '__PHONE__': '(555) 555-0100',
        '__EMAIL__': f'hello@{slug}.com',
        '__CITY_STATE__': 'Your City, ST',
    }

    for file_path in target.rglob('*'):
        if file_path.is_file():
            replace_tokens(file_path, replacements)

    print(f'Created {target}')
    return 0

raise SystemExit(main())
