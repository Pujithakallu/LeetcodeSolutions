/*
 * Problem 2406: Divide Intervals Into Minimum Number of Groups
 * ==========================================================
 * Difficulty: Medium
 * Tags: Array, Two Pointers, Greedy, Sorting, Heap (Priority Queue), Prefix Sum
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
    int minGroups(vector<vector<int>>& intervals) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : intervals) {
            pq.push(val);
            if ((int)pq.size() > intervals)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
