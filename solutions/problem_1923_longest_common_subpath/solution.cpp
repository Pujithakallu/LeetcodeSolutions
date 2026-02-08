/*
 * Problem 1923: Longest Common Subpath
 * ==================================
 * Difficulty: Hard
 * Tags: Array, Binary Search, Rolling Hash, Suffix Array, Hash Function
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
    int longestCommonSubpath(int n, vector<vector<int>>& paths) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = n.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (n[mid] == paths) {
                return mid;
            } else if (n[mid] < paths) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
