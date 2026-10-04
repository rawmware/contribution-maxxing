"""Run shared-vector smoke tests without installing any toolchains."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import json
import math
import os
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def reference(task, args):
    if task == 'gcd':
        return math.gcd(*args)
    n = args[0]
    if task == 'factorial':
        return math.factorial(n)
    if task == 'prime':
        return int(n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1)))
    if task == 'fibonacci':
        values = [0, 1]
        for _ in range(2, n + 1):
            values.append(values[-1] + values[-2])
        return values[n]
    raise ValueError(task)


def execute(argv):
    return subprocess.run(argv, cwd=ROOT, text=True, encoding='utf-8',
                          errors='replace', capture_output=True, timeout=120)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--language', action='append', help='Exact manifest language; repeatable')
    parser.add_argument('--require-all', action='store_true', help='Fail when a runtime is missing')
    options = parser.parse_args()
    manifest = json.loads((ROOT / 'manifest.json').read_text(encoding='utf-8'))
    specs = json.loads((ROOT / 'specs/vectors.json').read_text(encoding='utf-8'))
    known = {row['language'] for row in manifest}
    if options.language and not set(options.language) <= known:
        parser.error('Unknown language; choices: ' + ', '.join(sorted(known)))
    if len(manifest) != 100 or len(known) != 25:
        raise ValueError('Expected 100 examples in 25 languages')
    if len({(row['language'], row['task']) for row in manifest}) != 100:
        raise ValueError('Duplicate manifest entries')
    for task, spec in specs.items():
        actual = [reference(task, args) for args in spec['cases']]
        if actual != spec['expected']:
            raise ValueError('Invalid fixture: ' + task)
    for row in manifest:
        for key in ('source', 'project'):
            if row.get(key):
                path = (ROOT / row[key]).resolve()
                if not path.is_relative_to(ROOT) or not path.is_file():
                    raise ValueError('Invalid or absent source: ' + str(path))
    rows = [row for row in manifest if not options.language or row['language'] in options.language]
    results = []
    for row in rows:
        result = {'language': row['language'], 'task': row['task'], 'source': row['source']}
        tools = {}
        missing = []
        for name in row['requires']:
            found = sys.executable if name == 'python' else shutil.which(name)
            if name == 'powershell':
                found = shutil.which('pwsh') or found
            if found:
                tools[name] = found
            else:
                missing.append(name)
        if not missing and row['language'] == 'CSharp':
            sdk = execute([tools['dotnet'], '--list-sdks'])
            # net8.0 targeting pack/runtime is intentionally not downloaded by this harness.
            if sdk.returncode or not any(line.startswith('8.') for line in sdk.stdout.splitlines()):
                missing.append('.NET SDK 8')
        if missing:
            result.update(status='SKIP', reason='Missing: ' + ', '.join(missing))
        else:
            build = ROOT / '.build' / Path(row['source']).parent.relative_to('examples')
            build.mkdir(parents=True, exist_ok=True)
            context = dict(source=str(ROOT / row['source']), build=str(build), task=row['task'],
                           project=str(ROOT / row['project']) if row['project'] else '',
                           exe=str(build / ('example.exe' if os.name == 'nt' else 'example')))
            commands = []
            if row['compile']:
                commands.append(row['compile'])
            commands.append(row['run'])
            try:
                for command in commands:
                    argv = [part.format(**context) for part in command]
                    argv[0] = tools.get(argv[0], argv[0])
                    completed = execute(argv)
                    if completed.returncode:
                        raise RuntimeError('Command failed: ' + repr(argv) + '\n' + completed.stdout + completed.stderr)
                expected = list(map(str, specs[row['task']]['expected']))
                actual = completed.stdout.strip().splitlines()
                if actual != expected:
                    raise ValueError(f'Expected {expected!r}; got {actual!r}')
                result.update(status='PASS', cases=len(expected))
            except (OSError, subprocess.TimeoutExpired, RuntimeError, ValueError) as error:
                result.update(status='FAIL', reason=str(error))
        print(f"{result['status']:4} {row['language']:12} {row['task']:10} {result.get('reason', '')}", flush=True)
        results.append(result)
    counts = dict(Counter(result['status'] for result in results))
    report = dict(timestamp=datetime.now(timezone.utc).isoformat(),
                  summary=counts, passed_cases=sum(r.get('cases', 0) for r in results), results=results)
    (ROOT / 'verification.local.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: report[key] for key in ('summary', 'passed_cases')}))
    return int(bool(counts.get('FAIL') or (options.require_all and counts.get('SKIP'))))


if __name__ == '__main__':
    sys.exit(main())
