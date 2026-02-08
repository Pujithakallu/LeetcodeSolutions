/*
 * Problem 49: Group Anagrams
 * ==========================
 * Difficulty: Medium
 * Tags: Array, Hash Table, String, Sorting
 * Pattern: Hash Map / Sorting
 *
 * Time Complexity:  O(n * k log k)
 * Space Complexity: O(n * k)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // Sort-based approach - O(n log n) time
        sort(strs.begin(), strs.end());
        vector<vector<int>> result;
        result.push_back(strs[0]);
        for (int i = 1; i < (int)strs.size(); i++) {
            if (strs[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], strs[i][1]);
            } else {
                result.push_back(strs[i]);
            }
        }
        return result;
    }
};
