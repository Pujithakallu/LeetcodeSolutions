/*
 * Problem 1519: Number of Nodes in the Sub-Tree With the Same Label
 * ===============================================================
 * Difficulty: Medium
 * Tags: Hash Table, Tree, Depth-First Search, Breadth-First Search, Counting
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
    vector<int> countSubTrees(int n, vector<vector<int>>& edges, string& labels) {
        // DFS on binary tree - O(n) time, O(h) space
        function<int(TreeNode*)> dfs = [&](TreeNode* node) -> int {
            if (!node) return 0;
            int left = dfs(node->left);
            int right = dfs(node->right);
            return 1 + max(left, right);
        };
        return dfs(n);
    }
};
