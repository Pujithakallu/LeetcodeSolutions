/*
 * Problem 1742: Maximum Number of Balls in a Box
 * ============================================
 * Difficulty: Easy
 * Tags: Hash Table, Math, Counting
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
    int countBalls(int lowLimit, int highLimit) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < lowLimit.size(); i++) {
            int complement = highLimit - lowLimit[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[lowLimit[i]] = i;
        }
        return 0;
    }
};
