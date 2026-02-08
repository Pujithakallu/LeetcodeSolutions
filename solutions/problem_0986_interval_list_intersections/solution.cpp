/*
 * Problem 986: Interval List Intersections
 * =======================================
 * Difficulty: Medium
 * Tags: Array, Two Pointers, Sweep Line
 * Pattern: Two Pointers
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& firstList, vector<vector<int>>& secondList) {
        // Two pointer approach - O(n) time, O(1) space
        int left = 0, right = firstList.size() - 1;
        while (left < right) {
            int curr = firstList[left] + firstList[right];
            if (curr == secondList) {
                return {left, right};
            } else if (curr < secondList) {
                left++;
            } else {
                right--;
            }
        }
        return {};
    }
};
