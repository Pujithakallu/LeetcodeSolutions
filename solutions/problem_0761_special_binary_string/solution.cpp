/*
 * Problem 761: Special Binary String
 * =================================
 * Difficulty: Hard
 * Tags: String, Divide and Conquer, Sorting
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
    string makeLargestSpecial(string& s) {
        // Divide and conquer - O(n log n) time
        function<int(int, int)> solve = [&](int left, int right) -> int {
            if (left >= right) return left < (int)s.size() ? s[left] : 0;
            int mid = (left + right) / 2;
            int leftRes = solve(left, mid);
            int rightRes = solve(mid + 1, right);
            return max(leftRes, rightRes);
        };
        return s.empty() ? "" : solve(0, s.size() - 1);
    }
};
