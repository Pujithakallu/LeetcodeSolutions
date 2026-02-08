/*
 * Problem 155: Min Stack
 * =====================
 * Difficulty: Medium
 * Tags: Stack, Design
 * Pattern: Stack / Design
 *
 * Time Complexity:  O(1) per operation
 * Space Complexity: O(n)
 */

class MinStack {
    stack<int> st, minSt;
public:
    MinStack() {}
    void push(int val) {
        st.push(val);
        minSt.push(minSt.empty() ? val : min(val, minSt.top()));
    }
    void pop() { st.pop(); minSt.pop(); }
    int top() { return st.top(); }
    int getMin() { return minSt.top(); }
};
