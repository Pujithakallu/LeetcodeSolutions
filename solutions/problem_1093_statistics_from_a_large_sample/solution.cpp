/*
 * Problem 1093: Statistics from a Large Sample
 * ==========================================
 * Difficulty: Medium
 * Tags: Array, Math, Probability and Statistics
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
    vector<double> sampleStats(vector<int>& count) {
        // Mathematical approach
        long long result = 0;
        int x = count;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return (int)result;
    }
};
