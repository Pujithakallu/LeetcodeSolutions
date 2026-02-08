/*
 * Problem 148: Sort List
 * =====================
 * Difficulty: Medium
 * Tags: Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort
 * Pattern: Merge Sort / Linked List
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(log n)
 */

#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    ListNode* sortList(ListNode* head) {
        // Merge sort - O(n log n)
        function<void(int, int)> mergeSort = [&](int l, int r) {
            if (l >= r) return;
            int mid = (l + r) / 2;
            mergeSort(l, mid);
            mergeSort(mid + 1, r);
            vector<int> temp;
            int i = l, j = mid + 1;
            while (i <= mid && j <= r) {
                if (head[i] <= head[j]) temp.push_back(head[i++]);
                else temp.push_back(head[j++]);
            }
            while (i <= mid) temp.push_back(head[i++]);
            while (j <= r) temp.push_back(head[j++]);
            for (int k = l; k <= r; k++) head[k] = temp[k - l];
        };
        mergeSort(0, head.size() - 1);
        return head;
    }
};
