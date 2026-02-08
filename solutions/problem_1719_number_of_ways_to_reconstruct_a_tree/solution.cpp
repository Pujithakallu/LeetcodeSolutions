/*
 * Problem 1719: Number Of Ways To Reconstruct A Tree
 * ================================================
 * Difficulty: Hard
 * Tags: Array, Hash Table, Tree, Graph Theory, Simulation
 * Pattern: Tree Traversal
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(h)
 */

#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int checkWays(vector<vector<int>>& pairs) {
        // Tree traversal - O(n) time, O(h) space
        vector<int> result;
        function<void(TreeNode*)> traverse = [&](TreeNode* node) {
            if (!node) return;
            result.push_back(node->val);
            traverse(node->left);
            traverse(node->right);
        };
        traverse(pairs);
        return result;
    }
};
