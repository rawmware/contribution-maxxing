// Encode and decode Unicode scalar runs with output limits
/// Run-length encoding over Unicode scalar values, not grapheme clusters.
pub fn encode(text: &str) -> Vec<(char, usize)> {
    let mut runs: Vec<(char, usize)> = Vec::new();
    for ch in text.chars() {
        if let Some((last, count)) = runs.last_mut() {
            if *last == ch { *count += 1; continue; }
        }
        runs.push((ch, 1));
    }
    runs
}
/// Reject zero runs, integer overflow, or decoded UTF-8 output above max_bytes.
pub fn decode(runs: &[(char, usize)], max_bytes: usize) -> Option<String> {
    let mut bytes = 0usize;
    for &(ch, count) in runs {
        if count == 0 { return None; }
        bytes = bytes.checked_add(ch.len_utf8().checked_mul(count)?)?;
        if bytes > max_bytes { return None; }
    }
    let mut text = String::with_capacity(bytes);
    for &(ch, count) in runs { for _ in 0..count { text.push(ch); } }
    Some(text)
}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn round_trip() {
        let text = "aaéé🦀";
        assert_eq!(decode(&encode(text), text.len()), Some(text.into()));
        assert_eq!(decode(&encode(""), 0), Some(String::new()));
    }
    #[test] fn limits() {
        assert_eq!(decode(&[('🦀', 2)], 7), None);
        assert_eq!(decode(&[('x', 0)], 10), None);
        assert_eq!(decode(&[('🦀', usize::MAX)], usize::MAX), None);
    }
}
