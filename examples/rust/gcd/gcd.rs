fn solve(mut a: i64, mut b: i64) -> i64 { while b != 0 { let r = a % b; a = b; b = r; } a }

fn main() {
    println!("{}", solve(0, 0));
    println!("{}", solve(0, 7));
    println!("{}", solve(7, 0));
    println!("{}", solve(48, 18));
    println!("{}", solve(17, 13));
    println!("{}", solve(270, 192));
}
