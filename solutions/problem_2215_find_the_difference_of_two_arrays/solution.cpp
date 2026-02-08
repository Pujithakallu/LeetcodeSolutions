/*
 * Problem 2215: Find the Difference of Two Arrays
 * =============================================
 * Difficulty: Easy
 * Tags: Array, Hash Table
 * Pattern: Hash Set
 *
 * Time Complexity:  O(n+m)
 * Space Complexity: O(n+m)
 */

#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < nums1.size(); i++) {
            int complement = nums2 - nums1[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[nums1[i]] = i;
        }
        return {};
    }
};
