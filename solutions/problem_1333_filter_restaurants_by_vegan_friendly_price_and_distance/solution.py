"""
Problem 1333: Filter Restaurants by Vegan-Friendly, Price and Distance
====================================================================
Difficulty: Medium
Tags: Array, Sorting
Pattern: Sorting

Time Complexity:  O(n log n)
Space Complexity: O(n)
"""

class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        # Sort-based approach - O(n log n) time
        restaurants.sort(key=lambda x: x[0] if isinstance(x, (list, tuple)) else x)
        result = [restaurants[0]]
        for i in range(1, len(restaurants)):
            curr = restaurants[i]
            if isinstance(curr, (list, tuple)) and isinstance(result[-1], (list, tuple)):
                if curr[0] <= result[-1][1]:
                    result[-1] = [result[-1][0], max(result[-1][1], curr[1])]
                else:
                    result.append(curr)
            else:
                result.append(curr)
        return result
