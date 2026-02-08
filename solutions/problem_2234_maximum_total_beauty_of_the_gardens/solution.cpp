/*
 * Problem 2234: Maximum Total Beauty of the Gardens
 * ===============================================
 * Difficulty: Hard
 * Tags: Array, Two Pointers, Binary Search, Greedy, Sorting, Enumeration, Prefix Sum
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
    int maximumBeauty(vector<int>& flowers, int newFlowers, int target, int full, int partial) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = flowers.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (flowers[mid] == newFlowers) {
                return mid;
            } else if (flowers[mid] < newFlowers) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
