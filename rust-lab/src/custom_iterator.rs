// Implement a fused iterator with overflow-safe stepping
/// Inclusive ascending arithmetic sequence; zero step is rejected.
pub struct StepRange { next: Option<u64>, end: u64, step: u64 }
impl StepRange {
    pub fn new(start: u64, end: u64, step: u64) -> Option<Self> {
        if step == 0 { return None; }
        Some(Self { next: (start <= end).then_some(start), end, step })
    }
}
impl Iterator for StepRange {
    type Item = u64;
    fn next(&mut self) -> Option<Self::Item> {
        let value = self.next?;
        self.next = value.checked_add(self.step).filter(|&n| n <= self.end);
        Some(value)
    }
}
impl std::iter::FusedIterator for StepRange {}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn sequence_and_adapters() {
        assert_eq!(StepRange::new(1,8,3).unwrap().collect::<Vec<_>>(),[1,4,7]);
        assert_eq!(StepRange::new(0,10,2).unwrap().take(3).sum::<u64>(),6);
    }
    #[test] fn overflow_and_exhaustion() {
        let mut r = StepRange::new(u64::MAX,u64::MAX,1).unwrap();
        assert_eq!(r.next(),Some(u64::MAX)); assert_eq!(r.next(),None); assert_eq!(r.next(),None);
        assert!(StepRange::new(0,1,0).is_none());
    }
}
