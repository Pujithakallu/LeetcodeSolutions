/*
 * Problem 929: Unique Email Addresses
 * ==================================
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
    int numUniqueEmails(vector<string>& emails) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < emails.size(); i++) {
            int complement = emails - emails[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[emails[i]] = i;
        }
        return 0;
    }
};
