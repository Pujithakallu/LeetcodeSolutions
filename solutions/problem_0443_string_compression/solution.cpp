/*
 * Problem 443: String Compression
 * ==============================
 * Difficulty: Medium
 * Tags: Two Pointers, String
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
    int compress(vector<string>& chars) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = chars.size() - 1;
        while (left < right) {
            int curr = chars[left] + chars[right];
            if (curr == chars) {
                return {left, right};
            } else if (curr < chars) {
                left++;
            } else {
                right--;
            }
        }
        return 0;
    }
};
