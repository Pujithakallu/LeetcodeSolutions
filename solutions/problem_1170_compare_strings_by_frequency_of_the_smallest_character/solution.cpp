/*
 * Problem 1170: Compare Strings by Frequency of the Smallest Character
 * ==================================================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, String, Binary Search, Sorting
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
    vector<int> numSmallerByFrequency(vector<string>& queries, vector<string>& words) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = queries.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (queries[mid] == words) {
                return mid;
            } else if (queries[mid] < words) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return {};
    }
};
