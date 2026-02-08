/*
 * Problem 257: Binary Tree Paths
 * =============================
 * Difficulty: Easy
 * Tags: String, Backtracking, Tree, Depth-First Search, Binary Tree
 * Pattern: Backtracking
 *
 * Time Complexity:  O(k^n) or O(n!)
 * Space Complexity: O(n)
 */

#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(path);
            for (int i = start; i < (int)root.size(); i++) {
                path.push_back(root[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
