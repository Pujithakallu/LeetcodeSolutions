# Problem 1952: Three Divisors

**Difficulty:** Easy  
**Tags:** Math, Enumeration, Number Theory  
**Pattern:** Number Theory  
**Link:** [leetcode.com/problems/three-divisors](https://leetcode.com/problems/three-divisors/)

## Description

Given an integer `n`, return `true`* if *`n`* has **exactly three positive divisors**. Otherwise, return *`false`.

An integer `m` is a **divisor** of `n` if there exists an integer `k` such that `n = k * m`.

 

Example 1:

```

**Input:** n = 2
**Output:** false
**Explantion:** 2 has only two divisors: 1 and 2.

```

Example 2:

```

**Input:** n = 4
**Output:** true
**Explantion:** 4 has three divisors: 1, 2, and 4.

```

 

**Constraints:**

	- `1 <= n <= 10^4`

## Approach: Number Theory

Apply number theory: prime checking, factorization, GCD, modular exponentiation, sieve of Eratosthenes, or Euler's totient.

## Pseudocode

```
1. Apply number-theoretic algorithm:
   - Sieve for primes up to n
   - GCD via Euclidean algorithm
   - Modular exponentiation
2. Process results
3. Return answer
```

## Algorithm Flow

```mermaid
flowchart TD
    A[Input number n] --> B{Algorithm type?}
    B -- Primality --> C[Check divisors up to sqrt n]
    B -- GCD --> D["gcd(a,b) = gcd(b, a mod b)"]
    B -- Sieve --> E[Mark multiples of each prime]
    C --> F[Return result]
    D --> F
    E --> F
```

## Complexity Analysis

- **Time:** O(sqrt(n)) or O(n log log n)
- **Space:** O(n)

## Solution (Python3)

```python
class Solution:
    def isThree(self, n: int) -> bool:
        # Number theory approach
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        result = n[0] if isinstance(n, list) else n
        if isinstance(n, list):
            for val in n[1:]:
                result = gcd(result, val)
        return result
```

## Solution (C++)

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool isThree(int n) {
        // Number theory approach
        auto gcd_func = [](int a, int b) -> int {
            while (b) { int t = b; b = a % b; a = t; }
            return a;
        };
        int result = n[0];
        for (int i = 1; i < (int)n.size(); i++) {
            result = gcd_func(result, n[i]);
        }
        return result;
    }
};
```
