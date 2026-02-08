/*
 * Problem 1526: Minimum Number of Increments on Subarrays to Form a Target Array
 * ============================================================================
 * Difficulty: Hard
 * Tags: Array, Dynamic Programming, Stack, Greedy, Monotonic Stack
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
    int minNumberOperations(vector<int>& target) {
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
