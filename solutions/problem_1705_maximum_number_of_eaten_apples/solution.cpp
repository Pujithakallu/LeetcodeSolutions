/*
 * Problem 1705: Maximum Number of Eaten Apples
 * ==========================================
 * Difficulty: Medium
 * Tags: Array, Greedy, Heap (Priority Queue)
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
    int eatenApples(vector<int>& apples, vector<int>& days) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : apples) {
            pq.push(val);
            if ((int)pq.size() > days)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
