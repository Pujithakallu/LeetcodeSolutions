/*
 * Problem 1813: Sentence Similarity III
 * ===================================
 * Difficulty: Medium
 * Tags: Array, Two Pointers, String
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
    bool areSentencesSimilar(string& sentence1, string& sentence2) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = sentence1.size() - 1;
        while (left < right) {
            int curr = sentence1[left] + sentence1[right];
            if (curr == sentence2) {
                return {left, right};
            } else if (curr < sentence2) {
                left++;
            } else {
                right--;
            }
        }
        return false;
    }
};
