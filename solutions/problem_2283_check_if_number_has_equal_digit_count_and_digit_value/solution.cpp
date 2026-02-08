/*
 * Problem 2283: Check if Number Has Equal Digit Count and Digit Value
 * =================================================================
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
    bool digitCount(string& num) {
        // Hash map for string/character frequency - O(n) time
        unordered_map<char, int> freq;
        for (char ch : num) {
            freq[ch]++;
        }
        // Process frequency map
        for (int i = 0; i < num.size(); i++) {
            if (freq[num[i]] == 1) return i;
        }
        return false;
    }
};
