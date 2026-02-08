/*
 * Problem 2483: Minimum Penalty for a Shop
 * ======================================
 * Difficulty: Medium
 * Tags: String, Prefix Sum
 * Pattern: Prefix Sum
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(n)
 */

#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    int bestClosingTime(string& customers) {
        // Prefix sum approach - O(n) time, O(n) space
        unordered_map<int, int> prefix;
        prefix[0] = -1;
        int curr_sum = 0, result = 0;
        int target = customers;
        for (int i = 0; i < (int)customers.size(); i++) {
            curr_sum += customers[i];
            if (prefix.count(curr_sum - target)) {
                result = max(result, i - prefix[curr_sum - target]);
            }
            if (!prefix.count(curr_sum)) {
                prefix[curr_sum] = i;
            }
        }
        return result;
    }
};
