/*
 * Problem 893: Groups of Special-Equivalent Strings
 * ================================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, String, Sorting
 * Pattern: Sorting
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
    int numSpecialEquivGroups(vector<string>& words) {
        // Sort-based approach - O(n log n) time
        sort(words.begin(), words.end());
        vector<vector<int>> result;
        result.push_back(words[0]);
        for (int i = 1; i < (int)words.size(); i++) {
            if (words[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], words[i][1]);
            } else {
                result.push_back(words[i]);
            }
        }
        return result;
    }
};
