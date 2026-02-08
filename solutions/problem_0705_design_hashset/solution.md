# Problem 705: Design HashSet

**Difficulty:** Easy  
**Tags:** Array, Hash Table, Linked List, Design, Hash Function  
**Pattern:** Linked List  
**Link:** [leetcode.com/problems/design-hashset](https://leetcode.com/problems/design-hashset/)

## Description

Design a HashSet without using any built-in hash table libraries.

Implement `MyHashSet` class:

	- `void add(key)` Inserts the value `key` into the HashSet.
	- `bool contains(key)` Returns whether the value `key` exists in the HashSet or not.
	- `void remove(key)` Removes the value `key` in the HashSet. If `key` does not exist in the HashSet, do nothing.

 

Example 1:

```

**Input**
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
**Output**
[null, null, null, true, false, null, true, null, false]

**Explanation**
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
```

 

**Constraints:**

	- `0 <= key <= 10^6`
	- At most `10^4` calls will be made to `add`, `remove`, and `contains`.

## Approach: Linked List

Traverse or manipulate the linked list using pointer techniques. Common patterns: dummy head node for edge cases, fast/slow pointers for cycle detection or middle finding, in-place reversal, and merge operations.

## Pseudocode

```
1. Create dummy head if needed
2. Initialize pointer(s) at head
3. Traverse / modify list:
   a. Process current node
   b. Adjust next pointers as needed
   c. Move to next node
4. Return dummy.next or result
```

## Algorithm Flow

```mermaid
flowchart TD
    A[Create dummy head node] --> B[curr = head]
    B --> C{curr is not null?}
    C -- Yes --> D[Process current node]
    D --> E[Adjust pointers / links]
    E --> F[curr = curr.next]
    F --> C
    C -- No --> G[Return dummy.next or result]
```

## Visual State Transitions

**Linked List Operation (Reverse):**

**Frame 1: Initial list**
```mermaid
graph LR
    A["1"] --> B["2"] --> C["3"] --> D["4"] --> N[null]
    P["prev=null, curr=1"]
```

**Frame 2: Reverse first link**
```mermaid
graph LR
    A["1"] --> N[null]
    B["2"] --> C["3"] --> D["4"]
    P["prev=1, curr=2"]
```

**Frame 3: Reverse second link**
```mermaid
graph LR
    B["2"] --> A["1"] --> N[null]
    C["3"] --> D["4"]
    P["prev=2, curr=3"]
```

**Frame 4: Fully reversed**
```mermaid
graph LR
    D["4"] --> C["3"] --> B["2"] --> A["1"] --> N[null]
    P["New head = 4"]
```


## Complexity Analysis

- **Time:** O(n)
- **Space:** O(1)

## Solution (Python3)

```python
class MyHashSet:
    def __init__(self):
        # Initialize data structure
        pass

    def add(self, key: int) -> None:
        return None

    def remove(self, key: int) -> None:
        return None

    def contains(self, key: int) -> bool:
        return False

```

## Solution (C++)

```cpp
#include <string>
#include <vector>
using namespace std;

class MyHashSet {
public:
    MyHashSet() {
        // Initialize
    }

    void add(int key) {
        return ;
    }

    void remove(int key) {
        return ;
    }

    bool contains(int key) {
        return false;
    }

};
```
