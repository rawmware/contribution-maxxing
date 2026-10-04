// Sum borrowed slices with scoped threads and checked arithmetic
use std::thread;
/// Divide borrowed data across at most 64 scoped workers; sum into u128.
/// Workers are always joined. Returns errors for invalid worker counts,
/// spawn failures, worker panics, or arithmetic overflow. O(n) total work.
pub fn parallel_sum(values: &[u64], workers: usize) -> Result<u128, &'static str> {
    if workers == 0 || workers > 64 { return Err("workers must be in 1..=64"); }
    if values.is_empty() { return Ok(0); }
    let chunk_size = values.len()/workers + usize::from(values.len()%workers != 0);
    thread::scope(|scope| {
        let mut handles = Vec::new();
        for chunk in values.chunks(chunk_size) {
            let handle = thread::Builder::new().spawn_scoped(scope, move || {
                chunk.iter().try_fold(0u128, |sum,&v| sum.checked_add(u128::from(v)))
            }).map_err(|_| "worker spawn failed")?;
            handles.push(handle);
        }
        let mut total = 0u128;
        for handle in handles {
            let subtotal = handle.join().map_err(|_| "worker panicked")?.ok_or("sum overflow")?;
            total = total.checked_add(subtotal).ok_or("sum overflow")?;
        }
        Ok(total)
    })
}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn parallel_matches_sequential() {
        let data: Vec<u64> = (0..1000).collect();
        assert_eq!(parallel_sum(&data,4),Ok(499500));
        assert_eq!(parallel_sum(&[u64::MAX,u64::MAX],2),Ok(u128::from(u64::MAX)*2));
    }
    #[test] fn boundaries() {
        assert_eq!(parallel_sum(&[],1),Ok(0)); assert!(parallel_sum(&[1],0).is_err());
        assert_eq!(parallel_sum(&[7],64),Ok(7));
    }
}
