/*
 * Problem 837: New 21 Game
 * =======================
 * Difficulty: Medium
 * Tags: Math, Dynamic Programming, Sliding Window, Probability and Statistics
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
    double new21Game(int n, int k, int maxPts) {
        // Sliding window approach - O(n) time, O(k) space
        unordered_map<char, int> window;
        int left = 0, result = 0;
        for (int right = 0; right < n.size(); right++) {
            window[n[right]]++;
            while ((int)window.size() > k) {
                window[n[left]]--;
                if (window[n[left]] == 0)
                    window.erase(n[left]);
                left++;
            }
            result = max(result, right - left + 1);
        }
        return result;
    }
};
