/*
 * Problem 1657: Determine if Two Strings Are Close
 * ==============================================
 * Difficulty: Medium
 * Tags: Hash Table, String, Sorting, Counting
 * Pattern: Hash Map / String
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(1)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool closeStrings(string& word1, string& word2) {
        // Sort-based approach - O(n log n) time
        sort(word1.begin(), word1.end());
        vector<vector<int>> result;
        result.push_back(word1[0]);
        for (int i = 1; i < (int)word1.size(); i++) {
            if (word1[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], word1[i][1]);
            } else {
                result.push_back(word1[i]);
            }
        }
        return result;
    }
};
