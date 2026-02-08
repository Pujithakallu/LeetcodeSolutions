/*
 * Problem 1425: Constrained Subsequence Sum
 * =======================================
 * Difficulty: Hard
 * Tags: Array, Dynamic Programming, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue
 * Pattern: Monotonic Queue / Deque
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(k)
 */

#include <deque>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int constrainedSubsetSum(vector<int>& nums, int k) {
        // Monotonic deque - O(n) time
        deque<int> dq;
        vector<int> result;
        int k = k;
        for (int i = 0; i < (int)nums.size(); i++) {
            while (!dq.empty() && dq.front() < i - k + 1)
                dq.pop_front();
            while (!dq.empty() && nums[dq.back()] < nums[i])
                dq.pop_back();
            dq.push_back(i);
            if (i >= k - 1)
                result.push_back(nums[dq.front()]);
        }
        return result;
    }
};
