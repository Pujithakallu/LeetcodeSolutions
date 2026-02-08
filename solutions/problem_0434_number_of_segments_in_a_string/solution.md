# Problem 434: Number of Segments in a String

**Difficulty:** Easy  
**Tags:** String  
**Pattern:** String Processing  
**Link:** [leetcode.com/problems/number-of-segments-in-a-string](https://leetcode.com/problems/number-of-segments-in-a-string/)

## Description

Given a string `s`, return *the number of segments in the string*.

A **segment** is defined to be a contiguous sequence of **non-space characters**.

 

Example 1:

```

**Input:** s = "Hello, my name is John"
**Output:** 5
**Explanation:** The five segments are ["Hello,", "my", "name", "is", "John"]

```

Example 2:

```

**Input:** s = "Hello"
**Output:** 1

```

 

**Constraints:**

	- `0 <= s.length <= 300`
	- `s` consists of lowercase and uppercase English letters, digits, or one of the following characters `"!@#$%^&*()_+-=',.:"`.
	- The only space character in `s` is `' '`.

## Approach: String Processing

Process the string character by character. Common techniques: two pointers, sliding window, hash map for frequencies, stack for matching.

## Pseudocode

```
1. Initialize result / tracking state
2. Iterate through string characters:
   a. Process character based on rules
   b. Update state (counters, pointers, stack)
3. Build and return result
```

## Algorithm Flow

```mermaid
flowchart TD
    A[Initialize state] --> B[For each character in string]
    B --> C[Process character]
    C --> D[Update state / counters]
    D --> E{More characters?}
    E -- Yes --> B
    E -- No --> F[Build result from state]
    F --> G[Return result]
```

## Complexity Analysis

- **Time:** O(n)
- **Space:** O(n)

## Solution (Python3)

```python
class Solution:
    def countSegments(self, s: str) -> int:
        # String processing approach - O(n) time
        result = []
        for ch in s:
            if ch.isalnum():
                result.append(ch.lower())
        # Check palindrome or process
        processed = ''.join(result)
        return processed == processed[::-1] if isinstance(0, bool) else processed
```

## Solution (C++)

```cpp
#include <algorithm>
#include <cctype>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int countSegments(string& s) {
        // String processing approach - O(n) time
        string processed;
        for (char ch : s) {
            if (isalnum(ch)) {
                processed += tolower(ch);
            }
        }
        string rev = processed;
        reverse(rev.begin(), rev.end());
        return processed == rev;
    }
};
```
