/*
 * Problem 2281: Sum of Total Strength of Wizards
 * ============================================
 * Difficulty: Hard
 * Tags: Array, Stack, Monotonic Stack, Prefix Sum
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
    int totalStrength(vector<int>& strength) {
        // Monotonic stack - O(n) time, O(n) space
        int n = strength.size();
        vector<int> result(n, 0);
        stack<int> st;
        for (int i = 0; i < n; i++) {
            while (!st.empty() && strength[i] > strength[st.top()]) {
                int idx = st.top(); st.pop();
                result[idx] = i - idx;
            }
            st.push(i);
        }
        return result;
    }
};
