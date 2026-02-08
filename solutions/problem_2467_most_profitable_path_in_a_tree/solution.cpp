/*
 * Problem 2467: Most Profitable Path in a Tree
 * ==========================================
 * Difficulty: Medium
 * Tags: Array, Tree, Depth-First Search, Breadth-First Search, Graph Theory
 * Pattern: DFS Tree Traversal
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
    int mostProfitablePath(vector<vector<int>>& edges, int bob, vector<int>& amount) {
        // DFS on binary tree - O(n) time, O(h) space
        function<int(TreeNode*)> dfs = [&](TreeNode* node) -> int {
            if (!node) return 0;
            int left = dfs(node->left);
            int right = dfs(node->right);
            return 1 + max(left, right);
        };
        return dfs(edges);
    }
};
