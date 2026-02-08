/*
 * Problem 970: Powerful Integers
 * =============================
 * Difficulty: Medium
 * Tags: Hash Table, Math, Enumeration
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
    vector<int> powerfulIntegers(int x, int y, int bound) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < x.size(); i++) {
            int complement = y - x[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[x[i]] = i;
        }
        return {};
    }
};
