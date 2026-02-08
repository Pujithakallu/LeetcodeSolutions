/*
 * Problem 1475: Final Prices With a Special Discount in a Shop
 * ==========================================================
 * Difficulty: Easy
 * Tags: Array, Stack, Monotonic Stack
 * Pattern: Monotonic Stack
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(n)
 */

#include <stack>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> finalPrices(vector<int>& prices) {
        // Monotonic stack - O(n) time, O(n) space
        int n = prices.size();
        vector<int> result(n, 0);
        stack<int> st;
        for (int i = 0; i < n; i++) {
            while (!st.empty() && prices[i] > prices[st.top()]) {
                int idx = st.top(); st.pop();
                result[idx] = i - idx;
            }
            st.push(i);
        }
        return result;
    }
};
