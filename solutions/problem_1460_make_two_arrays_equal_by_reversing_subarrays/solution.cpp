/*
 * Problem 1460: Make Two Arrays Equal by Reversing Subarrays
 * ========================================================
 * Difficulty: Easy
 * Tags: Array, Hash Table, Sorting
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
    bool canBeEqual(vector<int>& target, vector<int>& arr) {
        // Sort-based approach - O(n log n) time
        sort(target.begin(), target.end());
        vector<vector<int>> result;
        result.push_back(target[0]);
        for (int i = 1; i < (int)target.size(); i++) {
            if (target[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], target[i][1]);
            } else {
                result.push_back(target[i]);
            }
        }
        return result;
    }
};
