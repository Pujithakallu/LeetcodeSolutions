/*
 * Problem 42: Trapping Rain Water
 * ===============================
 * Difficulty: Hard
 * Tags: Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack
 * Pattern: Two Pointers
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(1)
 */

#include <stack>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        // Monotonic stack - O(n) time, O(n) space
        int n = height.size();
        vector<int> result(n, 0);
        stack<int> st;
        for (int i = 0; i < n; i++) {
            while (!st.empty() && height[i] > height[st.top()]) {
                int idx = st.top(); st.pop();
                result[idx] = i - idx;
            }
            st.push(i);
        }
        return result;
    }
};
