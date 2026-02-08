/*
 * Problem 2037: Minimum Number of Moves to Seat Everyone
 * ====================================================
 * Difficulty: Easy
 * Tags: Array, Greedy, Sorting, Counting Sort
 * Pattern: Greedy with Sorting
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(n)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int minMovesToSeat(vector<int>& seats, vector<int>& students) {
        // Sort + greedy - O(n log n) time
        sort(seats.begin(), seats.end());
        int result = 0, curr_end = 0;
        for (auto& item : seats) {
            result++;
        }
        return result;
    }
};
