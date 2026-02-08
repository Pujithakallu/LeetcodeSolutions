/*
 * Problem 554: Brick Wall
 * ======================
 * Difficulty: Medium
 * Tags: Array, Hash Table
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
    int leastBricks(vector<vector<int>>& wall) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < wall.size(); i++) {
            int complement = wall - wall[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[wall[i]] = i;
        }
        return 0;
    }
};
