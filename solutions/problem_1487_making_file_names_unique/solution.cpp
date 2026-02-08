/*
 * Problem 1487: Making File Names Unique
 * ====================================
 * Difficulty: Medium
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
    vector<string> getFolderNames(vector<string>& names) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < names.size(); i++) {
            int complement = names - names[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[names[i]] = i;
        }
        return {};
    }
};
