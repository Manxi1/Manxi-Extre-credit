# Dynamic Programming #2 — Longest Common Subsequence (LCS)

## Problem Statement

Given two sequences **X** of length **m** and **Y** of length **n**, find the length of their **Longest Common Subsequence** — the longest sequence of characters that appears in **both** X and Y in the same relative order, but not necessarily contiguous.

**Example:**
```
X = "ABCBDAB"
Y = "BDCABA"
LCS = "BCBA" or "BDAB"  →  length 4
```

---

## Why Dynamic Programming?

### Naive Approach: Exponential
Generate all 2ᵐ subsequences of X and check which appear in Y — O(2ᵐ · n).

### DP Works Because:

1. **Optimal Substructure:**
   - If `X[m] == Y[n]`, then LCS must include that character → `1 + LCS(X[1..m-1], Y[1..n-1])`
   - If `X[m] != Y[n]`, then LCS comes from `max(LCS(X[1..m-1], Y), LCS(X, Y[1..n-1]))`

2. **Overlapping Subproblems:**
   - Without memoization, the same sub-problems (e.g., `LCS(X[1..3], Y[1..2])`) are recomputed exponentially many times
   - DP stores each result once → O(m × n) total work

---

## DP Formulation

**State:** `dp[i][j]` = LCS length of `X[0..i-1]` and `Y[0..j-1]`

**Recurrence:**
```
if X[i-1] == Y[j-1]:
    dp[i][j] = dp[i-1][j-1] + 1

else:
    dp[i][j] = max(dp[i-1][j],   ← skip char from X
                   dp[i][j-1])    ← skip char from Y
```

**Base case:** `dp[0][j] = dp[i][0] = 0`

---

## Complexity

| Version | Time | Space |
|---------|------|-------|
| Full table + backtrack | O(m × n) | O(m × n) |
| Length only (2 rows) | O(m × n) | **O(min(m,n))** |

---

## Example Walkthrough

X = `"ABCB"`, Y = `"BDCAB"`:

```
       ε  B  D  C  A  B
   ε [ 0  0  0  0  0  0 ]
   A [ 0  0  0  0  1  1 ]
   B [ 0  1  1  1  1  2 ]
   C [ 0  1  1  2  2  2 ]
   B [ 0  1  1  2  2  3 ]
```

**LCS length = 3**, string = "BCB"

---

## Backtracking to Reconstruct LCS

```
Start at dp[m][n]
While i>0 and j>0:
    if X[i-1] == Y[j-1]:    ← characters match → part of LCS
        record X[i-1]
        i--, j--
    elif dp[i-1][j] > dp[i][j-1]:
        i--                  ← came from above
    else:
        j--                  ← came from left
Read result in reverse
```

---

## LCS vs Edit Distance

LCS and **Edit Distance** are closely related DP problems:

| Metric | Description |
|--------|-------------|
| LCS | Longest sequence common to both strings |
| Edit Distance | Min insertions + deletions to convert X → Y |
| Relation | `edit_dist(X,Y) = m + n - 2 × LCS(X,Y)` |

---

## Running the Code

```bash
python lcs.py
```

**Expected output:**
```
=======================================================
  Longest Common Subsequence — Dynamic Programming
=======================================================

  X = "ABCBDAB"
  Y = "BDCABA"
  LCS = "BCBA"  (length 4)

  X = "AGGTAB"
  Y = "GXTXAYB"
  LCS = "GTAB"  (length 4)

  All tests passed ✔
```

---

## Real-World Applications

| Application | How LCS is Used |
|-------------|----------------|
| **`diff` / `git diff`** | Find what changed between file versions |
| **DNA sequence alignment** | Find common genetic subsequences |
| **Spell checkers** | Measure string similarity |
| **Plagiarism detection** | Find common text passages |
| **File comparison tools** | WinMerge, Beyond Compare, etc. |
