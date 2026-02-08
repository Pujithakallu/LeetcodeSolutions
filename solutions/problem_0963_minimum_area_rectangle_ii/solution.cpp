/*
 * Problem 963: Minimum Area Rectangle II
 * =====================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Math, Geometry
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
    double minAreaFreeRect(vector<vector<int>>& points) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < points.size(); i++) {
            int complement = points - points[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[points[i]] = i;
        }
        return 0.0;
    }
};
