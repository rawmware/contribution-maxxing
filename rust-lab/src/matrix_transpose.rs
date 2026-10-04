// Transpose owned rectangular matrices with shape validation
/// Transpose a rectangular matrix. Ragged input returns an error.
/// Empty or zero-column matrices transpose to an empty outer vector.
pub fn transpose<T: Clone>(rows: &[Vec<T>]) -> Result<Vec<Vec<T>>, &'static str> {
    let width = rows.first().map_or(0, Vec::len);
    if rows.iter().any(|row| row.len() != width) { return Err("ragged matrix"); }
    Ok((0..width).map(|column| rows.iter().map(|row| row[column].clone()).collect()).collect())
}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn rectangular() {
        assert_eq!(transpose(&[vec![1, 2, 3], vec![4, 5, 6]]),
                   Ok(vec![vec![1, 4], vec![2, 5], vec![3, 6]]));
    }
    #[test] fn shape_errors() {
        assert_eq!(transpose(&[vec![1], vec![]]), Err("ragged matrix"));
        assert_eq!(transpose::<i32>(&[]), Ok(vec![]));
    }
}
