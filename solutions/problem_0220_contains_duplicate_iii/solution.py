"""
Problem 220: Contains Duplicate III
==================================
Difficulty: Hard
Tags: Array, Sliding Window, Sorting, Bucket Sort, Ordered Set
Pattern: Sliding Window

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # Sliding window approach - O(n) time, O(k) space
        from collections import defaultdict
        window = defaultdict(int)
        left = 0
        result = 0
        for right in range(len(nums)):
            window[nums[right]] += 1
            while len(window) > (indexDiff if isinstance(indexDiff, int) else len(nums)):
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1
            result = max(result, right - left + 1)
        return result
