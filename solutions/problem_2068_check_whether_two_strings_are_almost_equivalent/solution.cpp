/*
 * Problem 2068: Check Whether Two Strings are Almost Equivalent
 * ===========================================================
 * Difficulty: Easy
 * Tags: Hash Table, String, Counting
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
    bool checkAlmostEquivalent(string& word1, string& word2) {
        // Hash map for string/character frequency - O(n) time
        unordered_map<char, int> freq;
        for (char ch : word1) {
            freq[ch]++;
        }
        // Process frequency map
        for (int i = 0; i < word1.size(); i++) {
            if (freq[word1[i]] == 1) return i;
        }
        return false;
    }
};
