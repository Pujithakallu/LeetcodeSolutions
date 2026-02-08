# Problem 2174: Remove All Ones With Row and Column Flips II

**Difficulty:** Medium  
**Tags:** Array, Bit Manipulation, Breadth-First Search, Matrix  
**Pattern:** BFS on Matrix / Grid  
**Link:** [leetcode.com/problems/remove-all-ones-with-row-and-column-flips-ii](https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips-ii/)

## Description

*(Premium problem -- description requires LeetCode subscription)*

## Approach: BFS on Matrix / Grid

Breadth-first search on the grid. Enqueue all starting cells, then expand level by level. BFS on grids finds shortest distance from source(s).

## Pseudocode

```
1. Enqueue all source cells, mark visited
2. distance = 0
3. While queue not empty:
   a. Process all cells at current distance
   b. For each cell, enqueue unvisited neighbors
   c. distance++
4. Return result
```

## Algorithm Flow

```mermaid
flowchart TD
    A[Enqueue source cells] --> B{Queue not empty?}
    B -- Yes --> C[Process current level]
    C --> D[For each cell in level]
    D --> E[Check 4 neighbors]
    E --> F{Valid and unvisited?}
    F -- Yes --> G[Mark visited, enqueue]
    F -- No --> E
    G --> E
    D --> H[distance++]
    H --> B
    B -- No --> I[Return distances]
```

## Visual State Transitions

**Multi-source BFS on Grid:**

**Frame 1: Enqueue all sources**
```mermaid
graph TD
    subgraph Grid
        R0["S  .  ."]
        R1[".  .  ."]
        R2[".  .  S"]
    end
    Q["Queue: [(0,0), (2,2)], dist=0"]
```

**Frame 2: Expand distance 1**
```mermaid
graph TD
    subgraph Grid
        R0["0  1  ."]
        R1["1  .  1"]
        R2[".  1  0"]
    end
    Q["Distance 1 cells processed"]
```

**Frame 3: Expand distance 2**
```mermaid
graph TD
    subgraph Grid
        R0["0  1  2"]
        R1["1  2  1"]
        R2["2  1  0"]
    end
    Q["All cells reached. Max distance = 2"]
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
