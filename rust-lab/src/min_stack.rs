// Track stack minima with generic owned values
/// Push/pop/min in O(1); O(n) storage. Values must support Ord and Clone.
pub struct MinStack<T> { entries: Vec<(T,T)> }
impl<T: Ord + Clone> Default for MinStack<T> {
    fn default() -> Self { Self { entries: Vec::new() } }
}
impl<T: Ord + Clone> MinStack<T> {
    pub fn push(&mut self, value: T) {
        let min = self.entries.last().map_or_else(|| value.clone(), |(_,m)| std::cmp::min(&value,m).clone());
        self.entries.push((value,min));
    }
    pub fn pop(&mut self) -> Option<T> { self.entries.pop().map(|(v,_)| v) }
    pub fn min(&self) -> Option<&T> { self.entries.last().map(|(_,m)| m) }
}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn repeated_minimum() {
        let mut s = MinStack::default(); for v in [3,1,1,2] { s.push(v); }
        assert_eq!(s.min(),Some(&1)); assert_eq!(s.pop(),Some(2)); s.pop();
        assert_eq!(s.min(),Some(&1)); s.pop(); assert_eq!(s.min(),Some(&3));
    }
    #[test] fn empty() { let mut s = MinStack::<String>::default(); assert_eq!(s.pop(),None); assert_eq!(s.min(),None); }
}
