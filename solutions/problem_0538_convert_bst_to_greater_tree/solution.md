# Problem 538: Convert BST to Greater Tree

**Difficulty:** Medium  
**Tags:** Tree, Depth-First Search, Binary Search Tree, Binary Tree  
**Pattern:** BST / Reverse Inorder  
**Link:** [leetcode.com/problems/convert-bst-to-greater-tree](https://leetcode.com/problems/convert-bst-to-greater-tree/)

## Description

Given the `root` of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a *binary search tree* is a tree that satisfies these constraints:

	- The left subtree of a node contains only nodes with keys **less than** the node's key.
	- The right subtree of a node contains only nodes with keys **greater than** the node's key.
	- Both the left and right subtrees must also be binary search trees.

 

Example 1:

```

**Input:** root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
**Output:** [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

```

Example 2:

```

**Input:** root = [0,null,1]
**Output:** [1,null,1]

```

 

**Constraints:**

	- The number of nodes in the tree is in the range `[0, 10^4]`.
	- `-10^4 <= Node.val <= 10^4`
	- All the values in the tree are **unique**.
	- `root` is guaranteed to be a valid binary search tree.

 

**Note:** This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

## Approach: BST / Reverse Inorder

Reverse inorder (right-root-left) accumulates running sum.

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
    def convertBST(self, root):
        self.total = 0
        def traverse(node):
            if not node:
                return
            traverse(node.right)
            self.total += node.val
            node.val = self.total
            traverse(node.left)
        traverse(root)
        return root
```

## Solution (C++)

```cpp
#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    TreeNode* convertBST(TreeNode* root) {
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
