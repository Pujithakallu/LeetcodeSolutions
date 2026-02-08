/*
 * Problem 878: Nth Magical Number
 * ==============================
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
    int nthMagicalNumber(int n, int a, int b) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = n.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (n[mid] == a) {
                return mid;
            } else if (n[mid] < a) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
