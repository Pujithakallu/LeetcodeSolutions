/*
 * Problem 114: Flatten Binary Tree to Linked List
 * ==============================================
 * Difficulty: Medium
 * Tags: Linked List, Stack, Tree, Depth-First Search, Binary Tree
 * Pattern: Linked List
 *
 * Time Complexity:  O(n)
 * Space Complexity: O(1)
 */

#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    void flatten(TreeNode* root) {
        // Linked list traversal/manipulation
        ListNode dummy(0);
        dummy.next = root;
        ListNode* prev = &dummy;
        ListNode* curr = root;
        while (curr) {
            ListNode* nxt = curr->next;
            // Process current node
            prev = curr;
            curr = nxt;
        }
        return dummy.next;
    }
};
