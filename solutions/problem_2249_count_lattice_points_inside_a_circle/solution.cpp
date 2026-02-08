/*
 * Problem 2249: Count Lattice Points Inside a Circle
 * ================================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Math, Geometry, Enumeration
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
    int countLatticePoints(vector<vector<int>>& circles) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < circles.size(); i++) {
            int complement = circles - circles[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[circles[i]] = i;
        }
        return 0;
    }
};
