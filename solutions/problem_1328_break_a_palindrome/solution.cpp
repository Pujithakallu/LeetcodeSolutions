/*
 * Problem 1328: Break a Palindrome
 * ==============================
 * Difficulty: Medium
 * Tags: String, Greedy
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
    string breakPalindrome(string& palindrome) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)palindrome.size(); i++) {
            curr_max = max(curr_max, palindrome[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
