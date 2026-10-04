// Validate nesting with enums and a stack
#[derive(Debug, PartialEq, Eq)]
pub enum DelimiterError { UnexpectedClose(usize), Mismatch(usize), Unclosed }
/// Validate (), [], and {}; ignore all other characters (not a source parser).
/// Error offsets are UTF-8 byte indices. O(n) time, O(depth) space.
pub fn validate(text: &str) -> Result<(), DelimiterError> {
    let mut stack = Vec::new();
    for (offset, ch) in text.char_indices() {
        match ch {
            '(' | '[' | '{' => stack.push(ch),
            ')' | ']' | '}' => {
                let open = stack.pop().ok_or(DelimiterError::UnexpectedClose(offset))?;
                if !matches!((open, ch), ('(', ')') | ('[', ']') | ('{', '}')) {
                    return Err(DelimiterError::Mismatch(offset));
                }
            }
            _ => {}
        }
    }
    if stack.is_empty() { Ok(()) } else { Err(DelimiterError::Unclosed) }
}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn nested() { assert_eq!(validate("a{b[c(d)]}"), Ok(())); }
    #[test] fn failures() {
        assert_eq!(validate("([)]"), Err(DelimiterError::Mismatch(2)));
        assert_eq!(validate("é)"), Err(DelimiterError::UnexpectedClose(2)));
        assert_eq!(validate("("), Err(DelimiterError::Unclosed));
    }
}
