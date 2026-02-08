/*
 * Problem 230: Kth Smallest Element in a BST
 * =========================================
 * Difficulty: Medium
 * Tags: Tree, Depth-First Search, Binary Search Tree, Binary Tree
 * Pattern: Tree / Inorder Traversal
 *
 * Time Complexity:  O(h+k)
 * Space Complexity: O(h)
 */

#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        // BST search/insert - O(h) time
        function<TreeNode*(TreeNode*, int)> search = [&](TreeNode* node, int target) -> TreeNode* {
            if (!node) return nullptr;
            if (target == node->val) return node;
            else if (target < node->val) return search(node->left, target);
            else return search(node->right, target);
        };
        return search(root, k);
    }
};
