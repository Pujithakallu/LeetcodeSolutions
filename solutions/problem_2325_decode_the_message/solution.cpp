/*
 * Problem 2325: Decode the Message
 * ==============================
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
    string decodeMessage(string& key, string& message) {
        // Hash map for string/character frequency - O(n) time
        unordered_map<char, int> freq;
        for (char ch : key) {
            freq[ch]++;
        }
        // Process frequency map
        for (int i = 0; i < key.size(); i++) {
            if (freq[key[i]] == 1) return i;
        }
        return "";
    }
};
