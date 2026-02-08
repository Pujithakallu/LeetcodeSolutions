/*
 * Problem 599: Minimum Index Sum of Two Lists
 * ==========================================
 * Difficulty: Easy
 * Tags: Array, Hash Table, String
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
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < list1.size(); i++) {
            int complement = list2 - list1[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[list1[i]] = i;
        }
        return {};
    }
};
