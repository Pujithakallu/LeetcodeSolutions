/*
 * Problem 2131: Longest Palindrome by Concatenating Two Letter Words
 * ================================================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, String, Greedy, Counting
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
    int longestPalindrome(vector<string>& words) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)words.size(); i++) {
            curr_max = max(curr_max, words[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
