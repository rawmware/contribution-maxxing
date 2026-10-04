// Generate primes with the sieve of Eratosthenes
/// Inclusive sieve, bounded at 10 million to limit allocation.
/// O(limit log log limit) time and O(limit) storage.
pub fn primes(limit: usize) -> Result<Vec<usize>, &'static str> {
    if limit > 10_000_000 { return Err("limit exceeds allocation policy"); }
    let mut prime = vec![true; limit + 1];
    prime[0] = false;
    if limit >= 1 { prime[1] = false; }
    let mut p = 2;
    while p <= limit / p {
        if prime[p] { for multiple in (p*p..=limit).step_by(p) { prime[multiple] = false; } }
        p += 1;
    }
    Ok(prime.iter().enumerate().filter_map(|(n, &yes)| yes.then_some(n)).collect())
}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn primes_to_thirty() { assert_eq!(primes(30).unwrap(), [2,3,5,7,11,13,17,19,23,29]); }
    #[test] fn boundaries() {
        assert!(primes(0).unwrap().is_empty());
        assert!(primes(1).unwrap().is_empty());
        assert_eq!(primes(2).unwrap(), [2]);
        assert!(primes(usize::MAX).is_err());
    }
}
