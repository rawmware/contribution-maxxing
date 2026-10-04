// Build a fixed-capacity FIFO that returns rejected values
use std::collections::VecDeque;
pub struct RingBuffer<T> { capacity: usize, queue: VecDeque<T> }
impl<T> RingBuffer<T> {
    pub fn new(capacity: usize) -> Self { Self { capacity, queue: VecDeque::new() } }
    /// Preserve ownership on rejection; never overwrite queued items.
    pub fn push(&mut self, value: T) -> Result<(), T> {
        if self.queue.len() == self.capacity { return Err(value); }
        self.queue.push_back(value); Ok(())
    }
    pub fn pop(&mut self) -> Option<T> { self.queue.pop_front() }
    pub fn len(&self) -> usize { self.queue.len() }
    pub fn is_empty(&self) -> bool { self.queue.is_empty() }
}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn fifo_and_capacity() {
        let mut q = RingBuffer::new(2); assert_eq!(q.push(1),Ok(())); q.push(2).unwrap();
        assert_eq!(q.push(3),Err(3)); assert_eq!(q.pop(),Some(1)); q.push(4).unwrap();
        assert_eq!(q.pop(),Some(2)); assert_eq!(q.pop(),Some(4)); assert!(q.is_empty());
    }
    #[test] fn zero_capacity() { assert_eq!(RingBuffer::new(0).push("owned"),Err("owned")); }
}
