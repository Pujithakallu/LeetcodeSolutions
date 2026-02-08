/*
 * Problem 1889: Minimum Space Wasted From Packaging
 * ===============================================
 * Difficulty: Hard
 * Tags: Array, Binary Search, Sorting, Prefix Sum
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
    int minWastedSpace(vector<int>& packages, vector<vector<int>>& boxes) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = packages.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (packages[mid] == boxes) {
                return mid;
            } else if (packages[mid] < boxes) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
