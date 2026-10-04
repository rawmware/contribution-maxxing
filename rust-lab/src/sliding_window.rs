// Compute sliding maxima with a monotonic deque
use std::collections::VecDeque;
/// O(n) time, O(window) auxiliary storage; window must be in 1..=len.
pub fn sliding_max(values: &[i64], window: usize) -> Option<Vec<i64>> {
    if window == 0 || window > values.len() { return None; }
    let mut queue: VecDeque<usize> = VecDeque::new();
    let mut output = Vec::new();
    for (i, &value) in values.iter().enumerate() {
        while queue.front().is_some_and(|&j| i - j >= window) { queue.pop_front(); }
        while queue.back().is_some_and(|&j| values[j] <= value) { queue.pop_back(); }
        queue.push_back(i);
        if i + 1 >= window { output.push(values[*queue.front().unwrap()]); }
    }
    Some(output)
}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn classic_sequence() {
        assert_eq!(sliding_max(&[1,3,-1,-3,5,3,6,7], 3), Some(vec![3,3,5,5,6,7]));
    }
    #[test] fn boundaries() {
        assert_eq!(sliding_max(&[2,2], 1), Some(vec![2,2]));
        assert_eq!(sliding_max(&[], 1), None);
        assert_eq!(sliding_max(&[1], 0), None);
    }
}
