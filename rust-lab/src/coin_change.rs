// Solve minimum coin change with bounded dynamic programming
/// Unlimited positive denomination coins; Ok(None) means no solution.
/// O(amount * coins.len()) time, O(amount) memory; amount capped at one million.
pub fn min_coins(coins: &[usize], amount: usize) -> Result<Option<usize>, &'static str> {
    if coins.contains(&0) { return Err("zero denomination"); }
    if amount > 1_000_000 { return Err("amount exceeds allocation policy"); }
    let mut dp = vec![None;amount+1]; dp[0] = Some(0usize);
    for total in 1..=amount {
        for &coin in coins {
            if coin <= total {
                if let Some(previous) = dp[total-coin] {
                    let candidate = previous+1;
                    dp[total] = Some(dp[total].map_or(candidate, |best| best.min(candidate)));
                }
            }
        }
    }
    Ok(dp[amount])
}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn non_greedy_optimum() { assert_eq!(min_coins(&[1,3,4],6),Ok(Some(2))); }
    #[test] fn impossible_and_invalid() {
        assert_eq!(min_coins(&[2],3),Ok(None));
        assert_eq!(min_coins(&[],0),Ok(Some(0)));
        assert!(min_coins(&[0],1).is_err()); assert!(min_coins(&[1],usize::MAX).is_err());
    }
}
