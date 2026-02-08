# Problem 206: Reverse Linked List

**Difficulty:** Easy  
**Tags:** Linked List, Recursion  
**Pattern:** Linked List Reversal  
**Link:** [leetcode.com/problems/reverse-linked-list](https://leetcode.com/problems/reverse-linked-list/)

## Description

Given the `head` of a singly linked list, reverse the list, and return *the reversed list*.

 

Example 1:

```

**Input:** head = [1,2,3,4,5]
**Output:** [5,4,3,2,1]

```

Example 2:

```

**Input:** head = [1,2]
**Output:** [2,1]

```

Example 3:

```

**Input:** head = []
**Output:** []

```

 

**Constraints:**

	- The number of nodes in the list is the range `[0, 5000]`.
	- `-5000 <= Node.val <= 5000`

 

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?

## Approach: Linked List Reversal

Iterative reversal: maintain prev and curr pointers, reverse links one at a time.

## Pseudocode

```
1. prev=None, curr=head
2. While curr: save next, reverse link, advance
3. Return prev
```

## Algorithm Flow

```mermaid
flowchart TD
    A[prev=None, curr=head] --> B{curr not null?}
    B -- Yes --> C[nxt = curr.next]
    C --> D[curr.next = prev]
    D --> E[prev = curr, curr = nxt]
    E --> B
    B -- No --> F[Return prev]
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
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
```

## Solution (C++)

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // Linked list traversal/manipulation
        ListNode dummy(0);
        dummy.next = head;
        ListNode* prev = &dummy;
        ListNode* curr = head;
        while (curr) {
            ListNode* nxt = curr->next;
            // Process current node
            prev = curr;
            curr = nxt;
        }
        return dummy.next;
    }
};
```
