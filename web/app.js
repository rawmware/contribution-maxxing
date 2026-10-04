const app = document.querySelector('#app');
const repo = 'https://github.com/rawmware/contribution-maxxing';
const base = new URL('./', import.meta.url);
const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const link = p => new URL(p, base).href;
const label = n => n === 'CSharp' ? 'C#' : n;
const sourceUrl = p => repo + '/blob/main/' + p.split('/').map(encodeURIComponent).join('/');

async function start() {
  const response = await fetch(link('catalog.json'));
  if (!response.ok) throw new Error(`Catalog HTTP ${response.status}`);
  const data = await response.json();
  const route = location.pathname.split('/').pop();
  const language = data.languages.find(l => l.id + '.html' === route);
  if (route === 'c-live.html') return liveC();
  if (language) {
    app.innerHTML = `<a href="${link('index.html')}">← All languages</a><p class="eyebrow">LANGUAGE WORKSPACE</p><h1>${esc(label(language.name))}<span> / source lab</span></h1><p>Actual repository implementations, not JavaScript translations.</p>${language.name === 'C' ? `<a class="button" href="${link('c-live.html')}">Run C in WebAssembly →</a>` : language.name === 'CSharp' ? `<a class="button" href="${link('csharp-live/')}">Run C# in WebAssembly →</a>` : '<p class="notice">Source explorer only. This language is not executed in the browser.</p>'}<section class="grid">${language.examples.map(row => {
      const result = data.verification?.results?.find(r => r.language === language.name && r.task === row.task);
      const vectors = data.vectors[row.task];
      return `<article><p class="eyebrow">${esc(row.task)}</p><h2>${esc(row.task)}</h2><p>${result ? esc(result.status + (result.reason ? ': ' + result.reason : ' — shared vectors')) : 'Not verified in this build'}</p><a href="${sourceUrl(row.source)}">${esc(row.source)} ↗</a><details><summary>Read actual source</summary><pre><code>${esc(row.code)}</code></pre></details><details><summary>Shared test vectors (expected, not live execution)</summary><pre>${esc(JSON.stringify(vectors, null, 2))}</pre></details><p class="hash">SHA-256 ${esc(row.sha256)}</p></article>`;
    }).join('')}</section>`;
  } else {
    app.innerHTML = `<p class="eyebrow">SOURCE-FIRST · MULTI-LANGUAGE</p><h1>One idea.<br><span>Many languages.</span></h1><p>A browser window into real code: ${data.languages.length} languages, ${data.languages.reduce((n,l)=>n+l.examples.length,0)} implementations. HTML is only the display layer.</p><div class="actions"><a class="button" href="${link('c-live.html')}">Live C / WebAssembly</a><a class="button" href="${link('csharp-live/')}">Live C# / WebAssembly</a></div><p class="notice">C and C# execute compiled code in your browser. Other pages display source and build-time test evidence; they do not pretend to run those languages.</p><label for="filter">Find a language</label><input id="filter" type="search" placeholder="Rust, Python, C#, C++…"><section class="grid" id="languages">${data.languages.map(l=>`<a class="card" data-name="${esc((label(l.name)+' '+l.name).toLowerCase())}" href="${link('languages/'+l.id+'.html')}"><p class="eyebrow">${l.examples.length} implementations</p><h2>${esc(label(l.name))}</h2><p>Source · vectors · verification →</p></a>`).join('')}</section><h2>Snapshot, not a hidden server</h2><p>Built ${esc(data.builtAt)} · revision ${esc(data.revision?.slice(0,12) || 'unknown')}. Pushes to main trigger a new Pages build. Open pages do not hot-reload; refresh after deployment.</p><p id="github-stats">Loading GitHub language byte counts…</p>`;
    document.querySelector('#filter').addEventListener('input', e => {
      document.querySelectorAll('[data-name]').forEach(el => el.hidden = !el.dataset.name.includes(e.target.value.toLowerCase()));
    });
    try {
      const r = await fetch('https://api.github.com/repos/rawmware/contribution-maxxing/languages');
      if (!r.ok) throw new Error('HTTP ' + r.status);
      const counts = await r.json();
      const total = Object.values(counts).reduce((a,b)=>a+b,0);
      document.querySelector('#github-stats').textContent = 'GitHub language bytes (not page count): ' + Object.entries(counts).map(([n,b])=>`${n} ${(b/total*100).toFixed(1)}%`).join(' · ');
    } catch(e) { document.querySelector('#github-stats').textContent = 'GitHub language statistics unavailable: ' + e.message; }
  }
}

async function liveC() {
  app.innerHTML = `<a href="${link('languages/c.html')}">← C source workspace</a><p class="eyebrow">COMPILED C · WEBASSEMBLY</p><h1>C<span> / live runtime</span></h1><p>These results come from compiled C, not a JavaScript reimplementation.</p><form><label>Algorithm<select id="task"><option value="gcd">GCD</option><option value="factorial">Factorial</option><option value="prime">Prime (1 / 0)</option><option value="fibonacci">Fibonacci</option></select></label><label>Input A / n<input id="a" type="number" min="0" max="1000000" step="1" value="48" required></label><label>Input B (GCD only)<input id="b" type="number" min="0" max="1000000" step="1" value="18" required></label><button disabled>Run compiled C</button></form><output aria-live="polite">Loading WebAssembly…</output><p>Bounds: GCD / prime 0–1,000,000; factorial 0–12; Fibonacci 0–30.</p><a href="${sourceUrl('web/c/algorithms.c')}">Inspect the C runtime source ↗</a>`;
  try {
    const {default: createModule} = await import(link('runtime/c.mjs'));
    const runtime = await createModule({locateFile: p => link('runtime/'+p)});
    const button = app.querySelector('button');
    const output = app.querySelector('output');
    button.disabled = false;
    output.textContent = 'C WebAssembly ready.';
    app.querySelector('form').addEventListener('submit', e => {
      e.preventDefault();
      const task = document.querySelector('#task').value;
      const a = Number(document.querySelector('#a').value);
      const b = Number(document.querySelector('#b').value);
      const max = task === 'factorial' ? 12 : task === 'fibonacci' ? 30 : 1000000;
      if (!Number.isInteger(a) || a < 0 || a > max || !Number.isInteger(b) || b < 0 || b > 1000000) {
        output.textContent = 'Input outside the documented domain.'; return;
      }
      const start = performance.now();
      const value = task === 'gcd' ? runtime._lab_gcd(a,b) : runtime['_lab_'+task](a);
      output.textContent = `${task} → ${value} · ${(performance.now()-start).toFixed(3)} ms (browser call, not a benchmark)`;
    });
  } catch(e) { app.querySelector('output').textContent = 'C runtime unavailable. Compile with the Pages workflow first. ' + e.message; }
}
start().catch(e => { app.textContent = 'Could not load this demo: ' + e.message; });
