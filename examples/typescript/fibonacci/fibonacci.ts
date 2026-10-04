function solve(n: number): number { let a = 0, b = 1; for (let i = 0; i < n; i++) [a, b] = [b, a + b]; return a; }

console.log(solve(0));
console.log(solve(1));
console.log(solve(2));
console.log(solve(3));
console.log(solve(10));
console.log(solve(20));
console.log(solve(30));
