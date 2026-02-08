/*
 * Problem 1817: Finding the Users Active Minutes
 * ============================================
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
    vector<int> findingUsersActiveMinutes(vector<vector<int>>& logs, int k) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < logs.size(); i++) {
            int complement = k - logs[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[logs[i]] = i;
        }
        return {};
    }
};
