/*
 * Problem 106: Construct Binary Tree from Inorder and Postorder Traversal
 * ======================================================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Divide and Conquer, Tree, Binary Tree
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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        // Tree traversal - O(n) time, O(h) space
        vector<int> result;
        function<void(TreeNode*)> traverse = [&](TreeNode* node) {
            if (!node) return;
            result.push_back(node->val);
            traverse(node->left);
            traverse(node->right);
        };
        traverse(inorder);
        return result;
    }
};
