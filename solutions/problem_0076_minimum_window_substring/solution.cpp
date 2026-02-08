/*
 * Problem 76: Minimum Window Substring
 * ====================================
 * Difficulty: Hard
 * Tags: Hash Table, String, Sliding Window
 * Pattern: Sliding Window
 *
 * Time Complexity:  O(m+n)
 * Space Complexity: O(m+n)
 */

#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    string minWindow(string& s, string& t) {
        // Sliding window approach - O(n) time, O(k) space
        unordered_map<char, int> window;
        int left = 0, result = 0;
        for (int right = 0; right < s.size(); right++) {
            window[s[right]]++;
            while ((int)window.size() > t) {
                window[s[left]]--;
                if (window[s[left]] == 0)
                    window.erase(s[left]);
                left++;
            }
            result = max(result, right - left + 1);
        }
        return result;
    }
};
