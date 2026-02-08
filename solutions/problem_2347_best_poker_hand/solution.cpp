/*
 * Problem 2347: Best Poker Hand
 * ===========================
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
    string bestHand(vector<int>& ranks, vector<string>& suits) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < ranks.size(); i++) {
            int complement = suits - ranks[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[ranks[i]] = i;
        }
        return "";
    }
};
