# Problem 459: Repeated Substring Pattern

**Difficulty:** Easy  
**Tags:** String, String Matching  
**Pattern:** String Matching  
**Link:** [leetcode.com/problems/repeated-substring-pattern](https://leetcode.com/problems/repeated-substring-pattern/)

## Description

Given a string `s`, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

```

**Input:** s = "abab"
**Output:** true
**Explanation:** It is the substring "ab" twice.

```

Example 2:

```

**Input:** s = "aba"
**Output:** false

```

Example 3:

```

**Input:** s = "abcabcabcabc"
**Output:** true
**Explanation:** It is the substring "abc" four times or the substring "abcabc" twice.

```

 

**Constraints:**

	- `1 <= s.length <= 10^4`
	- `s` consists of lowercase English letters.

## Approach: String Matching

Find pattern occurrences in text. Use KMP, Rabin-Karp, or Z-algorithm for efficient matching beyond brute force.

## Pseudocode

```
1. Preprocess pattern (build failure function / hash)
2. Scan text with pattern:
   a. Compare characters
   b. On mismatch: use preprocessed data to skip
   c. On full match: record position
3. Return matches
```

## Algorithm Flow

```mermaid
flowchart TD
    A[Preprocess pattern] --> B[Scan text position by position]
    B --> C{Characters match?}
    C -- Yes --> D[Advance both pointers]
    D --> E{Full pattern matched?}
    E -- Yes --> F[Record match position]
    E -- No --> B
    C -- No --> G[Use failure function to skip]
    G --> B
    F --> B
```

## Complexity Analysis

- **Time:** O(n + m)
- **Space:** O(m)

## Solution (Python3)

```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # String matching (KMP/Rolling Hash) - O(n+m) time
        if not s or not s:
            return False
        n, m = len(s), len(s)
        # Build failure function for KMP
        fail = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and s[i] != s[j]:
                j = fail[j-1]
            if s[i] == s[j]:
                j += 1
            fail[i] = j
        # Search
        j = 0
        for i in range(n):
            while j > 0 and s[i] != s[j]:
                j = fail[j-1]
            if s[i] == s[j]:
                j += 1
            if j == m:
                return i - m + 1
        return -1
```

## Solution (C++)

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool repeatedSubstringPattern(string& s) {
        // String matching (KMP) - O(n+m) time
        int n = s.size(), m = s.size();
        if (m == 0) return 0;
        vector<int> fail(m, 0);
        for (int i = 1, j = 0; i < m; i++) {
            while (j > 0 && s[i] != s[j]) j = fail[j-1];
            if (s[i] == s[j]) j++;
            fail[i] = j;
        }
        for (int i = 0, j = 0; i < n; i++) {
            while (j > 0 && s[i] != s[j]) j = fail[j-1];
            if (s[i] == s[j]) j++;
            if (j == m) return i - m + 1;
        }
        return -1;
    }
};
```
