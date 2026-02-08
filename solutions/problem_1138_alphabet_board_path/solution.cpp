/*
 * Problem 1138: Alphabet Board Path
 * ===============================
 * Difficulty: Medium
 * Tags: Hash Table, String
 * Pattern: Hash Map String Processing
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(n)
 */

#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    string alphabetBoardPath(string& target) {
        // Hash map for string/character frequency - O(n) time
        unordered_map<char, int> freq;
        for (char ch : target) {
            freq[ch]++;
        }
        // Process frequency map
        for (int i = 0; i < target.size(); i++) {
            if (freq[target[i]] == 1) return i;
        }
        return "";
    }
};
