fn solve(n: i64) -> i64 { let (mut a, mut b) = (0, 1); for _ in 0..n { let t = a+b; a = b; b = t; } a }

fn main() {
    println!("{}", solve(0));
    println!("{}", solve(1));
    println!("{}", solve(2));
    println!("{}", solve(3));
    println!("{}", solve(10));
    println!("{}", solve(20));
    println!("{}", solve(30));
}
