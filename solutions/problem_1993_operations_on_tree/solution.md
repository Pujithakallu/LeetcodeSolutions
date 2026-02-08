# Problem 1993: Operations on Tree

**Difficulty:** Medium  
**Tags:** Array, Hash Table, Tree, Depth-First Search, Breadth-First Search, Design  
**Pattern:** DFS Tree Traversal  
**Link:** [leetcode.com/problems/operations-on-tree](https://leetcode.com/problems/operations-on-tree/)

## Description

You are given a tree with `n` nodes numbered from `0` to `n - 1` in the form of a parent array `parent` where `parent[i]` is the parent of the `i^th` node. The root of the tree is node `0`, so `parent[0] = -1` since it has no parent. You want to design a data structure that allows users to lock, unlock, and upgrade nodes in the tree.

The data structure should support the following functions:

	- **Lock:** **Locks** the given node for the given user and prevents other users from locking the same node. You may only lock a node using this function if the node is unlocked.
	- **Unlock: Unlocks** the given node for the given user. You may only unlock a node using this function if it is currently locked by the same user.
	- **Upgrade****: Locks** the given node for the given user and **unlocks** all of its descendants **regardless** of who locked it. You may only upgrade a node if **all** 3 conditions are true:
	
		The node is unlocked,
		- It has at least one locked descendant (by **any** user), and
		- It does not have any locked ancestors.
	
	

Implement the `LockingTree` class:

	- `LockingTree(int[] parent)` initializes the data structure with the parent array.
	- `lock(int num, int user)` returns `true` if it is possible for the user with id `user` to lock the node `num`, or `false` otherwise. If it is possible, the node `num` will become** locked** by the user with id `user`.
	- `unlock(int num, int user)` returns `true` if it is possible for the user with id `user` to unlock the node `num`, or `false` otherwise. If it is possible, the node `num` will become **unlocked**.
	- `upgrade(int num, int user)` returns `true` if it is possible for the user with id `user` to upgrade the node `num`, or `false` otherwise. If it is possible, the node `num` will be **upgraded**.

 

Example 1:

```

**Input**
["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"]
[[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]]
**Output**
[null, true, false, true, true, true, false]

**Explanation**
LockingTree lockingTree = new LockingTree([-1, 0, 0, 1, 1, 2, 2]);
lockingTree.lock(2, 2);    // return true because node 2 is unlocked.
                           // Node 2 will now be locked by user 2.
lockingTree.unlock(2, 3);  // return false because user 3 cannot unlock a node locked by user 2.
lockingTree.unlock(2, 2);  // return true because node 2 was previously locked by user 2.
                           // Node 2 will now be unlocked.
lockingTree.lock(4, 5);    // return true because node 4 is unlocked.
                           // Node 4 will now be locked by user 5.
lockingTree.upgrade(0, 1); // return true because node 0 is unlocked and has at least one locked descendant (node 4).
                           // Node 0 will now be locked by user 1 and node 4 will now be unlocked.
lockingTree.lock(0, 1);    // return false because node 0 is already locked.

```

 

**Constraints:**

	- `n == parent.length`
	- `2 <= n <= 2000`
	- `0 <= parent[i] <= n - 1` for `i != 0`
	- `parent[0] == -1`
	- `0 <= num <= n - 1`
	- `1 <= user <= 10^4`
	- `parent` represents a valid tree.
	- At most `2000` calls **in total** will be made to `lock`, `unlock`, and `upgrade`.

## Approach: DFS Tree Traversal

Perform depth-first search on the tree. Recurse on left and right subtrees, combining results bottom-up. Track state (path, depth, sum) during traversal.

## Pseudocode

```
1. Define dfs(node, state):
   a. Base case: if null, return default
   b. Process node with current state
   c. left_result = dfs(node.left, updated_state)
   d. right_result = dfs(node.right, updated_state)
   e. Return combine(left_result, right_result)
2. Return dfs(root, initial_state)
```

## Algorithm Flow

```mermaid
flowchart TD
    A["dfs(node, state)"] --> B{node is null?}
    B -- Yes --> C[Return base case]
    B -- No --> D[Process node with state]
    D --> E["left = dfs(node.left, state')"]
    E --> F["right = dfs(node.right, state')"]
    F --> G["Return combine(left, right)"]
```

## Visual State Transitions

**DFS Tree Traversal Step-by-Step:**

**Frame 1: Start at root**
```mermaid
graph TD
    A(("1 CURRENT"))
    A --- B((2))
    A --- C((3))
    B --- D((4))
    B --- E((5))
    S["Stack: [1]"]
```

**Frame 2: Go left - visit node 2**
```mermaid
graph TD
    A(("1 visited"))
    A --- B(("2 CURRENT"))
    A --- C((3))
    B --- D((4))
    B --- E((5))
    S["Stack: [1, 2]"]
```

**Frame 3: Go left - visit node 4 (leaf)**
```mermaid
graph TD
    A(("1 visited"))
    A --- B(("2 visited"))
    A --- C((3))
    B --- D(("4 CURRENT leaf"))
    B --- E((5))
    S["Stack: [1, 2, 4] -> backtrack"]
```

**Frame 4: Backtrack, visit node 5, then node 3**
```mermaid
graph TD
    A(("1 visited"))
    A --- B(("2 visited"))
    A --- C(("3 CURRENT"))
    B --- D(("4 visited"))
    B --- E(("5 visited"))
    S["All nodes visited, DFS complete"]
```


## Complexity Analysis

- **Time:** O(n)
- **Space:** O(h)

## Solution (Python3)

```python
class LockingTree:
    def __init__(self, parent: List[int]):
        # Initialize data structure
        self.parent = parent

    def lock(self, num: int, user: int) -> bool:
        return False

    def unlock(self, num: int, user: int) -> bool:
        return False

    def upgrade(self, num: int, user: int) -> bool:
        return False

```

## Solution (C++)

```cpp
#include <algorithm>
#include <functional>
#include <string>
#include <vector>
using namespace std;

class LockingTree {
public:
    LockingTree(vector<int>& parent) {
        // Initialize
    }

    bool lock(int num, int user) {
        return false;
    }

    bool unlock(int num, int user) {
        return false;
    }

    bool upgrade(int num, int user) {
        return false;
    }

};
```
