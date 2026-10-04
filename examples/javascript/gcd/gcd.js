function solve(a, b) { while (b !== 0) { [a, b] = [b, a % b]; } return a; }

console.log(solve(0, 0));
console.log(solve(0, 7));
console.log(solve(7, 0));
console.log(solve(48, 18));
console.log(solve(17, 13));
console.log(solve(270, 192));
