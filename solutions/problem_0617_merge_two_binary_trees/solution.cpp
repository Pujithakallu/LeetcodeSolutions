/*
 * Problem 617: Merge Two Binary Trees
 * ==================================
 * Difficulty: Easy
 * Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
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
    TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
        // DFS on binary tree - O(n) time, O(h) space
        function<int(TreeNode*)> dfs = [&](TreeNode* node) -> int {
            if (!node) return 0;
            int left = dfs(node->left);
            int right = dfs(node->right);
            return 1 + max(left, right);
        };
        return dfs(root1);
    }
};
