/*
 * Problem 1455: Check If a Word Occurs As a Prefix of Any Word in a Sentence
 * ========================================================================
 * Difficulty: Easy
 * Tags: Two Pointers, String, String Matching
 * Pattern: Two Pointers
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int isPrefixOfWord(string& sentence, string& searchWord) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = sentence.size() - 1;
        while (left < right) {
            int curr = sentence[left] + sentence[right];
            if (curr == searchWord) {
                return {left, right};
            } else if (curr < searchWord) {
                left++;
            } else {
                right--;
            }
        }
        return 0;
    }
};
