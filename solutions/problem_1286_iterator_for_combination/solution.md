# Problem 1286: Iterator for Combination

**Difficulty:** Medium  
**Tags:** String, Backtracking, Design, Iterator  
**Pattern:** Backtracking  
**Link:** [leetcode.com/problems/iterator-for-combination](https://leetcode.com/problems/iterator-for-combination/)

## Description

Design the `CombinationIterator` class:

	- `CombinationIterator(string characters, int combinationLength)` Initializes the object with a string `characters` of **sorted distinct** lowercase English letters and a number `combinationLength` as arguments.
	- `next()` Returns the next combination of length `combinationLength` in **lexicographical order**.
	- `hasNext()` Returns `true` if and only if there exists a next combination.

 

Example 1:

```

**Input**
["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]
**Output**
[null, "ab", true, "ac", true, "bc", false]

**Explanation**
CombinationIterator itr = new CombinationIterator("abc", 2);
itr.next();    // return "ab"
itr.hasNext(); // return True
itr.next();    // return "ac"
itr.hasNext(); // return True
itr.next();    // return "bc"
itr.hasNext(); // return False

```

 

**Constraints:**

	- `1 <= combinationLength <= characters.length <= 15`
	- All the characters of `characters` are **unique**.
	- At most `10^4` calls will be made to `next` and `hasNext`.
	- It is guaranteed that all calls of the function `next` are valid.

## Approach: Backtracking

Explore all possible solutions by building candidates incrementally. At each step, make a choice and recurse. If the choice leads to a dead end, undo the choice (backtrack) and try the next option.

## Pseudocode

```
1. Define backtrack(path, choices):
   a. If path is a complete solution: add to results
   b. For each choice in choices:
      - If choice is valid:
        * Add choice to path
        * backtrack(path, remaining_choices)
        * Remove choice from path (backtrack)
2. Call backtrack([], all_choices)
```

## Algorithm Flow

```mermaid
flowchart TD
    A["backtrack(path, choices)"] --> B{Path complete?}
    B -- Yes --> C[Add path to results]
    B -- No --> D[For each valid choice]
    D --> E[Add choice to path]
    E --> F["backtrack(path, remaining)"]
    F --> G[Remove choice from path]
    G --> D
    D --> H{All choices tried}
    H --> I[Return]
```

## Visual State Transitions

**Backtracking Decision Tree:**

**Frame 1: Root - start with empty path**
```mermaid
graph TD
    R["[] choices: 1,2,3"]
    R --- A["[1]"]
    R --- B["[2]"]
    R --- C["[3]"]
```

**Frame 2: Explore branch [1]**
```mermaid
graph TD
    R["[]"]
    R --- A["[1]"]
    A --- A1["[1,2]"]
    A --- A2["[1,3]"]
    A1 --- A1a["[1,2,3] SOLUTION"]
    R --- B["[2] ..."]
    R --- C["[3] ..."]
```

**Frame 3: Backtrack, explore [2]**
```mermaid
graph TD
    R["[]"]
    R --- A["[1] done"]
    R --- B["[2]"]
    B --- B1["[2,1]"]
    B --- B2["[2,3]"]
    B1 --- B1a["[2,1,3] SOLUTION"]
    R --- C["[3] ..."]
```

**Frame 4: All solutions found**
```mermaid
graph TD
    R["Complete: 6 permutations found"]
    R --- S1["[1,2,3]"]
    R --- S2["[1,3,2]"]
    R --- S3["[2,1,3] ..."]
```


## Complexity Analysis

- **Time:** O(k^n) or O(n!)
- **Space:** O(n)

## Solution (Python3)

```python
class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        # Initialize data structure
        self.characters = characters
        self.combinationLength = combinationLength

    def next(self) -> str:
        return ""

    def hasNext(self) -> bool:
        return False

```

## Solution (C++)

```cpp
#include <functional>
#include <string>
#include <vector>
using namespace std;

class CombinationIterator {
public:
    CombinationIterator(string& characters, int combinationLength) {
        // Initialize
    }

    string next() {
        return "";
    }

    bool hasNext() {
        return false;
    }

};
```
