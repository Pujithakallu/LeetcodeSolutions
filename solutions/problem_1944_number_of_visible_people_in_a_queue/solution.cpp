/*
 * Problem 1944: Number of Visible People in a Queue
 * ===============================================
 * Difficulty: Hard
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
    vector<int> canSeePersonsCount(vector<int>& heights) {
        // Monotonic stack - O(n) time, O(n) space
        int n = heights.size();
        vector<int> result(n, 0);
        stack<int> st;
        for (int i = 0; i < n; i++) {
            while (!st.empty() && heights[i] > heights[st.top()]) {
                int idx = st.top(); st.pop();
                result[idx] = i - idx;
            }
            st.push(i);
        }
        return result;
    }
};
