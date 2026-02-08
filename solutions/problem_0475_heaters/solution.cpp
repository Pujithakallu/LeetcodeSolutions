/*
 * Problem 475: Heaters
 * ===================
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
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = houses.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (houses[mid] == heaters) {
                return mid;
            } else if (houses[mid] < heaters) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
