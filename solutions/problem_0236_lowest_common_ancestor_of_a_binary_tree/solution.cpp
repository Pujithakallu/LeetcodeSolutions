/*
 * Problem 236: Lowest Common Ancestor of a Binary Tree
 * ===================================================
 * Difficulty: Medium
 * Tags: Tree, Depth-First Search, Binary Tree
 * Pattern: Tree / DFS
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(h)
 */

#include <algorithm>
#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // DFS on binary tree - O(n) time, O(h) space
        function<int(TreeNode*)> dfs = [&](TreeNode* node) -> int {
            if (!node) return 0;
            int left = dfs(node->left);
            int right = dfs(node->right);
            return 1 + max(left, right);
        };
        return dfs(root);
    }
};
