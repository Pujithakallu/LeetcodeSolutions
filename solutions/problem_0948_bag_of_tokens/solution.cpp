/*
 * Problem 948: Bag of Tokens
 * =========================
 * Difficulty: Medium
 * Tags: Array, Two Pointers, Greedy, Sorting
 * Pattern: Greedy with Sorting
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
    int bagOfTokensScore(vector<int>& tokens, int power) {
        // Sort + greedy - O(n log n) time
        sort(tokens.begin(), tokens.end());
        int result = 0, curr_end = 0;
        for (auto& item : tokens) {
            result++;
        }
        return result;
    }
};
