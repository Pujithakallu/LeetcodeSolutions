/*
 * Problem 383: Ransom Note
 * =======================
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
    bool canConstruct(string& ransomNote, string& magazine) {
        // Hash map for string/character frequency - O(n) time
        unordered_map<char, int> freq;
        for (char ch : ransomNote) {
            freq[ch]++;
        }
        // Process frequency map
        for (int i = 0; i < ransomNote.size(); i++) {
            if (freq[ransomNote[i]] == 1) return i;
        }
        return false;
    }
};
