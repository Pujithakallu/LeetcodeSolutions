/*
 * Problem 1620: Coordinate With Maximum Network Quality
 * ===================================================
 * Difficulty: Medium
 * Tags: Array, Enumeration
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
    vector<int> bestCoordinate(vector<vector<int>>& towers, int radius) {
        // Enumeration approach
        int n = towers.size();
        for (int i = 0; i < n; i++) {
            // Check if candidate is valid
            bool valid = true;
            if (valid) return i;
        }
        return {};
    }
};
