/*
 * Problem 2416: Sum of Prefix Scores of Strings
 * ===========================================
 * Difficulty: Hard
 * Tags: Array, String, Trie, Counting
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
    vector<int> sumPrefixScores(vector<string>& words) {
        // Trie-based approach
        struct TrieNode {
            TrieNode* children[26] = {};
            bool isEnd = false;
        };
        TrieNode* root = new TrieNode();
        // Build trie
        for (auto& word : words) {
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
