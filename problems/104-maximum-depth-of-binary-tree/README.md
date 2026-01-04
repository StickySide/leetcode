# 104. Maximum Depth of Binary Tree

**Difficulty:** Easy

## Problem

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## Examples

**Example 1:**
```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

**Example 2:**
```
Input: root = [1,null,2]
Output: 2
```

## Approach

Simple recursive DFS solution. The depth of a tree is 1 + the maximum depth of its subtrees.

### Algorithm:
1. Base case: if node is None, depth is 0
2. Recursively find depth of left subtree
3. Recursively find depth of right subtree
4. Return 1 + max(left_depth, right_depth)

## Topics

- Tree
- DFS
- Recursion
