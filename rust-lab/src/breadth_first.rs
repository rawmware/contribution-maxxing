// Find shortest unweighted graph paths with BFS
use std::collections::VecDeque;
/// Validate all endpoints, then find a shortest path in O(V+E).
/// Ok(None) means unreachable; malformed graph indices return Err.
pub fn shortest_path(graph: &[Vec<usize>], start: usize, goal: usize)
    -> Result<Option<Vec<usize>>, &'static str> {
    let n = graph.len();
    if start >= n || goal >= n || graph.iter().flatten().any(|&v| v >= n) {
        return Err("invalid vertex");
    }
    let mut parent = vec![None; n];
    let mut queue = VecDeque::from([start]);
    parent[start] = Some(start);
    while let Some(v) = queue.pop_front() {
        if v == goal {
            let mut path = vec![v]; let mut current = v;
            while current != start { current = parent[current].unwrap(); path.push(current); }
            path.reverse(); return Ok(Some(path));
        }
        for &next in &graph[v] {
            if parent[next].is_none() { parent[next] = Some(v); queue.push_back(next); }
        }
    }
    Ok(None)
}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn paths() {
        let graph = vec![vec![1,2],vec![3],vec![3],vec![],vec![]];
        assert_eq!(shortest_path(&graph,0,3), Ok(Some(vec![0,1,3])));
        assert_eq!(shortest_path(&graph,0,4), Ok(None));
        assert_eq!(shortest_path(&graph,2,2), Ok(Some(vec![2])));
    }
    #[test] fn invalid() { assert!(shortest_path(&[vec![9]],0,0).is_err()); }
}
