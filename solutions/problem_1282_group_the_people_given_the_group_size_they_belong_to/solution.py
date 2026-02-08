"""
Problem 1282: Group the People Given the Group Size They Belong To
================================================================
Difficulty: Medium
Tags: Array, Hash Table, Greedy
Pattern: Greedy

Time Complexity:  O(n log n)
Space Complexity: O(1)
"""

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(groupSizes)):
            if isinstance(groupSizes[i], int):
                curr_max = max(curr_max, groupSizes[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
