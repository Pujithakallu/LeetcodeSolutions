/*
 * Problem 209: Minimum Size Subarray Sum
 * =====================================
 * Difficulty: Medium
 * Tags: Array, Binary Search, Sliding Window, Prefix Sum
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
    int minSubArrayLen(int target, vector<int>& nums) {
        // Sliding window approach - O(n) time, O(k) space
        unordered_map<char, int> window;
        int left = 0, result = 0;
        for (int right = 0; right < target.size(); right++) {
            window[target[right]]++;
            while ((int)window.size() > nums) {
                window[target[left]]--;
                if (window[target[left]] == 0)
                    window.erase(target[left]);
                left++;
            }
            result = max(result, right - left + 1);
        }
        return result;
    }
};
