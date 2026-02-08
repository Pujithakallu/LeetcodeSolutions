/*
 * Problem 1015: Smallest Integer Divisible by K
 * ===========================================
 * Difficulty: Medium
 * Tags: Hash Table, Math
 * Pattern: Hash Map Lookup
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
    int smallestRepunitDivByK(int k) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < k.size(); i++) {
            int complement = k - k[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[k[i]] = i;
        }
        return 0;
    }
};
