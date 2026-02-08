/*
 * Problem 1880: Check if Word Equals Summation of Two Words
 * =======================================================
 * Difficulty: Easy
 * Tags: String
 * Pattern: String Processing
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(n)
 */

#include <algorithm>
#include <cctype>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool isSumEqual(string& firstWord, string& secondWord, string& targetWord) {
        // String processing approach - O(n) time
        string processed;
        for (char ch : firstWord) {
            if (isalnum(ch)) {
                processed += tolower(ch);
            }
        }
        string rev = processed;
        reverse(rev.begin(), rev.end());
        return processed == rev;
    }
};
