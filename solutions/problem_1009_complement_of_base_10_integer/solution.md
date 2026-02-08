# Problem 1009: Complement of Base 10 Integer

**Difficulty:** Easy  
**Tags:** Bit Manipulation  
**Pattern:** Bit Manipulation  
**Link:** [leetcode.com/problems/complement-of-base-10-integer](https://leetcode.com/problems/complement-of-base-10-integer/)

## Description

The **complement** of an integer is the integer you get when you flip all the `0`'s to `1`'s and all the `1`'s to `0`'s in its binary representation.

	- For example, The integer `5` is `"101"` in binary and its **complement** is `"010"` which is the integer `2`.

Given an integer `n`, return *its complement*.

 

Example 1:

```

**Input:** n = 5
**Output:** 2
**Explanation:** 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.

```

Example 2:

```

**Input:** n = 7
**Output:** 0
**Explanation:** 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.

```

Example 3:

```

**Input:** n = 10
**Output:** 5
**Explanation:** 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.

```

 

**Constraints:**

	- `0 <= n < 10^9`

 

**Note:** This question is the same as 476: https://leetcode.com/problems/number-complement/

## Approach: Bit Manipulation

Operate on individual bits using bitwise operators (AND, OR, XOR, shift). Common tricks: x & (x-1) removes lowest set bit, x ^ x = 0, XOR all elements to find unique.

## Pseudocode

```
1. Apply bitwise operations:
   - XOR all elements to cancel paired bits
   - Use bitmask to track state
   - Shift and mask to extract/set individual bits
2. Return result
```

## Algorithm Flow

```mermaid
flowchart TD
    A[Initialize result = 0 or mask] --> B[For each element or bit position]
    B --> C[Apply bitwise operation]
    C --> D["AND / OR / XOR / SHIFT"]
    D --> E[Update result or mask]
    E --> F{More elements?}
    F -- Yes --> B
    F -- No --> G[Return result]
```

## Complexity Analysis

- **Time:** O(n) or O(log n)
- **Space:** O(1)

## Solution (Python3)

```python
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # Bit manipulation - O(n) time, O(1) space
        result = 0
        for val in n:
            result ^= val
        return result
```

## Solution (C++)

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int bitwiseComplement(int n) {
        // Bit manipulation - O(n) time, O(1) space
        int result = 0;
        for (int val : n) {
            result ^= val;
        }
        return result;
    }
};
```
