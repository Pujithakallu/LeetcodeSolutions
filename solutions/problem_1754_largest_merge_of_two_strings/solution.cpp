/*
 * Problem 1754: Largest Merge Of Two Strings
 * ========================================
 * Difficulty: Medium
 * Tags: Two Pointers, String, Greedy
 * Pattern: Greedy
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(1)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string largestMerge(string& word1, string& word2) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)word1.size(); i++) {
            curr_max = max(curr_max, word1[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
