// Find index pairs with a hash map and checked subtraction
use std::collections::HashMap;
/// Return distinct indices whose values sum to target. Expected O(n) time.
/// Checked subtraction excludes mathematically impossible i64 complements.
pub fn two_sum(values: &[i64], target: i64) -> Option<(usize, usize)> {
    let mut seen = HashMap::new();
    for (index, &value) in values.iter().enumerate() {
        if let Some(complement) = target.checked_sub(value) {
            if let Some(&previous) = seen.get(&complement) {
                return Some((previous, index));
            }
        }
        seen.entry(value).or_insert(index);
    }
    None
}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn duplicate_values() { assert_eq!(two_sum(&[3, 3], 6), Some((0, 1))); }
    #[test] fn missing_and_overflow() {
        assert_eq!(two_sum(&[1], 2), None);
        assert_eq!(two_sum(&[i64::MIN, -1], i64::MAX), None);
        assert_eq!(two_sum(&[2, 7, 11], 9), Some((0, 1)));
    }
}
