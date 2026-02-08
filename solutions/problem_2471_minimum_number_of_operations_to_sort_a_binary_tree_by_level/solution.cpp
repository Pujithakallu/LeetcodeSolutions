/*
 * Problem 2471: Minimum Number of Operations to Sort a Binary Tree by Level
 * =======================================================================
 * Difficulty: Medium
 * Tags: Tree, Breadth-First Search, Binary Tree
 * Pattern: BFS Level-Order Traversal
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(w)
 */

#include <queue>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int minimumOperations(TreeNode* root) {
        // BFS level-order traversal - O(n) time, O(n) space
        vector<vector<int>> result;
        if (!root) return result;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            int sz = q.size();
            vector<int> level;
            for (int i = 0; i < sz; i++) {
                TreeNode* node = q.front(); q.pop();
                level.push_back(node->val);
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            result.push_back(level);
        }
        return result;
    }
};
