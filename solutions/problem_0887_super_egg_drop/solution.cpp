/*
 * Problem 887: Super Egg Drop
 * ==========================
 * Difficulty: Hard
 * Tags: Math, Binary Search, Dynamic Programming
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
    int superEggDrop(int k, int n) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = k.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (k[mid] == n) {
                return mid;
            } else if (k[mid] < n) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
