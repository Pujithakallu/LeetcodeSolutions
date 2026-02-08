/*
 * Problem 932: Beautiful Array
 * ===========================
 * Difficulty: Medium
 * Tags: Array, Math, Divide and Conquer
 * Pattern: Divide and Conquer
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(n)
 */

#include <algorithm>
#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> beautifulArray(int n) {
        // Divide and conquer - O(n log n) time
        function<int(int, int)> solve = [&](int left, int right) -> int {
            if (left >= right) return left < (int)n.size() ? n[left] : 0;
            int mid = (left + right) / 2;
            int leftRes = solve(left, mid);
            int rightRes = solve(mid + 1, right);
            return max(leftRes, rightRes);
        };
        return n.empty() ? {} : solve(0, n.size() - 1);
    }
};
