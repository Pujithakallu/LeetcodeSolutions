/*
 * Problem 2094: Finding 3-Digit Even Numbers
 * ========================================
 * Difficulty: Easy
 * Tags: Array, Hash Table, Recursion, Sorting, Enumeration
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
    vector<int> findEvenNumbers(vector<int>& digits) {
        // Sort-based approach - O(n log n) time
        sort(digits.begin(), digits.end());
        vector<vector<int>> result;
        result.push_back(digits[0]);
        for (int i = 1; i < (int)digits.size(); i++) {
            if (digits[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], digits[i][1]);
            } else {
                result.push_back(digits[i]);
            }
        }
        return result;
    }
};
