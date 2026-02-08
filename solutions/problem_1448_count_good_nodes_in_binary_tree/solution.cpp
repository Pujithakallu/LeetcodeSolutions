/*
 * Problem 1448: Count Good Nodes in Binary Tree
 * ===========================================
 * Difficulty: Medium
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
    int goodNodes(TreeNode* root) {
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
