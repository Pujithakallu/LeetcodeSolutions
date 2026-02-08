/*
 * Problem 1604: Alert Using Same Key-Card Three or More Times in a One Hour Period
 * ==============================================================================
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
    vector<string> alertNames(vector<string>& keyName, vector<string>& keyTime) {
        // Sort-based approach - O(n log n) time
        sort(keyName.begin(), keyName.end());
        vector<vector<int>> result;
        result.push_back(keyName[0]);
        for (int i = 1; i < (int)keyName.size(); i++) {
            if (keyName[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], keyName[i][1]);
            } else {
                result.push_back(keyName[i]);
            }
        }
        return result;
    }
};
