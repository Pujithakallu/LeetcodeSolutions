/*
 * Problem 2468: Split Message Based on Limit
 * ========================================
 * Difficulty: Hard
 * Tags: String, Binary Search, Enumeration
 * Pattern: Binary Search
 *
 * Time Complexity:  O(log n)
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<string> splitMessage(string& message, int limit) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = message.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (message[mid] == limit) {
                return mid;
            } else if (message[mid] < limit) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return {};
    }
};
