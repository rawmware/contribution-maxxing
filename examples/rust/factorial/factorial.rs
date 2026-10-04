fn solve(n: i64) -> i64 { let mut r = 1; for i in 2..=n { r *= i; } r }

fn main() {
    println!("{}", solve(0));
    println!("{}", solve(1));
    println!("{}", solve(2));
    println!("{}", solve(5));
    println!("{}", solve(10));
    println!("{}", solve(12));
}
