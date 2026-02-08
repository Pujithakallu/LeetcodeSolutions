/*
 * Problem 621: Task Scheduler
 * ==========================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Counting
 * Pattern: Greedy / Math
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(1)
 */

#include <queue>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int leastInterval(vector<string>& tasks, int n) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : tasks) {
            pq.push(val);
            if ((int)pq.size() > n)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
