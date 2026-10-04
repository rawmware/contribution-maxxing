"""Compile and check the standalone C and C++ algorithm lab examples."""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads((ROOT / "examples/lab-catalog.json").read_text(encoding="utf-8"))


def main():
    compilers = {"c": shutil.which("gcc") or shutil.which("clang"),
                 "cpp": shutil.which("g++") or shutil.which("clang++")}
    missing = [lang for lang, compiler in compilers.items() if not compiler]
    if missing:
        print("SKIP: missing compiler(s): " + ", ".join(missing))
        return 2
    failed = []
    passed = 0
    with tempfile.TemporaryDirectory(prefix="contribution-maxxing-lab-") as tmp:
        for lang, ext, standard, warning in (("c", ".c", "c11", "-Werror"),
                                              ("cpp", ".cpp", "c++17", "-Werror")):
            compiler = compilers[lang]
            for row in CATALOG:
                source = ROOT / row[lang]
                binary = Path(tmp) / (row["name"] + (".exe" if sys.platform == "win32" else "") + ("-c" if lang == "c" else "-cpp"))
                command = [compiler, "-std=" + standard, "-Wall", "-Wextra", warning,
                           str(source), "-o", str(binary)]
                built = subprocess.run(command, capture_output=True, text=True)
                if built.returncode:
                    failed.append((lang, row["name"], "compile", built.stderr))
                    continue
                run = subprocess.run([str(binary)], capture_output=True, text=True, timeout=10)
                actual = run.stdout.strip()
                if run.returncode or actual != row["expected"]:
                    failed.append((lang, row["name"], "run", f"expected {row['expected']!r}, got {actual!r}; {run.stderr}"))
                else:
                    passed += 1
    print(f"{passed} examples passed ({len(CATALOG)} per language).")
    for lang, name, phase, detail in failed:
        print(f"FAIL {lang}/{name} ({phase}): {detail}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
