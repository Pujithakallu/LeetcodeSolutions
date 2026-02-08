/*
 * Problem 853: Car Fleet
 * =====================
 * Difficulty: Medium
 * Tags: Array, Stack, Sorting, Monotonic Stack
 * Pattern: Stack / Sorting
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(n)
 */

#include <stack>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        // Monotonic stack - O(n) time, O(n) space
        int n = target.size();
        vector<int> result(n, 0);
        stack<int> st;
        for (int i = 0; i < n; i++) {
            while (!st.empty() && target[i] > target[st.top()]) {
                int idx = st.top(); st.pop();
                result[idx] = i - idx;
            }
            st.push(i);
        }
        return result;
    }
};
