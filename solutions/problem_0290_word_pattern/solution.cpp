/*
 * Problem 290: Word Pattern
 * ========================
 * Difficulty: Easy
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
    bool wordPattern(string& pattern, string& s) {
        // Hash map for string/character frequency - O(n) time
        unordered_map<char, int> freq;
        for (char ch : pattern) {
            freq[ch]++;
        }
        // Process frequency map
        for (int i = 0; i < pattern.size(); i++) {
            if (freq[pattern[i]] == 1) return i;
        }
        return false;
    }
};
