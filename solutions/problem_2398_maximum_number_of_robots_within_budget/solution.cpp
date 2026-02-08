/*
 * Problem 2398: Maximum Number of Robots Within Budget
 * ==================================================
 * Difficulty: Hard
 * Tags: Array, Binary Search, Queue, Sliding Window, Heap (Priority Queue), Prefix Sum, Monotonic Queue
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
    int maximumRobots(vector<int>& chargeTimes, vector<int>& runningCosts, int budget) {
        // Monotonic deque - O(n) time
        deque<int> dq;
        vector<int> result;
        int k = runningCosts;
        for (int i = 0; i < (int)chargeTimes.size(); i++) {
            while (!dq.empty() && dq.front() < i - k + 1)
                dq.pop_front();
            while (!dq.empty() && chargeTimes[dq.back()] < chargeTimes[i])
                dq.pop_back();
            dq.push_back(i);
            if (i >= k - 1)
                result.push_back(chargeTimes[dq.front()]);
        }
        return result;
    }
};
