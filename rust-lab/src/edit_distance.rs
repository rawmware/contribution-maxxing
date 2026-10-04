// Compute Unicode scalar edit distance with rolling rows
/// Levenshtein distance in O(m*n) time and O(n) space.
/// Each insertion, deletion, and substitution costs one; compares Unicode scalars.
pub fn edit_distance(left: &str, right: &str) -> usize {
    let right: Vec<char> = right.chars().collect();
    let mut previous: Vec<usize> = (0..=right.len()).collect();
    let mut current = vec![0; right.len()+1];
    for (i,a) in left.chars().enumerate() {
        current[0] = i+1;
        for (j,&b) in right.iter().enumerate() {
            current[j+1] = (previous[j+1]+1).min(current[j]+1).min(previous[j]+usize::from(a != b));
        }
        std::mem::swap(&mut previous,&mut current);
    }
    previous[right.len()]
}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn classic() { assert_eq!(edit_distance("kitten","sitting"),3); }
    #[test] fn unicode_and_empty() {
        assert_eq!(edit_distance("🦀é","🦀e"),1);
        assert_eq!(edit_distance("","abc"),3);
        assert_eq!(edit_distance("same","same"),0);
    }
}
