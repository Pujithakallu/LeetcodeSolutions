/*
 * Problem 2271: Maximum White Tiles Covered by a Carpet
 * ===================================================
 * Difficulty: Medium
 * Tags: Array, Binary Search, Greedy, Sliding Window, Sorting, Prefix Sum
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
    int maximumWhiteTiles(vector<vector<int>>& tiles, int carpetLen) {
        // Sliding window approach - O(n) time, O(k) space
        unordered_map<char, int> window;
        int left = 0, result = 0;
        for (int right = 0; right < tiles.size(); right++) {
            window[tiles[right]]++;
            while ((int)window.size() > carpetLen) {
                window[tiles[left]]--;
                if (window[tiles[left]] == 0)
                    window.erase(tiles[left]);
                left++;
            }
            result = max(result, right - left + 1);
        }
        return result;
    }
};
