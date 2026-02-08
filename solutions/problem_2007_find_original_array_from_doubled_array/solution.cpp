/*
 * Problem 2007: Find Original Array From Doubled Array
 * ==================================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Greedy, Sorting
 * Pattern: Greedy with Sorting
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(n)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> findOriginalArray(vector<int>& changed) {
        // Sort + greedy - O(n log n) time
        sort(changed.begin(), changed.end());
        int result = 0, curr_end = 0;
        for (auto& item : changed) {
            result++;
        }
        return result;
    }
};
