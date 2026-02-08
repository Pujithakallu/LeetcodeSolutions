/*
 * Problem 1499: Max Value of Equation
 * =================================
 * Difficulty: Hard
 * Tags: Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue
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
    int findMaxValueOfEquation(vector<vector<int>>& points, int k) {
        // Monotonic deque - O(n) time
        deque<int> dq;
        vector<int> result;
        int k = k;
        for (int i = 0; i < (int)points.size(); i++) {
            while (!dq.empty() && dq.front() < i - k + 1)
                dq.pop_front();
            while (!dq.empty() && points[dq.back()] < points[i])
                dq.pop_back();
            dq.push_back(i);
            if (i >= k - 1)
                result.push_back(points[dq.front()]);
        }
        return result;
    }
};
