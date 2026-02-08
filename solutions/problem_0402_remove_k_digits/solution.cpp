/*
 * Problem 402: Remove K Digits
 * ===========================
 * Difficulty: Medium
 * Tags: String, Stack, Greedy, Monotonic Stack
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
    string removeKdigits(string& num, int k) {
        // Monotonic stack - O(n) time, O(n) space
        int n = num.size();
        vector<int> result(n, 0);
        stack<int> st;
        for (int i = 0; i < n; i++) {
            while (!st.empty() && num[i] > num[st.top()]) {
                int idx = st.top(); st.pop();
                result[idx] = i - idx;
            }
            st.push(i);
        }
        return result;
    }
};
