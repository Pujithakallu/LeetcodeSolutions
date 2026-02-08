/*
 * Problem 440: K-th Smallest in Lexicographical Order
 * ==================================================
 * Difficulty: Hard
 * Tags: Trie
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
    int findKthNumber(int n, int k) {
        // Trie-based approach
        struct TrieNode {
            TrieNode* children[26] = {};
            bool isEnd = false;
        };
        TrieNode* root = new TrieNode();
        // Build trie
        for (auto& word : n) {
            TrieNode* node = root;
            for (char ch : word) {
                int idx = ch - 'a';
                if (!node->children[idx])
                    node->children[idx] = new TrieNode();
                node = node->children[idx];
            }
            node->isEnd = true;
        }
        return 0;
    }
};
