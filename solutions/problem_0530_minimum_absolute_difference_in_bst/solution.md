# Problem 530: Minimum Absolute Difference in BST

**Difficulty:** Easy  
**Tags:** Tree, Depth-First Search, Breadth-First Search, Binary Search Tree, Binary Tree  
**Pattern:** BST / Inorder Traversal  
**Link:** [leetcode.com/problems/minimum-absolute-difference-in-bst](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)

## Description

Given the `root` of a Binary Search Tree (BST), return *the minimum absolute difference between the values of any two different nodes in the tree*.

 

Example 1:

```

**Input:** root = [4,2,6,1,3]
**Output:** 1

```

Example 2:

```

**Input:** root = [1,0,48,null,null,12,49]
**Output:** 1

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[2, 10^4]`.
	- `0 <= Node.val <= 10^5`

 

**Note:** This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/

## Approach: BST / Inorder Traversal

Inorder traversal gives sorted order. Min difference is between adjacent values.

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

- **Time:** O(n)
- **Space:** O(h)

## Solution (Python3)

```python
class Solution:
    def getMinimumDifference(self, root) -> int:
        self.prev = None
        self.min_diff = float('inf')
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)
        inorder(root)
        return self.min_diff
```

## Solution (C++)

```cpp
#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int getMinimumDifference(TreeNode* root) {
        // BST search/insert - O(h) time
        function<TreeNode*(TreeNode*, int)> search = [&](TreeNode* node, int target) -> TreeNode* {
            if (!node) return nullptr;
            if (target == node->val) return node;
            else if (target < node->val) return search(node->left, target);
            else return search(node->right, target);
        };
        return search(root, root);
    }
};
```
