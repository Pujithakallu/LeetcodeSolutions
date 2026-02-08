# Problem 1955: Count Number of Special Subsequences

**Difficulty:** Hard  
**Tags:** Array, Dynamic Programming  
**Pattern:** Dynamic Programming (1D)  
**Link:** [leetcode.com/problems/count-number-of-special-subsequences](https://leetcode.com/problems/count-number-of-special-subsequences/)

## Description

A sequence is **special** if it consists of a **positive** number of `0`s, followed by a **positive** number of `1`s, then a **positive** number of `2`s.

	- For example, `[0,1,2]` and `[0,0,1,1,1,2]` are special.
	- In contrast, `[2,1,0]`, `[1]`, and `[0,1,2,0]` are not special.

Given an array `nums` (consisting of **only** integers `0`, `1`, and `2`), return* the **number of different subsequences** that are special*. Since the answer may be very large, **return it modulo **`10^9 + 7`.

A **subsequence** of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements. Two subsequences are **different** if the **set of indices** chosen are different.

 

Example 1:

```

**Input:** nums = [0,1,2,2]
**Output:** 3
**Explanation:** The special subsequences are bolded [**0**,**1**,**2**,2], [**0**,**1**,2,**2**], and [**0**,**1**,**2**,**2**].

```

Example 2:

```

**Input:** nums = [2,2,0,0]
**Output:** 0
**Explanation:** There are no special subsequences in [2,2,0,0].

```

Example 3:

```

**Input:** nums = [0,1,2,0,1,2]
**Output:** 7
**Explanation:** The special subsequences are bolded:
- [**0**,**1**,**2**,0,1,2]
- [**0**,**1**,2,0,1,**2**]
- [**0**,**1**,**2**,0,1,**2**]
- [**0**,**1**,2,0,**1**,**2**]
- [**0**,1,2,**0**,**1**,**2**]
- [**0**,1,2,0,**1**,**2**]
- [0,1,2,**0**,**1**,**2**]

```

 

**Constraints:**

	- `1 <= nums.length <= 10^5`
	- `0 <= nums[i] <= 2`

## Approach: Dynamic Programming (1D)

Break the problem into overlapping subproblems. Define dp[i] as the optimal value for the subproblem ending at or considering index i. Build the solution bottom-up, using previously computed dp values.

## Pseudocode

```
1. Define dp[i] = optimal value for subproblem i
2. Base case: dp[0] = initial value
3. For i from 1 to n:
   a. dp[i] = recurrence(dp[i-1], dp[i-2], ...)
4. Return dp[n] or max/min of dp
```

## Algorithm Flow

```mermaid
flowchart TD
    A["Define dp[i] meaning"] --> B["Base case: dp[0]"]
    B --> C[For i = 1 to n]
    C --> D["dp[i] = f(dp[i-1], dp[i-2], ...)"]
    D --> E{i < n?}
    E -- Yes --> C
    E -- No --> F["Return dp[n] or aggregate"]
```

## Visual State Transitions

**1D Dynamic Programming Table Build:**

**Frame 1: Initialize base cases**
```mermaid
graph LR
    subgraph DP [DP Table]
        D0["dp[0]=base"]
        D1["dp[1]=?"]
        D2["dp[2]=?"]
        D3["dp[3]=?"]
        D4["dp[4]=?"]
    end
```

**Frame 2: Fill dp[1] from dp[0]**
```mermaid
graph LR
    subgraph DP [DP Table]
        D0["dp[0]=base"]
        D1["dp[1]=f(dp[0])"]
        D2["dp[2]=?"]
        D3["dp[3]=?"]
        D4["dp[4]=?"]
    end
    D0 -.->|"transition"| D1
```

**Frame 3: Fill remaining cells**
```mermaid
graph LR
    subgraph DP [DP Table]
        D0["dp[0]=base"]
        D1["dp[1]=f(dp[0])"]
        D2["dp[2]=f(dp[0],dp[1])"]
        D3["dp[3]=f(dp[1],dp[2])"]
        D4["dp[4]=f(dp[2],dp[3])"]
    end
    A["Answer = dp[4]"]
```


## Complexity Analysis

- **Time:** O(n)
- **Space:** O(n)

## Solution (Python3)

```python
class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        # Dynamic programming (1D) - O(n) time, O(n) space
        if not nums:
            return 0
        n = len(nums) if isinstance(nums, list) else nums
        dp = [0] * (n + 1)
        dp[0] = 1  # base case
        for i in range(1, n + 1):
            dp[i] = dp[i-1]  # transition (customize per problem)
            if i >= 2:
                dp[i] += dp[i-2]
        return dp[n]
```

## Solution (C++)

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int countSpecialSubsequences(vector<int>& nums) {
        // Dynamic programming (1D) - O(n) time, O(n) space
        int n = nums;
        if (n <= 0) return 0;
        vector<int> dp(n + 1, 0);
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            dp[i] = dp[i-1];
            if (i >= 2) dp[i] += dp[i-2];
        }
        return dp[n];
    }
};
```
