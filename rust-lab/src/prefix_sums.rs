// Answer half-open range queries with checked prefix sums
#[derive(Debug)]
pub struct PrefixSums { sums: Vec<i64> }
impl PrefixSums {
    pub fn new(values: &[i64]) -> Option<Self> {
        let mut sums = vec![0i64];
        for &value in values { sums.push(sums.last()?.checked_add(value)?); }
        Some(Self { sums })
    }
    /// O(1) sum for [start, end); None for invalid bounds or overflow.
    pub fn range(&self, start: usize, end: usize) -> Option<i64> {
        if start > end { return None; }
        self.sums.get(end)?.checked_sub(*self.sums.get(start)?)
    }
}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn queries() {
        let p = PrefixSums::new(&[2, -1, 4]).unwrap();
        assert_eq!(p.range(1, 3), Some(3));
        assert_eq!(p.range(2, 2), Some(0));
        assert_eq!(p.range(3, 2), None);
        assert_eq!(p.range(0, 4), None);
    }
    #[test] fn overflow() {
        assert!(PrefixSums::new(&[i64::MAX, 1]).is_none());
        let p = PrefixSums::new(&[i64::MIN, i64::MAX, 1]).unwrap();
        assert_eq!(p.range(1, 3), None);
    }
}
