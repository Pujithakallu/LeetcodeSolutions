/*
 * Problem 496: Next Greater Element I
 * ==================================
 * Difficulty: Easy
 * Tags: Array, Hash Table, Stack, Monotonic Stack
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
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        // Monotonic stack - O(n) time, O(n) space
        int n = nums1.size();
        vector<int> result(n, 0);
        stack<int> st;
        for (int i = 0; i < n; i++) {
            while (!st.empty() && nums1[i] > nums1[st.top()]) {
                int idx = st.top(); st.pop();
                result[idx] = i - idx;
            }
            st.push(i);
        }
        return result;
    }
};
