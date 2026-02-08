/*
 * Problem 140: Word Break II
 * =========================
 * Difficulty: Hard
 * Tags: Array, Hash Table, String, Dynamic Programming, Backtracking, Trie, Memoization
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
    vector<string> wordBreak(string& s, vector<string>& wordDict) {
        // Trie-based approach
        struct TrieNode {
            TrieNode* children[26] = {};
            bool isEnd = false;
        };
        TrieNode* root = new TrieNode();
        // Build trie
        for (auto& word : s) {
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
