# Problem 2087: Minimum Cost Homecoming of a Robot in a Grid

**Difficulty:** Medium  
**Tags:** Array, Greedy  
**Pattern:** Greedy  
**Link:** [leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid](https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/)

## Description

There is an `m x n` grid, where `(0, 0)` is the top-left cell and `(m - 1, n - 1)` is the bottom-right cell. You are given an integer array `startPos` where `startPos = [startrow, startcol]` indicates that **initially**, a **robot** is at the cell `(startrow, startcol)`. You are also given an integer array `homePos` where `homePos = [homerow, homecol]` indicates that its **home** is at the cell `(homerow, homecol)`.

The robot needs to go to its home. It can move one cell in four directions: **left**, **right**, **up**, or **down**, and it can not move outside the boundary. Every move incurs some cost. You are further given two **0-indexed** integer arrays: `rowCosts` of length `m` and `colCosts` of length `n`.

	- If the robot moves **up** or **down** into a cell whose **row** is `r`, then this move costs `rowCosts[r]`.
	- If the robot moves **left** or **right** into a cell whose **column** is `c`, then this move costs `colCosts[c]`.

Return *the **minimum total cost** for this robot to return home*.

 

Example 1:

```

**Input:** startPos = [1, 0], homePos = [2, 3], rowCosts = [5, 4, 3], colCosts = [8, 2, 6, 7]
**Output:** 18
**Explanation:** One optimal path is that:
Starting from (1, 0)
-> It goes down to (**2**, 0). This move costs rowCosts[2] = 3.
-> It goes right to (2, **1**). This move costs colCosts[1] = 2.
-> It goes right to (2, **2**). This move costs colCosts[2] = 6.
-> It goes right to (2, **3**). This move costs colCosts[3] = 7.
The total cost is 3 + 2 + 6 + 7 = 18
```

Example 2:

```

**Input:** startPos = [0, 0], homePos = [0, 0], rowCosts = [5], colCosts = [26]
**Output:** 0
**Explanation:** The robot is already at its home. Since no moves occur, the total cost is 0.

```

 

**Constraints:**

	- `m == rowCosts.length`
	- `n == colCosts.length`
	- `1 <= m, n <= 10^5`
	- `0 <= rowCosts[r], colCosts[c] <= 10^4`
	- `startPos.length == 2`
	- `homePos.length == 2`
	- `0 <= startrow, homerow < m`
	- `0 <= startcol, homecol < n`

## Approach: Greedy

Make the locally optimal choice at each step, trusting it leads to a global optimum. Greedy works when the problem has the greedy-choice property and optimal substructure.

## Pseudocode

```
1. Sort or organize data for greedy ordering
2. Initialize result
3. For each element in greedy order:
   a. If element satisfies constraint:
      - Take the greedy choice
      - Update result and state
4. Return result
```

## Algorithm Flow

```mermaid
flowchart TD
    A[Sort / organize for greedy order] --> B[Initialize result]
    B --> C[For each element in order]
    C --> D{Satisfies constraint?}
    D -- Yes --> E[Take greedy choice]
    E --> F[Update result and state]
    D -- No --> G[Skip element]
    F --> C
    G --> C
    C --> H[Return result]
```

## Complexity Analysis

- **Time:** O(n log n)
- **Space:** O(1)

## Solution (Python3)

```python
class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(startPos)):
            if isinstance(startPos[i], int):
                curr_max = max(curr_max, startPos[i])
                result = max(result, curr_max)
            else:
                result += 1
        return result
```

## Solution (C++)

```cpp
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int minCost(vector<int>& startPos, vector<int>& homePos, vector<int>& rowCosts, vector<int>& colCosts) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)startPos.size(); i++) {
            curr_max = max(curr_max, startPos[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
```
