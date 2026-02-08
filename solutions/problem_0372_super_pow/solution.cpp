/*
 * Problem 372: Super Pow
 * =====================
 * Difficulty: Medium
 * Tags: Math, Divide and Conquer
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
    int superPow(int a, vector<int>& b) {
        // Divide and conquer - O(n log n) time
        function<int(int, int)> solve = [&](int left, int right) -> int {
            if (left >= right) return left < (int)a.size() ? a[left] : 0;
            int mid = (left + right) / 2;
            int leftRes = solve(left, mid);
            int rightRes = solve(mid + 1, right);
            return max(leftRes, rightRes);
        };
        return a.empty() ? 0 : solve(0, a.size() - 1);
    }
};
