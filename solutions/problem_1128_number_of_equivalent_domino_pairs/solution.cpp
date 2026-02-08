/*
 * Problem 1128: Number of Equivalent Domino Pairs
 * =============================================
 * Difficulty: Easy
 * Tags: Array, Hash Table, Counting
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
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < dominoes.size(); i++) {
            int complement = dominoes - dominoes[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[dominoes[i]] = i;
        }
        return 0;
    }
};
