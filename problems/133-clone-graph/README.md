# 133. Clone Graph

**Difficulty:** Medium

## Problem

Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

Each node in the graph contains a value and a list of its neighbors.

## Example

```
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
```

This represents a graph where:
- Node 1 is connected to nodes 2 and 4
- Node 2 is connected to nodes 1 and 3
- Node 3 is connected to nodes 2 and 4
- Node 4 is connected to nodes 1 and 3

## Approach

Use DFS with a hash map to track cloned nodes and handle cycles in the graph.

### Algorithm:
1. Use a map to store already-cloned nodes (prevents infinite loops on cycles)
2. For each node, check if it's already been cloned
3. If yes, return the existing clone
4. If no, create a new clone and add to map
5. Recursively clone all neighbors
6. Return the cloned node

The map is crucial for handling cycles - when you encounter a node you've already cloned, you return the existing clone instead of creating a new one.

## Topics

- Graph
- DFS
- Hash Map
- Recursion
