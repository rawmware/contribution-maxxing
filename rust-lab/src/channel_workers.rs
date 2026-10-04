// Collect deterministic indexed results over owned channels
use std::sync::mpsc;
use std::thread;
/// One scoped worker per input (maximum 64). Results are restored to input order.
/// Each worker owns a Sender clone; dropping all senders terminates iteration.
pub fn channel_squares(values: &[i64]) -> Result<Vec<Option<i64>>, &'static str> {
    if values.len() > 64 { return Err("at most 64 jobs"); }
    thread::scope(|scope| {
        let (tx,rx) = mpsc::channel();
        let mut handles = Vec::new();
        for (index,&value) in values.iter().enumerate() {
            let sender = tx.clone();
            let handle = thread::Builder::new().spawn_scoped(scope, move || {
                sender.send((index,value.checked_mul(value)))
            }).map_err(|_| "worker spawn failed")?;
            handles.push(handle);
        }
        drop(tx);
        let mut results = vec![None;values.len()];
        let mut received = 0;
        for (index,value) in rx { results[index] = value; received += 1; }
        for handle in handles {
            handle.join().map_err(|_| "worker panicked")?.map_err(|_| "receiver closed")?;
        }
        if received != values.len() { return Err("missing result"); }
        Ok(results)
    })
}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn ordered_results() {
        assert_eq!(channel_squares(&[3,-4,0,i64::MAX]),Ok(vec![Some(9),Some(16),Some(0),None]));
    }
    #[test] fn boundaries() {
        assert_eq!(channel_squares(&[]),Ok(vec![])); assert!(channel_squares(&[1;65]).is_err());
    }
}
