function solve(n: number): number { let r = 1; for (let i = 2; i <= n; i++) r *= i; return r; }

console.log(solve(0));
console.log(solve(1));
console.log(solve(2));
console.log(solve(5));
console.log(solve(10));
console.log(solve(12));
