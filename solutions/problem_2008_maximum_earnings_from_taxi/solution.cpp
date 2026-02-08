/*
 * Problem 2008: Maximum Earnings From Taxi
 * ======================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Binary Search, Dynamic Programming, Sorting
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
    int maxTaxiEarnings(int n, vector<vector<int>>& rides) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = n.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (n[mid] == rides) {
                return mid;
            } else if (n[mid] < rides) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
