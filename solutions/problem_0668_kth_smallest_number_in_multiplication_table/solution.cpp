/*
 * Problem 668: Kth Smallest Number in Multiplication Table
 * =======================================================
 * Difficulty: Hard
 * Tags: Math, Binary Search
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
    int findKthNumber(int m, int n, int k) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = m.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (m[mid] == n) {
                return mid;
            } else if (m[mid] < n) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
