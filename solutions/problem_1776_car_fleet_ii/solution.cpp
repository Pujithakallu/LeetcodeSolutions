/*
 * Problem 1776: Car Fleet II
 * ========================
 * Difficulty: Hard
 * Tags: Array, Math, Stack, Heap (Priority Queue), Monotonic Stack
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
    vector<double> getCollisionTimes(vector<vector<int>>& cars) {
        // Monotonic stack - O(n) time, O(n) space
        int n = cars.size();
        vector<int> result(n, 0);
        stack<int> st;
        for (int i = 0; i < n; i++) {
            while (!st.empty() && cars[i] > cars[st.top()]) {
                int idx = st.top(); st.pop();
                result[idx] = i - idx;
            }
            st.push(i);
        }
        return result;
    }
};
