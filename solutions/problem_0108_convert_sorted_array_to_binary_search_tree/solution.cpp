/*
 * Problem 108: Convert Sorted Array to Binary Search Tree
 * ======================================================
 * Difficulty: Easy
 * Tags: Array, Divide and Conquer, Tree, Binary Search Tree, Binary Tree
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
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        // BST search/insert - O(h) time
        function<TreeNode*(TreeNode*, int)> search = [&](TreeNode* node, int target) -> TreeNode* {
            if (!node) return nullptr;
            if (target == node->val) return node;
            else if (target < node->val) return search(node->left, target);
            else return search(node->right, target);
        };
        return search(nums, nums);
    }
};
