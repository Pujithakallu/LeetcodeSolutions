"""
Problem 1610: Maximum Number of Visible Points
============================================
Difficulty: Hard
Tags: Array, Math, Geometry, Sliding Window, Sorting
Pattern: Sliding Window

Time Complexity:  O(n)
Space Complexity: O(k)
"""

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        # Sliding window approach - O(n) time, O(k) space
        from collections import defaultdict
        window = defaultdict(int)
        left = 0
        result = 0
        for right in range(len(points)):
            window[points[right]] += 1
            while len(window) > (angle if isinstance(angle, int) else len(points)):
                window[points[left]] -= 1
                if window[points[left]] == 0:
                    del window[points[left]]
                left += 1
            result = max(result, right - left + 1)
        return result
