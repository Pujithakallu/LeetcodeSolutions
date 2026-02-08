# Problem 225: Implement Stack using Queues

**Difficulty:** Easy  
**Tags:** Stack, Design, Queue  
**Pattern:** Stack  
**Link:** [leetcode.com/problems/implement-stack-using-queues](https://leetcode.com/problems/implement-stack-using-queues/)

## Description

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (`push`, `top`, `pop`, and `empty`).

Implement the `MyStack` class:

	- `void push(int x)` Pushes element x to the top of the stack.
	- `int pop()` Removes the element on the top of the stack and returns it.
	- `int top()` Returns the element on the top of the stack.
	- `boolean empty()` Returns `true` if the stack is empty, `false` otherwise.

**Notes:**

	- You must use **only** standard operations of a queue, which means that only `push to back`, `peek/pop from front`, `size` and `is empty` operations are valid.
	- Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

 

Example 1:

```

**Input**
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
**Output**
[null, null, null, 2, 2, false]

**Explanation**
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False

```

 

**Constraints:**

	- `1 <= x <= 9`
	- At most `100` calls will be made to `push`, `pop`, `top`, and `empty`.
	- All the calls to `pop` and `top` are valid.

 

**Follow-up:** Can you implement the stack using only one queue?

## Approach: Stack

Use a stack (LIFO) to process elements. Push elements when they might be needed later; pop when a matching or resolving condition is found. Common uses: parentheses matching, expression evaluation, next greater element.

## Pseudocode

```
1. Initialize empty stack
2. For each element:
   a. While stack is not empty and condition met:
      - Pop and process top element
   b. Push current element onto stack
3. Process remaining elements in stack if needed
4. Return result
```

## Algorithm Flow

```mermaid
flowchart TD
    A[Initialize empty stack] --> B[For each element]
    B --> C{Stack not empty AND condition?}
    C -- Yes --> D[Pop top element]
    D --> E[Process popped element]
    E --> C
    C -- No --> F[Push current element]
    F --> G{More elements?}
    G -- Yes --> B
    G -- No --> H[Return result]
```

## Complexity Analysis

- **Time:** O(n)
- **Space:** O(n)

## Solution (Python3)

```python
class MyStack:
    def __init__(self):
        # Initialize data structure
        pass

    def push(self, x: int) -> None:
        return None

    def pop(self) -> int:
        return 0

    def top(self) -> int:
        return 0

    def empty(self) -> bool:
        return False

```

## Solution (C++)

```cpp
#include <stack>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class MyStack {
public:
    MyStack() {
        // Initialize
    }

    void push(int x) {
        return ;
    }

    int pop() {
        return 0;
    }

    int top() {
        return 0;
    }

    bool empty() {
        return false;
    }

};
```
