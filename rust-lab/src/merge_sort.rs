// Implement stable generic merge sort
/// Stable ascending sort. O(n log n) time and O(n) peak auxiliary storage.
pub fn merge_sort<T: Ord + Clone>(items: &mut [T]) {
    if items.len() < 2 { return; }
    let mid = items.len() / 2;
    merge_sort(&mut items[..mid]);
    merge_sort(&mut items[mid..]);
    let (mut left, mut right) = (0, mid);
    let mut merged = Vec::with_capacity(items.len());
    while left < mid && right < items.len() {
        if items[left] <= items[right] {
            merged.push(items[left].clone()); left += 1;
        } else {
            merged.push(items[right].clone()); right += 1;
        }
    }
    merged.extend_from_slice(&items[left..mid]);
    merged.extend_from_slice(&items[right..]);
    items.clone_from_slice(&merged);
}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn sorts_duplicates() {
        let mut values = [5, -1, 2, 2, 0];
        merge_sort(&mut values);
        assert_eq!(values, [-1, 0, 2, 2, 5]);
    }
    #[test] fn empty_and_singleton() {
        merge_sort::<i32>(&mut []);
        let mut one = [7]; merge_sort(&mut one); assert_eq!(one, [7]);
    }
}
