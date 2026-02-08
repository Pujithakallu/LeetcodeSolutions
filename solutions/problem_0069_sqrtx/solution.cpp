/*
 * Problem 69: Sqrt(x)
 * ===================
 * Difficulty: Easy
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
    int mySqrt(int x) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = x.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (x[mid] == x) {
                return mid;
            } else if (x[mid] < x) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
