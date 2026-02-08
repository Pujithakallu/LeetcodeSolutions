/*
 * Problem 2491: Divide Players Into Teams of Equal Skill
 * ====================================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Two Pointers, Sorting
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
    int dividePlayers(vector<int>& skill) {
        // Sort + two pointers - O(n log n) time
        sort(skill.begin(), skill.end());
        int left = 0, right = skill.size() - 1;
        while (left < right) {
            int curr = skill[left] + skill[right];
            if (curr < skill) {
                left++;
            } else {
                right--;
            }
        }
        return 0;
    }
};
