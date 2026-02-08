# Problem 1778: Shortest Path in a Hidden Grid

**Difficulty:** Medium  
**Tags:** Array, Depth-First Search, Breadth-First Search, Matrix, Interactive  
**Pattern:** DFS on Matrix / Grid  
**Link:** [leetcode.com/problems/shortest-path-in-a-hidden-grid](https://leetcode.com/problems/shortest-path-in-a-hidden-grid/)

## Description

*(Premium problem -- description requires LeetCode subscription)*

## Approach: DFS on Matrix / Grid

Treat the grid as a graph where each cell connects to its 4 (or 8) neighbors. DFS from target cells, marking visited to avoid revisiting.

## Pseudocode

```
1. For each cell (r, c) in grid:
   a. If cell meets start condition:
      - Call dfs(r, c)
2. dfs(r, c):
   a. If out of bounds or visited or invalid: return
   b. Mark cell visited
   c. Recurse on 4 neighbors: up, down, left, right
3. Return result
```

## Algorithm Flow

```mermaid
flowchart TD
    A[For each cell in grid] --> B{Matches start condition?}
    B -- Yes --> C["dfs(r, c)"]
    B -- No --> A
    C --> D{Out of bounds or visited?}
    D -- Yes --> E[Return]
    D -- No --> F[Mark visited, process cell]
    F --> G["dfs(r+1,c), dfs(r-1,c)"]
    G --> H["dfs(r,c+1), dfs(r,c-1)"]
    H --> I[Return result]
```

## Visual State Transitions

**DFS on Grid (Island/Flood Fill):**

**Frame 1: Find first land cell**
```mermaid
graph TD
    subgraph Grid
        R0["1  1  0"]
        R1["1  0  0"]
        R2["0  0  1"]
    end
    S["Start DFS at (0,0)"]
```

**Frame 2: DFS explores connected cells**
```mermaid
graph TD
    subgraph Grid
        R0["V  1  0"]
        R1["1  0  0"]
        R2["0  0  1"]
    end
    S["Visited (0,0), explore neighbors"]
```

**Frame 3: Mark entire island**
```mermaid
graph TD
    subgraph Grid
        R0["V  V  0"]
        R1["V  0  0"]
        R2["0  0  1"]
    end
    S["Island 1 complete, area=3"]
```

**Frame 4: Find second island**
```mermaid
graph TD
    subgraph Grid
        R0["V  V  0"]
        R1["V  0  0"]
        R2["0  0  V"]
    end
    S["Island 2 at (2,2), area=1. Total=2 islands"]
```


## Complexity Analysis

- **Time:** O(m * n)
- **Space:** O(m * n)

## Solution (Python3)

```python
class Solution:
    pass
```

## Solution (C++)

```cpp
class Solution {
public:
    // Design problem stub
};
```
