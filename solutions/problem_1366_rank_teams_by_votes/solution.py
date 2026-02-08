"""
Problem 1366: Rank Teams by Votes
===============================
Difficulty: Medium
Tags: Array, Hash Table, String, Sorting, Counting
Pattern: Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        # Sort-based approach - O(n log n) time
        votes.sort(key=lambda x: x[0] if isinstance(x, (list, tuple)) else x)
        result = [votes[0]]
        for i in range(1, len(votes)):
            curr = votes[i]
            if isinstance(curr, (list, tuple)) and isinstance(result[-1], (list, tuple)):
                if curr[0] <= result[-1][1]:
                    result[-1] = [result[-1][0], max(result[-1][1], curr[1])]
                else:
                    result.append(curr)
            else:
                result.append(curr)
        return result
