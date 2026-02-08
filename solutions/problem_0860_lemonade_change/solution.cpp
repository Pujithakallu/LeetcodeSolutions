/*
 * Problem 860: Lemonade Change
 * ===========================
 * Difficulty: Easy
 * Tags: Array, Greedy
 * Pattern: Greedy
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(1)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)bills.size(); i++) {
            curr_max = max(curr_max, bills[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
