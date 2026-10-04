"""Generate a source-first polyglot website. No generated HTML is committed.
Run from anywhere: python web/build_site.py
Output: .site/ (publish this directory with GitHub Pages).
"""
from collections import defaultdict
from datetime import datetime, timezone
import hashlib
import html
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / '.site'
WEB = ROOT / 'web'
REPO = 'https://github.com/rawmware/contribution-maxxing'


def language_id(name):
    # C, C++ and CSharp must never collide.
    return {'C++': 'cpp', 'CSharp': 'csharp'}.get(name, name.lower().replace(' ', '-'))


def shell(title, prefix='./'):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} · Polyglot Lab</title><link rel="stylesheet" href="{prefix}style.css"></head>
<body><header><a href="{prefix}index.html">contribution-maxxing / <b>POLYGLOT LAB</b></a><a href="{REPO}">GitHub ↗</a></header><main id="app"><p>Loading repository snapshot…</p></main><noscript>This explorer needs JavaScript. All language sources remain accessible on GitHub.</noscript><footer>Real source. Explicit runtime boundaries. Rebuilt from the repository on deployment.</footer><script type="module" src="{prefix}app.js"></script></body></html>'''


def main():
    OUT.mkdir(exist_ok=True)
    grouped = defaultdict(list)
    manifest = json.loads((ROOT / 'manifest.json').read_text(encoding='utf-8'))
    report_path = ROOT / 'verification.local.json'
    report = json.loads(report_path.read_text(encoding='utf-8')) if report_path.exists() else None
    for row in manifest:
        source = ROOT / row['source']
        if not source.resolve().is_relative_to(ROOT) or not source.is_file():
            raise ValueError('Invalid source: ' + row['source'])
        grouped[row['language']].append({**row, 'code': source.read_text(encoding='utf-8'),
                                       'sha256': hashlib.sha256(source.read_bytes()).hexdigest()})
    # Include the substantive labs and the exact browser runtime implementations.
    for name, pattern in [('Rust', 'rust-lab/src/*.rs'), ('C', 'examples/c/lab/*.c'),
                          ('Rust', 'web/rust/src/*.rs'), ('C', 'web/c/*.c'),
                          ('CSharp', 'web/csharp/*.cs')]:
        for source in sorted(ROOT.glob(pattern)):
            grouped[name].append({'task': source.stem, 'source': source.relative_to(ROOT).as_posix(),
                                  'code': source.read_text(encoding='utf-8'),
                                  'sha256': hashlib.sha256(source.read_bytes()).hexdigest()})
    languages = []
    ids = set()
    for name, examples in sorted(grouped.items()):
        key = language_id(name)
        if key in ids:
            raise ValueError('Language route collision: ' + key)
        ids.add(key)
        languages.append({'name': name, 'id': key, 'examples': examples})
    try:
        revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        revision = None
    data = {'languages': languages, 'vectors': json.loads((ROOT / 'specs/vectors.json').read_text(encoding='utf-8')),
            'builtAt': datetime.now(timezone.utc).isoformat(), 'revision': revision,
            'verification': report}
    (OUT / 'catalog.json').write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')
    shutil.copyfile(WEB / 'csharp/wwwroot/index.html', OUT / 'index.html')
    (OUT / '.nojekyll').write_text('', encoding='utf-8')
    for name in ('app.js', 'style.css'):
        shutil.copyfile(WEB / name, OUT / name)
    print(f'Built one catalog with {len(languages)} languages in {OUT}')


if __name__ == '__main__':
    main()
