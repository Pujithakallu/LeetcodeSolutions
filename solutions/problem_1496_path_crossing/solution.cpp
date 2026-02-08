/*
 * Problem 1496: Path Crossing
 * =========================
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
    bool isPathCrossing(string& path) {
        // Hash map for string/character frequency - O(n) time
        unordered_map<char, int> freq;
        for (char ch : path) {
            freq[ch]++;
        }
        // Process frequency map
        for (int i = 0; i < path.size(); i++) {
            if (freq[path[i]] == 1) return i;
        }
        return false;
    }
};
