/*
 * Problem 691: Stickers to Spell Word
 * ==================================
 * Difficulty: Hard
 * Tags: Array, Hash Table, String, Dynamic Programming, Backtracking, Bit Manipulation, Memoization, Bitmask
 * Pattern: Backtracking
 *
 * Time Complexity:  O(k^n) or O(n!)
 * Space Complexity: O(n)
 */

#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int minStickers(vector<string>& stickers, string& target) {
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(path);
            for (int i = start; i < (int)stickers.size(); i++) {
                path.push_back(stickers[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
