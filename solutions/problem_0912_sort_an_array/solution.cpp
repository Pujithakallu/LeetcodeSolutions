/*
 * Problem 912: Sort an Array
 * =========================
 * Difficulty: Medium
 * Tags: Array, Divide and Conquer, Sorting, Heap (Priority Queue), Merge Sort, Bucket Sort, Radix Sort, Counting Sort
 * Pattern: Merge Sort
 *
 * Time Complexity:  O(n log n)
 * Space Complexity: O(n)
 */

#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        // Merge sort - O(n log n)
        function<void(int, int)> mergeSort = [&](int l, int r) {
            if (l >= r) return;
            int mid = (l + r) / 2;
            mergeSort(l, mid);
            mergeSort(mid + 1, r);
            vector<int> temp;
            int i = l, j = mid + 1;
            while (i <= mid && j <= r) {
                if (nums[i] <= nums[j]) temp.push_back(nums[i++]);
                else temp.push_back(nums[j++]);
            }
            while (i <= mid) temp.push_back(nums[i++]);
            while (j <= r) temp.push_back(nums[j++]);
            for (int k = l; k <= r; k++) nums[k] = temp[k - l];
        };
        mergeSort(0, nums.size() - 1);
        return nums;
    }
};
