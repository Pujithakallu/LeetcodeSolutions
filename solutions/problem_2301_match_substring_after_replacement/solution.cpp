/*
 * Problem 2301: Match Substring After Replacement
 * =============================================
 * Difficulty: Hard
 * Tags: Array, Hash Table, String, String Matching
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
    bool matchReplacement(string& s, string& sub, vector<vector<string>>& mappings) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < s.size(); i++) {
            int complement = sub - s[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[s[i]] = i;
        }
        return false;
    }
};
