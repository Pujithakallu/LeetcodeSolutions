/*
 * Problem 843: Guess the Word
 * ==========================
 * Difficulty: Hard
 * Tags: Array, Math, String, Interactive, Game Theory
 * Pattern: Math
 *
 * Time Complexity:  O(n) or O(sqrt(n))
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    void findSecretWord(vector<string>& words, 'Master' master) {
        // Mathematical approach
        long long result = 0;
        int x = words;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return (int)result;
    }
};
