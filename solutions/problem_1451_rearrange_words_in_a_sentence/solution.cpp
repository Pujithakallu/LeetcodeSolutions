/*
 * Problem 1451: Rearrange Words in a Sentence
 * =========================================
 * Difficulty: Medium
 * Tags: String, Sorting
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
    string arrangeWords(string& text) {
        // Sort-based approach - O(n log n) time
        sort(text.begin(), text.end());
        vector<vector<int>> result;
        result.push_back(text[0]);
        for (int i = 1; i < (int)text.size(); i++) {
            if (text[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], text[i][1]);
            } else {
                result.push_back(text[i]);
            }
        }
        return result;
    }
};
