/*
 * Problem 1079: Letter Tile Possibilities
 * =====================================
 * Difficulty: Medium
 * Tags: Hash Table, String, Backtracking, Counting
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
    int numTilePossibilities(string& tiles) {
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(path);
            for (int i = start; i < (int)tiles.size(); i++) {
                path.push_back(tiles[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
