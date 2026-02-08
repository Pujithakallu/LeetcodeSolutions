/*
 * Problem 572: Subtree of Another Tree
 * ===================================
 * Difficulty: Easy
 * Tags: Tree, Depth-First Search, String Matching, Binary Tree, Hash Function
 * Pattern: Tree / DFS
 *
 * Time Complexity:  O(m*n)
 * Space Complexity: O(h)
 */

#include <algorithm>
#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
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
