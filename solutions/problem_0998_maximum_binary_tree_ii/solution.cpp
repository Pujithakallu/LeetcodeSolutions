/*
 * Problem 998: Maximum Binary Tree II
 * ==================================
 * Difficulty: Medium
 * Tags: Tree, Binary Tree
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
    TreeNode* insertIntoMaxTree(TreeNode* root, int val) {
        // Tree traversal - O(n) time, O(h) space
        vector<int> result;
        function<void(TreeNode*)> traverse = [&](TreeNode* node) {
            if (!node) return;
            result.push_back(node->val);
            traverse(node->left);
            traverse(node->right);
        };
        traverse(root);
        return result;
    }
};
