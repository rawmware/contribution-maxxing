"""Build the dependency-free GitHub Pages language explorer in docs/."""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REPO = "https://github.com/rawmware/contribution-maxxing"
CATALOG = json.loads((ROOT / "examples/lab-catalog.json").read_text(encoding="utf-8"))
MANIFEST = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))

STYLE = """
:root{color-scheme:dark;--bg:#0b1020;--panel:#111a2d;--line:#26334d;--muted:#a6b2c8;--text:#edf3ff;--mint:#76f2c0;--blue:#83b7ff}*{box-sizing:border-box}body{margin:0;background:radial-gradient(ellipse at 75% -20%,#183153 0,transparent 46%),var(--bg);color:var(--text);font:16px/1.6 ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif}a{color:var(--mint)}.wrap{max-width:1120px;margin:auto;padding:24px}.top{display:flex;justify-content:space-between;gap:16px;align-items:center;border-bottom:1px solid var(--line);padding:12px 0 20px}.brand{font-weight:800;letter-spacing:.02em;color:var(--text);text-decoration:none}.pill{border:1px solid var(--line);border-radius:99px;padding:5px 12px;color:var(--mint);font-size:.85rem}.hero{padding:65px 0 38px;max-width:850px}.eyebrow{color:var(--mint);text-transform:uppercase;letter-spacing:.18em;font-size:.75rem;font-weight:700}h1{font-size:clamp(2.5rem,7vw,5.3rem);line-height:1.02;letter-spacing:-.055em;margin:15px 0 18px}h2{letter-spacing:-.03em}p{color:var(--muted)}.actions{display:flex;gap:12px;flex-wrap:wrap;margin:24px 0}.button{display:inline-block;background:var(--mint);color:#07120f;padding:10px 16px;border-radius:10px;font-weight:750;text-decoration:none}.button.secondary{background:transparent;color:var(--text);border:1px solid var(--line)}.stats,.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(225px,1fr));gap:14px}.card{background:linear-gradient(145deg,#121d31,#0e1627);border:1px solid var(--line);border-radius:15px;padding:18px}.stat strong{display:block;font-size:1.65rem;color:var(--mint)}.toolbar{display:flex;gap:12px;flex-wrap:wrap;margin:28px 0 14px}input,select{background:#0d1525;color:var(--text);border:1px solid var(--line);padding:11px 13px;border-radius:9px;font:inherit}input{flex:1;min-width:210px}.tag{display:inline-block;color:var(--blue);font-size:.8rem;margin-right:8px}.card h3{margin:6px 0}.card p{margin:8px 0}.code{display:block;overflow:auto;background:#080e19;border:1px solid var(--line);border-radius:10px;padding:14px;color:#d6e3fa;font:13px/1.6 ui-monospace,SFMono-Regular,Consolas,monospace}.section{padding:30px 0}.notice{border-left:3px solid var(--mint);padding:4px 16px;background:#101a2b}.foot{border-top:1px solid var(--line);padding:22px 0;margin-top:42px;color:var(--muted);font-size:.9rem}.back{color:var(--muted)}@media(max-width:600px){.wrap{padding:18px}.hero{padding:44px 0 25px}.top{align-items:flex-start}}
""".strip()


def esc(value):
    return html.escape(str(value), quote=True)


def slug(value):
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def shell(title, content, depth=0):
    base = "../" * depth
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Explore runnable polyglot algorithm examples in {esc(title)}."><title>{esc(title)} · contribution-maxxing lab</title><style>{STYLE}</style></head>
<body><div class="wrap"><header class="top"><a class="brand" href="{base}index.html">contribution-maxxing <span class="pill">POLYGLOT LAB</span></a><a href="{REPO}">GitHub repository ↗</a></header>{content}<footer class="foot">Built from the repository manifest and shared examples. Algorithms are learning demos, not a public API. <a href="{REPO}">Source on GitHub</a></footer></div></body></html>'''


def main():
    for path in (DOCS / "languages").glob("*.html"):
        path.unlink()
    (DOCS / "languages").mkdir(parents=True, exist_ok=True)
    languages = {}
    for row in MANIFEST:
        languages.setdefault(row["language"], []).append(row)
    lab = {"C": "c", "C++": "cpp"}
    language_cards = []
    for language, rows in sorted(languages.items()):
        key = slug(language)
        href = f"languages/{key}.html"
        language_cards.append(f'<a class="card" data-language="{esc(language.lower())}" href="{href}"><span class="tag">LANGUAGE</span><h3>{esc(language)}</h3><p>{len(rows)} shared-vector examples · 4 algorithms</p></a>')
        examples = list(rows)
        if language in lab:
            for item in CATALOG:
                examples.append({"task": item["name"], "source": item[lab[language]], "description": item["description"]})
        cards = []
        for row in examples:
            task = row["task"]
            source = row["source"]
            source_url = f"{REPO}/blob/main/{source}"
            description = next((item["description"] for item in CATALOG if item["name"] == task), None)
            cards.append(f'<article class="card"><span class="tag">{esc(language)} · {esc(task)}</span><h3>{esc(description or task.title())}</h3><p><a href="{source_url}">View source ↗</a></p></article>')
        body = f'''<main><section class="hero"><a class="back" href="../index.html">← All languages</a><div class="eyebrow">Language workspace</div><h1>{esc(language)}<br><span style="color:var(--mint)">examples.</span></h1><p>Browse {len(examples)} inspectable examples, with links to the actual source files in this repository.</p><div class="actions"><a class="button" href="{REPO}/tree/main/examples/{'cpp' if language == 'C++' else key}">Browse {esc(language)} source ↗</a><a class="button secondary" href="../index.html">Language index</a></div></section><section class="section"><h2>Algorithm shelf</h2><div class="toolbar"><input id="q" type="search" placeholder="Filter algorithms…" aria-label="Filter algorithms"></div><div class="grid" id="items">{"".join(cards)}</div></section></main><script>const q=document.querySelector('#q');q.addEventListener('input',()=>{const x=q.value.toLowerCase();document.querySelectorAll('#items article').forEach(c=>c.hidden=!c.innerText.toLowerCase().includes(x))})</script>'''
        (DOCS / href).write_text(shell(f"{language} examples", body, 1), encoding="utf-8")
    body = f'''<main><section class="hero"><div class="eyebrow">An inspectable polyglot playground</div><h1>One idea.<br><span style="color:var(--mint)">Many languages.</span></h1><p>Explore small algorithms across a diverse set of programming languages. Read the source, compare approaches, and verify shared outputs locally—no hosted code execution or hidden API calls.</p><div class="actions"><a class="button" href="#languages">Explore languages ↓</a><a class="button secondary" href="{REPO}">Open repository ↗</a></div><div class="notice"><strong>TZ application note</strong><p>As described by the project owner: TZ is connected to a GPT API using Luna 6, with a locally built harness developed with help from Jev and other GitHub code engineers. This preview is a static showcase; it does not connect to TZ or make GPT API requests.</p></div></section><section class="stats"><div class="card stat"><strong>25</strong>languages in the existing shared suite</div><div class="card stat"><strong>100</strong>manifest examples · 4 common algorithms</div><div class="card stat"><strong>50</strong>additional C and C++ lab examples</div><div class="card stat"><strong>28</strong>shared test vectors per example</div></section><section class="section" id="languages"><div class="eyebrow">Choose a language</div><h2>Language workspaces</h2><p>HTML is only the thin wrapper for this preview. The examples are source-code-first; C and C++ include additional algorithm labs, with more languages represented in the original suite.</p><div class="toolbar"><input id="filter" type="search" placeholder="Filter languages…" aria-label="Filter languages"><span class="pill">{"".join(esc(k) + " · " for k in sorted(languages))}</span></div><div class="grid" id="language-list">{"".join(language_cards)}</div></section><section class="section"><h2>How to verify locally</h2><pre class="code">python tools/verify.py\npython tools/verify.py --language Rust\npython tools/verify_lab.py</pre><p>The shared harness checks known outputs and reports unavailable toolchains as skipped. The extra C/C++ lab verifier needs GCC or Clang installed.</p></section><section class="section"><h2>What this preview is—and isn’t</h2><p>GitHub Pages serves these static pages and source links. It does not compile programs in the browser, run untrusted code, provide a live TZ chat, or expose API credentials. Use the linked repository and local verification commands to inspect what is actually in the project.</p></section></main><script>const f=document.querySelector('#filter');f.addEventListener('input',()=>{const x=f.value.toLowerCase();document.querySelectorAll('#language-list [data-language]').forEach(c=>c.hidden=!c.dataset.language.includes(x))})</script>'''
    (DOCS / "index.html").write_text(shell("Polyglot algorithm explorer", body), encoding="utf-8")
    (DOCS / "styles.css").write_text(STYLE + "\n", encoding="utf-8")
    print(f"Built index plus {len(languages)} language subpages in docs/.")


if __name__ == "__main__":
    main()
