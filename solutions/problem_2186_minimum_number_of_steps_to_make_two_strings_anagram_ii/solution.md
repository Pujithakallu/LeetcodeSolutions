# Problem 2186: Minimum Number of Steps to Make Two Strings Anagram II

**Difficulty:** Medium  
**Tags:** Hash Table, String, Counting  
**Pattern:** Hash Map String Processing  
**Link:** [leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii](https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/)

## Description

You are given two strings `s` and `t`. In one step, you can append **any character** to either `s` or `t`.

Return *the minimum number of steps to make *`s`* and *`t`* **anagrams** of each other.*

An **anagram** of a string is a string that contains the same characters with a different (or the same) ordering.

 

Example 1:

```

**Input:** s = "**lee**tco**de**", t = "co**a**t**s**"
**Output:** 7
**Explanation:** 
- In 2 steps, we can append the letters in "as" onto s = "leetcode", forming s = "leetcode**as**".
- In 5 steps, we can append the letters in "leede" onto t = "coats", forming t = "coats**leede**".
"leetcodeas" and "coatsleede" are now anagrams of each other.
We used a total of 2 + 5 = 7 steps.
It can be shown that there is no way to make them anagrams of each other with less than 7 steps.

```

Example 2:

```

**Input:** s = "night", t = "thing"
**Output:** 0
**Explanation:** The given strings are already anagrams of each other. Thus, we do not need any further steps.

```

 

**Constraints:**

	- `1 <= s.length, t.length <= 2 * 10^5`
	- `s` and `t` consist of lowercase English letters.

## Approach: Hash Map String Processing

Use a hash map to count character frequencies or map characters/strings for O(1) lookups. Process the string in one or two passes.

## Pseudocode

```
1. Build frequency map / char-to-index map
2. Iterate through string:
   a. Look up character in map
   b. Update counts or mappings
3. Return result based on map state
```

## Algorithm Flow

```mermaid
flowchart TD
    A[Build character frequency map] --> B[Iterate through string]
    B --> C{Lookup char in map}
    C --> D[Update map / counters]
    D --> E{All chars processed?}
    E -- No --> B
    E -- Yes --> F[Return result from map]
```

## Complexity Analysis

- **Time:** O(n)
- **Space:** O(n)

## Solution (Python3)

```python
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # Hash map for string/character frequency - O(n) time
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        # Process frequency map
        for ch, cnt in freq.items():
            if cnt == 1:
                return s.index(ch)
        return 0
```

## Solution (C++)

```cpp
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    int minSteps(string& s, string& t) {
        // Hash map for string/character frequency - O(n) time
        unordered_map<char, int> freq;
        for (char ch : s) {
            freq[ch]++;
        }
        // Process frequency map
        for (int i = 0; i < s.size(); i++) {
            if (freq[s[i]] == 1) return i;
        }
        return 0;
    }
};
```
