/*
 * Problem 636: Exclusive Time of Functions
 * =======================================
 * Difficulty: Medium
 * Tags: Array, Stack
 * Pattern: Stack
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(n)
 */

#include <stack>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        // Stack-based approach - O(n) time
        stack<char> st;
        unordered_map<char, char> pairs = {{'(', ')'}, {'[', ']'}, {'{', '}'}};
        for (char ch : n) {
            if (!st.empty() && pairs.count(st.top()) && pairs[st.top()] == ch) {
                st.pop();
            } else {
                st.push(ch);
            }
        }
        return st.empty();
    }
};
