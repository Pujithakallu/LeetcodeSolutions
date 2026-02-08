/*
 * Problem 30: Substring with Concatenation of All Words
 * =====================================================
 * Difficulty: Hard
 * Tags: Hash Table, String, Sliding Window
 * Pattern: Sliding Window / Hash Map
 *
 * Time Complexity:  O(n * m * w) where n=len(s), m=num words, w=word len
 * Space Complexity: O(m)
 */

#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> findSubstring(string& s, vector<string>& words) {
        // Sliding window approach - O(n) time, O(k) space
        unordered_map<char, int> window;
        int left = 0, result = 0;
        for (int right = 0; right < s.size(); right++) {
            window[s[right]]++;
            while ((int)window.size() > words) {
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
