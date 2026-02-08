/*
 * Problem 575: Distribute Candies
 * ==============================
 * Difficulty: Easy
 * Tags: Array, Hash Table
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
    int distributeCandies(vector<int>& candyType) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < candyType.size(); i++) {
            int complement = candyType - candyType[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[candyType[i]] = i;
        }
        return 0;
    }
};
