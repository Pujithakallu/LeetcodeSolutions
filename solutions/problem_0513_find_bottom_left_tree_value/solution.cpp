/*
 * Problem 513: Find Bottom Left Tree Value
 * =======================================
 * Difficulty: Medium
 * Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
 * Pattern: BFS / Tree
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(n)
 */

#include <algorithm>
#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
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
