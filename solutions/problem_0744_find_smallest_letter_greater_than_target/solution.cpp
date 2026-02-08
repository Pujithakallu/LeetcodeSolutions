/*
 * Problem 744: Find Smallest Letter Greater Than Target
 * ====================================================
 * Difficulty: Easy
 * Tags: Array, Binary Search
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
    string nextGreatestLetter(vector<string>& letters, string& target) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = letters.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (letters[mid] == target) {
                return mid;
            } else if (letters[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return "";
    }
};
