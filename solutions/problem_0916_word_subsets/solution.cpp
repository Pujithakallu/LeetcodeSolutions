/*
 * Problem 916: Word Subsets
 * ========================
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
    vector<string> wordSubsets(vector<string>& words1, vector<string>& words2) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < words1.size(); i++) {
            int complement = words2 - words1[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[words1[i]] = i;
        }
        return {};
    }
};
