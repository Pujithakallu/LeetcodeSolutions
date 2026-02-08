/*
 * Problem 2290: Minimum Obstacle Removal to Reach Corner
 * ====================================================
 * Difficulty: Hard
 * Tags: Array, Breadth-First Search, Graph Theory, Heap (Priority Queue), Matrix, Shortest Path
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
    int minimumObstacles(vector<vector<int>>& grid) {
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
