# Problem 447: Number of Boomerangs

**Difficulty:** Medium  
**Tags:** Array, Hash Table, Math  
**Pattern:** Hash Map Lookup  
**Link:** [leetcode.com/problems/number-of-boomerangs](https://leetcode.com/problems/number-of-boomerangs/)

## Description

You are given `n` `points` in the plane that are all **distinct**, where `points[i] = [xi, yi]`. A **boomerang** is a tuple of points `(i, j, k)` such that the distance between `i` and `j` equals the distance between `i` and `k` **(the order of the tuple matters)**.

Return *the number of boomerangs*.

 

Example 1:

```

**Input:** points = [[0,0],[1,0],[2,0]]
**Output:** 2
**Explanation:** The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].

```

Example 2:

```

**Input:** points = [[1,1],[2,2],[3,3]]
**Output:** 2

```

Example 3:

```

**Input:** points = [[1,1]]
**Output:** 0

```

 

**Constraints:**

	- `n == points.length`
	- `1 <= n <= 500`
	- `points[i].length == 2`
	- `-10^4 <= xi, yi <= 10^4`
	- All the points are **unique**.

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
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
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
    int numberOfBoomerangs(vector<vector<int>>& points) {
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
