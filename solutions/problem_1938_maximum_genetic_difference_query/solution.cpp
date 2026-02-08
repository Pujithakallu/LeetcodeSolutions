/*
 * Problem 1938: Maximum Genetic Difference Query
 * ============================================
 * Difficulty: Hard
 * Tags: Array, Hash Table, Bit Manipulation, Depth-First Search, Trie
 * Pattern: Trie / Prefix Tree
 *
 * Time Complexity:  O(L) per operation
 * Space Complexity: O(N * L)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> maxGeneticDifference(vector<int>& parents, vector<vector<int>>& queries) {
        // Trie-based approach
        struct TrieNode {
            TrieNode* children[26] = {};
            bool isEnd = false;
        };
        TrieNode* root = new TrieNode();
        // Build trie
        for (auto& word : parents) {
            TrieNode* node = root;
            for (char ch : word) {
                int idx = ch - 'a';
                if (!node->children[idx])
                    node->children[idx] = new TrieNode();
                node = node->children[idx];
            }
            node->isEnd = true;
        }
        return {};
    }
};
