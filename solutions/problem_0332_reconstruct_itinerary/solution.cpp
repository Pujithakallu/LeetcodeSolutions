/*
 * Problem 332: Reconstruct Itinerary
 * =================================
 * Difficulty: Hard
 * Tags: Array, String, Depth-First Search, Graph Theory, Sorting, Heap (Priority Queue), Eulerian Circuit
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
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : tickets) {
            pq.push(val);
            if ((int)pq.size() > tickets)
                pq.pop();
        }
        return pq.empty() ? {} : pq.top();
    }
};
