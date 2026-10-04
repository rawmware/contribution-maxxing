// Search sorted slices with a generic binary search
/// Return an index of target in an ascending sorted slice, or None.
/// O(log n) comparisons; duplicate values may return any matching index.
pub fn binary_search<T: Ord>(items: &[T], target: &T) -> Option<usize> {
    let (mut low, mut high) = (0, items.len());
    while low < high {
        let mid = low + (high - low) / 2;
        match items[mid].cmp(target) {
            std::cmp::Ordering::Less => low = mid + 1,
            std::cmp::Ordering::Greater => high = mid,
            std::cmp::Ordering::Equal => return Some(mid),
        }
    }
    None
}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn boundaries() {
        assert_eq!(binary_search::<i32>(&[], &1), None);
        assert_eq!(binary_search(&[1, 3, 5], &1), Some(0));
        assert_eq!(binary_search(&[1, 3, 5], &5), Some(2));
        assert_eq!(binary_search(&[1, 3, 5], &4), None);
    }
    #[test] fn generic_strings() {
        assert_eq!(binary_search(&["ant", "bee", "cat"], &"bee"), Some(1));
    }
}
