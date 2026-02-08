/*
 * Problem 522: Longest Uncommon Subsequence II
 * ===========================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Two Pointers, String, Sorting
 * Pattern: Two Pointers on Sorted Array
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
    int findLUSlength(vector<string>& strs) {
        // Sort + two pointers - O(n log n) time
        sort(strs.begin(), strs.end());
        int left = 0, right = strs.size() - 1;
        while (left < right) {
            int curr = strs[left] + strs[right];
            if (curr < strs) {
                left++;
            } else {
                right--;
            }
        }
        return 0;
    }
};
