/*
 * Problem 274: H-Index
 * ===================
 * Difficulty: Medium
 * Tags: Array, Sorting, Counting Sort
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
    int hIndex(vector<int>& citations) {
        // Sort-based approach - O(n log n) time
        sort(citations.begin(), citations.end());
        vector<vector<int>> result;
        result.push_back(citations[0]);
        for (int i = 1; i < (int)citations.size(); i++) {
            if (citations[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], citations[i][1]);
            } else {
                result.push_back(citations[i]);
            }
        }
        return result;
    }
};
