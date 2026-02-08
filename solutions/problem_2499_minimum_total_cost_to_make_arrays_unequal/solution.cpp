/*
 * Problem 2499: Minimum Total Cost to Make Arrays Unequal
 * =====================================================
 * Difficulty: Hard
 * Tags: Array, Hash Table, Greedy, Counting
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
    int minimumTotalCost(vector<int>& nums1, vector<int>& nums2) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)nums1.size(); i++) {
            curr_max = max(curr_max, nums1[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
