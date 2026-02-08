/*
 * Problem 771: Jewels and Stones
 * =============================
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
    int numJewelsInStones(string& jewels, string& stones) {
        // Hash map for string/character frequency - O(n) time
        unordered_map<char, int> freq;
        for (char ch : jewels) {
            freq[ch]++;
        }
        // Process frequency map
        for (int i = 0; i < jewels.size(); i++) {
            if (freq[jewels[i]] == 1) return i;
        }
        return 0;
    }
};
