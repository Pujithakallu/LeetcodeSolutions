/*
 * Problem 1713: Minimum Operations to Make a Subsequence
 * ====================================================
 * Difficulty: Hard
 * Tags: Array, Hash Table, Binary Search, Greedy
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
    int minOperations(vector<int>& target, vector<int>& arr) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = target.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (target[mid] == arr) {
                return mid;
            } else if (target[mid] < arr) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
