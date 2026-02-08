/*
 * Problem 1790: Check if One String Swap Can Make Strings Equal
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
    bool areAlmostEqual(string& s1, string& s2) {
        // Hash map for string/character frequency - O(n) time
        unordered_map<char, int> freq;
        for (char ch : s1) {
            freq[ch]++;
        }
        // Process frequency map
        for (int i = 0; i < s1.size(); i++) {
            if (freq[s1[i]] == 1) return i;
        }
        return false;
    }
};
