/*
 * Problem 875: Koko Eating Bananas
 * ===============================
 * Difficulty: Medium
 * Tags: Array, Binary Search
 * Pattern: Binary Search on Answer
 *
 * Time Complexity:  O(n log m)
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = piles.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (piles[mid] == h) {
                return mid;
            } else if (piles[mid] < h) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
