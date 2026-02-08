/*
 * Problem 524: Longest Word in Dictionary through Deleting
 * =======================================================
 * Difficulty: Medium
 * Tags: Array, Two Pointers, String, Sorting
 * Pattern: Two Pointers on Sorted Array
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(1)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string findLongestWord(string& s, vector<string>& dictionary) {
        // Sort + two pointers - O(n log n) time
        sort(s.begin(), s.end());
        int left = 0, right = s.size() - 1;
        while (left < right) {
            int curr = s[left] + s[right];
            if (curr < dictionary) {
                left++;
            } else {
                right--;
            }
        }
        return "";
    }
};
