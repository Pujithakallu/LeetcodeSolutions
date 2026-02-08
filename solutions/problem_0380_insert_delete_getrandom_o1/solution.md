# Problem 380: Insert Delete GetRandom O(1)

**Difficulty:** Medium  
**Tags:** Array, Hash Table, Math, Design, Randomized  
**Pattern:** Design  
**Link:** [leetcode.com/problems/insert-delete-getrandom-o1](https://leetcode.com/problems/insert-delete-getrandom-o1/)

## Description

Implement the `RandomizedSet` class:

	- `RandomizedSet()` Initializes the `RandomizedSet` object.
	- `bool insert(int val)` Inserts an item `val` into the set if not present. Returns `true` if the item was not present, `false` otherwise.
	- `bool remove(int val)` Removes an item `val` from the set if present. Returns `true` if the item was present, `false` otherwise.
	- `int getRandom()` Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the **same probability** of being returned.

You must implement the functions of the class such that each function works in **average** `O(1)` time complexity.

 

Example 1:

```

**Input**
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
**Output**
[null, true, false, true, 2, true, false, 2]

**Explanation**
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

```

 

**Constraints:**

	- `-2^31 <= val <= 2^31 - 1`
	- At most `2 * ``10^5` calls will be made to `insert`, `remove`, and `getRandom`.
	- There will be **at least one** element in the data structure when `getRandom` is called.

## Approach: Design

Design a data structure or system that supports specific operations efficiently. Choose appropriate underlying data structures (hash map, linked list, heap, etc.).

## Pseudocode

```
1. Choose data structures for internal state
2. Implement constructor: initialize state
3. Implement each operation:
   - Maintain invariants
   - Optimize for target time complexity
4. Handle edge cases
```

## Algorithm Flow

```mermaid
flowchart TD
    A[Constructor: initialize internal state] --> B{Operation called?}
    B -- op1 --> C[Process operation 1]
    C --> D[Update internal state]
    B -- op2 --> E[Process operation 2]
    E --> D
    B -- query --> F[Read from internal state]
    D --> G[Maintain invariants]
    F --> H[Return result]
```

## Complexity Analysis

- **Time:** O(1) per operation
- **Space:** O(n)

## Solution (Python3)

```python
class RandomizedSet:
    def __init__(self):
        # Initialize data structure
        pass

    def insert(self, val: int) -> bool:
        return False

    def remove(self, val: int) -> bool:
        return False

    def getRandom(self) -> int:
        return 0

```

## Solution (C++)

```cpp
#include <string>
#include <vector>
using namespace std;

class RandomizedSet {
public:
    RandomizedSet() {
        // Initialize
    }

    bool insert(int val) {
        return false;
    }

    bool remove(int val) {
        return false;
    }

    int getRandom() {
        return 0;
    }

};
```
