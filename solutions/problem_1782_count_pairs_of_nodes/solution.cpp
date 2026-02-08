/*
 * Problem 1782: Count Pairs Of Nodes
 * ================================
 * Difficulty: Hard
 * Tags: Array, Hash Table, Two Pointers, Binary Search, Graph Theory, Sorting, Counting
 * Pattern: Binary Search
 *
 * Time Complexity:  O(log n)
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> countPairs(int n, vector<vector<int>>& edges, vector<int>& queries) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = n.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (n[mid] == edges) {
                return mid;
            } else if (n[mid] < edges) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return {};
    }
};
