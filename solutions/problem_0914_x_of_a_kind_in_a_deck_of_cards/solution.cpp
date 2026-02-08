/*
 * Problem 914: X of a Kind in a Deck of Cards
 * ==========================================
 * Difficulty: Easy
 * Tags: Array, Hash Table, Math, Counting, Number Theory
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
    bool hasGroupsSizeX(vector<int>& deck) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < deck.size(); i++) {
            int complement = deck - deck[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[deck[i]] = i;
        }
        return false;
    }
};
