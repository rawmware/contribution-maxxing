//! Small, allocation-free browser exports. Invalid inputs return -1.
//! The same functions run in native tests and compiled WebAssembly.

#[no_mangle]
pub extern "C" fn lab_gcd(mut a: i32, mut b: i32) -> i32 {
    if !(0..=1_000_000).contains(&a) || !(0..=1_000_000).contains(&b) { return -1; }
    while b != 0 { (a, b) = (b, a % b); }
    a
}

#[no_mangle]
pub extern "C" fn lab_factorial(n: i32) -> i32 {
    if !(0..=12).contains(&n) { return -1; }
    (1..=n).product()
}

#[no_mangle]
pub extern "C" fn lab_prime(n: i32) -> i32 {
    if !(0..=1_000_000).contains(&n) { return -1; }
    if n < 2 { return 0; }
    let mut divisor = 2;
    while divisor <= n / divisor {
        if n % divisor == 0 { return 0; }
        divisor += 1;
    }
    1
}

#[no_mangle]
pub extern "C" fn lab_fibonacci(n: i32) -> i32 {
    if !(0..=30).contains(&n) { return -1; }
    let (mut previous, mut current) = (0, 1);
    for _ in 0..n { (previous, current) = (current, previous + current); }
    previous
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn boundaries_and_representative_values() {
        assert_eq!(lab_gcd(0, 0), 0);
        assert_eq!(lab_gcd(48, 18), 6);
        assert_eq!(lab_factorial(0), 1);
        assert_eq!(lab_factorial(12), 479001600);
        assert_eq!(lab_prime(997), 1);
        assert_eq!(lab_prime(121), 0);
        assert_eq!(lab_fibonacci(30), 832040);
    }
    #[test]
    fn rejects_inputs_before_arithmetic() {
        for value in [-1, i32::MIN, i32::MAX] {
            assert_eq!(lab_gcd(value, 1), -1);
            assert_eq!(lab_gcd(1, value), -1);
            assert_eq!(lab_factorial(value), -1);
            assert_eq!(lab_prime(value), -1);
            assert_eq!(lab_fibonacci(value), -1);
        }
        assert_eq!(lab_factorial(13), -1);
        assert_eq!(lab_fibonacci(31), -1);
        assert_eq!(lab_prime(1_000_001), -1);
    }
}
