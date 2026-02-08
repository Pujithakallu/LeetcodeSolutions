/*
 * Problem 420: Strong Password Checker
 * ===================================
 * Difficulty: Hard
 * Tags: String, Greedy, Heap (Priority Queue)
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
    int strongPasswordChecker(string& password) {
        // Heap/Priority Queue - O(n log k) time
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int val : password) {
            pq.push(val);
            if ((int)pq.size() > password)
                pq.pop();
        }
        return pq.empty() ? 0 : pq.top();
    }
};
