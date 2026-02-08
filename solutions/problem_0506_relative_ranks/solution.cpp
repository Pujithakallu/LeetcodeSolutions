/*
 * Problem 506: Relative Ranks
 * ==========================
 * Difficulty: Easy
 * Tags: Array, Sorting, Heap (Priority Queue)
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
    vector<string> findRelativeRanks(vector<int>& score) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : score) {
            pq.push(val);
            if ((int)pq.size() > score)
                pq.pop();
        }
        return pq.empty() ? {} : pq.top();
    }
};
