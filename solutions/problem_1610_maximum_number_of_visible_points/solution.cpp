/*
 * Problem 1610: Maximum Number of Visible Points
 * ============================================
 * Difficulty: Hard
 * Tags: Array, Math, Geometry, Sliding Window, Sorting
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
    int visiblePoints(vector<vector<int>>& points, int angle, vector<int>& location) {
        // Sliding window approach - O(n) time, O(k) space
        unordered_map<char, int> window;
        int left = 0, result = 0;
        for (int right = 0; right < points.size(); right++) {
            window[points[right]]++;
            while ((int)window.size() > angle) {
                window[points[left]]--;
                if (window[points[left]] == 0)
                    window.erase(points[left]);
                left++;
            }
            result = max(result, right - left + 1);
        }
        return result;
    }
};
