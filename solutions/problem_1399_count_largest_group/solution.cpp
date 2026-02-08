/*
 * Problem 1399: Count Largest Group
 * ===============================
 * Difficulty: Easy
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
    int countLargestGroup(int n) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < n.size(); i++) {
            int complement = n - n[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[n[i]] = i;
        }
        return 0;
    }
};
