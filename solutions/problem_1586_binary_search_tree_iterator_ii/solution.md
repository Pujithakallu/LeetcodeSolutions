# Problem 1586: Binary Search Tree Iterator II

**Difficulty:** Medium  
**Tags:** Stack, Tree, Design, Binary Search Tree, Binary Tree, Iterator  
**Pattern:** Binary Search Tree  
**Link:** [leetcode.com/problems/binary-search-tree-iterator-ii](https://leetcode.com/problems/binary-search-tree-iterator-ii/)

## Description

*(Premium problem -- description requires LeetCode subscription)*

## Approach: Binary Search Tree

Leverage BST property: left < root < right. Navigate left for smaller values, right for larger values. Inorder traversal yields sorted order.

## Pseudocode

```
1. Start at root
2. Compare target with current node:
   a. If target < node.val: go left
   b. If target > node.val: go right
   c. If equal: found
3. Return result
```

## Algorithm Flow

```mermaid
flowchart TD
    A[Start at root] --> B{node is null?}
    B -- Yes --> C[Not found / insert here]
    B -- No --> D{target vs node.val?}
    D -- Less --> E[Go to node.left]
    D -- Greater --> F[Go to node.right]
    D -- Equal --> G[Found target node]
    E --> B
    F --> B
```

## Complexity Analysis

- **Time:** O(h)
- **Space:** O(h)

## Solution (Python3)

```python
class Solution:
    pass
```

## Solution (C++)

```cpp
class Solution {
public:
    // Design problem stub
};
```
