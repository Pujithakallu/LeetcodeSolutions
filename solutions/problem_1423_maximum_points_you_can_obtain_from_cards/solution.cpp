/*
 * Problem 1423: Maximum Points You Can Obtain from Cards
 * ====================================================
 * Difficulty: Medium
 * Tags: Array, Sliding Window, Prefix Sum
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
    int maxScore(vector<int>& cardPoints, int k) {
        // Sliding window approach - O(n) time, O(k) space
        unordered_map<char, int> window;
        int left = 0, result = 0;
        for (int right = 0; right < cardPoints.size(); right++) {
            window[cardPoints[right]]++;
            while ((int)window.size() > k) {
                window[cardPoints[left]]--;
                if (window[cardPoints[left]] == 0)
                    window.erase(cardPoints[left]);
                left++;
            }
            result = max(result, right - left + 1);
        }
        return result;
    }
};
