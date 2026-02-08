/*
 * Problem 1996: The Number of Weak Characters in the Game
 * =====================================================
 * Difficulty: Medium
 * Tags: Array, Stack, Greedy, Sorting, Monotonic Stack
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
    int numberOfWeakCharacters(vector<vector<int>>& properties) {
        // Monotonic stack - O(n) time, O(n) space
        int n = properties.size();
        vector<int> result(n, 0);
        stack<int> st;
        for (int i = 0; i < n; i++) {
            while (!st.empty() && properties[i] > properties[st.top()]) {
                int idx = st.top(); st.pop();
                result[idx] = i - idx;
            }
            st.push(i);
        }
        return result;
    }
};
