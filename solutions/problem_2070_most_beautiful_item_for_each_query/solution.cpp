/*
 * Problem 2070: Most Beautiful Item for Each Query
 * ==============================================
 * Difficulty: Medium
 * Tags: Array, Binary Search, Sorting
 * Pattern: Binary Search
 *
 * Time Complexity:  O(log n)
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> maximumBeauty(vector<vector<int>>& items, vector<int>& queries) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = items.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (items[mid] == queries) {
                return mid;
            } else if (items[mid] < queries) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return {};
    }
};
