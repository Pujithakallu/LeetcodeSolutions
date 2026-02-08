/*
 * Problem 1652: Defuse the Bomb
 * ===========================
 * Difficulty: Easy
 * Tags: Array, Sliding Window
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
    vector<int> decrypt(vector<int>& code, int k) {
        // Sliding window approach - O(n) time, O(k) space
        unordered_map<char, int> window;
        int left = 0, result = 0;
        for (int right = 0; right < code.size(); right++) {
            window[code[right]]++;
            while ((int)window.size() > k) {
                window[code[left]]--;
                if (window[code[left]] == 0)
                    window.erase(code[left]);
                left++;
            }
            result = max(result, right - left + 1);
        }
        return result;
    }
};
