/*
 * Problem 275: H-Index II
 * ======================
 * Difficulty: Medium
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
    int hIndex(vector<int>& citations) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = citations.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (citations[mid] == citations) {
                return mid;
            } else if (citations[mid] < citations) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
