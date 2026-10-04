// Order DAG vertices with cycle detection
use std::collections::VecDeque;
/// Kahn's algorithm in O(V+E); supports parallel edges.
pub fn topological_sort(graph: &[Vec<usize>]) -> Result<Vec<usize>, &'static str> {
    let mut degree = vec![0usize; graph.len()];
    for &v in graph.iter().flatten() {
        let count = degree.get_mut(v).ok_or("invalid vertex")?;
        *count += 1;
    }
    let mut ready: VecDeque<_> = degree.iter().enumerate()
        .filter_map(|(v,&d)| (d == 0).then_some(v)).collect();
    let mut order = Vec::new();
    while let Some(v) = ready.pop_front() {
        order.push(v);
        for &next in &graph[v] {
            degree[next] -= 1;
            if degree[next] == 0 { ready.push_back(next); }
        }
    }
    if order.len() == graph.len() { Ok(order) } else { Err("cycle detected") }
}
#[cfg(test)] mod tests {
    use super::*;
    #[test] fn dag() {
        assert_eq!(topological_sort(&[vec![1,2],vec![3],vec![3],vec![]]), Ok(vec![0,1,2,3]));
        assert_eq!(topological_sort(&[]), Ok(vec![]));
    }
    #[test] fn cycle_and_bad_vertex() {
        assert_eq!(topological_sort(&[vec![1],vec![0]]), Err("cycle detected"));
        assert_eq!(topological_sort(&[vec![2]]), Err("invalid vertex"));
    }
}
