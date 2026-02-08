/*
 * Problem 2103: Rings and Rods
 * ==========================
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
    int countPoints(string& rings) {
        // Hash map for string/character frequency - O(n) time
        unordered_map<char, int> freq;
        for (char ch : rings) {
            freq[ch]++;
        }
        // Process frequency map
        for (int i = 0; i < rings.size(); i++) {
            if (freq[rings[i]] == 1) return i;
        }
        return 0;
    }
};
