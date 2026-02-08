# Problem 829: Consecutive Numbers Sum

**Difficulty:** Hard  
**Tags:** Math, Enumeration  
**Pattern:** Math  
**Link:** [leetcode.com/problems/consecutive-numbers-sum](https://leetcode.com/problems/consecutive-numbers-sum/)

## Description

Given an integer `n`, return *the number of ways you can write *`n`* as the sum of consecutive positive integers.*

 

Example 1:

```

**Input:** n = 5
**Output:** 2
**Explanation:** 5 = 2 + 3

```

Example 2:

```

**Input:** n = 9
**Output:** 3
**Explanation:** 9 = 4 + 5 = 2 + 3 + 4

```

Example 3:

```

**Input:** n = 15
**Output:** 4
**Explanation:** 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5

```

 

**Constraints:**

	- `1 <= n <= 10^9`

## Approach: Math

Apply mathematical properties, formulas, or number-theoretic concepts. Look for patterns, modular arithmetic, or closed-form solutions.

## Pseudocode

```
1. Identify the mathematical pattern or formula
2. Apply computation:
   - Modular arithmetic for large numbers
   - GCD/LCM for divisibility
   - Sieve for primes
3. Handle edge cases
4. Return result
```

## Algorithm Flow

```mermaid
flowchart TD
    A[Identify mathematical pattern] --> B[Apply formula or computation]
    B --> C{Edge cases?}
    C -- Yes --> D[Handle special cases]
    C -- No --> E[Compute result]
    D --> E
    E --> F[Return answer]
```

## Complexity Analysis

- **Time:** O(n) or O(sqrt(n))
- **Space:** O(1)

## Solution (Python3)

```python
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # Mathematical approach
        result = 0
        x = n
        while x != 0:
            result = result * 10 + x % 10
            x //= 10 if isinstance(x, int) else 1
        return result
```

## Solution (C++)

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int consecutiveNumbersSum(int n) {
        // Mathematical approach
        long long result = 0;
        int x = n;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        return (int)result;
    }
};
```
