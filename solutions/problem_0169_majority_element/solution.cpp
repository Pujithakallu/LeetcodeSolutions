/*
 * Problem 169: Majority Element
 * ============================
 * Difficulty: Easy
 * Tags: Array, Hash Table, Divide and Conquer, Sorting, Counting
 * Pattern: Boyer-Moore Voting
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(1)
 */

#include <algorithm>
#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        // Divide and conquer - O(n log n) time
        function<int(int, int)> solve = [&](int left, int right) -> int {
            if (left >= right) return left < (int)nums.size() ? nums[left] : 0;
            int mid = (left + right) / 2;
            int leftRes = solve(left, mid);
            int rightRes = solve(mid + 1, right);
            return max(leftRes, rightRes);
        };
        return nums.empty() ? 0 : solve(0, nums.size() - 1);
    }
};
