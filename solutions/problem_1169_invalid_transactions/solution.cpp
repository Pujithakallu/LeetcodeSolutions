/*
 * Problem 1169: Invalid Transactions
 * ================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, String, Sorting
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
    vector<string> invalidTransactions(vector<string>& transactions) {
        // Sort-based approach - O(n log n) time
        sort(transactions.begin(), transactions.end());
        vector<vector<int>> result;
        result.push_back(transactions[0]);
        for (int i = 1; i < (int)transactions.size(); i++) {
            if (transactions[i][0] <= result.back()[1]) {
                result.back()[1] = max(result.back()[1], transactions[i][1]);
            } else {
                result.push_back(transactions[i]);
            }
        }
        return result;
    }
};
