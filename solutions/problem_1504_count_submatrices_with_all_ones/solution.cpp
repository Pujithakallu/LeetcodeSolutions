/*
 * Problem 1504: Count Submatrices With All Ones
 * ===========================================
 * Difficulty: Medium
 * Tags: Array, Dynamic Programming, Stack, Matrix, Monotonic Stack
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
    int numSubmat(vector<vector<int>>& mat) {
        // Monotonic stack - O(n) time, O(n) space
        int n = mat.size();
        vector<int> result(n, 0);
        stack<int> st;
        for (int i = 0; i < n; i++) {
            while (!st.empty() && mat[i] > mat[st.top()]) {
                int idx = st.top(); st.pop();
                result[idx] = i - idx;
            }
            st.push(i);
        }
        return result;
    }
};
