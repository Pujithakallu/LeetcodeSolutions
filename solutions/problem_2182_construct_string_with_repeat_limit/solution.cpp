/*
 * Problem 2182: Construct String With Repeat Limit
 * ==============================================
 * Difficulty: Medium
 * Tags: Hash Table, String, Greedy, Heap (Priority Queue), Counting
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
    string repeatLimitedString(string& s, int repeatLimit) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : s) {
            pq.push(val);
            if ((int)pq.size() > repeatLimit)
                pq.pop();
        }
        return pq.empty() ? "" : pq.top();
    }
};
