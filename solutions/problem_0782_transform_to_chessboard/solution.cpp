/*
 * Problem 782: Transform to Chessboard
 * ===================================
 * Difficulty: Hard
 * Tags: Array, Math, Bit Manipulation, Matrix
 * Pattern: Bit Manipulation
 *
 * Time Complexity:  O(n) or O(log n)
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int movesToChessboard(vector<vector<int>>& board) {
        // Bit manipulation - O(n) time, O(1) space
        int result = 0;
        for (int val : board) {
            result ^= val;
        }
        return result;
    }
};
