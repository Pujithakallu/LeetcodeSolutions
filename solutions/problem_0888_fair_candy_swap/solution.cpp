/*
 * Problem 888: Fair Candy Swap
 * ===========================
 * Difficulty: Easy
 * Tags: Array, Hash Table, Binary Search, Sorting
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
    vector<int> fairCandySwap(vector<int>& aliceSizes, vector<int>& bobSizes) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = aliceSizes.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (aliceSizes[mid] == bobSizes) {
                return mid;
            } else if (aliceSizes[mid] < bobSizes) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return {};
    }
};
