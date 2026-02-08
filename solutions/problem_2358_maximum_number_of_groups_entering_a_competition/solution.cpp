/*
 * Problem 2358: Maximum Number of Groups Entering a Competition
 * ===========================================================
 * Difficulty: Medium
 * Tags: Array, Math, Binary Search, Greedy
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
    int maximumGroups(vector<int>& grades) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = grades.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (grades[mid] == grades) {
                return mid;
            } else if (grades[mid] < grades) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
