/*
 * Problem 2109: Adding Spaces to a String
 * =====================================
 * Difficulty: Medium
 * Tags: Array, Two Pointers, String, Simulation
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
    string addSpaces(string& s, vector<int>& spaces) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = s.size() - 1;
        while (left < right) {
            int curr = s[left] + s[right];
            if (curr == spaces) {
                return {left, right};
            } else if (curr < spaces) {
                left++;
            } else {
                right--;
            }
        }
        return "";
    }
};
