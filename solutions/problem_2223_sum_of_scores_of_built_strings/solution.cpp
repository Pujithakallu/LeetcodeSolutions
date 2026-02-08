/*
 * Problem 2223: Sum of Scores of Built Strings
 * ==========================================
 * Difficulty: Hard
 * Tags: String, Binary Search, Rolling Hash, Suffix Array, String Matching, Hash Function
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
    int sumScores(string& s) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = s.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (s[mid] == s) {
                return mid;
            } else if (s[mid] < s) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
