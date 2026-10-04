# First polyglot batch

100 standalone algorithm examples in 25 programming languages, with one code commit per example.

Algorithms: Euclidean GCD, factorial, trial-division primality, and iterative or tail-recursive Fibonacci.

Languages: Python, JavaScript, TypeScript, Ruby, PHP, Go, Rust, C, C++, Java,
C#, Lua, Perl, R, Julia, Swift, Kotlin, Scala, Clojure, Elixir, Haskell,
OCaml, Racket, Common Lisp, and PowerShell.

## Run

From the repository root:

```text
python tools/verify.py
python tools/verify.py --language Python --require-all
```

The harness does not install toolchains. It reports missing ones as SKIP and
writes an ignored `verification.local.json`. See [SPECIFICATION.md](SPECIFICATION.md)
for input bounds, complexity, intended toolchains, and test limitations.

## Observed local verification

- 12 examples passed: all Python, JavaScript, and PowerShell examples.
- 84 output comparisons passed.
- 88 examples skipped because their required compiler/runtime/SDK was unavailable.
- No executed example failed.
- Other language implementations are not claimed as runtime-verified.

Each example embeds the same task-specific input vectors; the manifest and
`specs/vectors.json` make the suite inspectable and repeatable.
No empty commits, backdating, or changes to the existing license.
Repository commit counts do not establish GitHub profile contribution credit.
