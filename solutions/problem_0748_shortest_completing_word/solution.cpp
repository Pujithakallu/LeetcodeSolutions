/*
 * Problem 748: Shortest Completing Word
 * ====================================
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
    string shortestCompletingWord(string& licensePlate, vector<string>& words) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < licensePlate.size(); i++) {
            int complement = words - licensePlate[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[licensePlate[i]] = i;
        }
        return "";
    }
};
