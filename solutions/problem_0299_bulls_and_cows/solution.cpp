/*
 * Problem 299: Bulls and Cows
 * ==========================
 * Difficulty: Medium
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
    string getHint(string& secret, string& guess) {
        // Hash map for string/character frequency - O(n) time
        unordered_map<char, int> freq;
        for (char ch : secret) {
            freq[ch]++;
        }
        // Process frequency map
        for (int i = 0; i < secret.size(); i++) {
            if (freq[secret[i]] == 1) return i;
        }
        return "";
    }
};
