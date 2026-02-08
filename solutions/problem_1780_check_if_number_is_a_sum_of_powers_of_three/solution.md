# Problem 1780: Check if Number is a Sum of Powers of Three

**Difficulty:** Medium  
**Tags:** Math  
**Pattern:** Math  
**Link:** [leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three](https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/)

## Description

Given an integer `n`, return `true` *if it is possible to represent *`n`* as the sum of distinct powers of three.* Otherwise, return `false`.

An integer `y` is a power of three if there exists an integer `x` such that `y == 3^x`.

 

Example 1:

```

**Input:** n = 12
**Output:** true
**Explanation:** 12 = 31 + 32

```

Example 2:

```

**Input:** n = 91
**Output:** true
**Explanation:** 91 = 30 + 32 + 34

```

Example 3:

```

**Input:** n = 21
**Output:** false

```

 

**Constraints:**

	- `1 <= n <= 10^7`

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
    def checkPowersOfThree(self, n: int) -> bool:
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
    bool checkPowersOfThree(int n) {
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
