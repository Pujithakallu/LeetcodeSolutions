/*
 * Problem 2379: Minimum Recolors to Get K Consecutive Black Blocks
 * ==============================================================
 * Difficulty: Easy
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
    int minimumRecolors(string& blocks, int k) {
        // Sliding window approach - O(n) time, O(k) space
        unordered_map<char, int> window;
        int left = 0, result = 0;
        for (int right = 0; right < blocks.size(); right++) {
            window[blocks[right]]++;
            while ((int)window.size() > k) {
                window[blocks[left]]--;
                if (window[blocks[left]] == 0)
                    window.erase(blocks[left]);
                left++;
            }
            result = max(result, right - left + 1);
        }
        return result;
    }
};
