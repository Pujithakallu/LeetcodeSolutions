/*
 * Problem 826: Most Profit Assigning Work
 * ======================================
 * Difficulty: Medium
 * Tags: Array, Two Pointers, Binary Search, Greedy, Sorting
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
    int maxProfitAssignment(vector<int>& difficulty, vector<int>& profit, vector<int>& worker) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = difficulty.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (difficulty[mid] == profit) {
                return mid;
            } else if (difficulty[mid] < profit) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
