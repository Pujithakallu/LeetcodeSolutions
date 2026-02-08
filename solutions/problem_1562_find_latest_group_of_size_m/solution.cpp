/*
 * Problem 1562: Find Latest Group of Size M
 * =======================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Binary Search, Simulation
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
    int findLatestStep(vector<int>& arr, int m) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = arr.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] == m) {
                return mid;
            } else if (arr[mid] < m) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
