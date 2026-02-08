/*
 * Problem 1768: Merge Strings Alternately
 * =====================================
 * Difficulty: Easy
 * Tags: Two Pointers, String
 * Pattern: Two Pointers / String
 *
 * Time Complexity:  O(n+m)
 * Space Complexity: O(n+m)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string mergeAlternately(string& word1, string& word2) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = word1.size() - 1;
        while (left < right) {
            int curr = word1[left] + word1[right];
            if (curr == word2) {
                return {left, right};
            } else if (curr < word2) {
                left++;
            } else {
                right--;
            }
        }
        return "";
    }
};
