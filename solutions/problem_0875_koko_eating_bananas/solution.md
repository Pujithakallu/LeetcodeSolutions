# Problem 875: Koko Eating Bananas

**Difficulty:** Medium  
**Tags:** Array, Binary Search  
**Pattern:** Binary Search on Answer  
**Link:** [leetcode.com/problems/koko-eating-bananas](https://leetcode.com/problems/koko-eating-bananas/)

## Description

Koko loves to eat bananas. There are `n` piles of bananas, the `i^th` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return *the minimum integer* `k` *such that she can eat all the bananas within* `h` *hours*.

 

Example 1:

```

**Input:** piles = [3,6,7,11], h = 8
**Output:** 4

```

Example 2:

```

**Input:** piles = [30,11,23,4,20], h = 5
**Output:** 30

```

Example 3:

```

**Input:** piles = [30,11,23,4,20], h = 6
**Output:** 23

```

 

**Constraints:**

	- `1 <= piles.length <= 10^4`
	- `piles.length <= h <= 10^9`
	- `1 <= piles[i] <= 10^9`

## Approach: Binary Search on Answer

Binary search on eating speed k. For each k, compute total hours and compare with h.

## Pseudocode

```
1. lo = lower_bound, hi = upper_bound
2. While lo <= hi (or lo < hi):
   a. mid = (lo + hi) // 2
   b. If condition(mid) is satisfied: record answer, search left half
   c. Else: search right half
3. Return answer
```

## Algorithm Flow

```mermaid
flowchart TD
    A[lo=1, hi=max piles] --> B{lo < hi?}
    B -- Yes --> C[mid = lo+hi / 2]
    C --> D[Compute hours at speed mid]
    D --> E{hours <= h?}
    E -- Yes --> F[hi = mid]
    E -- No --> G[lo = mid + 1]
    F --> B
    G --> B
    B -- No --> H[Return lo]
```

## Visual State Transitions

**Binary Search on Answer:**

**Input:** piles = [3, 6, 7, 11], h = 8

**Frame 1: Initial search space**
```mermaid
graph LR
    L["lo=1"] --- M["mid=6"] --- H["hi=11"]
    C["At speed 6: hours = 1+1+2+2 = 6 <= 8 -> go left"]
```

**Frame 2: Narrow to [1, 6]**
```mermaid
graph LR
    L["lo=1"] --- M["mid=3"] --- H["hi=6"]
    C["At speed 3: hours = 1+2+3+4 = 10 > 8 -> go right"]
```

**Frame 3: Narrow to [4, 6]**
```mermaid
graph LR
    L["lo=4"] --- M["mid=5"] --- H["hi=6"]
    C["At speed 5: hours = 1+2+2+3 = 8 <= 8 -> go left"]
```

**Frame 4: Narrow to [4, 5]**
```mermaid
graph LR
    L["lo=4"] --- M["mid=4"] --- H["hi=5"]
    C["At speed 4: hours = 1+2+2+3 = 8 <= 8 -> go left"]
```

**Frame 5: lo=4, hi=4 -> Answer = 4**
```mermaid
graph LR
    A["Minimum eating speed k = 4"]
    V["Verify: ceil(3/4)+ceil(6/4)+ceil(7/4)+ceil(11/4) = 1+2+2+3 = 8 <= 8"]
```


## Complexity Analysis

- **Time:** O(n log m)
- **Space:** O(1)

## Solution (Python3)

```python
import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            hours = sum(math.ceil(p / mid) for p in piles)
            if hours <= h:
                hi = mid
            else:
                lo = mid + 1
        return lo
```

## Solution (C++)

```cpp
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        // Binary search - O(log n) time, O(1) space
        int lo = 0, hi = piles.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (piles[mid] == h) {
                return mid;
            } else if (piles[mid] < h) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return 0;
    }
};
```
