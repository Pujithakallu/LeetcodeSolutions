/*
 * Problem 1452: People Whose List of Favorite Companies Is Not a Subset of Another List
 * ===================================================================================
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
    vector<int> peopleIndexes(vector<vector<string>>& favoriteCompanies) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < favoriteCompanies.size(); i++) {
            int complement = favoriteCompanies - favoriteCompanies[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[favoriteCompanies[i]] = i;
        }
        return {};
    }
};
