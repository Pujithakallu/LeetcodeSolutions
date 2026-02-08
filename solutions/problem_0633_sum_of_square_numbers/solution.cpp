/*
 * Problem 633: Sum of Square Numbers
 * =================================
 * Difficulty: Medium
 * Tags: Math, Two Pointers, Binary Search
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
    bool judgeSquareSum(int c) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = c.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (c[mid] == c) {
                return mid;
            } else if (c[mid] < c) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return false;
    }
};
