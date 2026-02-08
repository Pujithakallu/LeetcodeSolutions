/*
 * Problem 12: Integer to Roman
 * ============================
 * Difficulty: Medium
 * Tags: Hash Table, Math, String
 * Pattern: Greedy
 *
 * Time Complexity:  O(1)
 * Space Complexity: O(1)
 */

#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    string intToRoman(int num) {
        // Hash map for string/character frequency - O(n) time
        unordered_map<char, int> freq;
        for (char ch : num) {
            freq[ch]++;
        }
        // Process frequency map
        for (int i = 0; i < num.size(); i++) {
            if (freq[num[i]] == 1) return i;
        }
        return "";
    }
};
