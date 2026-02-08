/*
 * Problem 2285: Maximum Total Importance of Roads
 * =============================================
 * Difficulty: Medium
 * Tags: Greedy, Graph Theory, Sorting, Heap (Priority Queue)
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
    int maximumImportance(int n, vector<vector<int>>& roads) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : n) {
            pq.push(val);
            if ((int)pq.size() > roads)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
