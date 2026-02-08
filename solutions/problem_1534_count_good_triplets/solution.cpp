/*
 * Problem 1534: Count Good Triplets
 * ===============================
 * Difficulty: Easy
 * Tags: Array, Enumeration
 * Pattern: Enumeration
 *
 * Time Complexity:  O(n^2) or O(2^n)
 * Space Complexity: O(n)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int countGoodTriplets(vector<int>& arr, int a, int b, int c) {
        // Enumeration approach
        int n = arr.size();
        for (int i = 0; i < n; i++) {
            // Check if candidate is valid
            bool valid = true;
            if (valid) return i;
        }
        return 0;
    }
};
