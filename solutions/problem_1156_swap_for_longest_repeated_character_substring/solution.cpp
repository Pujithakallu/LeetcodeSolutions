/*
 * Problem 1156: Swap For Longest Repeated Character Substring
 * =========================================================
 * Difficulty: Medium
 * Tags: Hash Table, String, Sliding Window
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
    int maxRepOpt1(string& text) {
        // Sliding window approach - O(n) time, O(k) space
        unordered_map<char, int> window;
        int left = 0, result = 0;
        for (int right = 0; right < text.size(); right++) {
            window[text[right]]++;
            while ((int)window.size() > text) {
                window[text[left]]--;
                if (window[text[left]] == 0)
                    window.erase(text[left]);
                left++;
            }
            result = max(result, right - left + 1);
        }
        return result;
    }
};
