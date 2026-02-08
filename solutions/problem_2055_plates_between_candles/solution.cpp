/*
 * Problem 2055: Plates Between Candles
 * ==================================
 * Difficulty: Medium
 * Tags: Array, String, Binary Search, Prefix Sum
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
    vector<int> platesBetweenCandles(string& s, vector<vector<int>>& queries) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = s.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (s[mid] == queries) {
                return mid;
            } else if (s[mid] < queries) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return {};
    }
};
