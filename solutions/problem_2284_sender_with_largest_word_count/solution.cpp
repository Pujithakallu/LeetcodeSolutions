/*
 * Problem 2284: Sender With Largest Word Count
 * ==========================================
 * Difficulty: Medium
 * Tags: Array, Hash Table, String, Counting
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
    string largestWordCount(vector<string>& messages, vector<string>& senders) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < messages.size(); i++) {
            int complement = senders - messages[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[messages[i]] = i;
        }
        return "";
    }
};
