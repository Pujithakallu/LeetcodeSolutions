/*
 * Problem 937: Reorder Data in Log Files
 * =====================================
 * Difficulty: Medium
 * Tags: Array, String, Sorting
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
    vector<string> reorderLogFiles(vector<string>& logs) {
        // Sort-based approach - O(n log n) time
        sort(logs.begin(), logs.end());
        vector<vector<int>> result;
        result.push_back(logs[0]);
        for (int i = 1; i < (int)logs.size(); i++) {
            if (logs[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], logs[i][1]);
            } else {
                result.push_back(logs[i]);
            }
        }
        return result;
    }
};
