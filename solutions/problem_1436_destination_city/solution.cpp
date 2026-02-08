/*
 * Problem 1436: Destination City
 * ============================
 * Difficulty: Easy
 * Tags: Array, Hash Table, String
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
    string destCity(vector<vector<string>>& paths) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < paths.size(); i++) {
            int complement = paths - paths[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[paths[i]] = i;
        }
        return "";
    }
};
