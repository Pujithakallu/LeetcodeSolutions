/*
 * Problem 1897: Redistribute Characters to Make All Strings Equal
 * =============================================================
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
    bool makeEqual(vector<string>& words) {
        // Hash map for string/character frequency - O(n) time
        unordered_map<char, int> freq;
        for (char ch : words) {
            freq[ch]++;
        }
        // Process frequency map
        for (int i = 0; i < words.size(); i++) {
            if (freq[words[i]] == 1) return i;
        }
        return false;
    }
};
