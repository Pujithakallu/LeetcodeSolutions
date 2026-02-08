/*
 * Problem 2418: Sort the People
 * ===========================
 * Difficulty: Easy
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
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        // Sort-based approach - O(n log n) time
        sort(names.begin(), names.end());
        vector<vector<int>> result;
        result.push_back(names[0]);
        for (int i = 1; i < (int)names.size(); i++) {
            if (names[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], names[i][1]);
            } else {
                result.push_back(names[i]);
            }
        }
        return result;
    }
};
