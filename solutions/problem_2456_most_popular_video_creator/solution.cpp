/*
 * Problem 2456: Most Popular Video Creator
 * ======================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, String, Sorting, Heap (Priority Queue)
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
    vector<vector<string>> mostPopularCreator(vector<string>& creators, vector<string>& ids, vector<int>& views) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : creators) {
            pq.push(val);
            if ((int)pq.size() > ids)
                pq.pop();
        }
        return pq.empty() ? {} : pq.top();
    }
};
