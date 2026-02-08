/*
 * Problem 470: Implement Rand10() Using Rand7()
 * ============================================
 * Difficulty: Medium
 * Tags: Math, Rejection Sampling, Randomized, Probability and Statistics
 * Pattern: Randomized Algorithm
 *
 * Time Complexity:  O(n) or varies
 * Space Complexity: O(n)
 */

#include <cstdlib>
#include <ctime>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    void rand10() {
        // Randomized approach (Fisher-Yates shuffle)
        vector<int> arr = nums;
        srand(time(0));
        for (int i = arr.size() - 1; i > 0; i--) {
            int j = rand() % (i + 1);
            swap(arr[i], arr[j]);
        }
        return arr;
    }
};
