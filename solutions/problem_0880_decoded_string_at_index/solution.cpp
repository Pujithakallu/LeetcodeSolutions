/*
 * Problem 880: Decoded String at Index
 * ===================================
 * Difficulty: Medium
 * Tags: String, Stack
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
    string decodeAtIndex(string& s, int k) {
        // Stack-based approach - O(n) time
        stack<char> st;
        unordered_map<char, char> pairs = {{'(', ')'}, {'[', ']'}, {'{', '}'}};
        for (char ch : s) {
            if (!st.empty() && pairs.count(st.top()) && pairs[st.top()] == ch) {
                st.pop();
            } else {
                st.push(ch);
            }
        }
        return st.empty();
    }
};
