/*
 * Problem 354: Russian Doll Envelopes
 * ==================================
 * Difficulty: Hard
 * Tags: Array, Binary Search, Dynamic Programming, Sorting
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
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = envelopes.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (envelopes[mid] == envelopes) {
                return mid;
            } else if (envelopes[mid] < envelopes) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
