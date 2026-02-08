/*
 * Problem 718: Maximum Length of Repeated Subarray
 * ===============================================
 * Difficulty: Medium
 * Tags: Array, Binary Search, Dynamic Programming, Sliding Window, Rolling Hash, Hash Function
 * Pattern: Sliding Window
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(k)
 */

#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    int findLength(vector<int>& nums1, vector<int>& nums2) {
        // Sliding window approach - O(n) time, O(k) space
        unordered_map<char, int> window;
        int left = 0, result = 0;
        for (int right = 0; right < nums1.size(); right++) {
            window[nums1[right]]++;
            while ((int)window.size() > nums2) {
                window[nums1[left]]--;
                if (window[nums1[left]] == 0)
                    window.erase(nums1[left]);
                left++;
            }
            result = max(result, right - left + 1);
        }
        return result;
    }
};
