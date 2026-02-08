/*
 * Problem 791: Custom Sort String
 * ==============================
 * Difficulty: Medium
 * Tags: Hash Table, String, Sorting
 * Pattern: Sorting
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(n)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string customSortString(string& order, string& s) {
        // Sort-based approach - O(n log n) time
        sort(order.begin(), order.end());
        vector<vector<int>> result;
        result.push_back(order[0]);
        for (int i = 1; i < (int)order.size(); i++) {
            if (order[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], order[i][1]);
            } else {
                result.push_back(order[i]);
            }
        }
        return result;
    }
};
