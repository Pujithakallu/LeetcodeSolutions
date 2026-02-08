/*
 * Problem 2300: Successful Pairs of Spells and Potions
 * ==================================================
 * Difficulty: Medium
 * Tags: Array, Two Pointers, Binary Search, Sorting
 * Pattern: Binary Search + Sorting
 *
 * Time Complexity:  O((m+n) log n)
 * Space Complexity: O(1) extra
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, int success) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = spells.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (spells[mid] == potions) {
                return mid;
            } else if (spells[mid] < potions) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return {};
    }
};
