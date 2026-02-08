/*
 * Problem 804: Unique Morse Code Words
 * ===================================
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
    int uniqueMorseRepresentations(vector<string>& words) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < words.size(); i++) {
            int complement = words - words[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[words[i]] = i;
        }
        return 0;
    }
};
