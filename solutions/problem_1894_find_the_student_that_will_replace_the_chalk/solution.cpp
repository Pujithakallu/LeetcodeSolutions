/*
 * Problem 1894: Find the Student that Will Replace the Chalk
 * ========================================================
 * Difficulty: Medium
 * Tags: Array, Binary Search, Simulation, Prefix Sum
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
    int chalkReplacer(vector<int>& chalk, int k) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = chalk.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (chalk[mid] == k) {
                return mid;
            } else if (chalk[mid] < k) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
