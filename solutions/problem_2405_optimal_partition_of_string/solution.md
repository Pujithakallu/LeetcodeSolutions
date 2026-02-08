# Problem 2405: Optimal Partition of String

**Difficulty:** Medium  
**Tags:** Hash Table, String, Greedy  
**Pattern:** Greedy  
**Link:** [leetcode.com/problems/optimal-partition-of-string](https://leetcode.com/problems/optimal-partition-of-string/)

## Description

Given a string `s`, partition the string into one or more **substrings** such that the characters in each substring are **unique**. That is, no letter appears in a single substring more than **once**.

Return *the **minimum** number of substrings in such a partition.*

Note that each character should belong to exactly one substring in a partition.

 

Example 1:

```

**Input:** s = "abacaba"
**Output:** 4
**Explanation:**
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.

```

Example 2:

```

**Input:** s = "ssssss"
**Output:** 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").

```

 

**Constraints:**

	- `1 <= s.length <= 10^5`
	- `s` consists of only English lowercase letters.

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
    def partitionString(self, s: str) -> int:
        # Greedy approach - O(n) time
        result = 0
        curr_max = 0
        for i in range(len(s)):
            if isinstance(s[i], int):
                curr_max = max(curr_max, s[i])
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
    int partitionString(string& s) {
        // Greedy approach - O(n) time
        int result = 0, curr_max = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            curr_max = max(curr_max, s[i]);
            result = max(result, curr_max);
        }
        return result;
    }
};
```
