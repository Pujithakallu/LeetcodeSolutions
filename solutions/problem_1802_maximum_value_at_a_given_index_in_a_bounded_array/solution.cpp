/*
 * Problem 1802: Maximum Value at a Given Index in a Bounded Array
 * =============================================================
 * Difficulty: Medium
 * Tags: Math, Binary Search, Greedy
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
    int maxValue(int n, int index, int maxSum) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = n.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (n[mid] == index) {
                return mid;
            } else if (n[mid] < index) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
