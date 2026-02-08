/*
 * Problem 811: Subdomain Visit Count
 * =================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, String, Counting
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
    vector<string> subdomainVisits(vector<string>& cpdomains) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < cpdomains.size(); i++) {
            int complement = cpdomains - cpdomains[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[cpdomains[i]] = i;
        }
        return {};
    }
};
