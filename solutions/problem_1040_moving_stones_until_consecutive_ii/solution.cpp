/*
 * Problem 1040: Moving Stones Until Consecutive II
 * ==============================================
 * Difficulty: Medium
 * Tags: Array, Math, Sliding Window, Sorting
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
    vector<int> numMovesStonesII(vector<int>& stones) {
        // Sliding window approach - O(n) time, O(k) space
        unordered_map<char, int> window;
        int left = 0, result = 0;
        for (int right = 0; right < stones.size(); right++) {
            window[stones[right]]++;
            while ((int)window.size() > stones) {
                window[stones[left]]--;
                if (window[stones[left]] == 0)
                    window.erase(stones[left]);
                left++;
            }
            result = max(result, right - left + 1);
        }
        return result;
    }
};
