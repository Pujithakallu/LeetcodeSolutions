/*
 * Problem 1711: Count Good Meals
 * ============================
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
    int countPairs(vector<int>& deliciousness) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < deliciousness.size(); i++) {
            int complement = deliciousness - deliciousness[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[deliciousness[i]] = i;
        }
        return 0;
    }
};
