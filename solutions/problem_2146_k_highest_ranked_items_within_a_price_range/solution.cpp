/*
 * Problem 2146: K Highest Ranked Items Within a Price Range
 * =======================================================
 * Difficulty: Medium
 * Tags: Array, Breadth-First Search, Sorting, Heap (Priority Queue), Matrix
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
    vector<vector<int>> highestRankedKItems(vector<vector<int>>& grid, vector<int>& pricing, vector<int>& start, int k) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : grid) {
            pq.push(val);
            if ((int)pq.size() > pricing)
                pq.pop();
        }
        return pq.empty() ? {} : pq.top();
    }
};
