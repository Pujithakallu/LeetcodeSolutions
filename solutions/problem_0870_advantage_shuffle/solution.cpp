/*
 * Problem 870: Advantage Shuffle
 * =============================
 * Difficulty: Medium
 * Tags: Array, Two Pointers, Greedy, Sorting
 * Pattern: Greedy with Sorting
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(n)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> advantageCount(vector<int>& nums1, vector<int>& nums2) {
        // Sort + greedy - O(n log n) time
        sort(nums1.begin(), nums1.end());
        int result = 0, curr_end = 0;
        for (auto& item : nums1) {
            result++;
        }
        return result;
    }
};
