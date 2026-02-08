# Problem 149: Max Points on a Line

**Difficulty:** Hard  
**Tags:** Array, Hash Table, Math, Geometry  
**Pattern:** Hash Map Lookup  
**Link:** [leetcode.com/problems/max-points-on-a-line](https://leetcode.com/problems/max-points-on-a-line/)

## Description

Given an array of `points` where `points[i] = [xi, yi]` represents a point on the **X-Y** plane, return *the maximum number of points that lie on the same straight line*.

 

Example 1:

```

**Input:** points = [[1,1],[2,2],[3,3]]
**Output:** 3

```

Example 2:

```

**Input:** points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
**Output:** 4

```

 

**Constraints:**

	- `1 <= points.length <= 300`
	- `points[i].length == 2`
	- `-10^4 <= xi, yi <= 10^4`
	- All the `points` are **unique**.

## Approach: Hash Map Lookup

Use a hash map (dictionary) to store elements for O(1) lookup. Iterate through the input, checking membership or counting frequencies in the map.

## Pseudocode

```
1. Initialize hash map
2. Iterate through elements:
   a. Check if target/complement exists in map
   b. If found: process result
   c. Otherwise: store element in map
3. Return result
```

## Algorithm Flow

```mermaid
flowchart TD
    A[Initialize hash map] --> B[For each element]
    B --> C{Target in map?}
    C -- Yes --> D[Process / return result]
    C -- No --> E[Store element in map]
    E --> B
    D --> F[Return answer]
```

## Complexity Analysis

- **Time:** O(n)
- **Space:** O(n)

## Solution (Python3)

```python
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Hash map approach - O(n) time, O(n) space
        seen = {}
        for i, val in enumerate(points):
            complement = points - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
        return 0
```

## Solution (C++)

```cpp
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        // Hash map approach - O(n) time, O(n) space
        unordered_map<int, int> seen;
        for (int i = 0; i < points.size(); i++) {
            int complement = points - points[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[points[i]] = i;
        }
        return 0;
    }
};
```
