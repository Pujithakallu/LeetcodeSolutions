/*
 * Problem 1617: Count Subtrees With Max Distance Between Cities
 * ===========================================================
 * Difficulty: Hard
 * Tags: Dynamic Programming, Bit Manipulation, Tree, Enumeration, Bitmask
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
    vector<int> countSubgraphsForEachDiameter(int n, vector<vector<int>>& edges) {
        // Tree traversal - O(n) time, O(h) space
        vector<int> result;
        function<void(TreeNode*)> traverse = [&](TreeNode* node) {
            if (!node) return;
            result.push_back(node->val);
            traverse(node->left);
            traverse(node->right);
        };
        traverse(n);
        return result;
    }
};
