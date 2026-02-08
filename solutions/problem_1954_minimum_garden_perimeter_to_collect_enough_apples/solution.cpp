/*
 * Problem 1954: Minimum Garden Perimeter to Collect Enough Apples
 * =============================================================
 * Difficulty: Medium
 * Tags: Math, Binary Search
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
    int minimumPerimeter(int neededApples) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = neededApples.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (neededApples[mid] == neededApples) {
                return mid;
            } else if (neededApples[mid] < neededApples) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
