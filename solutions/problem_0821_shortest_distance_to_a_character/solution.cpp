/*
 * Problem 821: Shortest Distance to a Character
 * ============================================
 * Difficulty: Easy
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
    vector<int> shortestToChar(string& s, string& c) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = s.size() - 1;
        while (left < right) {
            int curr = s[left] + s[right];
            if (curr == c) {
                return {left, right};
            } else if (curr < c) {
                left++;
            } else {
                right--;
            }
        }
        return {};
    }
};
