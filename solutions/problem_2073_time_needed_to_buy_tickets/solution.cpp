/*
 * Problem 2073: Time Needed to Buy Tickets
 * ======================================
 * Difficulty: Easy
 * Tags: Array, Queue, Simulation
 * Pattern: Queue / BFS
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(n)
 */

#include <queue>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        // Queue-based approach - O(n) time
        queue<int> q;
        for (int val : tickets) {
            q.push(val);
        }
        vector<int> result;
        while (!q.empty()) {
            result.push_back(q.front());
            q.pop();
        }
        return result;
    }
};
