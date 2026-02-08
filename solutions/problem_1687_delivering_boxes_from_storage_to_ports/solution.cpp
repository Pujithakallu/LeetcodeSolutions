/*
 * Problem 1687: Delivering Boxes from Storage to Ports
 * ==================================================
 * Difficulty: Hard
 * Tags: Array, Dynamic Programming, Segment Tree, Queue, Heap (Priority Queue), Prefix Sum, Monotonic Queue
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
    int boxDelivering(vector<vector<int>>& boxes, int portsCount, int maxBoxes, int maxWeight) {
        // Monotonic deque - O(n) time
        deque<int> dq;
        vector<int> result;
        int k = portsCount;
        for (int i = 0; i < (int)boxes.size(); i++) {
            while (!dq.empty() && dq.front() < i - k + 1)
                dq.pop_front();
            while (!dq.empty() && boxes[dq.back()] < boxes[i])
                dq.pop_back();
            dq.push_back(i);
            if (i >= k - 1)
                result.push_back(boxes[dq.front()]);
        }
        return result;
    }
};
