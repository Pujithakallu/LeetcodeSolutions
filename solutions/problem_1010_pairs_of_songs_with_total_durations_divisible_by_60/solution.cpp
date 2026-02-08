/*
 * Problem 1010: Pairs of Songs With Total Durations Divisible by 60
 * ===============================================================
 * Difficulty: Medium
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
    int numPairsDivisibleBy60(vector<int>& time) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < time.size(); i++) {
            int complement = time - time[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[time[i]] = i;
        }
        return 0;
    }
};
