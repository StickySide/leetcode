# 743. Network Delay Time

**Difficulty:** Medium

## Problem Description

You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (ui, vi, wi)`, where `ui` is the source node, `vi` is the target node, and `wi` is the time it takes for a signal to travel from source to target.

We will send a signal from a given node `k`. Return the minimum time it takes for all the `n` nodes to receive the signal. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

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

This solution uses Dijkstra's Algorithm with a min heap to find the shortest path from the starting node to all other nodes in the graph.

### Algorithm Steps:
1. Build an adjacency list representation of the graph
2. Initialize all nodes with infinite distance except the starting node `k` (set to 0)
3. Use a min heap to always process the node with the shortest distance first
4. For each node, relax (update) the distances to all its neighbors if a shorter path is found
5. Skip stale heap entries that have already been processed with a better path
6. Return the maximum distance among all nodes (or -1 if any node is unreachable)

## Solutions

- [heap_solution.py](./heap_solution.py) - Optimized Dijkstra's with min heap
- [solution.py](./solution.py) - Basic Dijkstra's implementation

## Topics

- Graph
- Shortest Path
- Dijkstra's Algorithm
- Heap / Priority Queue
