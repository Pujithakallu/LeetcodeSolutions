# Problem 263: Ugly Number

**Difficulty:** Easy  
**Tags:** Math  
**Pattern:** Math  
**Link:** [leetcode.com/problems/ugly-number](https://leetcode.com/problems/ugly-number/)

## Description

An **ugly number** is a *positive* integer which does not have a prime factor other than 2, 3, and 5.

Given an integer `n`, return `true` *if* `n` *is an **ugly number***.

 

Example 1:

```

**Input:** n = 6
**Output:** true
**Explanation:** 6 = 2 × 3

```

Example 2:

```

**Input:** n = 1
**Output:** true
**Explanation:** 1 has no prime factors.

```

Example 3:

```

**Input:** n = 14
**Output:** false
**Explanation:** 14 is not ugly since it includes the prime factor 7.

```

 

**Constraints:**

	- `-2^31 <= n <= 2^31 - 1`

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
    def isUgly(self, n: int) -> bool:
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
    bool isUgly(int n) {
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
