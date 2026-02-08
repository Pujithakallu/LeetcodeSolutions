/*
 * Problem 36: Valid Sudoku
 * ========================
 * Difficulty: Medium
 * Tags: Array, Hash Table, Matrix
 * Pattern: Hash Set
 *
 * Time Complexity:  O(1) (fixed 9x9 board)
 * Space Complexity: O(1)
 */

#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<string>>& board) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < board.size(); i++) {
            int complement = board - board[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[board[i]] = i;
        }
        return false;
    }
};
