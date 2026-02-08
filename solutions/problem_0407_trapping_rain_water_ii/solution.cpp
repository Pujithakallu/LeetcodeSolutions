/*
 * Problem 407: Trapping Rain Water II
 * ==================================
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
    int trapRainWater(vector<vector<int>>& heightMap) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : heightMap) {
            pq.push(val);
            if ((int)pq.size() > heightMap)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
