fn solve(n: i64) -> i64 { if n < 2 { return 0; } let mut d = 2; while d*d <= n { if n%d == 0 { return 0; } d += 1; } 1 }

fn main() {
    println!("{}", solve(0));
    println!("{}", solve(1));
    println!("{}", solve(2));
    println!("{}", solve(3));
    println!("{}", solve(4));
    println!("{}", solve(25));
    println!("{}", solve(97));
    println!("{}", solve(121));
    println!("{}", solve(997));
}
