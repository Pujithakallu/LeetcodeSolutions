/*
 * Problem 669: Trim a Binary Search Tree
 * =====================================
 * Difficulty: Medium
 * Tags: Tree, Depth-First Search, Binary Search Tree, Binary Tree
 * Pattern: Binary Search Tree
 *
 * Time Complexity:  O(h)
 * Space Complexity: O(h)
 */

#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    TreeNode* trimBST(TreeNode* root, int low, int high) {
        // BST search/insert - O(h) time
        function<TreeNode*(TreeNode*, int)> search = [&](TreeNode* node, int target) -> TreeNode* {
            if (!node) return nullptr;
            if (target == node->val) return node;
            else if (target < node->val) return search(node->left, target);
            else return search(node->right, target);
        };
        return search(root, low);
    }
};
