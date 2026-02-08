# Problem 958: Check Completeness of a Binary Tree

**Difficulty:** Medium  
**Tags:** Tree, Breadth-First Search, Binary Tree  
**Pattern:** BFS Level-Order Traversal  
**Link:** [leetcode.com/problems/check-completeness-of-a-binary-tree](https://leetcode.com/problems/check-completeness-of-a-binary-tree/)

## Description

Given the `root` of a binary tree, determine if it is a *complete binary tree*.

In a **complete binary tree**, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between `1` and `2^h` nodes inclusive at the last level `h`.

 

Example 1:

```

**Input:** root = [1,2,3,4,5,6]
**Output:** true
**Explanation:** Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

```

Example 2:

```

**Input:** root = [1,2,3,4,5,null,7]
**Output:** false
**Explanation:** The node with value 7 isn't as far left as possible.

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[1, 100]`.
	- `1 <= Node.val <= 1000`

## Approach: BFS Level-Order Traversal

Traverse the tree level by level using a queue. Process all nodes at the current depth before moving to the next level.

## Pseudocode

```
1. If root is null, return empty
2. Queue = [root]
3. While queue not empty:
   a. level_size = len(queue)
   b. For i in range(level_size):
      - node = dequeue
      - Process node
      - Enqueue node.left, node.right if not null
4. Return result
```

## Algorithm Flow

```mermaid
flowchart TD
    A["Queue = [root]"] --> B{Queue not empty?}
    B -- Yes --> C[level_size = len queue]
    C --> D[Process level_size nodes]
    D --> E[Enqueue children of each node]
    E --> F[Record level result]
    F --> B
    B -- No --> G[Return all level results]
```

## Complexity Analysis

- **Time:** O(n)
- **Space:** O(w)

## Solution (Python3)

```python
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # BFS level-order traversal - O(n) time, O(n) space
        from collections import deque
        if not root:
            return False
        result = []
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
```

## Solution (C++)

```cpp
#include <queue>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool isCompleteTree(TreeNode* root) {
        // BFS level-order traversal - O(n) time, O(n) space
        vector<vector<int>> result;
        if (!root) return result;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            int sz = q.size();
            vector<int> level;
            for (int i = 0; i < sz; i++) {
                TreeNode* node = q.front(); q.pop();
                level.push_back(node->val);
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            result.push_back(level);
        }
        return result;
    }
};
```
