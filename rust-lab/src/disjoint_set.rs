// Implement union-find with compression and union by size
pub struct DisjointSet { parent: Vec<usize>, size: Vec<usize> }
impl DisjointSet {
    pub fn new(n: usize) -> Self { Self { parent: (0..n).collect(), size: vec![1;n] } }
    pub fn find(&mut self, mut node: usize) -> Option<usize> {
        if node >= self.parent.len() { return None; }
        while self.parent[node] != node {
            self.parent[node] = self.parent[self.parent[node]];
            node = self.parent[node];
        }
        Some(node)
    }
    /// Some(true) when two components merge, Some(false) if already joined.
    pub fn union(&mut self, a: usize, b: usize) -> Option<bool> {
        let (mut a, mut b) = (self.find(a)?, self.find(b)?);
        if a == b { return Some(false); }
        if self.size[a] < self.size[b] { std::mem::swap(&mut a, &mut b); }
        self.parent[b] = a; self.size[a] += self.size[b]; Some(true)
    }
}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn components() {
        let mut d = DisjointSet::new(5);
        assert_eq!(d.union(0,1),Some(true)); assert_eq!(d.union(1,2),Some(true));
        assert_eq!(d.find(0),d.find(2)); assert_ne!(d.find(0),d.find(4));
        assert_eq!(d.union(2,0),Some(false));
    }
    #[test] fn invalid() { assert_eq!(DisjointSet::new(0).find(0),None); }
}
