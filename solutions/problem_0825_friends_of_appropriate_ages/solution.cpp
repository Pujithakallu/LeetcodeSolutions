/*
 * Problem 825: Friends Of Appropriate Ages
 * =======================================
 * Difficulty: Medium
 * Tags: Array, Two Pointers, Binary Search, Sorting
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
    int numFriendRequests(vector<int>& ages) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = ages.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (ages[mid] == ages) {
                return mid;
            } else if (ages[mid] < ages) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
