/*
 * Problem 167: Two Sum II - Input Array Is Sorted
 * ==============================================
 * Difficulty: Medium
 * Tags: Array, Two Pointers, Binary Search
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
    vector<int> twoSum(vector<int>& numbers, int target) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = numbers.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (numbers[mid] == target) {
                return mid;
            } else if (numbers[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return {};
    }
};
