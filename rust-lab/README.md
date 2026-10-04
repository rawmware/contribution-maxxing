# Rust lab: 25 focused additions

A dependency-free library with 25 modules and 50 unit tests, targeting Rust 1.70+
(edition 2021). This batch adds Rust depth, not additional programming languages.
Each module has its own code commit; this index and package infrastructure accompany
the first module. No changes to the original four standalone Rust examples.

## Run with an installed Rust toolchain

```text
cargo test --manifest-path rust-lab/Cargo.toml --offline
cargo clippy --manifest-path rust-lab/Cargo.toml --offline --all-targets
cargo doc --manifest-path rust-lab/Cargo.toml --offline --no-deps
```

Individual modules can also be tested with `rustc --edition=2021 --test`.
No third-party crates, unsafe blocks, network access, or application file I/O.
The two concurrency examples create at most 64 threads and keep results deterministic.
Recursive merge sort and trie destruction remain subject to ordinary stack limits.
Allocation failures are not converted into application errors.

## Verification status at creation

Rust and Cargo are not installed on the authoring machine. Source/package structure
was checked, but compilation, unit tests, rustfmt, and Clippy have NOT been run.
The 50 tests are supplied for execution, not reported as passing. No CI run is claimed.

## Modules

1. [`binary_search`](src/binary_search.rs) — Search sorted slices with a generic binary search.
2. [`merge_sort`](src/merge_sort.rs) — Implement stable generic merge sort.
3. [`two_sum`](src/two_sum.rs) — Find index pairs with a hash map and checked subtraction.
4. [`balanced_delimiters`](src/balanced_delimiters.rs) — Validate nesting with enums and a stack.
5. [`run_length`](src/run_length.rs) — Encode and decode Unicode scalar runs with output limits.
6. [`word_frequency`](src/word_frequency.rs) — Count normalized words in an ordered map.
7. [`matrix_transpose`](src/matrix_transpose.rs) — Transpose owned rectangular matrices with shape validation.
8. [`sieve`](src/sieve.rs) — Generate primes with the sieve of Eratosthenes.
9. [`checked_power`](src/checked_power.rs) — Compute integer powers with checked exponentiation by squaring.
10. [`prefix_sums`](src/prefix_sums.rs) — Answer half-open range queries with checked prefix sums.
11. [`sliding_window`](src/sliding_window.rs) — Compute sliding maxima with a monotonic deque.
12. [`breadth_first`](src/breadth_first.rs) — Find shortest unweighted graph paths with BFS.
13. [`topological_sort`](src/topological_sort.rs) — Order DAG vertices with cycle detection.
14. [`disjoint_set`](src/disjoint_set.rs) — Implement union-find with compression and union by size.
15. [`trie`](src/trie.rs) — Store Unicode words in a trie with prefix queries.
16. [`min_stack`](src/min_stack.rs) — Track stack minima with generic owned values.
17. [`ring_buffer`](src/ring_buffer.rs) — Build a fixed-capacity FIFO that returns rejected values.
18. [`interval_merge`](src/interval_merge.rs) — Merge closed intervals with explicit bound validation.
19. [`edit_distance`](src/edit_distance.rs) — Compute Unicode scalar edit distance with rolling rows.
20. [`coin_change`](src/coin_change.rs) — Solve minimum coin change with bounded dynamic programming.
21. [`custom_iterator`](src/custom_iterator.rs) — Implement a fused iterator with overflow-safe stepping.
22. [`trait_dispatch`](src/trait_dispatch.rs) — Demonstrate trait objects and generic static dispatch.
23. [`typed_parser`](src/typed_parser.rs) — Parse bounded integers with a custom Error implementation.
24. [`scoped_threads`](src/scoped_threads.rs) — Sum borrowed slices with scoped threads and checked arithmetic.
25. [`channel_workers`](src/channel_workers.rs) — Collect deterministic indexed results over owned channels.
