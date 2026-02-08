/*
 * Problem 2110: Number of Smooth Descent Periods of a Stock
 * =======================================================
 * Difficulty: Medium
 * Tags: Array, Math, Two Pointers, Dynamic Programming, Sliding Window
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
    int getDescentPeriods(vector<int>& prices) {
        // Sliding window approach - O(n) time, O(k) space
        unordered_map<char, int> window;
        int left = 0, result = 0;
        for (int right = 0; right < prices.size(); right++) {
            window[prices[right]]++;
            while ((int)window.size() > prices) {
                window[prices[left]]--;
                if (window[prices[left]] == 0)
                    window.erase(prices[left]);
                left++;
            }
            result = max(result, right - left + 1);
        }
        return result;
    }
};
