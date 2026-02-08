/*
 * Problem 502: IPO
 * ===============
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
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : k) {
            pq.push(val);
            if ((int)pq.size() > w)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
