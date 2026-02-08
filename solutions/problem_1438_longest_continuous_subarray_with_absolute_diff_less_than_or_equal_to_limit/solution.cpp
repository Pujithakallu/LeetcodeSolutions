/*
 * Problem 1438: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
 * ======================================================================================
 * Difficulty: Medium
 * Tags: Array, Queue, Sliding Window, Heap (Priority Queue), Ordered Set, Monotonic Queue
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
    int longestSubarray(vector<int>& nums, int limit) {
        // Monotonic deque - O(n) time
        deque<int> dq;
        vector<int> result;
        int k = limit;
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
