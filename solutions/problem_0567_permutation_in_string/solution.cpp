/*
 * Problem 567: Permutation in String
 * =================================
 * Difficulty: Medium
 * Tags: Hash Table, Two Pointers, String, Sliding Window
 * Pattern: Sliding Window
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(1)
 */

#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    bool checkInclusion(string& s1, string& s2) {
        // Sliding window approach - O(n) time, O(k) space
        unordered_map<char, int> window;
        int left = 0, result = 0;
        for (int right = 0; right < s1.size(); right++) {
            window[s1[right]]++;
            while ((int)window.size() > s2) {
                window[s1[left]]--;
                if (window[s1[left]] == 0)
                    window.erase(s1[left]);
                left++;
            }
            result = max(result, right - left + 1);
        }
        return result;
    }
};
