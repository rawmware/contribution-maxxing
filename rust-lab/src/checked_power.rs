// Compute integer powers with checked exponentiation by squaring
/// O(log exponent) checked multiplication; 0^0 is defined as 1.
pub fn checked_power(mut base: u64, mut exponent: u32) -> Option<u64> {
    let mut result = 1u64;
    while exponent != 0 {
        if exponent & 1 == 1 { result = result.checked_mul(base)?; }
        exponent >>= 1;
        if exponent != 0 { base = base.checked_mul(base)?; }
    }
    Some(result)
}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn powers() {
        assert_eq!(checked_power(2, 10), Some(1024));
        assert_eq!(checked_power(0, 0), Some(1));
        assert_eq!(checked_power(0, 12), Some(0));
    }
    #[test] fn overflow_boundary() {
        assert_eq!(checked_power(u64::MAX, 1), Some(u64::MAX));
        assert_eq!(checked_power(2, 64), None);
    }
}
