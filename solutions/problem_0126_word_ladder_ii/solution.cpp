/*
 * Problem 126: Word Ladder II
 * ==========================
 * Difficulty: Hard
 * Tags: Hash Table, String, Backtracking, Breadth-First Search
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
    vector<vector<string>> findLadders(string& beginWord, string& endWord, vector<string>& wordList) {
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(path);
            for (int i = start; i < (int)beginWord.size(); i++) {
                path.push_back(beginWord[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
