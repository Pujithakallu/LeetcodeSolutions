/*
 * Problem 1160: Find Words That Can Be Formed by Characters
 * =======================================================
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
    int countCharacters(vector<string>& words, string& chars) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < words.size(); i++) {
            int complement = chars - words[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[words[i]] = i;
        }
        return 0;
    }
};
