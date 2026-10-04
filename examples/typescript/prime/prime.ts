function solve(n: number): number { if (n < 2) return 0; for (let d = 2; d * d <= n; d++) if (n % d === 0) return 0; return 1; }

console.log(solve(0));
console.log(solve(1));
console.log(solve(2));
console.log(solve(3));
console.log(solve(4));
console.log(solve(25));
console.log(solve(97));
console.log(solve(121));
console.log(solve(997));
