/*
 * Problem 2260: Minimum Consecutive Cards to Pick Up
 * ================================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Sliding Window
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
    int minimumCardPickup(vector<int>& cards) {
        // Sliding window approach - O(n) time, O(k) space
        unordered_map<char, int> window;
        int left = 0, result = 0;
        for (int right = 0; right < cards.size(); right++) {
            window[cards[right]]++;
            while ((int)window.size() > cards) {
                window[cards[left]]--;
                if (window[cards[left]] == 0)
                    window.erase(cards[left]);
                left++;
            }
            result = max(result, right - left + 1);
        }
        return result;
    }
};
