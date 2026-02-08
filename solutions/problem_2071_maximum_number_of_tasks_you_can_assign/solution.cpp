/*
 * Problem 2071: Maximum Number of Tasks You Can Assign
 * ==================================================
 * Difficulty: Hard
 * Tags: Array, Two Pointers, Binary Search, Greedy, Queue, Sorting, Monotonic Queue
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
    int maxTaskAssign(vector<int>& tasks, vector<int>& workers, int pills, int strength) {
        // Monotonic deque - O(n) time
        deque<int> dq;
        vector<int> result;
        int k = workers;
        for (int i = 0; i < (int)tasks.size(); i++) {
            while (!dq.empty() && dq.front() < i - k + 1)
                dq.pop_front();
            while (!dq.empty() && tasks[dq.back()] < tasks[i])
                dq.pop_back();
            dq.push_back(i);
            if (i >= k - 1)
                result.push_back(tasks[dq.front()]);
        }
        return result;
    }
};
