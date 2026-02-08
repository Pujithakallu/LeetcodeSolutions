/*
 * Problem 2269: Find the K-Beauty of a Number
 * =========================================
 * Difficulty: Easy
 * Tags: Math, String, Sliding Window
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
    int divisorSubstrings(int num, int k) {
        // Sliding window approach - O(n) time, O(k) space
        unordered_map<char, int> window;
        int left = 0, result = 0;
        for (int right = 0; right < num.size(); right++) {
            window[num[right]]++;
            while ((int)window.size() > k) {
                window[num[left]]--;
                if (window[num[left]] == 0)
                    window.erase(num[left]);
                left++;
            }
            result = max(result, right - left + 1);
        }
        return result;
    }
};
