# Problem 47: Permutations II

**Difficulty:** Medium  
**Tags:** Array, Backtracking, Sorting  
**Pattern:** Backtracking  
**Link:** [leetcode.com/problems/permutations-ii](https://leetcode.com/problems/permutations-ii/)

## Description

Given a collection of numbers, `nums`, that might contain duplicates, return *all possible unique permutations **in any order**.*

 

Example 1:

```

**Input:** nums = [1,1,2]
**Output:**
[[1,1,2],
 [1,2,1],
 [2,1,1]]

```

Example 2:

```

**Input:** nums = [1,2,3]
**Output:** [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

```

 

**Constraints:**

	- `1 <= nums.length <= 8`
	- `-10 <= nums[i] <= 10`

## Approach: Backtracking

Sort + backtrack with used array. Skip duplicate elements at the same level.

## Pseudocode

```
1. Sort nums, used = [False]*n
2. backtrack(path):
   Skip used or same-level duplicates
   Mark used, recurse, unmark
```

## Algorithm Flow

```mermaid
flowchart TD
    A[Sort nums] --> B[backtrack with used array]
    B --> C{Duplicate at same level?}
    C -- Yes --> D[Skip]
    C -- No --> E[Use element, recurse]
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

- **Time:** O(n!)
- **Space:** O(n)

## Solution (Python3)

```python
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        used = [False] * len(nums)
        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False
        backtrack([])
        return result
```

## Solution (C++)

```cpp
#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        // Backtracking - O(2^n) or O(n!) time
        vector<vector<int>> result;
        vector<int> path;
        function<void(int)> backtrack = [&](int start) {
            result.push_back(path);
            for (int i = start; i < (int)nums.size(); i++) {
                path.push_back(nums[i]);
                backtrack(i + 1);
                path.pop_back();
            }
        };
        backtrack(0);
        return result;
    }
};
```
