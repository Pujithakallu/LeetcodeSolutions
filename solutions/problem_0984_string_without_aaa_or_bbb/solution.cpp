/*
 * Problem 984: String Without AAA or BBB
 * =====================================
 * Difficulty: Medium
 * Tags: String, Greedy
 * Pattern: Greedy
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(1)
 */

#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string strWithout3a3b(int a, int b) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)a.size(); i++) {
            curr_max = max(curr_max, a[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
