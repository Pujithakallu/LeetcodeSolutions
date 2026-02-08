/*
 * Problem 2487: Remove Nodes From Linked List
 * =========================================
 * Difficulty: Medium
 * Tags: Linked List, Stack, Recursion, Monotonic Stack
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
    ListNode* removeNodes(ListNode* head) {
        // Monotonic stack - O(n) time, O(n) space
        int n = head.size();
        vector<int> result(n, 0);
        stack<int> st;
        for (int i = 0; i < n; i++) {
            while (!st.empty() && head[i] > head[st.top()]) {
                int idx = st.top(); st.pop();
                result[idx] = i - idx;
            }
            st.push(i);
        }
        return result;
    }
};
