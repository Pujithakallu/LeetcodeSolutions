/*
 * Problem 1851: Minimum Interval to Include Each Query
 * ==================================================
 * Difficulty: Hard
 * Tags: Array, Binary Search, Sweep Line, Sorting, Heap (Priority Queue)
 * Pattern: Heap + Sorting
 *
 * Time Complexity:  O((n+q) log n)
 * Space Complexity: O(n+q)
 */

#include <queue>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : intervals) {
            pq.push(val);
            if ((int)pq.size() > queries)
                pq.pop();
        }
        return pq.empty() ? {} : pq.top();
    }
};
