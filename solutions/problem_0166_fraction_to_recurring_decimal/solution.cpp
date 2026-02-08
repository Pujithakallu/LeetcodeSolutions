/*
 * Problem 166: Fraction to Recurring Decimal
 * =========================================
 * Difficulty: Medium
 * Tags: Hash Table, Math, String
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
    string fractionToDecimal(int numerator, int denominator) {
        // Hash map for string/character frequency - O(n) time
        unordered_map<char, int> freq;
        for (char ch : numerator) {
            freq[ch]++;
        }
        // Process frequency map
        for (int i = 0; i < numerator.size(); i++) {
            if (freq[numerator[i]] == 1) return i;
        }
        return "";
    }
};
