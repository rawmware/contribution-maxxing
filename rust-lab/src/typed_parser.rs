// Parse bounded integers with a custom Error implementation
use std::fmt;
#[derive(Debug, PartialEq, Eq)]
pub enum ParseBoundedError { InvalidBounds, InvalidInteger, OutsideBounds }
impl fmt::Display for ParseBoundedError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.write_str(match self {
            Self::InvalidBounds => "minimum exceeds maximum",
            Self::InvalidInteger => "expected a signed 64-bit decimal integer",
            Self::OutsideBounds => "integer outside inclusive bounds",
        })
    }
}
impl std::error::Error for ParseBoundedError {}
pub fn parse_bounded(text: &str, min: i64, max: i64) -> Result<i64, ParseBoundedError> {
    if min > max { return Err(ParseBoundedError::InvalidBounds); }
    let value = text.trim().parse::<i64>().map_err(|_| ParseBoundedError::InvalidInteger)?;
    if !(min..=max).contains(&value) { return Err(ParseBoundedError::OutsideBounds); }
    Ok(value)
}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn valid() { assert_eq!(parse_bounded(" +42 ",0,42),Ok(42)); }
    #[test] fn errors() {
        assert_eq!(parse_bounded("x",0,9),Err(ParseBoundedError::InvalidInteger));
        assert_eq!(parse_bounded("10",0,9),Err(ParseBoundedError::OutsideBounds));
        assert_eq!(parse_bounded("1",9,0),Err(ParseBoundedError::InvalidBounds));
        assert_eq!(ParseBoundedError::InvalidBounds.to_string(),"minimum exceeds maximum");
    }
}
