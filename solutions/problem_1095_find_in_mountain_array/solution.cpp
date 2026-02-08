/*
 * Problem 1095: Find in Mountain Array
 * ==================================
 * Difficulty: Hard
 * Tags: Array, Binary Search, Interactive
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
    int findInMountainArray(int target, 'MountainArray' mountainArr) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = target.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (target[mid] == mountainArr) {
                return mid;
            } else if (target[mid] < mountainArr) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
