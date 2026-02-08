/*
 * Problem 819: Most Common Word
 * ============================
 * Difficulty: Easy
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
    string mostCommonWord(string& paragraph, vector<string>& banned) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < paragraph.size(); i++) {
            int complement = banned - paragraph[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[paragraph[i]] = i;
        }
        return "";
    }
};
