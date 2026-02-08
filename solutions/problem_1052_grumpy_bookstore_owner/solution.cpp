/*
 * Problem 1052: Grumpy Bookstore Owner
 * ==================================
 * Difficulty: Medium
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
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int minutes) {
        // Sliding window approach - O(n) time, O(k) space
        unordered_map<char, int> window;
        int left = 0, result = 0;
        for (int right = 0; right < customers.size(); right++) {
            window[customers[right]]++;
            while ((int)window.size() > grumpy) {
                window[customers[left]]--;
                if (window[customers[left]] == 0)
                    window.erase(customers[left]);
                left++;
            }
            result = max(result, right - left + 1);
        }
        return result;
    }
};
