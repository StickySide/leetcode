# 100. Same Tree

**Difficulty:** Easy

## Problem

Given the roots of two binary trees `p` and `q`, check if they are the same tree.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

## Examples

**Example 1:**
```
Input: p = [1,2,3], q = [1,2,3]
Output: true
```

**Example 2:**
```
Input: p = [1,2], q = [1,null,2]
Output: false
```

**Example 3:**
```
Input: p = [1,2,1], q = [1,1,2]
Output: false
```

## Approach

BFS traversal to serialize both trees into lists, then compare them.

## Topics

- Tree
- BFS
- Binary Tree
