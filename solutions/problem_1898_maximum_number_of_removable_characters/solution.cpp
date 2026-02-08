/*
 * Problem 1898: Maximum Number of Removable Characters
 * ==================================================
 * Difficulty: Medium
 * Tags: Array, Two Pointers, String, Binary Search
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
    int maximumRemovals(string& s, string& p, vector<int>& removable) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = s.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (s[mid] == p) {
                return mid;
            } else if (s[mid] < p) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
