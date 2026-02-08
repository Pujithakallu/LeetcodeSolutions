/*
 * Problem 1263: Minimum Moves to Move a Box to Their Target Location
 * ================================================================
 * Difficulty: Hard
 * Tags: Array, Breadth-First Search, Heap (Priority Queue), Matrix
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
    int minPushBox(vector<vector<string>>& grid) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : grid) {
            pq.push(val);
            if ((int)pq.size() > grid)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
