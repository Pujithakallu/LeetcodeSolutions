/*
 * Problem 871: Minimum Number of Refueling Stops
 * =============================================
 * Difficulty: Hard
 * Tags: Array, Dynamic Programming, Greedy, Heap (Priority Queue)
 * Pattern: Heap / Priority Queue
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(n)
 */

#include <queue>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int minRefuelStops(int target, int startFuel, vector<vector<int>>& stations) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : target) {
            pq.push(val);
            if ((int)pq.size() > startFuel)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
