/*
 * Problem 2024: Maximize the Confusion of an Exam
 * =============================================
 * Difficulty: Medium
 * Tags: String, Binary Search, Sliding Window, Prefix Sum
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
    int maxConsecutiveAnswers(string& answerKey, int k) {
        // Sliding window approach - O(n) time, O(k) space
        unordered_map<char, int> window;
        int left = 0, result = 0;
        for (int right = 0; right < answerKey.size(); right++) {
            window[answerKey[right]]++;
            while ((int)window.size() > k) {
                window[answerKey[left]]--;
                if (window[answerKey[left]] == 0)
                    window.erase(answerKey[left]);
                left++;
            }
            result = max(result, right - left + 1);
        }
        return result;
    }
};
