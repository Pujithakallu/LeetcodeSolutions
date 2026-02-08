/*
 * Problem 2476: Closest Nodes Queries in a Binary Search Tree
 * =========================================================
 * Difficulty: Medium
 * Tags: Array, Binary Search, Tree, Depth-First Search, Binary Search Tree, Binary Tree
 * Pattern: Binary Search Tree
 *
 * Time Complexity:  O(h)
 * Space Complexity: O(h)
 */

#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> closestNodes(TreeNode* root, vector<int>& queries) {
        // BST search/insert - O(h) time
        function<TreeNode*(TreeNode*, int)> search = [&](TreeNode* node, int target) -> TreeNode* {
            if (!node) return nullptr;
            if (target == node->val) return node;
            else if (target < node->val) return search(node->left, target);
            else return search(node->right, target);
        };
        return search(root, queries);
    }
};
