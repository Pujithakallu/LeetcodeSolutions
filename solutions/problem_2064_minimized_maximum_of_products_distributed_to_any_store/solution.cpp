/*
 * Problem 2064: Minimized Maximum of Products Distributed to Any Store
 * ==================================================================
 * Difficulty: Medium
 * Tags: Array, Binary Search, Greedy
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
    int minimizedMaximum(int n, vector<int>& quantities) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = n.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (n[mid] == quantities) {
                return mid;
            } else if (n[mid] < quantities) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
