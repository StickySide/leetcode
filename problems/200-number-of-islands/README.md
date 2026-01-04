# 200. Number of Islands

**Difficulty:** Medium

## Problem

Given an m x n 2D binary grid which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

## Examples

**Example 1:**
```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

**Example 2:**
```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

## Approaches

### DFS (Recursive) - Recommended
Uses depth-first search to explore each island. When a land cell is found, mark the entire island by recursively visiting all connected land cells and changing them to water.

### BFS (Iterative)
Uses breadth-first search with a queue. Explores islands level-by-level but has more overhead from queue operations.

## Solutions

- [recursive_solution.py](./recursive_solution.py) - DFS approach (faster)
- [bfs_solution.py](./bfs_solution.py) - BFS approach

## Topics

- Graph
- DFS
- BFS
- Matrix
