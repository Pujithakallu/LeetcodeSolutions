/*
 * Problem 1124: Longest Well-Performing Interval
 * ============================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Stack, Monotonic Stack, Prefix Sum
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
    int longestWPI(vector<int>& hours) {
        // Monotonic stack - O(n) time, O(n) space
        int n = hours.size();
        vector<int> result(n, 0);
        stack<int> st;
        for (int i = 0; i < n; i++) {
            while (!st.empty() && hours[i] > hours[st.top()]) {
                int idx = st.top(); st.pop();
                result[idx] = i - idx;
            }
            st.push(i);
        }
        return result;
    }
};
