// Browser bridge only. Algorithms execute in compiled Rust and C.
const runtimes = {};
window.polyglot = {
  async run(language, task, a, b) {
    if (!['Rust', 'C'].includes(language)) throw new Error('Unknown runtime');
    if (!['gcd', 'factorial', 'prime', 'fibonacci'].includes(task)) throw new Error('Unknown algorithm');
    if (!runtimes[language]) {
      runtimes[language] = (language === 'Rust'
        ? fetch('runtime/rust.wasm').then(response => {
            if (!response.ok) throw new Error('Rust runtime download failed');
            return response.arrayBuffer();
          }).then(bytes => WebAssembly.instantiate(bytes)).then(result => result.instance.exports)
        : import('./runtime/c.mjs').then(module => module.default())
      ).catch(error => { delete runtimes[language]; throw error; });
    }
    const runtime = await runtimes[language];
    return runtime[(language === 'C' ? '_' : '') + 'lab_' + task](a, b);
  }
};
