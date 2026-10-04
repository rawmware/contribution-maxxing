// Store Unicode words in a trie with prefix queries
use std::collections::BTreeMap;
#[derive(Default)]
pub struct Trie { terminal: bool, children: BTreeMap<char, Trie> }
impl Trie {
    pub fn insert(&mut self, word: &str) {
        let mut node = self;
        for ch in word.chars() { node = node.children.entry(ch).or_default(); }
        node.terminal = true;
    }
    fn walk(&self, text: &str) -> Option<&Self> {
        let mut node = self;
        for ch in text.chars() { node = node.children.get(&ch)?; }
        Some(node)
    }
    pub fn contains(&self, word: &str) -> bool { self.walk(word).is_some_and(|n| n.terminal) }
    pub fn has_prefix(&self, prefix: &str) -> bool { self.walk(prefix).is_some() }
}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn prefixes_and_words() {
        let mut t = Trie::default(); t.insert("rust"); t.insert("rusty");
        assert!(t.contains("rust")); assert!(!t.contains("rus"));
        assert!(t.has_prefix("rus")); assert!(!t.has_prefix("ruby"));
    }
    #[test] fn empty_and_unicode() {
        let mut t = Trie::default(); assert!(!t.contains(""));
        t.insert(""); t.insert("🦀é"); assert!(t.contains("")); assert!(t.has_prefix("🦀"));
    }
}
