# 743. Network Delay Time

**Difficulty:** Medium

## Problem Description

You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (ui, vi, wi)`, where `ui` is the source node, `vi` is the target node, and `wi` is the time it takes for a signal to travel from source to target.

We will send a signal from a given node `k`. Return the **minimum** time it takes for all the `n` nodes to receive the signal. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

## Examples

### Example 1:
```
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
```

### Example 2:
```
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
```

### Example 3:
```
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
```

## Constraints

- `1 <= k <= n <= 100`
- `1 <= times.length <= 6000`
- `times[i].length == 3`
- `1 <= ui, vi <= n`
- `ui != vi`
- `0 <= wi <= 100`
- All the pairs `(ui, vi)` are **unique**. (i.e., no multiple edges.)

## Approach

This solution uses **Dijkstra's Algorithm** to find the shortest path from the starting node `k` to all other nodes in the graph.

### Algorithm Steps:
1. Build an adjacency list representation of the graph
2. Initialize all nodes with infinite distance except the starting node `k` (set to 0)
3. Repeatedly select the unprocessed node with the shortest distance
4. Update (relax) the distances to all its neighbors
5. Mark the node as processed
6. Return the maximum distance among all nodes (or -1 if any node is unreachable)

### Time Complexity
- **O(n² + E)** where n is the number of nodes and E is the number of edges

### Space Complexity
- **O(n + E)** for the adjacency list and auxiliary data structures

## Topics

- Graph
- Shortest Path
- Dijkstra's Algorithm
