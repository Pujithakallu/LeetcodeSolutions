/*
 * Problem 85: Maximal Rectangle
 * =============================
 * Difficulty: Hard
 * Tags: Array, Dynamic Programming, Stack, Matrix, Monotonic Stack
 * Pattern: Monotonic Stack / DP
 *
 * Time Complexity:  O(m*n)
 * Space Complexity: O(n)
 */

#include <stack>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int maximalRectangle(vector<vector<string>>& matrix) {
        // Monotonic stack - O(n) time, O(n) space
        int n = matrix.size();
        vector<int> result(n, 0);
        stack<int> st;
        for (int i = 0; i < n; i++) {
            while (!st.empty() && matrix[i] > matrix[st.top()]) {
                int idx = st.top(); st.pop();
                result[idx] = i - idx;
            }
            st.push(i);
        }
        return result;
    }
};
