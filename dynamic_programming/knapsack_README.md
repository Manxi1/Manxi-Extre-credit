# Dynamic Programming #1 — 0/1 Knapsack Problem

## Problem Statement

Given **n items**, each with a **weight** `wᵢ` and **value** `vᵢ`, and a knapsack with maximum weight capacity **W**, select a subset of items to **maximize total value** subject to the constraint that total weight ≤ W.

Each item may be included **at most once** (the "0/1" constraint — take it or leave it).

---

## Why Dynamic Programming?

### Naive Approach: Exponential
There are 2ⁿ possible subsets. For n=30 that's over 1 billion — infeasible.

### Greedy Fails Here
Taking the highest value-to-weight ratio item first does **not** always give the optimal solution.

**Example:** capacity=5, items = [(w=4, v=5), (w=3, v=4), (w=3, v=4)]
- Greedy takes item 1 (ratio 1.25) → value 5
- Optimal takes items 2+3 → value **8**

### DP Works Because:
1. **Optimal substructure** — optimal solution to the full problem contains optimal solutions to subproblems
2. **Overlapping subproblems** — same subproblems recomputed repeatedly in recursion → store and reuse

---

## DP Formulation

**State:** `dp[i][w]` = maximum value achievable using items `1..i` with capacity `w`

**Recurrence:**
```
dp[i][w] = dp[i-1][w]                              if wᵢ > w  (can't fit)
dp[i][w] = max(dp[i-1][w],  dp[i-1][w-wᵢ] + vᵢ)   otherwise
            ↑ skip item i       ↑ take item i
```

**Base case:** `dp[0][w] = 0` for all w (no items → value 0)

**Answer:** `dp[n][W]`

---

## Complexity

| Version | Time | Space |
|---------|------|-------|
| Full table | O(n × W) | O(n × W) |
| Space-optimized | O(n × W) | **O(W)** |

> Note: This is **pseudo-polynomial** — polynomial in the *value* of W, not its *bit length*. This is why Knapsack is NP-hard in general.

---

## Example Walkthrough

Items: `[(w=1,v=1), (w=2,v=6), (w=3,v=10), (w=5,v=16)]`, Capacity = 7

```
     W→  0   1   2   3   4   5   6   7
i=0      0   0   0   0   0   0   0   0
i=1(w=1) 0   1   1   1   1   1   1   1
i=2(w=2) 0   1   6   7   7   7   7   7
i=3(w=3) 0   1   6   10  11  16  17  17
i=4(w=5) 0   1   6   10  11  16  17  22
```

**Answer:** `dp[4][7] = 22`

**Backtrack:** Item 4 taken (w=5), then item 2 taken (w=2) → total weight = 7

---

## Backtracking to Find Solution

```
Start at dp[n][W]
For i = n down to 1:
    if dp[i][W] != dp[i-1][W]:    ← item i was included
        record item i
        W -= weight[i]
```

---

## Space-Optimized Version

Process weights in **reverse** order to avoid counting an item twice:

```python
dp = [0] * (W + 1)
for each item (w, v):
    for cap in range(W, w-1, -1):    # ← REVERSE!
        dp[cap] = max(dp[cap], dp[cap - w] + v)
```

---

## Running the Code

```bash
python knapsack.py
```

**Expected output:**
```
=======================================================
  0/1 Knapsack — Dynamic Programming
=======================================================
  Capacity: 7 kg

  DP Table (rows = items, cols = capacity):
  ...

  ✅ Selected Items:
     • Book           2kg  $3
     • Phone          1kg  $2
     • Tablet         5kg  $7

  Total Weight : 7 / 7 kg
  Total Value  : $12
```

---

## Real-World Applications

- **Resource allocation** — maximize productivity given budget/time
- **Financial portfolio** — maximize returns given risk constraints
- **Cargo loading** — maximize value of shipped goods
- **Memory management** — optimal page replacement policies
- **Cryptography** — the subset-sum variant underlies early cryptosystems
