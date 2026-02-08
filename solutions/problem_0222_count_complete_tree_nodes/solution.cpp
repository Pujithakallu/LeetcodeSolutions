/*
 * Problem 222: Count Complete Tree Nodes
 * =====================================
 * Difficulty: Easy
 * Tags: Binary Search, Bit Manipulation, Tree, Binary Tree
 * Pattern: Binary Search
 *
 * Time Complexity:  O(log n)
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int countNodes(TreeNode* root) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = root.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (root[mid] == root) {
                return mid;
            } else if (root[mid] < root) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
