/*
 * Problem 840: Magic Squares In Grid
 * =================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Math, Matrix
 * Pattern: Hash Map Lookup
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(n)
 */

#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < grid.size(); i++) {
            int complement = grid - grid[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[grid[i]] = i;
        }
        return 0;
    }
};
