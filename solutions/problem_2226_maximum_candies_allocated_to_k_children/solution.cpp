/*
 * Problem 2226: Maximum Candies Allocated to K Children
 * ===================================================
 * Difficulty: Medium
 * Tags: Array, Binary Search
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
    int maximumCandies(vector<int>& candies, int k) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = candies.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (candies[mid] == k) {
                return mid;
            } else if (candies[mid] < k) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
