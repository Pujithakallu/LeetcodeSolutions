/*
 * Problem 966: Vowel Spellchecker
 * ==============================
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
    vector<string> spellchecker(vector<string>& wordlist, vector<string>& queries) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < wordlist.size(); i++) {
            int complement = queries - wordlist[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[wordlist[i]] = i;
        }
        return {};
    }
};
