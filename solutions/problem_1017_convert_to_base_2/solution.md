# Problem 1017: Convert to Base -2

**Difficulty:** Medium  
**Tags:** Math  
**Pattern:** Math  
**Link:** [leetcode.com/problems/convert-to-base-2](https://leetcode.com/problems/convert-to-base-2/)

## Description

Given an integer `n`, return *a binary string representing its representation in base* `-2`.

**Note** that the returned string should not have leading zeros unless the string is `"0"`.

 

Example 1:

```

**Input:** n = 2
**Output:** "110"
**Explantion:** (-2)2 + (-2)1 = 2

```

Example 2:

```

**Input:** n = 3
**Output:** "111"
**Explantion:** (-2)2 + (-2)1 + (-2)0 = 3

```

Example 3:

```

**Input:** n = 4
**Output:** "100"
**Explantion:** (-2)2 = 4

```

 

**Constraints:**

	- `0 <= n <= 10^9`

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
    def baseNeg2(self, n: int) -> str:
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
    string baseNeg2(int n) {
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
