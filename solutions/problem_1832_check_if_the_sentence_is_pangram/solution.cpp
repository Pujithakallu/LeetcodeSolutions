/*
 * Problem 1832: Check if the Sentence Is Pangram
 * ============================================
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
    bool checkIfPangram(string& sentence) {
        // Hash map for string/character frequency - O(n) time
        unordered_map<char, int> freq;
        for (char ch : sentence) {
            freq[ch]++;
        }
        // Process frequency map
        for (int i = 0; i < sentence.size(); i++) {
            if (freq[sentence[i]] == 1) return i;
        }
        return false;
    }
};
