/*
 * Problem 2412: Minimum Money Required Before Transactions
 * ======================================================
 * Difficulty: Hard
 * Tags: Array, Greedy, Sorting
 * Pattern: Greedy with Sorting
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
    int minimumMoney(vector<vector<int>>& transactions) {
        // Sort + greedy - O(n log n) time
        sort(transactions.begin(), transactions.end());
        int result = 0, curr_end = 0;
        for (auto& item : transactions) {
            result++;
        }
        return result;
    }
};
