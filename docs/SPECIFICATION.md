# Polyglot algorithm specification

Every example defines `solve`, then prints one base-10 integer per shared test vector.
The manifest links each standalone source to its compiler/runtime invocation.
Inputs are nonnegative integers within the bounded domains below. Invalid input
handling is outside this demonstration's contract; these are examples, not a public API.

| Algorithm | Domain | Result | Target complexity |
|---|---|---|---|
| gcd | a,b in 0..1000000 | Euclidean GCD, including gcd(0,0)=0 | O(log(max(a,b))) time for nonzero inputs |
| factorial | n in 0..12 | n!, including 0!=1 | O(n) time |
| prime | n in 0..1000000 | 1 if prime, otherwise 0 | O(sqrt(n)) trial division |
| fibonacci | n in 0..30 | F(0)=0, F(1)=1 | O(n) time |

Iterative implementations use constant auxiliary state. Recursive examples may
consume stack proportional to iteration count depending on runtime tail-call support.
Bounds keep results within signed 32-bit range. The primality loop uses d*d <= n;
this multiplication is safe for the specified domain.

## Verification contract

`specs/vectors.json` supplies 28 cases per language (700 observations in total).
The executable examples embed those inputs and compute, rather than hard-code,
the results. The Python harness compares exact output lines against the fixtures.
This is a finite-vector smoke test, not a proof or exhaustive property test.
A missing compiler is SKIP; a compilation error, timeout, or output mismatch is FAIL.
The runner checks fixture results against independent Python reference functions.

## Toolchain targets

Python 3.10+, Node.js 18+, TypeScript 5+, Ruby 3+, PHP 8+, Go 1.20+,
Rust stable, C11, C++17, JDK 17+, .NET SDK 8, Lua 5.3+, Perl 5.30+,
R 4+, Julia 1.9+, Swift 5+, Kotlin 1.9+, Scala 2.13, Clojure 1.11+,
Elixir 1.14+, GHC 9+, OCaml 4.14+, Racket 8+, SBCL 2+,
and Windows PowerShell 5.1 or PowerShell 7. These are intended targets,
not a claim that every toolchain has been exercised.

No external language libraries or runtime package downloads are required by the
examples. Compilers may need their usual installed SDKs. The test harness never
installs tools automatically. Install only the toolchains you want to exercise.
