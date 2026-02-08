/*
 * Problem 387: First Unique Character in a String
 * ==============================================
 * Difficulty: Easy
 * Tags: Hash Table, String, Queue, Counting
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
    int firstUniqChar(string& s) {
        // Queue-based approach - O(n) time
        queue<int> q;
        for (int val : s) {
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
