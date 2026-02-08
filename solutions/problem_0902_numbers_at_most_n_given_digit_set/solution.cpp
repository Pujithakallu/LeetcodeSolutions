/*
 * Problem 902: Numbers At Most N Given Digit Set
 * =============================================
 * Difficulty: Hard
 * Tags: Array, Math, String, Binary Search, Dynamic Programming
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
    int atMostNGivenDigitSet(vector<string>& digits, int n) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = digits.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (digits[mid] == n) {
                return mid;
            } else if (digits[mid] < n) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
