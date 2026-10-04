// Count normalized words in an ordered map
use std::collections::BTreeMap;
/// Split on non-alphanumeric Unicode scalars and lowercase each token.
/// No Unicode normalization or language-specific word segmentation is performed.
pub fn word_frequency(text: &str) -> BTreeMap<String, usize> {
    let mut counts = BTreeMap::new();
    for word in text.split(|ch: char| !ch.is_alphanumeric()).filter(|s| !s.is_empty()) {
        *counts.entry(word.to_lowercase()).or_insert(0) += 1;
    }
    counts
}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn case_and_punctuation() {
        let counts = word_frequency("Rust, rust! GO; 42");
        assert_eq!(counts.get("rust"), Some(&2));
        assert_eq!(counts.keys().map(String::as_str).collect::<Vec<_>>(), ["42", "go", "rust"]);
    }
    #[test] fn unicode_and_empty() {
        assert_eq!(word_frequency("É é").get("é"), Some(&2));
        assert!(word_frequency("---").is_empty());
    }
}
