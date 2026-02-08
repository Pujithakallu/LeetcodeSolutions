/*
 * Problem 1839: Longest Substring Of All Vowels in Order
 * ====================================================
 * Difficulty: Medium
 * Tags: String, Sliding Window
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
    int longestBeautifulSubstring(string& word) {
        // Sliding window approach - O(n) time, O(k) space
        unordered_map<char, int> window;
        int left = 0, result = 0;
        for (int right = 0; right < word.size(); right++) {
            window[word[right]]++;
            while ((int)window.size() > word) {
                window[word[left]]--;
                if (window[word[left]] == 0)
                    window.erase(word[left]);
                left++;
            }
            result = max(result, right - left + 1);
        }
        return result;
    }
};
