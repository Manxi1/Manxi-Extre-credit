# Divide & Conquer #2 — Binary Search

## Problem Statement

Given a **sorted** array of **n** elements and a **target** value, find the **index** of the target in O(log n) time, or return -1 if it is not present.

---

## Divide & Conquer Strategy

| Phase | Action | Cost |
|-------|--------|------|
| **Divide** | Compute midpoint of current search range | O(1) |
| **Conquer** | Recurse on **one** half (left or right) | T(n/2) |
| **Combine** | No merging — answer is returned directly | O(1) |

> Unlike Merge Sort, Binary Search only recurses into **one** subproblem, which is why it achieves O(log n) instead of O(n log n).

---

## Recurrence Relation

```
T(n) = T(n/2) + O(1)
```

Solved by the **Master Theorem** (Case 2 variant):

```
a = 1,  b = 2,  f(n) = O(1)
log_b(a) = log_2(1) = 0  →  f(n) = Θ(n^0) = Θ(1)
⟹  T(n) = Θ(log n)
```

---

## Complexity

| Version | Time | Space |
|---------|------|-------|
| Iterative | O(log n) | **O(1)** |
| Recursive | O(log n) | O(log n) — call stack |

---

## Algorithm Steps

```
binary_search(arr, target):
    lo = 0,  hi = len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if arr[mid] == target:  return mid      # Found!
        if arr[mid] < target:   lo = mid + 1    # Discard left half
        else:                   hi = mid - 1    # Discard right half

    return -1                                   # Not found
```

---

## Execution Trace

Searching for **7** in `[1, 3, 5, 7, 9, 11, 13]`:

```
Step 1:  lo=0  hi=6  mid=3  arr[3]=7  → FOUND at index 3
```

Searching for **6** in `[1, 3, 5, 7, 9, 11, 13]`:

```
Step 1:  lo=0  hi=6  mid=3  arr[3]=7  > 6  →  hi = 2
Step 2:  lo=0  hi=2  mid=1  arr[1]=3  < 6  →  lo = 2
Step 3:  lo=2  hi=2  mid=2  arr[2]=5  < 6  →  lo = 3
         lo(3) > hi(2)  → NOT FOUND
```

Each step **eliminates half** the remaining elements. With 1 billion elements, at most **30 comparisons** are needed.

---

## Power of Logarithms

| n | Linear Search | Binary Search |
|---|---------------|---------------|
| 10 | 10 | 4 |
| 1,000 | 1,000 | 10 |
| 1,000,000 | 1,000,000 | 20 |
| 1,000,000,000 | 1,000,000,000 | 30 |

---

## Extensions Included

| Function | Description |
|----------|-------------|
| `lower_bound(arr, x)` | First index where x could be inserted |
| `upper_bound(arr, x)` | Last index where x could be inserted |
| `count_occurrences(arr, x)` | Count duplicates in O(log n) |

---

## Running the Code

```bash
python binary_search.py
```

**Expected output:**
```
====================================================
  Binary Search — Divide & Conquer
====================================================

  Searching for 47 in [2, 5, 9, ...]
  Step    lo    hi   mid   arr[mid]  Action
  --------------------------------------------------
  1        0    14     7         32  go right →
  2        8    14    11         58  ← go left
  ...
                                     FOUND ✔

  All tests passed ✔
```

---

## Real-World Applications

- **Database indexing** — B-trees use binary search at each level
- **Git bisect** — finds the commit that introduced a bug in O(log n) steps
- **Dictionary/phonebook lookups**
- **Square root / power calculations** — binary search on answer space
- **Machine learning** — hyperparameter search, threshold finding
