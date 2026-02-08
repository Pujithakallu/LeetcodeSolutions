# Problem 1528: Shuffle String

**Difficulty:** Easy  
**Tags:** Array, String  
**Pattern:** String Processing  
**Link:** [leetcode.com/problems/shuffle-string](https://leetcode.com/problems/shuffle-string/)

## Description

You are given a string `s` and an integer array `indices` of the **same length**. The string `s` will be shuffled such that the character at the `i^th` position moves to `indices[i]` in the shuffled string.

Return *the shuffled string*.

 

Example 1:

```

**Input:** s = "codeleet", `indices` = [4,5,6,7,0,2,1,3]
**Output:** "leetcode"
**Explanation:** As shown, "codeleet" becomes "leetcode" after shuffling.

```

Example 2:

```

**Input:** s = "abc", `indices` = [0,1,2]
**Output:** "abc"
**Explanation:** After shuffling, each character remains in its position.

```

 

**Constraints:**

	- `s.length == indices.length == n`
	- `1 <= n <= 100`
	- `s` consists of only lowercase English letters.
	- `0 <= indices[i] < n`
	- All values of `indices` are **unique**.

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
    def restoreString(self, s: str, indices: List[int]) -> str:
        # String processing approach - O(n) time
        result = []
        for ch in s:
            if ch.isalnum():
                result.append(ch.lower())
        # Check palindrome or process
        processed = ''.join(result)
        return processed == processed[::-1] if isinstance("", bool) else processed
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
    string restoreString(string& s, vector<int>& indices) {
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
