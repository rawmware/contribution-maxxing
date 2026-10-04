// Merge closed intervals with explicit bound validation
/// Merge overlapping closed intervals; touching endpoints overlap.
/// O(n log n) time. Reversed bounds are rejected, not silently normalized.
pub fn merge_intervals(mut intervals: Vec<(i64,i64)>) -> Result<Vec<(i64,i64)>, &'static str> {
    if intervals.iter().any(|&(a,b)| a > b) { return Err("reversed interval"); }
    intervals.sort_unstable();
    let mut merged: Vec<(i64,i64)> = Vec::new();
    for (start,end) in intervals {
        if let Some(last) = merged.last_mut() {
            if start <= last.1 { last.1 = last.1.max(end); continue; }
        }
        merged.push((start,end));
    }
    Ok(merged)
}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn overlaps() {
        assert_eq!(merge_intervals(vec![(8,10),(1,3),(2,6),(10,12)]),Ok(vec![(1,6),(8,12)]));
    }
    #[test] fn boundaries() {
        assert_eq!(merge_intervals(vec![]),Ok(vec![]));
        assert!(merge_intervals(vec![(2,1)]).is_err());
        assert_eq!(merge_intervals(vec![(i64::MIN,i64::MAX),(0,0)]),Ok(vec![(i64::MIN,i64::MAX)]));
    }
}
