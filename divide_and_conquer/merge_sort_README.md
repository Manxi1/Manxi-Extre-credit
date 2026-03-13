# Divide & Conquer #1 — Merge Sort

## Problem Statement

Given an unsorted array of **n** comparable elements, sort them in **non-decreasing order** in the most efficient way possible.

---

## Divide & Conquer Strategy

Merge Sort is the textbook example of the **Divide & Conquer** paradigm:

| Phase | Action | Cost |
|-------|--------|------|
| **Divide** | Split array at midpoint into two halves | O(1) |
| **Conquer** | Recursively sort each half | 2 × T(n/2) |
| **Combine** | Merge the two sorted halves | O(n) |

---

## Recurrence Relation

```
T(n) = 2·T(n/2) + O(n)
```

Solved by the **Master Theorem** (Case 2):

```
a = 2,  b = 2,  f(n) = n
log_b(a) = log_2(2) = 1  →  f(n) = Θ(n^1)
⟹  T(n) = Θ(n log n)
```

---

## Complexity

| Case | Time | Space |
|------|------|-------|
| Best | O(n log n) | O(n) |
| Average | O(n log n) | O(n) |
| Worst | O(n log n) | O(n) |

> Unlike Quick Sort, Merge Sort has **no worst-case degradation** — it is always O(n log n).

---

## Algorithm Steps

```
merge_sort(arr):
    if len(arr) <= 1: return arr          # Base case

    mid   = len(arr) // 2
    left  = merge_sort(arr[:mid])         # Divide & Conquer left
    right = merge_sort(arr[mid:])         # Divide & Conquer right
    return merge(left, right)             # Combine

merge(left, right):
    result = []
    while both lists non-empty:
        pick the smaller front element → append to result
    append remainder of whichever list is non-empty
    return result
```

---

## Execution Trace

Input: `[5, 3, 8, 1]`

```
                [5, 3, 8, 1]
               /             \
          [5, 3]           [8, 1]
          /    \           /    \
        [5]   [3]        [8]   [1]
          \  /              \  /
          [3,5]            [1,8]
               \          /
              [1, 3, 5, 8]
```

**Merge of `[3,5]` and `[1,8]`:**
```
Compare 3 vs 1 → take 1  →  [1]
Compare 3 vs 8 → take 3  →  [1,3]
Compare 5 vs 8 → take 5  →  [1,3,5]
Remaining: [8]            →  [1,3,5,8]
```

---

## Running the Code

```bash
python merge_sort.py
```

**Expected output:**
```
==================================================
  Merge Sort — Divide & Conquer
==================================================

[Traced execution on [5, 3, 8, 1, 9, 2]]
  ↓ split  [5, 3, 8, 1, 9, 2]
    ↓ split  [5, 3, 8]
      ...
Final sorted: [1, 2, 3, 5, 8, 9]

All tests passed ✔
```

---

## Why Not Just Use Python's `sorted()`?

Python's built-in sort (`Timsort`) is faster in practice because it exploits pre-existing order. However, **Merge Sort is the conceptual foundation** of all comparison-based sorting and is ideal for:

- **External sorting** (data too large for RAM — merge from disk)
- **Linked lists** (no random access needed for merging)
- **Stable sorting** required (equal elements preserve original order)

---

## Comparison with Other Sorts

| Algorithm | Best | Average | Worst | Stable |
|-----------|------|---------|-------|--------|
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | ✔ |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | ✗ |
| Bubble Sort | O(n) | O(n²) | O(n²) | ✔ |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | ✗ |
