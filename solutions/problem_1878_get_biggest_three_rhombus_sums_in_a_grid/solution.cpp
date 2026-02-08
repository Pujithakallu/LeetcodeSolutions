/*
 * Problem 1878: Get Biggest Three Rhombus Sums in a Grid
 * ====================================================
 * Difficulty: Medium
 * Tags: Array, Math, Sorting, Heap (Priority Queue), Matrix, Prefix Sum
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
    vector<int> getBiggestThree(vector<vector<int>>& grid) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : grid) {
            pq.push(val);
            if ((int)pq.size() > grid)
                pq.pop();
        }
        return pq.empty() ? {} : pq.top();
    }
};
