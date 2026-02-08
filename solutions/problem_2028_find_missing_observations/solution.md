# Problem 2028: Find Missing Observations

**Difficulty:** Medium  
**Tags:** Array, Math, Simulation  
**Pattern:** Simulation  
**Link:** [leetcode.com/problems/find-missing-observations](https://leetcode.com/problems/find-missing-observations/)

## Description

You have observations of `n + m` **6-sided** dice rolls with each face numbered from `1` to `6`. `n` of the observations went missing, and you only have the observations of `m` rolls. Fortunately, you have also calculated the **average value** of the `n + m` rolls.

You are given an integer array `rolls` of length `m` where `rolls[i]` is the value of the `i^th` observation. You are also given the two integers `mean` and `n`.

Return *an array of length *`n`* containing the missing observations such that the **average value **of the *`n + m`* rolls is **exactly** *`mean`. If there are multiple valid answers, return *any of them*. If no such array exists, return *an empty array*.

The **average value** of a set of `k` numbers is the sum of the numbers divided by `k`.

Note that `mean` is an integer, so the sum of the `n + m` rolls should be divisible by `n + m`.

 

Example 1:

```

**Input:** rolls = [3,2,4,3], mean = 4, n = 2
**Output:** [6,6]
**Explanation:** The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.

```

Example 2:

```

**Input:** rolls = [1,5,6], mean = 3, n = 4
**Output:** [2,3,2,2]
**Explanation:** The mean of all n + m rolls is (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3.

```

Example 3:

```

**Input:** rolls = [1,2,3,4], mean = 6, n = 4
**Output:** []
**Explanation:** It is impossible for the mean to be 6 no matter what the 4 missing rolls are.

```

 

**Constraints:**

	- `m == rolls.length`
	- `1 <= n, m <= 10^5`
	- `1 <= rolls[i], mean <= 6`

## Approach: Simulation

Simulate the process described in the problem step by step. Follow the rules exactly, tracking state at each step.

## Pseudocode

```
1. Initialize state (grid, pointers, counters)
2. For each step / iteration:
   a. Apply the transformation rules
   b. Update state
   c. Check termination condition
3. Return final state or result
```

## Algorithm Flow

```mermaid
flowchart TD
    A[Initialize state] --> B[Apply transformation rules]
    B --> C[Update state]
    C --> D{Termination condition?}
    D -- No --> B
    D -- Yes --> E[Return final state]
```

## Complexity Analysis

- **Time:** O(n) or O(n * k)
- **Space:** O(n)

## Solution (Python3)

```python
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # Simulation approach - follow the rules step by step
        result = []
        for i in range(len(rolls) if isinstance(rolls, list) else rolls):
            # Simulate each step
            pass
        return result
```

## Solution (C++)

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        // Simulation approach
        int n = rolls.size();
        for (int i = 0; i < n; i++) {
            // Simulate each step
        }
        return {};
    }
};
```
