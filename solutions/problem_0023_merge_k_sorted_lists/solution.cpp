/*
 * Problem 23: Merge k Sorted Lists
 * ================================
 * Difficulty: Hard
 * Tags: Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort
 * Pattern: Heap / Priority Queue
 *
 * Time Complexity:  O(N log k)
 * Space Complexity: O(k)
 */

#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // Merge sort - O(n log n)
        function<void(int, int)> mergeSort = [&](int l, int r) {
            if (l >= r) return;
            int mid = (l + r) / 2;
            mergeSort(l, mid);
            mergeSort(mid + 1, r);
            vector<int> temp;
            int i = l, j = mid + 1;
            while (i <= mid && j <= r) {
                if (lists[i] <= lists[j]) temp.push_back(lists[i++]);
                else temp.push_back(lists[j++]);
            }
            while (i <= mid) temp.push_back(lists[i++]);
            while (j <= r) temp.push_back(lists[j++]);
            for (int k = l; k <= r; k++) lists[k] = temp[k - l];
        };
        mergeSort(0, lists.size() - 1);
        return lists;
    }
};
