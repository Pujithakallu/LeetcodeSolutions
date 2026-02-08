/*
 * Problem 1268: Search Suggestions System
 * =====================================
 * Difficulty: Medium
 * Tags: Array, String, Binary Search, Trie, Sorting, Heap (Priority Queue)
 * Pattern: Binary Search / Trie
 *
 * Time Complexity:  O(n log n + m*log n)
 * Space Complexity: O(1) extra
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<string>> suggestedProducts(vector<string>& products, string& searchWord) {
        // Trie-based approach
        struct TrieNode {
            TrieNode* children[26] = {};
            bool isEnd = false;
        };
        TrieNode* root = new TrieNode();
        // Build trie
        for (auto& word : products) {
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
