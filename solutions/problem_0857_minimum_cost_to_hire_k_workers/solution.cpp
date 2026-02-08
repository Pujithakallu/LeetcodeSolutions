/*
 * Problem 857: Minimum Cost to Hire K Workers
 * ==========================================
 * Difficulty: Hard
 * Tags: Array, Greedy, Sorting, Heap (Priority Queue)
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
    double mincostToHireWorkers(vector<int>& quality, vector<int>& wage, int k) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : quality) {
            pq.push(val);
            if ((int)pq.size() > wage)
                pq.pop();
        }
        return pq.empty() ? 0.0 : pq.top();
    }
};
