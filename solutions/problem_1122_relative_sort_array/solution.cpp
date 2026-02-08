/*
 * Problem 1122: Relative Sort Array
 * ===============================
 * Difficulty: Easy
 * Tags: Array, Hash Table, Sorting, Counting Sort
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
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        // Sort-based approach - O(n log n) time
        sort(arr1.begin(), arr1.end());
        vector<vector<int>> result;
        result.push_back(arr1[0]);
        for (int i = 1; i < (int)arr1.size(); i++) {
            if (arr1[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], arr1[i][1]);
            } else {
                result.push_back(arr1[i]);
            }
        }
        return result;
    }
};
