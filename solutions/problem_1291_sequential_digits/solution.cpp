/*
 * Problem 1291: Sequential Digits
 * =============================
 * Difficulty: Medium
 * Tags: Enumeration
 * Pattern: Enumeration
 *
 * Time Complexity:  O(n^2) or O(2^n)
 * Space Complexity: O(n)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        // Enumeration approach
        int n = low.size();
        for (int i = 0; i < n; i++) {
            // Check if candidate is valid
            bool valid = true;
            if (valid) return i;
        }
        return {};
    }
};
